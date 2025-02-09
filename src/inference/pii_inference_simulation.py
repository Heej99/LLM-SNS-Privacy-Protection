# LLM model import
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForCausalLM.from_pretrained(
    model_name, 
    torch_dtype=torch.float16,  # FP16으로 로드 (VRAM 절약)
    device_map="auto"  # 자동으로 GPU 할당
)

# System prompt 
system_prompt = """
You are an expert investigator with years of experience in online profiling and text analysis.
Your primary role is to identify potential personal information in user-generated text and provide guidance on how to rewrite it to minimize privacy risks.

Task:
1. Analyze a given social media post to detect personal information that could lead to identification.
2. Consider the following categories of personal information:
[full_name, contact_number, date_of_birth, sex, occupation, income, income_level,location (not home address) , address (home address), place_of_birth, mbti, education, mental_health_history_detail, physical_health_history_detail, religion, political_ideology]
3. Highlight text segments that reveal or imply personal information and explain why they pose a risk.
4. Assign a diffculty rating score (1 to 4) based on how easily someone could infer personal information:
Difficulty 1: Direct identification of a specific person is possible.
Difficulty 2: A specific person can be inferred through simple reasoning.
Difficulty 3: A specific person is difficult to identify but could be inferred through external searches.
Difficulty 4: Almost no risk of exposing personal information.
5. Rewrite the identified segments to preserve the intended meaning while reducing or removing personal information exposure. Ensure the rewritten text maintains clarity and coherence while making personal identification nearly impossible.

By following this approach, your goal is to help users express themselves freely while minimizing privacy risks.
"""

user_prompt =  """
Here is the given post: <user_given_post>

Task:
1. Identify and highlight parts of the post that may reveal or imply personal information.  
2. For each identified part, provide the following details:  
- Type of personal information (e.g., address, occupation, etc.)  
- Privacy exposure level (1-4) (1 = highly identifiable, 4 = minimal risk)  
- Explanation of why this part may reveal personal information  
3. Rewrite the post while modifying only the parts that meet the specified privacy exposure level (i.e., difficulty level) threshold:
- Modify Level 1 or lower: Modify only directly stated personal information.
- Modify Level 2 or lower: Modify Level 1 + personal information that can be easily inferred.
- Modify Level 3 or lower: Modify Level 2 + information that has even a slight possibility of indirect inference.

Structure the output as in the example below:
inference = {
'text': '오늘 서울 성수동에 있는 카페플렉스에서 디자인 아이디어를 구상하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 아이디어도 개많이 나오는 듯~ 추천추천',
'result': {
    '서울 성수동에 있는 카페플렉스': {
        'info_type': 'location',
        'difficulty': 1,
        'reason': '특정한 장소(서울 성수동, 카페플렉스)를 언급하고 있기 때문에, 해당 지역과 연관이 있을 가능성이 높음.'
    },
    '디자인 아이디어': {
        'info_type': 'occupation',
        'difficulty': 2,
        'reason': '"디자인 아이디어"라는 표현이 디자인 관련 직업을 가지고 있거나 디자인을 전공하는 사람일 가능성을 암시함.'
    },
  },
'modified_text': {
    "difficulty 1": "오늘 카페에서 디자인 아이디어를 구상하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 아이디어도 개많이 나오는 듯~ 추천추천",
    "difficulty 2": "오늘 카페에서 작업하면서 커피 한 잔 했음. 여기 커피 진짜 존맛~ DM 주면 카페 정보 알려줌~",
    "difficulty 3": "오늘 카페에서 작업하면서 커피 한 잔 했음. 커피 맛있네. 여기 커피 진짜 존맛~ DM 주면 카페 정보 알려줌~",
  }
}

"""
# input data
user_given_post = input()
user_prompt = user_prompt.replace(<user_given_post>, str(user_given_post))


# personal information inference
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

input_text = tokenizer.apply_chat_template(messages, tokenize=False)
inputs = tokenizer(input_text, return_tensors="pt").to("cuda")

with torch.no_grad():
    output = model.generate(**inputs, max_length=512)

response = tokenizer.decode(output[0], skip_special_tokens=True)
print(response)

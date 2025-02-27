import torch
from transformers import pipeline
import ast

# 시스템 프롬프트 정의
system_prompt = """
You are an expert investigator with years of experience in online profiling and text analysis.
Your primary role is to identify potential personal information in user-generated text and provide guidance on how to rewrite it to minimize privacy risks.

Task:
1. Analyze a given social media post to detect personal information that could lead to identification.
2. Consider the following categories of personal information:
[full_name, contact_number, date_of_birth, sex, occupation, income, income_level,location (not home address), address (home address), place_of_birth, mbti, education, mental_health_history_detail, physical_health_history_detail, religion, political_ideology]
3. Highlight text segments that reveal or imply personal information and explain why they pose a risk.
4. Assign a difficulty rating score (1 to 4) based on how easily someone could infer personal information:
    - Difficulty 1: Direct identification of a specific person is possible.
    - Difficulty 2: A specific person can be inferred through simple reasoning.
    - Difficulty 3: A specific person is difficult to identify but could be inferred through external searches.
    - Difficulty 4: Almost no risk of exposing personal information.
5. Rewrite the identified segments to preserve the intended meaning while reducing or removing personal information exposure. Ensure the rewritten text maintains clarity and coherence while making personal identification nearly impossible.

By following this approach, your goal is to help users express themselves freely while minimizing privacy risks.
"""

# 사용자 프롬프트 템플릿
user_prompt_template = """
Here is the given post: <user_given_text>


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
{
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

Your response must be a valid Python dictionary. 
Start with '{' and end with '}'
Do not include any explanations, markdown, or formatting like "```json" in your response.
"""

# Model ID
model_id = "Qwen/Qwen2.5-7B-Instruct"

'''
# Initialize pipeline with automatic device allocation
pipe = pipeline(
    task="text-generation",
    model=model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto"  # Automatically assigns model layers across available devices
)
'''

def generate_message(user_post):
    """ 사용자 입력을 프롬프트로 변환 """
    user_prompt = user_prompt_template.replace("<user_given_text>",str(user_post))
    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': user_prompt}
    ]
    return messages

def infer_pii(input_text):
    """
    Identifies Personally Identifiable Information (PII) in the given text 
    and generates a modified version of the text with privacy protection.

    Args:
        input_text (str): The input text containing potential PII.

    Returns:
        dict: Parsed JSON output containing:
            - 'text': The original text
            - 'result': Dictionary of detected PII information
            - 'modified_text': Text modified for privacy protection
    """
    # Generate structured prompt using generate_message()
    messages = generate_message(input_text)
    
    # Convert the message structure into a formatted text prompt
    prompt = f"{messages[0]['content']}\n\nUser: {messages[1]['content']}\nAssistant:" 

    # Generate response using pipeline (tokenization happens internally)
    response = pipe(prompt, max_new_tokens=512, return_full_text=False)[0]["generated_text"]

    # Convert response from string to dictionary
    resp_dict = ast.literal_eval(response)

    return resp_dict
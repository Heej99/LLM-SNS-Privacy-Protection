import os
from groq import Groq
import ast

api_keys="YOUR_API_KEY"

# 시스템 프롬프트 정의
system_prompt = """
You are an expert investigator with years of experience in online profiling and text analysis.
Your primary role is to detect and mitigate potential privacy risks in user-generated text.
"""

# 사용자 프롬프트 템플릿
user_prompt_template = """
Here is the given post: <user_given_text>

Task:
1. Identify and highlight parts of the social media post that may reveal or imply personal information.  
2. For each identified part, provide the following 3 details:  
- Type of personal information (only if it directly identifies or describes the individual providing the text): [full_name, contact_number, date_of_birth,place_of_birth,relationship_status, sex, occupation, income, income_level, location,home address, place_of_birth, mbti, education, mental_health_history_detail, physical_health_history_detail, religion, political_ideology]
- Privacy exposure level (1-3):  
    - Difficulty 1: The information directly identifies a specific individual.  
    - Difficulty 2: A specific individual can be inferred through simple reasoning.  
    - Difficulty 3: A specific individual is difficult to identify but could be inferred through external searches or additional context.  
- Explanation of why this part may reveal personal information.  
3. Rewrite the post by modifying only highlighted parts based on the specified privacy exposure level:  
- For Difficulty 1: Modify personal information that falls under Difficulty 1 in a way that maintains the original meaning and context while preventing identification.  
- For Difficulty 2: Modify all information classified as Difficulty 2 or lower to prevent inference about the individual.  
- For Difficulty 3: Modify all information classified as Difficulty 3 or lower to minimize the possibility of indirect identification through external searches.  

Please, Ensure that the modified text remains clear, natural, and contextually coherent while minimizing privacy risks.  
- Do NOT replace information with repetitive or generic placeholders.  
- Adjust sentence structure naturally so that the modified text does not sound awkward or robotic.  
- Keep the original meaning intact while generalizing personal details.

Structure the output as in the example below:
Example 1 = {
'text': '오늘 서울 성수동에 있는 카페플렉스에서 디자인 아이디어를 구상하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 다음에 남편이랑도 같이 와야지~ 추천추천',
'result': {
    '서울 성수동에 있는 카페플렉스': {
        'info_type': 'location',
        'difficulty': 1,
        'reason': '특정한 장소(서울 성수동, 카페플렉스)에 있음을 드러내고 있음.'
    },
    '디자인 아이디어': {
        'info_type': 'occupation',
        'difficulty': 2,
        'reason': '디자인 관련 직업을 가지고 있거나 디자인을 전공하는 사람일 가능성을 암시함.'
    },
    '남편': {
        'info_type': 'relationship_status',
        'difficulty': 1,
        'reason': '결혼한 상태인 것을 알 수 있음.'
    },
    '남편': {
        'info_type': 'sex',
        'difficulty': 1,
        'reason': '여성일 가능성이 높음.'
    },
  },
'modified_text': {
    "difficulty 1": "오늘 카페에서 디자인 아이디어를 구상하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 다음에 또 와야지~ 추천추천",
    "difficulty 2": "오늘 카페에서 일하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 다음에 또 와야지~ 추천추천",
    "difficulty 3": "오늘 카페에서 일하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 다음에 또 와야지~ 추천추천",
  }
}
Example 2 ={
    'text': '어릴 때 마포에서 살다가 지금은 강남에서 사는데, 여행 가면 새로운 동네 구경하는 게 제일 좋다. ✈️ 이번엔 어디로 떠나볼까?',
    'result': {
        '어릴 때 마포에서 살다가': {
            'info_type': 'place_of_birth',
            'difficulty': 1,
            'reason': '태어난 곳을 언급함.'
        },
        '지금은 강남에서 사는데': {
            'info_type': 'home address',
            'difficulty': 1,
            'reason': '사는 곳을 언급함.'
        }
    },
    'modified_text': {
        'difficulty 1': '여행 가면 새로운 동네 구경하는 게 제일 좋다. ✈️ 이번엔 어디로 떠나볼까?',
        'difficulty 2': '여행 가면 새로운 동네 구경하는 게 제일 좋다. ✈️ 이번엔 어디로 떠나볼까?',
        'difficulty 3': '여행 가면 새로운 동네 구경하는 게 제일 좋다. ✈️ 이번엔 어디로 떠나볼까?'
    }
}
Your response must be a valid Python dictionary.
Start with '{' and end with '}'
The output for "text", "reason", and "modified_text" must be in Korean
Do not include any explanations, markdown, or formatting like "```json" in your response.
"""

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

    # Import Python
    client = Groq(
    api_key=api_keys
    )

    chat_completion = client.chat.completions.create(
        model="qwen-2.5-32b", 
        messages=messages,  
        temperature = 0.5,
        seed=42
    )
    # Generate response using pipeline (tokenization happens internally)
    response = chat_completion.choices[0].message.content

    # Convert response from string to dictionary
    resp_dict = ast.literal_eval(response)

    return resp_dict
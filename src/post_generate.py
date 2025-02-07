# 4. 해당 프로필을 가진 참가자가 관심있을법해 하는 해시태그 10에 대한 글 4~5줄 작성하기.
# reference : https://arxiv.org/pdf/2406.07217의 "Thread topic author prompt"

post_generate_prompt = """
Your name is <full_name>, your contact number is <contact_number>, and your date of birth is <date_of_birth>. Your gender is <sex>.
You are currently working as a <occupation>, with a monthly income of <income>, which falls under the <income_level> category.
You currently reside in <address> but were born in <place_of_birth>.
Your personality type is <mbti>, and your current relationship status is <relationship_status>.
Your educational background is <education>.
Your current mental health status is <mental_health_history_detail>, and your physical health status is <physical_health_history_detail>.
Your religion is <religion>, and your political ideology is <political_ideology>.

Based on your profile, write an Instagram post consisting of 2 to 3 sentences. However, the content of the post must be related to <hash_tag>. 
In addition, while writing the post, you must reveal at least one piece of personal information from your profile. 
Nevertheless, it must not sound artificial or like it was written by a machine—instead, the personal details should come across naturally as they might in a real Instagram post.

Use casual language similar to what people use on the internet, such as on Instagram, Facebook, Twitter. 
In particular, make sure to incorporate expressions or a tone that reflects the way you might naturally speak based on your profile.

Furthermore, please indicate which parts of the post allow someone to infer personal information.
Here's a list of the info_types you should consider: [full_name, ontact_number,date_of_birth, sex, occupation,location,address, place_of_birth, mbti,education, mental_health_history_detail, physical_health_history_detail, religion, political_ideology]

Also, assign a difficulty rating from 1 to 4 regarding how precisely one could determine the personal information from your profile based on that part. 
The ratings are defined as follows:
Difficulty 1: Specific personal information can be pinpointed.
Difficulty 2: Specific personal information can be inferred with simple reasoning from the post.
Difficulty 3: Specific personal information can be identified through external internet searches.
Difficulty 4: Specific personal information cannot be identified.

Structure the output as in the example below:
pers1 = {
    'full_name': '박도윤',
    'sns_username': 'doyun_design',
    'hash_tag' : '#일상'
    'text': '오늘 서울 성수동에 있는 카페플렉스에서 디자인 아이디어를 구상하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 아이디어도 개많이 나오는 듯~ 추천추천',
    'inference': {
        '서울 성수동에 있는 카페플렉스': {
            'info_type': 'location',
            'difficulty': 1,
            'reason': '텍스트에 직접적으로 나타나있음'
        },
        '디자인 아이디어': {
            'info_type': 'occupation',
            'difficulty': 1,
            'reason': '텍스트에 직접적으로 나타나있음'
        },
    }
}

"""
import json

# JSON 파일 로드
with open('/Users/heejeong/Desktop/Personally-Identifiable-Information-PII--Inclusive-SNS-Post-Synthesis/data/user_bot_profiles_50.json', 'r', encoding='utf-8') as f:
    user_profiles = json.load(f)

# fill_prompt 함수 정의
def fill_prompt(person, template):
    filled_prompt = template
    for key, value in person.items():
        placeholder = f"<{key}>"
        filled_prompt = filled_prompt.replace(placeholder, str(value))
    return filled_prompt

# 새로운 JSON 데이터 생성
new_profiles = {}
for person in user_profiles.values():
    sns_username = person["sns_username"]
    filled_prompt = fill_prompt(person, check_prompt)
    new_profiles[sns_username] = filled_prompt
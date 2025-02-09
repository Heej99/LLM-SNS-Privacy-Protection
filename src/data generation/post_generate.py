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

Based on the profile above, write Instagram posts of 3 sentences for each of the 10 given <hash_tag>.
Each post must be related to the given hash tag. Ensure each post is as diverse as possible, avoiding repetition in contetn, theme, and message.
AND, The post MUST naturally include at least one piece of personal information from the profile.
However, the personal detail should not sound artificial or machine-generated—it should flow naturally, as people would typically write on social media.
Use casual language similar to what people use on the internet, such as on Instagram, Facebook, Twitter. 
In particular, make sure to incorporate expressions or a tone that reflects the way you might naturally speak based on your profile.

Furthermore, please indicate which parts of the post allow someone to infer personal information.
Here's a list of the info_types you should consider: [full_name, contact_number,date_of_birth, sex, occupation, income, income_level, location (not home address) , address (home address), place_of_birth, mbti,education, mental_health_history_detail, physical_health_history_detail, religion, political_ideology]

Also, assign a difficulty rating from 1 to 4 regarding how precisely one could determine the personal information from your profile based on that part. 
The ratings are defined as follows:
Difficulty 1: Direct identification of a specific person is possible.
Difficulty 2: A specific person can be inferred through simple reasoning.
Difficulty 3: A specific person is difficult to identify but could be inferred through external searches.
Difficulty 4: Almost no risk of exposing personal information.

Structure the output as in the example below:
pers1 = {
    'full_name': '박도윤',
    'sns_username': 'doyun_design',
    'hash_tag 1' : {
    'keyword: '#일상',
    'text': '오늘 서울 성수동에 있는 카페플렉스에서 디자인 아이디어를 구상하면서 커피 한 잔 했음. 여기 커피 진짜 존맛. 아이디어도 개많이 나오는 듯~ 추천추천',
    'inference': {
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
    'hash_tag 2' : {
    'keyword: '#감성',
    'text': '새벽 감성에 집에서 차 한잔하며 올리는 글... 오늘 밤하늘이 참 예쁘다. 내일 일어나서 화장하고, 출근할 생각하니까 밤하늘 보기가 싫어진다...',
    'inference': {
        '집에서': {
            'info_type': 'location',
            'difficulty': 4,
            'reason': '집에 있다는 일반적인 진술로, 구체적인 개인정보를 추론하기 어려움.'
        },
        '화장하고': {
            'info_type': 'sex',
            'difficulty': 2,
            'reason': '"화장하고"라는 표현이 들어가 있어, 일반적으로 여성일 가능성이 높다고 추측할 수 있음. 물론, 화장을 하는 남성도 있지만 통계적으로 여성일 가능성이 더 큼. '
        },
    },
}
"""
import json

# JSON 파일 로드
with open('/data/user_bot_profiles_50.json', 'r', encoding='utf-8') as f:
    user_profiles = json.load(f)
with open('/data/user_bot_hashtag.json', 'r', encoding='utf-8') as f:
    user_hash_tag = json.load(f)


# fill_prompt 함수 정의
def fill_prompt(sns_username, person, template):
    filled_prompt = template

    # profile 채우기
    for key, value in person.items():
        placeholder = f"<{key}>"
        filled_prompt = filled_prompt.replace(placeholder, str(value))
    # hash_tag 채우기
    result = {key: value for key, value in user_hash_tag.items() if value.get("sns_username") == sns_username}
    interest_hash_tag_value = next(iter(result.values()), {}).get("interest_hash_tag")
    filled_prompt = filled_prompt.replace("<hash_tag>",str(interest_hash_tag_value))

    return filled_prompt

# 새로운 JSON 데이터 생성
new_profiles = {}
for person in user_profiles.values():
    sns_username = person["sns_username"]
    filled_prompt = fill_prompt(sns_username, person, post_generate_prompt)
    new_profiles[sns_username] = filled_prompt

#새로운 JSON 파일 저장  # API key 대신 GUI를 사용하기 위함.
with open('/user_bot_post_prompt.json', 'w', encoding='utf-8') as f:
    json.dump(new_profiles, f, ensure_ascii=False, indent=4)

print("새로운 JSON 파일이 성공적으로 생성되었습니다: user_bot_post_prompt.json")

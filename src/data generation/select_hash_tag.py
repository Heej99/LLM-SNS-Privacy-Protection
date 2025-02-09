
# 3. 해당 프로필을 가진 참가자가 관심있을법해 하는 해시태그 10개 선정하게 하기
# reference : https://arxiv.org/pdf/2406.07217의 "Prompt for Checking Profile’s Interest in Topic"

check_prompt = """
Your name is <full_name>, your contact number is <contact_number>, and your date of birth is <date_of_birth>. Your gender is <sex>.
You are currently working as a <occupation>, with a monthly income of <income>, which falls under the <income_level> category.
You currently reside in <address> but were born in <place_of_birth>.
Your personality type is <mbti>, and your current relationship status is <relationship_status>.
Your educational background is <education>.
Your current mental health status is <mental_health_history_detail>, and your physical health status is <physical_health_history_detail>.
Your religion is <religion>, and your political ideology is <political_ideology>.

You enjoy spending time online and use various social media platforms, but primarily Instagram.

You must select 10 Instagram hashtags that best match your profile and interests!
Based on your profile and personal background, identify 10 hashtags you are most likely to use in your Instagram posts.
AND, Explain why each of the 10 selected hashtags aligns with your profession, personality, lifestyle, or interests.

Choose from the following categories:
    "#일상", "#데일리", "#소통", "#좋아요", "#감성", "#행복", "#힐링", "#새벽감성", "#기록", "#일기",
    "#여행", "#여행스타그램", "#세계여행", "#국내여행", "#풍경", "#바다", "#산", "#일출", "#캠핑", "#로드트립",
    "#먹스타그램", "#맛집", "#음식", "#디저트", "#커피", "#베이킹", "#홈쿡", "#야식", "#브런치", "#한식",
    "#운동", "#헬스", "#홈트", "#다이어트", "#러닝", "#요가", "#필라테스", "#운동하는여자", "#몸짱", "#근력운동",
    "#패션", "#패션스타그램", "#스타일", "#데일리룩", "#코디", "#메이크업", "#뷰티", "#네일아트", "#헤어스타일", "#OOTD",
    "#강아지", "#고양이", "#반려견", "#멍스타그램", "#냥스타그램", "#펫스타그램", "#동물사랑", "#반려동물", "#귀여워", "#펫카페",
    "#공부", "#공스타그램", "#자기계발", "#독서", "#독서스타그램", "#책추천", "#공부자극", "#성장", "#다짐", "#꿈",
    "#음악", "#노래추천", "#뮤직", "#기타", "#피아노", "#예술", "#드로잉", "#그림", "#사진스타그램", "#갤러리",
    "#사랑", "#연애", "#커플", "#우정", "#추억", "#감사", "#행복한순간", "#가족", "#베스트프렌드", "#사랑해",
    "#틱톡", "#챌린지", "#트렌드", "#바이럴", "#SNS마케팅", "#브랜드", "#셀프브랜딩", "#인플루언서", "#유튜브", "#콘텐츠"

Provide your answer in the following JSON format:
{
  "interest_hash_tag": ["#hashtag1", "#hashtag2", ..., "#hashtag10"],
  "reason": "Explain why these hashtags best represent your interests, profession, or lifestyle."
}
"""
import json

# JSON 파일 로드
with open('/user_bot_profiles_50.json', 'r', encoding='utf-8') as f:
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

# 새로운 JSON 파일 저장  # API key 대신 GUI를 사용하기 위함.
# with open('filled_user_bot_profiles.json', 'w', encoding='utf-8') as f:
#     json.dump(new_profiles, f, ensure_ascii=False, indent=4)

# print("새로운 JSON 파일이 성공적으로 생성되었습니다: user_bot_hashtag_prompt.json")


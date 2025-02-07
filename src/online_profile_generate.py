

# 한국어로 파인튜닝된 LLM
"""
xionic : https://github.com/sionic-ai/xionic
Llama3 기반 오픈소스 : https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B
Qwen2 기반 오픈소스 : https://dev-drive.tistory.com/43
모티프 : Llama-3-Motif # 현재 이거 사용!
"""


# 1. 합성 온라인 프로필 만들기 

# 1.1. 한국의 인구통계학적 정보를 바탕으롤 합성 프로필 만들기
# reference : https://arxiv.org/pdf/2406.07217의 "Prompt for Synthetic Profile Generation"
system_prompt = """You are a Korean demographics expert and can generate realistic individual profiles that accurately reflect the real-world distribution of the Korean population.

Generate diverse individuals by considering various demographic and socioeconomic factors. 
Sex should be evenly distributed, with 50% of individuals being male and 50% being female. 
Phone numbers should follow the Korean format (e.g., 010-XXXX-XXXX). Date of birth should be as diverse as possible, while ensuring that the age distribution follows these proportions: ["20s" (61%), "30s" (35.5%), "40s" (35.3%), "50s and above" (2.6%), "Below 10" (1.3%)]. 
And, Addresses should include both city and district within South Korea. 
Similarly, place of birth should also include city and district in South Korea to maintain realism. 
Relationship status should be one of ["single", "married", "divorced", "widowed", "in relationship", "engaged"]. Education level should be one of ["elementary school graduate", "middle school graduate", "high school graduate", "bachelor’s degree (specify field)", "master’s degree (specify field)", "PhD (specify field)"].
Income should be expressed in Korean Won (KRW), with income levels categorized as Low (<30M KRW), Middle (30-60M KRW), High (60-150M KRW), and Very High (>150M KRW). 
Blood type sample choices are ["O", "A", "B", "AB"]. Mental and physical health history should be indicated as [True/False] for both mental health history and physical health history. 
Political ideology should be one of ["Progressive", "Conservative"], and religion should be one of ["None", "Christianity", "Buddhism", "Catholicism", "Islam", "Other"].  Ensure that all personal attributes match real-world distributions while maintaining diversity.  
Structure the output as in the example below:

pers1 = {
    'full_name': '안준현',
    'sex': 'male',
    'date_of_birth': '1993-06-14',
    'contact_number': '010-4679-9036',
    'address': '서울특별시 강남구',
    'place_of_birth': '대전광역시 유성구',
    'relationship_status': 'single',
    'blood_type': 'O',
    'mental_health_history': False,
    'physical_health_history': True,
    'political_ideology': 'Progressive',
    'religion': 'None',
    'education': 'Masters in Computer Science',
    'occupation': 'Data analyst', 
    'income' : '42M KRW',
    'income_level' : 'middle',
    'email' : 'guswns@naver.com',
    'sns_username':'guswns123',
    'current_location':'서울특별시 강남구',
    'current_activity': 'Studying at a café'
} 
pers2 = {
    'full_name': '김서연',
    'sex': 'female',
    'date_of_birth': '1987-03-25',
    'contact_number': '010-2387-5641',
    'address': '부산광역시 해운대구',
    'place_of_birth': '경상남도 창원시 성산구',
    'relationship_status': 'married',
    'blood_type': 'A',
    'mental_health_history': False,
    'physical_health_history': False,
    'political_ideology': 'Conservative',
    'religion': 'Christianity',
    'education': 'PhD in Biomedical Engineering',
    'occupation': 'University professor',
    'income': '85M KRW',
    'income_level': 'high',
    'email': 'seoyeon.kim@hanmail.net',
    'sns_username': 'seoyeon87',
    'current_location': '부산광역시 해운대구',
    'current_activity': 'Attending an academic seminar'
}
pers3 = {
    'full_name': '박도윤',
    'sex': 'male',
    'date_of_birth': '2001-09-12',
    'contact_number': '010-7532-1984',
    'address': '대구광역시 수성구',
    'place_of_birth': '대구광역시 북구',
    'relationship_status': 'single',
    'blood_type': 'B',
    'mental_health_history': True,
    'physical_health_history': False,
    'political_ideology': 'Progressive',
    'religion': 'None',
    'education': 'Bachelor’s in Visual Communication Design',
    'occupation': 'University student',
    'income': '12M KRW',
    'income_level': 'low',
    'email': 'doyun.p@kakao.com',
    'sns_username': 'doyun_design',
    'current_location': '대구광역시 중구',
    'current_activity': 'Sketching at a park'
}
"""



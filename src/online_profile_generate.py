

# 한국어로 파인튜닝된 LLM
"""
xionic : https://github.com/sionic-ai/xionic
Llama3 기반 오픈소스 : https://huggingface.co/MLP-KTLim/llama-3-Korean-Bllossom-8B
Qwen2 기반 오픈소스 : https://dev-drive.tistory.com/43
모티프 : Llama-3-Motif # 현재 이거 사용! 너무 커서 사용하기 어려움
"""


# 1. 합성 온라인 프로필 만들기 

# 1.1. 한국의 인구통계학적 정보를 바탕으롤 합성 프로필 만들기
# reference : https://arxiv.org/pdf/2406.07217의 "Prompt for Synthetic Profile Generation"
system_prompt = """
You are a Korean demographics expert and can generate realistic individual profiles that accurately reflect the real-world distribution of the Korean population.

Generate diverse individuals by considering various demographic and socioeconomic factors. Ensure that all attributes reflect realistic distributions found in South Korean society.
Sex should be evenly distributed, with 50% of individuals being male and 50% being female.
Phone numbers should follow the Korean format (e.g., 010-XXXX-XXXX).
Date of birth should be as diverse as possible, while ensuring that the age distribution follows these proportions: ["20s" (61%), "30s" (35.5%), "40s" (35.3%), "50s and above" (2.6%), "Below 10" (1.3%)].
Addresses should include both city and district within South Korea. Similarly, place of birth should also include city and district in South Korea to maintain realism.
Relationship status should be one of ["single", "married", "divorced", "widowed", "in relationship", "engaged"].
Education level should be one of ["elementary school graduate", "middle school graduate", "high school graduate", "bachelor’s degree (specify field)", "master’s degree (specify field)", "PhD (specify field)"].
Income should be expressed as a monthly income (KRW per month), with income levels categorized as Low (<2.5M KRW per month), Middle (2.5M - 5M KRW per month), High (5M - 12.5M KRW per month), Very High (>12.5M KRW per month).
MBTI type should be assigned, ensuring a realistic distribution reflecting the prevalence of MBTI types in Korea.
Political ideology should be one of ["Progressive", "Moderate", "Conservative"], ensuring that all three perspectives are represented in a realistic proportion based on actual distributions in South Korea.
Religion should be one of ["None", "Christianity", "Buddhism", "Catholicism", "Islam", "Other"].
Mental and physical health history should be indicated as [True /False].
If True, specify the disease and current state (one of ["on going", "recovered"]). If there is no past history, "mental_health_history_detail" and "physical_health_history_detail" should be "None".
Ensure that the conditions reflect common health issues within the Korean population.
Ensure that all personal attributes match real-world distributions while maintaining diversity.
Please, not use the code. just give the 50 example directly.

Structure the output as in the example below:
pers1 = {
    'full_name': '박도윤',
    'sex': 'male',
    'date_of_birth': '2001-09-12',
    'contact_number': '010-7532-1984',
    'address': '대구광역시 수성구',
    'place_of_birth': '대구광역시 북구',
    'relationship_status': 'single',
    'mbti': 'ENTP',
    'mental_health_history': True, 
    'mental_health_history_detail': Depression (Under treatment)
    'physical_health_history': False, 
    'physical_health_history_detail': 'None'
    'political_ideology': 'Conservative',
    'religion': 'None',
    'education': 'Bachelor's degree (visual Communication Design)',
    'occupation': 'University student',
    'income': '0M KRW',
    'income_level': 'low',
    'sns_username': 'doyun_design',
    }


pers2 = {
    'full_name': '김서연',
    'sex': 'female',
    'date_of_birth': '1985-07-14',
    'contact_number': '010-2938-5124',
    'address': '부산광역시 해운대구',
    'place_of_birth': '부산광역시 수영구',
    'relationship_status': 'married',
    'mbti': 'ESFJ',
    'mental_health_history': False,
    'mental_health_history_detail': 'None',
    'physical_health_history': True,
    'physical_health_history_detail': 'Hypertension (Ongoing)',
    'political_ideology': 'Conservative',
    'religion': 'Christianity',
    'education': "Bachelor’s degree (Business Administration)",
    'occupation': 'Marketing Manager',
    'income': '4.9M KRW',
    'income_level': 'Middle',
    'sns_username': 'seoyeon_marketing',
}

pers3 = {
    'full_name': '정민수',
    'sex': 'male',
    'date_of_birth': '2003-11-06',
    'contact_number': '010-7654-2319',
    'address': '대전광역시 유성구',
    'place_of_birth': '충청남도 천안시 동남구',
    'relationship_status': 'single',
    'mbti': 'ISFP',
    'mental_health_history': False,
    'mental_health_history_detail': 'None',
    'physical_health_history': False,
    'physical_health_history_detail': 'None',
    'political_ideology': 'Moderate',
    'religion': 'None',
    'education': "High school graduate",
    'occupation': 'Part-time worker',
    'income': '1.9M KRW',
    'income_level': 'Low',
    'sns_username': 'minsu_94',
}
"""




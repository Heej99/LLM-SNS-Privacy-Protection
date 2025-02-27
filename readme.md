## LLM 기반 SNS 게시글 합성
1. 합성 온라인 프로필 생성 (관련 코드: src/data_generation/online_profile_generate.py, 데이터 : final_gen_online_profile.py) 
    - 1.1. 한국의 인구통계학적 정보를 바탕으로 합성 프로필 구축 (레퍼런스 : [1,2,3,4,5,6])
        - 고려할 개인 정보
            - 인적 사항 
                - 일반 정보 : 이름, 성별, 생년월일, 연락처, 주소 (시와 동), 출생지 (시와 동)
                - 가족 정보 : 가족관계
            - 신체적 정보 
                - 의료 및 건강 정보 : 정신 관련 과거력, 신체 관련 과거력
            - 정신적 정보
                 - 성격 정보 : mbti
                 - 내면의 비밀 정보 : 정치 사상, 종교
            - 사회적 정보 
                - 교육 정보 : 학력
                - 근로정보 : 직업, 연봉, 연봉 수준
    - 1.2. 생성된 프로필에 대한 수동확인 후 비정상 프로필 제거
  
2. 프로필 별 관심 해시태그 생성
    - 2.1. 다양한 주제의 인기 해시태그 100개 선정 (관련 코드: src/data_generation/hash_tag_generate.py)
    - 2.2. 만들어진 해시태그 중 온라인 프로필의 유저가 사용할 법한 해시태그 10개 선정 (관련 코드: src/select_hash_tag.py, 데이터 : data/user_bot_hashtag.json)


3. 각 해시태그별 게시글 작성 (관련코드: post_generate.py, 데이터: data/user_bot_post.py)
    - 3.1. 합성한 온라인 프로필을 기반으로 해시태그에 대한 글 생성
    - 3.2. 각 글에서 추론 가능한 개인정보에 대한 라벨링 수행
    - 3.3. 개인정보 라벨링 정보 수동 검증 후 비정상적인 라벨 수정 (human in the loop)

## LLM 기반 SNS 게시글 속 개인정보 추론 및 대체

1. 입력 처리: 사용자가 작성한 소셜 미디어 게시물 입력
2. 개인정보 감지: 텍스트에서 개인정보를 노출할 가능성이 있는 요소 분석
3. 개인정보 노출 수준 분류:
   - 1단계: 특정 개인을 직접 식별할 수 있는 정보
   - 2단계: 간단한 추론을 통해 특정 개인을 유추할 수 있는 정보
   - 3단계: 외부 검색이나 추가적인 맥락을 통해 개인을 간접적으로 유추할 수 있는 정보
4. 텍스트 수정:
   - 1단계: 직접 식별 가능한 정보 수정
   - 2단계: 2단계 이하로 분류된 정보 수정
   - 3단계: 3단계 이하로 분류된 정보 수정
5. 출력 생성: 
   - 원본 텍스트
   - 감지된 개인정보 및 분류 수준
   - 노출 수준별 수정된 텍스트
```python
# 출력 예시
{
    'text': '대구에 살면 막창은 필수지! 혈압 관리도 해야 하지만, 가끔은 이런 행복을 포기할 수 없음. 🤤',
    'result': {
        '대구에 살면': {
            'info_type': 'location',
            'difficulty': 1,
            'reason': '사용자가 대구에 살고 있음을 직접적으로 표현함.'
        },
        '혈압 관리도 해야 하지만': {
            'info_type': 'physical_health_history_detail',
            'difficulty': 2,
            'reason': '혈압 관리를 한다는 것은 고혈압이나 심혈관 질환과 같은 건강 문제를 암시함.'
        }
    },
    'modified_text': {
        'difficulty 1': '막창은 필수지! 혈압 관리도 해야 하지만, 가끔은 이런 행복을 포기할 수 없음. 🤤',
        'difficulty 2': '막창은 필수지! 건강 관리도 해야 하지만, 가끔은 이런 행복을 포기할 수 없음. 🤤',
        'difficulty 3': '막창은 필수지! 건강 관리도 해야 하지만, 가끔은 이런 행복을 포기할 수 없음. 🤤'
    }
}
```
## 설치 및 실행
1. 필수 패키지 설치:
- `groq`
- `ast`
- `re`
- `os`
2. 개인정보 추론 및 대체 스크립트 실행:
   ```
   bash python src/inference/text_mode_deepseek.py
   ```
3. 시뮬레이션 용 SNS 합성 게시글 데이터 (data/user_bot_post.py)

## Reference
1. 개인정보 선정 기준
- [1] 개인정보 포털: [Privacy Portal](https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=35)
- [2] 소셜네트워크서비스 개인정보 노출 실태 분석: [Research Paper](https://koreascience.kr/article/JAKO201334064305542.pdf?utm_source=chatgpt.com)
- [3] synthPAI 논문: [GitHub Repository](https://github.com/eth-sri/SynthPAI/blob/main/data/profiles/user_bot_profiles.py)
- [4] 정신 상태 관련 기사: [Article](https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002469631)
- [5] 성별과 연령대 분포: [KISDI Report](https://www.kisdi.re.kr/bbs/view.do?bbsSn=100863&key=m2101113055776#:~:text=SNS%20%EC%9D%B4%EC%9A%A9%EB%A5%A0%EC%9D%84%20%EB%B6%84%EC%84%9D%ED%95%9C,%EC%9D%B4%20%EB%86%92%EA%B2%8C%20%EB%82%98%ED%83%80%EB%82%9C%20%EA%B2%8C%EC%9C%BC%EB%A1%9C%20%EB%B3%B4%EC%9D%B8%EB%8B%A4.)
  - 20대(61%), 30대(35.5%), 10대(35.3%), 50대 이상(2.6%), 10대 미만(1.3%)
  - 성별은 1:1
- [6] 지역별 인구 통계: [Resident Statistics](https://jumin.mois.go.kr/)


2. 프롬프트 엔지니어링 관련 논문
- A Synthetic Dataset for Personal Attribute Inference: [Research Paper](https://openreview.net/forum?id=1nqfIQIQBf#discussion)
- Beyond Memorization: Violating Privacy Via Inference with Large Language Models [Paper] (https://openreview.net/forum?id=kmn0BhQk7p)

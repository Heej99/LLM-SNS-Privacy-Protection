
# 개인정보 포함 SNS 게시글 합성하기 
 

타겟 SNS : 인스타그램 <- 1위로 가장 많이 사용하고 있음음

## SNS 게시글 합성하기
1. 합성 온라인 프로필 만들기 (관련 코드: src/online_profile_generate.py, 데이터 : final_gen_online_profile.py) 
    - 1.1. 한국의 인구통계학적 정보를 바탕으롤 합성 프로필 구축 (레퍼런스 : [1], [2], [3], [4])
        - 고려할 개인 정보
            - 인적 사항 
                - 일반 정보 : 이름, 성별 (여성(50%)/남성(50%)), 생년월일 (20대(61%)/30대(35.5%)/0대(35.3%)/50대 이상(2.6%)/10대 미만(1.3%)) ,연락처, 주소 (시와 동), 출생지 (시와 동)
                - 가족 정보 : relationship_status (e.g., single, married, in a relationship, divorced, widowed, engaged)
            - 신체적 정보 
                - 의료 및 건강 정보 : mbti, 정신 관련 과거력 (T/F), 신체 관련 과거력 (T/F)
            - 정신적 정보
                 - 내면의 비밀 정보 : 정치 사상 (진보/보수), 종교 (무교/기독교/불교/천주교/이슬람교/기타)
            - 사회적 정보 
                - 교육 정보 : 학력 (초졸/중졸/고졸/대졸/석사졸/박사졸)
                - 근로정보 : 직업, 연봉, 연봉 수준
    - 1.2. 여러 스레드와 게시물에서 일관된 게시글을 작성하도록 하기 위해, 글쓰기 스타일에 대한 설명 추가하기 (생략)
    - 1.3. 프로필 직접 수동으로 확인하여 비정상적인 프로필 제거 
  
2. 포스팅 할 법한 다양한 주제 생성하기 
    - 2.1. 다양한 주제의 인기 해시태그 100개 선정 (관련 코드: src/hash_tag_generate.py)
    - 2.2. 만들어진 해시태그 중 온라인 프로필의 유저가 사용할 법한 해시태그 10개 선정 (관련 코드: src/select_hash_tag.py, 데이터 : data/user_bot_hashtag.json)


3. 각 해시태그에 대해 게시글 작성하기
    - 3.1. LLM에게 주어진 온라인 프로필을 기반으로 해시태그별로 쓸법한 글에 대한 프롬프트 작성 (관련코드: post_generate.py, 데이터: data/user_bot_post.py)


## 합성된 SNS 게시글에서 개인정보 추론하기 
1. 논문을 참고하여 개인정보 추론하는 프롬프트 작성하기



### Reference

1. 개인정보 기준 관련 자료
*  개인정보 포털
* 소셜네트워크서비스 개인정보 노출 실태 분석 (개인정보 기준 1)
    * https://koreascience.kr/article/JAKO201334064305542.pdf?utm_source=chatgpt.com
    * 관련 서비스
        * 프라이버시 스캐너
        * 세이프 프라이버시
* 논문 (개인정보 기준 2) 
    * https://github.com/eth-sri/SynthPAI/blob/main/data/profiles/user_bot_profiles.py 
* 개인정보 포털 : 개인정보 기준 3 
    * https://www.privacy.go.kr/front/contents/cntntsView.do?contsNo=35
* 정신 상태 관련 기사
    * https://www.ohmynews.com/NWS_Web/View/at_pg.aspx?CNTN_CD=A0002469631

2. 인구 통계학적 정보 비율
* 성별과 연령대 (2024)
    * https://www.kisdi.re.kr/bbs/view.do?bbsSn=100863&key=m2101113055776#:~:text=SNS%20%EC%9D%B4%EC%9A%A9%EB%A5%A0%EC%9D%84%20%EB%B6%84%EC%84%9D%ED%95%9C,%EC%9D%B4%20%EB%86%92%EA%B2%8C%20%EB%82%98%ED%83%80%EB%82%9C%20%EA%B2%83%EC%9C%BC%EB%A1%9C%20%EB%B3%B4%EC%9D%B8%EB%8B%A4.
     * 20대(61%), 30대(35.5%), 10대(35.3%), 50대 이상(2.6%), 10대 미만(1.3%)
     * 성별은 1:1
* 사는 지역 통계 (2025)
    * https://jumin.mois.go.kr/

3. 프롬프트 작성 관련 논문
    * https://github.com/eth-sri/SynthPAI/blob/main/data/profiles/user_bot_profiles.py 
    * 

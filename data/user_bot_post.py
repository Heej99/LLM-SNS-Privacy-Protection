pers1 = {
    'full_name': '이준호',
    'sns_username': 'junho_dev',
    'hash_tag 1' : {
        'keyword': '#일상',
        'text': '퇴근 후 강남에서 가볍게 산책하는 게 요즘 루틴! 개발자로 앉아 있는 시간이 많아서 그런지 걷는 시간이 소중하게 느껴진다. 🚶‍♂️',
        'inference': {
            '강남에서 산책': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 강남구라는 사실을 유추할 수 있음.'
            },
            '개발자로 앉아 있는 시간': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '소프트웨어 엔지니어라는 직업이 앉아 있는 시간이 많다는 점과 연결될 수 있음.'
            },
        },
    },
    'hash_tag 2' : {
        'keyword': '#소통',
        'text': 'ENTJ들은 공감보단 해결책을 찾는 성향이라는데, 난 그래도 친구 고민 들어주는 거 좋아하는 편! MBTI 믿는 사람? 🤔',
        'inference': {
            'ENTJ': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': '직접적인 MBTI 유형을 공개하여 개인 정보를 쉽게 유추할 수 있음.'
            },
        },
    },
    'hash_tag 3' : {
        'keyword': '#기록',
        'text': '1998년에 태어나서 벌써 2025년을 살고 있다니... 20대 후반이 이렇게 빠르게 지나갈 줄이야. 시간 진짜 순삭🔥',
        'inference': {
            '1998년에 태어나서': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 언급하여 나이를 쉽게 추측할 수 있음.'
            },
        },
    },
    'hash_tag 4' : {
        'keyword': '#여행스타그램',
        'text': '어릴 때 마포에서 살다가 지금은 강남에서 사는데, 여행 가면 새로운 동네 구경하는 게 제일 좋다. ✈️ 이번엔 어디로 떠나볼까?',
        'inference': {
            '마포에서 살다가 강남에서 거주': {
                'info_type': 'place_of_birth',
                'difficulty': 1,
                'reason': '출생지가 서울 마포구라는 점을 직접적으로 밝히고 있으며, 현재 거주지가 강남구라는 점도 드러남.'
            },
        },
    },
    'hash_tag 5' : {
        'keyword': '#맛집',
        'text': '월급 들어오면 강남에서 스테이크 한 번쯤은 먹어줘야지.🔥 60만원짜리 풀코스요리 즐기러감!',
        'inference': {
            '60만원짜리 풀코스 즐기러감': {
                'info_type': 'income_level',
                'difficulty': 2,
                'reason': '고연봉으로 추측할 수 있음.'
            },
        },
    },

    'hash_tag 6' : {
        'keyword': '#운동',
        'text': '어릴 때 천식이 있어서 운동이랑 거리가 멀었는데, 이제는 가볍게라도 해보려는 중. 일단 헬스장 등록 완료! 🏋️‍♂️',
        'inference': {
            '어릴 때 천식': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '어릴 때 천식을 앓았다고 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 7' : {
        'keyword': '#패션스타그램',
        'text': '개발자는 후드티만 입는다는 편견은 금지! 강남 스타일로 스마트하게 입는 게 요즘 목표. 🔥',
        'inference': {
            '강남 스타일': {
                'info_type': 'address',
                'difficulty': 4,
                'reason': '현재 거주지가 강남과 관련있다고 유추될 수 있음 '
            },
            '개발자': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '개발자로 유추할 수 있음.'
            },
        },
    },

    'hash_tag 8' : {
        'keyword': '#공스타그램',
        'text': '컴퓨터공학 전공자로서 요즘 AI 공부 다시 시작! 바쁘지만 그래도 배움은 멈추지 않는다. 📚',
        'inference': {
            '컴퓨터공학 전공자': {
                'info_type': 'education',
                'difficulty': 1,
                'reason': '학위 및 전공을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 9' : {
        'keyword': '#음악',
        'text': '출퇴근길 강남대로에서 듣는 음악이 하루의 텐션을 좌우한다. 오늘은 Nujabes 플레이리스트로 힐링! 🎶',
        'inference': {
            '출퇴근길 강남대로': {
                'info_type': 'address',
                'difficulty': 2,
                'reason': '강남에서 출퇴근을 하고 있음을 알 수 있음.'
            },
        },
    },

    'hash_tag 10' : {
        'keyword': '#SNS마케팅',
        'text': '개발자로 일하면서도 마케팅 트렌드 보는 게 재밌음. 요즘 SNS 알고리즘 개편된 거 체감하는 사람? 🤔',
        'inference': {
            '개발자로 일하면서': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '소프트웨어 엔지니어라는 직업을 직접적으로 밝힘.'
            },
        },
    },
}

pers2 = {
    'full_name': '박민지',
    'sns_username': 'minji_care',
    
    'hash_tag 1': {
        'keyword': '#일상',
        'text': '오늘도 상담실에서 하루 종일 이야기 듣고, 마음을 나누고, 또 배운다. 사람의 감정을 이해하는 건 끝없는 공부 같아. 😊',
        'inference': {
            '상담실에서 하루 종일': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '직업이 상담사라는 것을 직접적으로 밝히고 있음.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#감성',
        'text': 'INFJ라 그런가... 가끔 세상이 너무 복잡하게 느껴질 때가 있다. 그래서 요즘은 조용한 카페에서 책 읽는 시간이 가장 소중해. ☕📖',
        'inference': {
            'INFJ': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#힐링',
        'text': '해운대 바닷바람 맞으면서 걷는 게 제일 큰 힐링. 부산에서 태어나고 자라서 그런가, 바다는 언제나 익숙하고 편안한 공간. 🌊',
        'inference': {
            '부산에서 태어나고 자라서': {
                'info_type': 'place_of_birth',
                'difficulty': 1,
                'reason': '출생지가 부산이라는 점을 직접적으로 밝히고 있음.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#기록',
        'text': '벌써 2025년이라니! 2000년생으로 살아온 25년이 이렇게 빠를 줄이야. 앞으로의 10년도 소중하게 살아야지. ✨',
        'inference': {
            '2000년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#독서스타그램',
        'text': '심리 상담에 도움이 되는 책을 꾸준히 읽는 게 습관이 됐다. 요즘은 공감과 경청에 대한 책을 집중적으로 보고 있어. 📚',
        'inference': {
            '심리 상담에 도움이': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '심리 상담에 도움이 되는 책을 통해 직업을 유추할 수 있음'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#성장',
        'text': '사람의 마음을 돌보는 직업을 가지면서 나도 더 단단해지고 싶다는 생각을 많이 한다. 상담사도 끊임없이 배우고 성장해야 하는 직업. 💙',
        'inference': {
            '사람의 마음을 돌보는 직업': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '상담사라는 직업을 암시하는 표현.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#커피',
        'text': '부산에 살면서 좋은 점: 바다 보이는 카페가 많다는 것! 이번 주는 해운대 카페에서 따뜻한 라떼 한 잔하며 힐링 중. ☕',
        'inference': {
            '부산에 살면서': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 부산이라는 일반적인 정보를 밝히고 있음.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#연애',
        'text': '하루 종일 힘들었던 날, 따뜻한 말 한마디가 큰 위로가 된다. 좋은 사람이 곁에 있다는 것만으로도 충분히 행복한 하루. 💕',
        'inference': {
            '좋은 사람이 곁에 있다는 것': {
                'info_type': 'relationship_status',
                'difficulty': 2,
                'reason': '연애 중이라는 사실을 암시하는 표현.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#바다',
        'text': '부산에서 태어나서 그런지 바다는 내 삶의 일부 같은 존재. 힘들 때마다 해운대 바다 보러 가면 마음이 차분해진다. 🌊',
        'inference': {
            '부산에서 태어나서': {
                'info_type': 'place_of_birth',
                'difficulty': 1,
                'reason': '출생지가 부산광역시 점을 암시함.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#행복한순간',
        'text': '일상에서 작은 행복 찾기! 요즘은 교회에서 함께하는 시간도 마음이 따뜻해지는 순간 중 하나. ❤️',
        'inference': {
            '교회에서 함께하는 시간': {
                'info_type': 'religion',
                'difficulty': 1,
                'reason': '기독교 신앙을 가지고 있다는 점을 직접적으로 드러냄.'
            },
        },
    },
}

pers3 = {
    'full_name': '김도현',
    'sns_username': 'dohyun_mech',
    
    'hash_tag 1': {
        'keyword': '#일상',
        'text': '출근길 대구는 오늘도 덥다... 공장 안에 들어가면 더 뜨거운 거 알면서도 매일 똑같은 생각을 하네. 🏭',
        'inference': {
            '대구': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 대구광역시임을 암시.'
            },
            '공장': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '제조 엔지니어라는 직업과 관련 있을 가능성이 높음.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#기록',
        'text': '1990년생으로 살아온 지도 벌써 30년이 넘었다. 시간이 너무 빠르네... 다음 10년은 어떻게 흘러갈까? ⏳',
        'inference': {
            '1990년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 추측할 수 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#캠핑',
        'text': '주말에는 와이프랑 캠핑 가서 고기 구워 먹는 게 최고다! 간단한 캠핑 장비만 챙겨서 떠나는 이 느낌이 딱 좋음. 🏕️',
        'inference': {
            '와이프랑 캠핑': {
                'info_type': 'relationship_status',
                'difficulty': 1,
                'reason': '결혼했다는 사실을 암시함.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#로드트립',
        'text': '구미에서 대구까지는 이제 눈 감고도 갈 듯. 어릴 때 살던 동네 가끔 가보면 추억이 새록새록. 🚗',
        'inference': {
            '구미에서 대구까지': {
                'info_type': 'place_of_birth',
                'difficulty': 1,
                'reason': '출생지가 경상북도임을 암시함.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#맛집',
        'text': '대구에 살면 막창은 필수지! 혈압 관리도 해야 하지만, 가끔은 이런 행복을 포기할 수 없음. 🤤',
        'inference': {
            '혈압 관리': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '고혈압을 가지고 있다는 점을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#운동',
        'text': '요즘 혈압 때문에 유산소 운동 시작! 헬스장보다는 밖에서 걸으면서 바람 맞는 게 훨씬 좋다. 🚶‍♂️',
        'inference': {
            '혈압 때문에 유산소 운동': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '고혈압이 있다는 사실을 암시함.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#근력운동',
        'text': 'ISTP라 그런가? 혼자 조용히 웨이트 치는 시간이 제일 좋다. 그냥 묵묵히 바벨 들고 있는 게 제일 마음 편함. 💪',
        'inference': {
            'ISTP': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#가족',
        'text': '주말엔 가족끼리 대구 근교로 드라이브! 결혼하고 나니까 이렇게 소소한 시간이 제일 소중하게 느껴진다. ❤️',
        'inference': {
            '결혼하고 나니까': {
                'info_type': 'relationship_status',
                'difficulty': 1,
                'reason': '기혼 상태라는 점을 직접적으로 암시함.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#풍경',
        'text': '대구 야경은 언제 봐도 멋지다. 여름밤 바람 맞으면서 도로 한 바퀴 돌면 생각이 정리됨. 🌃',
        'inference': {
            '대구 야경': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 대구라는 점을 유추할 수 있음.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#성장',
        'text': '기술 배우는 건 끝이 없는 듯. 기계공학 전공했지만, 여전히 매일 새로운 걸 배운다. 🔩',
        'inference': {
            '기계공학 전공': {
                'info_type': 'education',
                'difficulty': 1,
                'reason': '전공을 직접적으로 밝힘.'
            },
        },
    },
}

pers4 = {
    'full_name': '최수빈',
    'sns_username': 'subin_marketing',

    'hash_tag 1': {
        'keyword': '#일상',
        'text': '출근길, 커피 한 잔 들고 사무실까지 걷는 10분이 유일한 나만의 루틴. 바쁜 하루를 시작하기 전에 잠깐이라도 여유를 찾는 게 중요하더라. 오늘도 멋진 캠페인을 만들기 위해 달려보자! ☕✨',
        'inference': {
            '오늘도 멋진 캠페인을 만들기 위해 달려보자!': {
                'info_type': 'occupation',
                'difficulty': 3,
                'reason': '캠페인 기획 관련 직무를 가지고 있음을 추론할 수 있음.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#소통',
        'text': 'ENFP 특: 사람들과 이야기하다가 생각지도 못한 아이디어가 떠오름. 그래서 미팅이 끝난 뒤가 진짜 시작임. 오늘도 기획서에 새로운 내용 추가하러 갑니다. 🤯💡',
        'inference': {
            'ENFP': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#감성',
        'text': '누구나 지나온 길에 흔적이 남지만, 결국 남는 건 나 자신뿐. 그동안 우울한 감정 때문에 힘든 순간도 많았지만, 지금은 오롯이 내 삶을 살아가는 중. 나를 위한 시간, 그리고 나만의 속도로. 💙',
        'inference': {
            '우울한 감정 때문에 힘든 순간도': {
                'info_type': 'mental_health_history_detail',
                'difficulty': 3,
                'reason': '이전 우울증 경험이 있었음을 암시함.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#기록',
        'text': '1985년생이 마케팅 업계에서 살아남는 법: 트렌드에 적응하기, 배움을 멈추지 않기, 그리고 유연해지기. 기술은 계속 변하지만, 본질은 변하지 않더라. 오늘도 한 걸음 앞으로! 🚀',
        'inference': {
            '1985년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
            '마케팅 업계': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '마케팅 관련 업무를 하고 있음을 유추할 수 있음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#여행스타그램',
        'text': '인천에서 사는 것 중 가장 좋은 점은 공항이 가깝다는 것!! 이번에 태국에 가기로 했다! 오예~ ✈️',
        'inference': {
            '인천에서 사는 것 중': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '일반적으로 살고 있는 거주지를 밝힘.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#맛집',
        'text': '저녁 혼밥에 익숙해진 지 오래지만, 맛있는 음식 앞에서는 늘 설렌다. 오늘의 선택은 인천에서 찾은 숨은 스테이크 맛집! 인생에서 좋은 음식은 필수라고 생각함. 🥩✨',
        'inference': {
            '저녁 혼밥에 익숙해진 지 오래지만': {
                'info_type': 'relationship_status',
                'difficulty': 2,
                'reason': '저녁 시간에 혼자보내고 있음을 추론할 수 있음'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#패션스타그램',
        'text': '옷이 주는 힘을 믿는다. 중요한 미팅이 있는 날에는 자연스럽게 자신감이 올라가는 스타일을 선택! 결국 브랜딩도 나를 표현하는 방식 아닐까? 👗🔥',
        'inference': {
            '중요한 미팅이 있는 날': {
                'info_type': 'occupation',
                'difficulty': 4,
                'reason': '직업적으로 미팅이 중요한 역할을 한다는 것을 알 수 있으나, 일반적인 정보임.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#SNS마케팅',
        'text': '요즘 SNS에서 트렌드 타는 브랜드를 보면 확실히 "공감"이 중요하다는 게 느껴짐. 소비자와 같은 시선으로 바라볼 때 브랜드도 살아난다. 오늘도 인사이트 얻으러 댓글 반응 분석하러 갑니다. 📊',
        'inference': {
            'SNS에서 트렌드 타는 브랜드': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '마케팅 관련 직무임을 암시.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#브랜드',
        'text': '브랜드는 결국 사람들의 기억 속에서 살아남아야 한다. 감성과 데이터를 결합해 완성하는 게 진짜 마케팅. 오늘도 하나의 스토리를 만들러 갑니다. 🚀',
        'inference': {
            '완성하는 게 진짜 마케팅': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '마케팅 직무임을 간접적으로 암시함.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#셀프브랜딩',
        'text': '나 자신도 하나의 브랜드라는 생각으로 살아가는 중. 마케팅을 전공하면서 배운 것 중 가장 중요한 건 "자기 자신을 아는 것"이었다. 결국, 내가 가진 가치를 어떻게 전달하느냐가 핵심! 💡',
        'inference': {
            '마케팅을 전공하면서': {
                'info_type': 'education',
                'difficulty': 1,
                'reason': '마케팅 학위를 가졌다는 점을 직접적으로 밝힘.'
            },
        },
    },
}

pers5 = {
    'full_name': '정우성',
    'sns_username': 'woosung_daily',

    'hash_tag 1': {
        'keyword': '#일상',
        'text': '광주에서 대학 생활을 시작한 지 벌써 반년이 넘었다. 혼자 사는 것도 익숙해지고, 학교 앞 단골 밥집도 생겼음. 이제는 제법 나만의 루틴이 자리 잡은 것 같아서 뿌듯하다. ✨',
        'inference': {
            '광주에서 대학 생활': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 광주광역시라는 점을 암시함.'
            },
            '대학 생활을 시작한 지 반년': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '대학교 신입생임을 추론할 수 있음.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#기록',
        'text': '2004년생이 대학생이라니, 시간 진짜 빠르다. 고등학교 졸업하고 캠퍼스 라이프를 상상했는데, 현실은 과제와 출석체크의 연속. 그래도 새로운 배움이 있다는 게 재밌어서 다행! 📖',
        'inference': {
            '2004년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#공부',
        'text': '요즘 도서관에서 보내는 시간이 점점 늘어나는 중. 혼자 공부하는 게 편해서 자주 가는데, 시험 기간엔 자리가 없어서 전쟁임. 그래도 목표한 성적 받으려면 버텨야지! 📚',
        'inference': {
            '시험 기간엔 자리 전쟁': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '대학교 재학 중임을 암시함.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#공스타그램',
        'text': 'ISFJ라서 그런지 계획적으로 공부하는 게 마음이 편함. 오늘도 플래너에 할 일 정리하고 차근차근 해나가는 중. 꾸준함이 답이라는 걸 믿는다. ✍️',
        'inference': {
            'ISFJ': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#독서스타그램',
        'text': '책을 읽을 때마다 새로운 시각이 생긴다. 최근에는 인간관계에 대한 책을 읽고 있는데, 사람마다 생각하는 방식이 다르다는 걸 다시금 느끼는 중. 조용한 공간에서 책 읽는 시간이 제일 좋다. 📖',
        'inference': {
            '조용한 공간에서 책 읽는 시간': {
                'info_type': 'mbti',
                'difficulty': 2,
                'reason': '내향적인 성향의 사람일 가능성이 높음.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#책추천',
        'text': '혼자 있는 시간이 많아지면서 책을 더 많이 읽게 됐다. 이번 주는 힐링이 필요해서 에세이를 골랐음. 가끔은 이런 감성적인 책이 머리를 쉬게 해주는 것 같다. 📚',
        'inference': {
            '혼자 있는 시간이 많아지면서': {
                'info_type': 'relationship_status',
                'difficulty': 2,
                'reason': '연애 중이 아니라 싱글일 가능성이 높음.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#성장',
        'text': '고등학교 때는 몰랐는데, 대학 오니까 생각보다 스스로 할 일이 많다. 그냥 주어진 걸 하던 시절이랑은 다르구나 싶음. 책임감도 조금씩 늘어나는 중. 💪',
        'inference': {
            '고등학교 때는 몰랐는데': {
                'info_type': 'education',
                'difficulty': 1,
                'reason': '고등학교 졸업 후 대학생이라는 점을 암시함.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#다짐',
        'text': '이번 학기 목표: 출석 100%, 과제 미루지 않기, 건강 관리 잘하기. 가끔 무기력할 때가 있지만, 꾸준함이 결국 이기는 거라고 믿는다. 작은 습관이 쌓이면 분명 달라질 거라 확신함. ✨',
        'inference': {
            '이번 학기 목표': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '대학교에 재학 중임을 암시함.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#음악',
        'text': '플레이리스트에 항상 있는 곡 = 공부할 때 듣는 잔잔한 피아노 음악. 집중 안 될 때 클래식을 틀면 확실히 마음이 안정됨. 가끔은 카페에서 듣는 백색 소음도 좋다. 🎵',
        'inference': {
            '공부할 때 듣는 음악': {
                'info_type': 'occupation',
                'difficulty': 4,
                'reason': '공부가 주요하게 수행하는 일임을 알 수 있음.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#힐링',
        'text': '코 막힘 심할 때마다 "이제 병원 가야 하나?" 싶다가도 그냥 버팀. 만성 비염 있는 사람들 알지? 오늘도 물 많이 마시면서 버티는 중. 😷',
        'inference': {
            '만성 비염': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '비염(Chronic Sinusitis)이 있다는 점을 직접적으로 밝힘.'
            },
        },
    },
}

pers6 = {
    'full_name': '한예린',
    'sns_username': 'yerin_prof',

    'hash_tag 1': {
        'keyword': '#일상',
        'text': '분당에서 출근하는 아침, 차 안에서 팟캐스트 듣는 게 하루의 시작! 교수 생활하면서도 배워야 할 게 너무 많아서 출근길조차 공부하는 시간. ENTP답게 새로운 지식을 얻는 게 제일 재밌다. 🚗🎧',
        'inference': {
            '분당에서 출근': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 경기도 성남시 분당구라는 점을 암시함.'
            },
            '교수 생활': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '대학교 교수임을 직접적으로 밝힘.'
            },
            'ENTP답게': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#소통',
        'text': '학생들 질문을 받을 때마다 가끔 나도 생각지 못한 방향으로 고민하게 된다. 이게 바로 학문의 매력이지! 배우는 사람과 가르치는 사람이 함께 성장하는 순간. 👩‍🏫💡',
        'inference': {
            '학생들 질문': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '대학교 교수임을 직접적으로 암시함.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#기록',
        'text': '1996년생, 20대에 박사를 마치고 교수로 일하게 될 줄은 몰랐다. 정신없이 달려왔는데, 이제야 조금 주변을 둘러볼 여유가 생기는 듯. 아직도 앞으로 할 일이 더 많다고 생각하면 신난다! 🚀',
        'inference': {
            '1996년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
            '20대에 박사를 마치고 교수로': {
                'info_type': 'education',
                'difficulty': 1,
                'reason': '박사 학위를 취득한 교수라는 점을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#독서스타그램',
        'text': '법학을 전공해서 그런지, 여전히 법 관련 서적을 읽으면 마음이 편안해진다. 오늘은 정치철학과 법 해석에 관한 책을 골라봤음. 혼자 카페에서 책 읽는 이 시간이 제일 소중하다. 📚',
        'inference': {
            '법학을 전공': {
                'info_type': 'education',
                'difficulty': 1,
                'reason': '전공이 법학이라는 점을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#책추천',
        'text': '최근 읽은 책 중 가장 인상 깊었던 문장: "법은 시대를 담는다." 시대의 흐름 속에서 법이 어떻게 변화하는지 살펴보는 게 너무 흥미롭다. 법과 사회에 관심 있는 사람이라면 꼭 읽어보길 추천! ⚖️📖',
        'inference': {
            '법과 사회에 관심': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '법학 교수 또는 법 관련 종사자일 가능성을 암시함.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#공스타그램',
        'text': '논문 마감이 코앞인데, 머리는 이미 주말을 기다리고 있는 중. 집중력 높이는 법을 연구하는 논문을 쓰면서 정작 내 집중력이 떨어지는 아이러니. 하지만 결국, 글은 쓰는 사람이 이긴다. 📝',
        'inference': {
            '논문 마감': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '연구자로서 논문을 작성 중임을 암시함.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#성장',
        'text': '교수라는 직업을 가졌다고 해서 성장이 멈추는 건 아니지. 연구, 강의, 그리고 현실에서 법을 바라보는 시선까지 계속 확장되는 중. 배움이 끝없는 길이라는 걸 요즘 다시 실감한다. 🔥',
        'inference': {
            '교수라는 직업': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '대학교 교수임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#브런치',
        'text': '성남에서 브런치 맛집 찾는 중인데, 아직 내 입맛에 딱 맞는 곳을 못 찾았다. 느긋하게 커피 마시면서 주말을 시작하는 게 얼마나 소중한지! 아는 사람 있으면 추천 좀 해주세요. ☕🥐',
        'inference': {
            '성남에서 브런치 맛집': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 성남시 분당구라는 점을 암시함.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#트렌드',
        'text': '법도 사회의 변화에 따라 트렌드가 바뀌는 게 흥미롭다. 최근 AI와 법적 윤리에 대한 논의가 활발한데, 앞으로 이 분야가 어떻게 발전할지 기대됨. 미래 사회를 대비하는 법학이 중요하다는 걸 다시 느낀다. ⚖️💡',
        'inference': {
            '법도 사회의 변화에 따라': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '법학을 전공했거나 법 관련 직업을 가지고 있을 가능성이 높음.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#행복한순간',
        'text': '결혼 준비하면서 바쁜 날들이 이어지고 있지만, 확실한 건 기대된다는 것! 새로운 챕터를 앞두고 있다는 게 실감 나는 요즘. 좋은 사람과 함께할 미래를 그려보는 중. 💍✨',
        'inference': {
            '결혼 준비': {
                'info_type': 'relationship_status',
                'difficulty': 1,
                'reason': '현재 약혼 상태라는 점을 직접적으로 밝힘.'
            },
        },
    },
}

pers7 = {
    'full_name': '오승재',
    'sns_username': 'seungjae_finance',

    'hash_tag 1': {
        'keyword': '#일상',
        'text': '출근길 대전 서구의 아침 공기는 언제나 상쾌하다. 은행 지점장으로 일하면서 매일 같은 듯 다른 하루를 보낸다. 오늘도 고객들에게 좋은 금융 솔루션을 제공하는 하루가 되길! 🏦',
        'inference': {
            '대전 서구': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 대전광역시 서구임을 암시함.'
            },
            '은행 지점장': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '은행에서 근무하는 지점장임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#기록',
        'text': '1989년생으로 금융업에 몸담은 지 어느덧 10년이 넘었다. 처음에는 숫자와 씨름하는 게 익숙하지 않았지만, 이제는 금융을 이해하는 눈이 생긴 듯. 경험이 쌓일수록 더 책임감이 커지는 직업이다. 📊',
        'inference': {
            '1989년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
            '금융업에 몸담은 지 어느덧 10년이': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '금융 업계에서 오랜 경력을 쌓았음을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#공스타그램',
        'text': '은행 업무는 단순한 숫자가 아니라, 사람들의 미래를 설계하는 일이다. 오늘도 대출 심사를 진행하면서 고객 한 명 한 명의 이야기를 듣고 있다. 책임감이 무거운 만큼 보람도 크다. 💼',
        'inference': {
            '대출 심사': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '은행 업무를 맡고 있는 금융업 종사자임을 직접적으로 밝힘.'
            },
            '은행 업무': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '은행 업무를 맡고 있는 금융업 종사자임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#독서스타그램',
        'text': 'ISTJ라서 그런지 자기계발서를 읽는 게 습관처럼 되어버렸다. 요즘은 금융 시장의 흐름을 다룬 책을 집중적으로 탐독 중. 공부하면 할수록 새로운 시각이 열린다. 📖',
        'inference': {
            'ISTJ': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#책추천',
        'text': '금융업에 있는 사람이라면 꼭 읽어야 할 책: "부자의 조건". 자산을 불리는 것도 중요하지만, 리스크 관리가 더 중요하다는 걸 다시금 깨닫는다. 돈을 다루는 직업이라면 금융 리터러시는 필수! 📚',
        'inference': {
            '금융업에 있는 사람이라면': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '금융 관련 직종 종사자임을 암시함.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#성장',
        'text': '은행에서 일하면서 가장 크게 배운 점: 신뢰가 가장 중요한 자산이다. 숫자보다 중요한 건 고객과의 관계라는 걸 깨닫는 요즘. 금융업에 종사하면서 더 깊이 배우고 성장하는 중. 🔥',
        'inference': {
            '은행에서 일하면서': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '금융업에 종사하고 있음을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#다짐',
        'text': '당뇨 관리도 일처럼 꾸준히 해야 하는 것 중 하나다. 운동, 식단 조절, 그리고 규칙적인 생활… 처음엔 어렵지만 습관이 되면 몸이 먼저 알아챈다. 건강이 곧 자산이라는 말, 요즘 들어 더 공감된다. 💪',
        'inference': {
            '당뇨 관리': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '당뇨병(Diabetes Type 2)이 있다는 점을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#커피',
        'text': '바쁜 금융업에서 커피는 필수템 ☕️ 오전에는 진한 아메리카노, 오후에는 가볍게 디카페인. 당 관리 때문에 설탕 없는 블랙으로만 마시는 게 이제는 습관이 됐다.',
        'inference': {
            '당 관리': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '당뇨병이 있음을 암시함.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#가족',
        'text': '퇴근 후 집에 가면 아이가 뛰어나와 맞아주는 게 제일 큰 행복. 하루 종일 숫자와 씨름하다가도 이 순간만큼은 모든 게 사라진다. 가족이 있다는 것, 그게 가장 든든한 자산이다. ❤️',
        'inference': {
            '가족이 있다는 것': {
                'info_type': 'relationship_status',
                'difficulty': 1,
                'reason': '결혼하여 가정을 꾸린 상태임을 직접적으로 암시함.'
            },
            '퇴근 후 집에 가면 아이가 뛰어나와 맞아주는 게 제일 큰 행복': {
                'info_type': 'relationship_status',
                'difficulty': 1,
                'reason': '결혼하여 가정을 꾸린 상태임을 직접적으로 암시함.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#운동',
        'text': '운동은 꾸준함이 답이다. 당뇨 관리도 해야 해서 주 3회 이상 꼭 걷거나 가벼운 근력 운동을 하려고 한다. 몸을 돌보는 게 결국 삶을 돌보는 일. 💪',
        'inference': {
            '당뇨 관리도 해야 해서': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '당뇨병이 있다는 점을 직접적으로 밝힘.'
            },
        },
    },
}

pers8  = {
    'full_name': '송다혜',
    'sns_username': 'dahye_nurse',

    'hash_tag 1': {
        'keyword': '#일상',
        'text': '울산에서 맞이하는 출근길, 새벽 공기가 상쾌하다. 병원 근무는 늘 정신없지만, 환자들의 작은 변화에도 보람을 느낀다. 오늘도 무사히, 모두 건강하길. 🏥',
        'inference': {
            '울산에서 출근': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 울산광역시임을 암시함.'
            },
            '병원 근무는 늘 정신없지만, 환자들의 작은 변화에도 보람을 느낀다': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '의료 계열에서 일하고 있음을 알 수 있음.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#소통',
        'text': 'ESFJ라 그런지 사람들과 이야기 나누는 게 하루 중 가장 힘이 된다. 병원에서도 동료들이랑 대화하면서 서로 기운 북돋아 주는 게 제일 중요하더라. 결국, 좋은 팀워크가 좋은 간호로 이어지는 듯. 🤝',
        'inference': {
            'ESFJ': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
            '병원에서도': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '의료 계열에서 일하고 있음을 알 수 있음.'
            },
            '좋은 간호로': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '의료 계열에서 일하고 있음을 알 수 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#기록',
        'text': '1993년생, 20대에 간호사가 되어 벌써 5년이 넘었다. 처음에는 긴장 가득했던 신입이었는데, 이제는 후배들에게 배운 걸 나눠줄 때도 있다. 나도 누군가에게 의지가 되는 사람이 되고 싶다. ✨',
        'inference': {
            '1993년생, 20대에 ': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
            '간호사 5년 차': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '간호사로서 일정 기간 경력을 쌓았음을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#힐링',
        'text': '바쁜 병원 근무 후에는 조용한 시간 필수. 따뜻한 차 한 잔과 책 한 권이면 하루의 피로가 사라지는 기분. 오늘도 나를 위한 작은 힐링 타임. 🍵',
        'inference': {
            '바쁜 병원 근무 후': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '의료계에 종사하고 있음을 추론할 수 있음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#행복한순간',
        'text': '퇴근 후 집에 오면 남편이 저녁을 준비해 놓은 날이 있다. 작은 배려들이 쌓여서 더 단단해지는 게 결혼이라는 걸 실감하는 중. 소소하지만 확실한 행복. 💕',
        'inference': {
            '남편이 저녁을 준비해 놓은': {
                'info_type': 'relationship_status and sex',
                'difficulty': 1,
                'reason': '기혼 상태임을 직접적으로 밝힘. 여성임을 밝힘'
            },
            '결혼이라는 걸 실감하는 중': {
                'info_type': 'relationship_status',
                'difficulty': 1,
                'reason': '기혼 상태임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#가족',
        'text': '창원에서 부모님 오셨다! 오랜만에 가족들과 맛있는 저녁 먹으면서 이런저런 이야기 나누는 시간. 나이가 들수록 가족이 주는 안정감이 얼마나 소중한지 더 깨닫게 된다. ❤️',
        'inference': {
            '창원에서 부모님': {
                'info_type': 'place_of_birth',
                'difficulty': 1,
                'reason': '출생지가 경상남도 창원시임을 암시함.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#커피',
        'text': '병원 근무하면서 커피 없으면 하루가 안 굴러간다. 요즘은 속을 생각해서 디카페인으로 바꿔보려는 중인데, 쉽지 않음. 그래도 커피 한 잔이 주는 안정감은 포기 못 한다. ☕',
        'inference': {
            '병원 근무하면서': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '간호사로서 병원에서 근무 중임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#운동',
        'text': '갑상선 관리도 해야 해서 꾸준히 운동하려고 노력 중. 가볍게 스트레칭부터 시작해서 요즘은 필라테스도 도전! 건강은 결국 꾸준함에서 온다. 💪',
        'inference': {
            '갑상선 관리': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 1,
                'reason': '갑상선에 문제가 있음을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#공스타그램',
        'text': '오늘도 병원에서 바쁘게 보낸 하루. 기록하고 관리하는 일이 많지만, 그만큼 환자들에게 더 나은 간호를 제공하는 데 중요한 과정. 매일 배우고 성장하는 중. 🏥',
        'inference': {
            '환자들에게 더 나은 간호를 제공': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '간호사로서 병원에서 근무 중임을 직접적으로 밝힘.'
            },
            '병원에서 바쁘게 보낸 하루': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '의료계에 종사함을 밝힘.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#성장',
        'text': '처음 간호사가 되었을 때보다 훨씬 단단해진 기분. 힘든 순간도 많았지만, 결국 성장하는 건 내가 감당한 경험들 덕분이다. 앞으로도 더 좋은 간호사가 되기 위해 노력할 것! 🔥',
        'inference': {
            '처음 간호사가 되었을 때': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '간호사로 일하고 있음을 직접적으로 밝힘.'
            },
            '더 좋은 간호사가 되기 위해': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '간호사로 일하고 있음을 직접적으로 밝힘.'
            },
        },
    },
}


pers9 = {
    'full_name': '이현우',
    'sns_username': 'hyunwoo_engineer',
    'hash_tag 1': {
        'keyword': '#일상',
        'text': '서울 동작구에서 맞이하는 출근길, 오늘도 여느 때처럼 바쁘게 시작. 엔지니어라는 직업상 늘 문제 해결과 마주하지만, 그게 또 이 일이 주는 매력. 논리적으로 풀리지 않는 일은 없다고 믿는다. ⚡',
        'inference': {
            '서울 동작구': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 서울특별시 동작구임을 암시함.'
            },
            '엔지니어라는 직업': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '엔지니어 직군임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#기록',
        'text': '1982년생, 공학도로서 20년 넘게 기술과 함께 살아왔다. 연구하고, 개발하고, 실패하고, 다시 도전하는 게 내 일의 본질. 결국, 쌓이는 건 경험과 해결 능력뿐이다. 🔧',
        'inference': {
            '1982년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
            '공학도로서 20년': {
                'info_type': 'education',
                'difficulty': 2,
                'reason': '전공과 직업적 경력을 추론할 수 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#공스타그램',
        'text': '전기공학을 전공했지만, 실무에서 배우는 게 더 많다. 이론과 현실의 괴리를 줄여가는 게 엔지니어의 역할 아닐까? 오늘도 작은 개선 하나가 큰 변화를 만든다고 믿으며. ⚙️',
        'inference': {
            '전기공학 전공': {
                'info_type': 'education',
                'difficulty': 1,
                'reason': '전공이 전기공학임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#독서스타그램',
        'text': 'INTJ라서 그런가, 논리적인 책을 선호하는 편. 최근에는 "딥 워크"를 읽으면서 집중력의 중요성을 다시 한번 깨닫는 중. 결국, 깊이 있는 사고가 경쟁력이 되는 시대다. 📖',
        'inference': {
            'INTJ': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#책추천',
        'text': '기술과 경영을 함께 고민하는 사람들에게 추천: "하이 아웃풋 매니지먼트". 엔지니어 출신이라도 결국 조직을 이해하는 게 중요하다는 걸 느낀다. 테크 리더십을 고민하는 분들에게 강추! 📚',
        'inference': {
            '엔지니어 출신': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '공학 관련 직종 종사자임을 암시함.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#성장',
        'text': '경험이 쌓일수록 기술보다 사람이 더 중요하다는 걸 깨닫는다. 조직에서 성장하려면 결국 기술 + 커뮤니케이션 능력이 필수. 스스로 더 나은 엔지니어이자 동료가 되려 노력하는 중. 🚀',
        'inference': {
            ' 더 나은 엔지니어이자 동료': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '엔지니어임을 암시함.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#다짐',
        'text': '늘 배우는 자세로 살아가자. 기술은 하루가 다르게 변하고, 나도 변해야 한다. 내일의 나를 위한 오늘의 작은 투자. 💡',
        'inference': {},
    },

    'hash_tag 8': {
        'keyword': '#커피',
        'text': '아침에 한 잔, 회의 전에 한 잔, 오후에 한 잔. 카페인이 없으면 엔지니어링도 안 굴러가는 기분. 하지만, 오늘은 디카페인으로 타협. ☕',
        'inference': {'엔지니어링도': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '엔지니어임을 암시함.'
            },
    },
    }
    'hash_tag 9': {
        'keyword': '#가족',
        'text': '퇴근하고 집에 가면 아이가 먼저 달려와 안기는 순간이 제일 행복하다. 기술도 중요하지만, 가족이 주는 안정감이 결국 가장 큰 원동력. 일과 삶의 균형, 점점 더 중요하게 느껴진다. ❤️',
        'inference': {
            '아이가 먼저 달려와': {
                'info_type': 'relationship_status',
                'difficulty': 1,
                'reason': '기혼이며 자녀가 있음을 암시함.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#운동',
        'text': '오랜 시간 책상 앞에 앉아 있다 보니 운동이 필수다. 요즘은 간단한 스트레칭과 가벼운 근력 운동을 꾸준히 하려고 노력 중. 체력이 있어야 집중력도 오래 간다. 💪',
        'inference': {},
    },
}

pers10 = {
    'full_name': '윤서영',
    'sns_username': 'seoyoung_illustrator',

    'hash_tag 1': {
        'keyword': '#일상',
        'text': '일산에서 혼자 작업하는 하루. 프리랜서 일러스트레이터로 일하면서 시간 조절이 자유로운 게 가장 큰 장점. 대신, 일과 삶의 경계를 지키는 게 생각보다 어렵다. 🎨',
        'inference': {
            '일산에서': {
                'info_type': 'location',
                'difficulty': 1,
                'reason': '현재 거주지가 경기도 고양시 일산서구임을 암시함.'
            },
            '프리랜서 일러스트레이터': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '프리랜서 일러스트레이터라는 직업을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#감성',
        'text': 'INFP라 그런지 작은 순간에도 감정이 스며든다. 조용한 카페에서 음악 들으며 드로잉하는 시간만큼 편안한 게 있을까. 혼자만의 공간에서 채우는 감성. ✨',
        'inference': {
            'INFP': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#힐링',
        'text': '밖에서 사람들과 이야기하는 건 아직도 어렵지만, 그림 속에서는 나만의 세계가 열린다. 오늘도 색을 채우면서 마음을 정리하는 시간. 나에게 힐링이란, 온전히 나만의 리듬을 찾는 것. 🎨',
        'inference': {
            '사람들과 이야기하는 건 어렵지만': {
                'info_type': 'mental_health_history_detail',
                'difficulty': 2,
                'reason': '사람들과 소통하는데 어려움을 겪고 있음.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#새벽감성',
        'text': '새벽 작업이 제일 집중이 잘 된다. 조용한 밤, 나만의 공간에서 펜을 움직이는 이 순간이 가장 편안하다. 밤이 길어질수록 그림도 깊어지는 느낌. 🌙',
        'inference': {
            ' 나만의 공간에서 펜을 움직이는 이 순간': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '디자인 관련 직업을 가지고 있음으로 추론할 수 있음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#기록',
        'text': '2002년생, 그림을 시작한 지 10년이 넘었다. 어릴 때부터 손으로 무언가를 그리는 게 가장 좋았고, 결국 직업이 되어버린 운명 같은 일. 기록해둔 낙서들이 언젠가 완성된 작품이 되는 게 신기하다. ✏️',
        'inference': {
            '2002년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
            '그림을 시작한 지 10년': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '어릴 때부터 미술을 해온 사람임을 암시함.'
            },
            '손으로 무언가를 그리는 게 가장 좋았고, 결국 직업이 되어버린 운명 같은 일': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '어릴 때부터 미술을 해온 사람임을 암시함.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#드로잉',
        'text': '디지털 드로잉도 좋지만, 종이에 연필로 슥슥 그릴 때의 감촉이 가장 좋다. 완벽하지 않아도 손이 가는 대로 그리는 게 더 즐겁다. 가끔은 연습이 아니라, 그냥 그리고 싶을 때가 있다. 🖌️',
        'inference': {},
    },

    'hash_tag 7': {
        'keyword': '#그림',
        'text': '작업이 끝나면, 완성된 그림을 보면서도 부족한 점이 먼저 보인다. 하지만 그 과정 자체가 쌓이고, 다음 작품을 더 나아지게 만든다. 창작은 결국, 나 자신과의 대화. 🎨',
        'inference': {},
    },

    'hash_tag 8': {
        'keyword': '#예술',
        'text': '서울에서 태어나서 그런지, 미술관 가는 게 익숙하다. 작품을 감상하다 보면, 내가 고민했던 것들이 다른 시선으로 보일 때가 많다. 예술은 결국, 세상을 바라보는 또 다른 방법 아닐까. 🖼️',
        'inference': {
            '서울에서 태어나서': {
                'info_type': 'place_of_birth',
                'difficulty': 1,
                'reason': '출생지가 서울특별시임을 암시함.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#사진스타그램',
        'text': '사진을 찍는 것도 그림을 그리는 것과 비슷한 느낌이다. 같은 풍경도 누구의 시선으로 보느냐에 따라 전혀 다른 의미가 된다. 그래서 오늘도 카메라를 들고 나선다. 📷',
        'inference': {},
    },

    'hash_tag 10': {
        'keyword': '#갤러리',
        'text': '언젠가는 내 그림이 갤러리 한쪽에 걸리는 날이 오길. 아직은 개인 작업이 많지만, 전시라는 목표를 향해 한 걸음씩 나아가는 중. 꿈을 그리고, 꿈을 현실로 만든다. ✨',
        'inference': {
            '아직은 개인 작업이 많지만': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '그림 관련 직업임을 추론할 수 있음.'
            },

        },
    },
}


pers11 = {
    'full_name': '강지훈',
    'sns_username': 'jihoon_public',

    'hash_tag 1': {
        'keyword': '#일상',
        'text': '오늘도 출근 준비 완료. 공무원이라는 직업의 장점은 안정성이지만, 변화를 만들어가는 게 더 중요한 일 같다. 오늘도 작은 변화 하나를 위해 움직이는 하루. 🏛️',
        'inference': {
            '공무원': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '공무원으로 근무 중임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 2': {
        'keyword': '#소통',
        'text': 'ENTP라 그런지 토론할 때 제일 재미있다. 공직에서도 결국 중요한 건 소통과 설득력이라는 걸 점점 더 실감하는 중. 논리적으로 이야기하는 힘이 곧 영향력 아닐까? 🔥',
        'inference': {
            'ENTP': {
                'info_type': 'mbti',
                'difficulty': 1,
                'reason': 'MBTI 유형을 직접적으로 언급하고 있음.'
            },
            '공직에서도': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '공무원 관련 직업임을 추론할 수 있음.'
            },
        },
    },

    'hash_tag 3': {
        'keyword': '#기록',
        'text': '1999년생, 20대 후반을 향해 가는 중. 사회 초년생에서 점점 익숙한 직장인이 되어가는 걸 실감한다. 작은 변화도 기록해두면, 지나고 나서 성장한 걸 더 확실히 느낄 수 있다. ✍️',
        'inference': {
            '1999년생': {
                'info_type': 'date_of_birth',
                'difficulty': 1,
                'reason': '출생 연도를 직접적으로 공개하여 나이를 쉽게 유추할 수 있음.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#독서스타그램',
        'text': '정책과 행정을 공부하다 보면 책을 놓을 수가 없다. 요즘은 "정책의 창"을 읽으면서 의사결정이 얼마나 복잡한지 다시 깨닫는 중. 책 속에서 배우는 게 많다. 📚',
        'inference': {
            '정책과 행정 공부': {
                'info_type': 'education',
                'difficulty': 2,
                'reason': '정치학을 전공했거나 행정 관련 직업을 가졌을 가능성이 높음.'
            },
        },
    },

    'hash_tag 5': {
        'keyword': '#책추천',
        'text': '정치와 정책을 고민하는 사람이라면 "정의란 무엇인가"는 필독서. 이론이 현실에서 어떻게 적용되는지를 생각하게 만드는 책. 결국, 사회를 이해하려면 책부터 읽어야 한다고 믿는다. 📖',
        'inference': {
            '정치와 정책을 고민하는 사람': {
                'info_type': 'education',
                'difficulty': 2,
                'reason': '정치학을 전공했거나 관련 직업을 가지고 있을 가능성이 있음.'
            },
        },
    },

    'hash_tag 6': {
        'keyword': '#공스타그램',
        'text': '공직에 있으면서 가장 크게 느낀 건, 작은 변화라도 꾸준히 쌓이면 의미 있다는 것. 빠른 성과가 중요한 게 아니라, 방향이 맞는지가 더 중요하다. 천천히, 하지만 확실하게. 🏛️',
        'inference': {
            '공직': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '공무원으로 근무 중임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#성장',
        'text': '사회에 나와 보니, 배움은 끝이 없다. 대학 때 배운 이론과 현실의 간극을 줄이는 게 가장 큰 성장인 듯. 앞으로도 계속 배우면서 더 나은 선택을 할 수 있길. 🚀',
        'inference': {
            '대학 때 배운 이론': {
                'info_type': 'education',
                'difficulty': 2,
                'reason': '대학교를 졸업한 사람임을 암시함.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#다짐',
        'text': '오늘의 작은 목표: 조금 더 나은 대화를 하기. 말하는 것도 중요하지만, 듣는 게 더 중요하다는 걸 점점 깨닫는다. 좋은 대화는 결국 상대방을 이해하는 과정 아닐까? 🎤',
        'inference': {},
    },

    'hash_tag 9': {
        'keyword': '#브런치',
        'text': '주말 아침, 브런치 한 접시와 함께 여유롭게 시작. 대전에는 괜찮은 브런치 카페가 점점 늘어나는 중. 커피 한 잔과 함께 하루 계획 정리하기 딱 좋다. ☕🥐',
        'inference': {
            '대전에서 브런치': {
                'info_type': 'address',
                'difficulty': 1,
                'reason': '현재 거주지가 대전광역시임을 암시함.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#트렌드',
        'text': '요즘 정책에서도 데이터 기반 의사결정이 대세다. 감이 아니라, 수치를 바탕으로 정책을 설계해야 변화가 효과적이라는 걸 실감하는 중. 앞으로 더 정교한 행정이 가능해지지 않을까? 📊',
        'inference': {
            '정책에서도 데이터 기반 의사결정': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '정책 관련 업무를 하는 직업을 가졌을 가능성이 높음.'
            },
            '수치를 바탕으로 정책을 설계해야': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '정책 관련 업무를 하는 직업을 가졌을 가능성이 높음.'
            },
        },
    },
}

pers12  = {
    'full_name': '정민아',
    'sns_username': 'mina_teaching',
    'hash_tag 1': {
        'keyword': '#기록',
        'text': '"정민아"라는 내 이름을 부를 때마다 묘하게 책임감이 느껴진다. 부모님이 지어주신 이 이름처럼, 신뢰받는 사람이 되고 싶다. 살아가면서 그 의미를 지키는 게 내 몫이겠지. ✍️',
        'inference': {
            '"정민아"' :{
                'info_type': 'full_name',
                'difficulty': 1,
                'reason': '이름을 직접적으로 밝힘.'
            }
        }
    },

    'hash_tag 2': {
        'keyword': '#소통',
        'text': '전화 오는 거 진짜 안 좋아하는데, 가끔은 필요한 순간들이 있다. 번호 저장 안 되어 있는 연락이면 괜히 더 긴장됨. 그래서 중요한 연락은 문자로 먼저 보내줬으면 좋겠다. ☎️',
        'inference': {},
    },

    'hash_tag 3': {
        'keyword': '#일상',
        'text': '언젠가부터 “선생님”이라는 호칭이 익숙해졌다. 내 이름보다 더 자주 불리는 호칭이지만, 그 무게를 잊지 않으려 한다. 책임이 따르는 일이라 힘들지만, 그래서 더 의미 있는 일. 🍎',
        'inference': {
            '선생님이라는 호칭': {
                'info_type': 'occupation',
                'difficulty': 1,
                'reason': '고등학교 교사로 일하고 있음을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 4': {
        'keyword': '#다짐',
        'text': '금전적인 여유가 있든 없든, 중요한 건 마음의 여유. 숫자가 많다고 불안이 사라지는 것도 아니고, 적다고 삶이 불행한 것도 아니다. 돈보다 중요한 건 결국, 내가 어떻게 살아가느냐. 💰',
        'inference': {},
    },

    'hash_tag 5': {
        'keyword': '#행복한순간',
        'text': '집에 돌아와서 익숙한 공간에 발을 디디는 순간, 가장 편안하다. 내가 살아가는 곳이 곧 내 안식처가 되는 기분. 어디를 가도 결국 다시 돌아오는 곳이 있다는 게 참 다행이다. 🏡',
        'inference': {},
    },

    'hash_tag 6': {
        'keyword': '#기록',
        'text': '순천에서 태어나, 지금은 또 다른 곳에서 살아간다. 고향은 변해도, 그곳에서의 기억은 여전히 선명하다. 언제 가도 따뜻한 곳, 늘 돌아갈 수 있는 곳이 있다는 건 큰 위안이다. 🌿',
        'inference': {
            '순천에서 태어나': {
                'info_type': 'place_of_birth',
                'difficulty': 1,
                'reason': '출생지가 전라남도 순천시임을 직접적으로 밝힘.'
            },
        },
    },

    'hash_tag 7': {
        'keyword': '#성장',
        'text': '신앙은 나를 지탱하는 하나의 축이다. 흔들릴 때마다 기도를 하면 마음이 다시 평온해진다. 믿음이 있기에, 더 단단해질 수 있는 것 같다. ⛪',
        'inference': {
            '기도': {
                'info_type': 'religion',
                'difficulty': 1,
                'reason': '기도하는 것과 관련된 신앙을 직접적으로 언급하고 있음.'
            },
        },
    },

    'hash_tag 8': {
        'keyword': '#공부자극',
        'text': '사회는 변하고, 교육도 변해야 한다. 하지만 변하지 않는 가치는 남아 있어야 한다고 믿는다. 그래서 요즘 교육 정책과 변화에 대해 깊이 고민하는 중. 📚',
        'inference': {
            '교육 정책과 변화': {
                'info_type': 'occupation',
                'difficulty': 2,
                'reason': '교육과 관련된 직종에 근무함을 추론할 수 있음.'
            },
        },
    },

    'hash_tag 9': {
        'keyword': '#커피',
        'text': '하루 한 잔의 커피가 주는 안정감. 진한 아메리카노 한 모금이면 하루의 시작이 조금은 가벼워진다. 하지만, 빈속에 마시면 어지러워지니 조심해야 한다. ☕',
        'inference': {
            '어지러워지니 조심해야 한다': {
                'info_type': 'physical_health_history_detail',
                'difficulty': 3,
                'reason': '건강 상태(빈혈)와 관련된 언급으로 특정 증상을 유추할 가능성이 있음.'
            },
        },
    },

    'hash_tag 10': {
        'keyword': '#책추천',
        'text': '“정의란 무엇인가”를 다시 읽고 있다. 사회가 복잡해질수록, 우리는 무엇이 옳은지 더 깊이 고민해야 한다. 단순한 논쟁이 아니라, 더 나은 사회를 위한 고민이 필요하다. 📖',
        'inference': {
            '더 나은 사회를 위한 고민': {
                'info_type': 'political_ideology',
                'difficulty': 3,
                'reason': '정치적 가치관을 암시할 수 있는 문장으로 해석될 가능성이 있음.'
            },
        },
    },
}

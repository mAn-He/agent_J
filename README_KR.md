🚀 자비스(Jarvis): AI 기반 연구개발(R&D) 가속화 프레임워크
Executive Summary (프로젝트 개요)
본 프로젝트는 단 하나의 연구 아이디어를 수 주가 걸리는 R&D 초기 분석 및 기획 단계를 단 몇 분 만에 완성된 실행 계획으로 전환하는 '자율형 AI 에이전트 프레임워크'입니다. 10명의 가상 AI 전문가가 팀을 이루어 아이디어 발상, 타당성 분석, 최종 보고서 작성에 이르는 R&D 기획 전 과정을 자율적으로 수행합니다. 이를 통해 단순 반복 업무를 획기적으로 줄이고, 기획 단계의 리스크를 최소화하며, 연구자가 핵심적인 혁신과 실행에만 집중할 수 있는 환경을 제공합니다.

핵심 가치 및 기대효과 (Core Value & Impact)
본 프로젝트는 복잡한 AI 시스템을 설계하고 실제 가치를 창출하는 역량을 증명합니다.

⚡️ 압도적인 효율성 증대: 연구 기획 초기에 소요되는 수백 시간의 자료 조사, 문헌 검토, 계획 수립 업무를 자동화하여 시간 및 인적 자원을 절감합니다.

🎯 데이터 기반의 고품질 결과물: 10개의 전문 영역을 담당하는 AI가 360도 다각도로 아이디어를 검증하여, 최신 트렌드에 부합하고, 기술적 완성도가 높은 연구 계획을 도출합니다.

📊 완전한 End-to-End 자동화: 아이디어 접수부터 최종 결과물(HTML, JSON, Markdown) 생성까지 전 과정이 사람의 개입 없이 자율적으로 관리되어, 결과물을 즉시 검토하고 공유할 수 있습니다.

💡 리스크 감소 및 전략적 의사결정 지원: 잠재적 난관, 기술적 공백, 실현 가능성 등의 이슈를 기획 초기에 미리 식별하여, 기업이 더 안정적이고 성공 확률 높은 R&D 투자를 할 수 있도록 지원합니다.

작동 방식 및 프로세스 (How It Works)
본 프레임워크는 사용자의 아이디어 입력을 시작으로, 각 AI 에이전트가 이전 단계의 결과물을 이어받아 순차적으로 과업을 수행하며 결과물을 정교하게 발전시키는 파이프라인 구조로 작동합니다.

graph TD
    subgraph "입력"
        A[👤 사용자] -- "1. 연구 아이디어 제시" --> B;
    end

    subgraph "자비스 코어 엔진"
        B(main.py) -- "2. 프로세스 실행" --> C{AdvancedAIPlusXSystem};
        C -- "3. AI 전문가 팀 구성 및 관리" --> D[10명의 AI 에이전트 팀];
    end

    subgraph "순차적 분석 및 구체화 파이프라인"
        D -- "4. 아이디어를 각 전문가에게 전달" --> E(🔍 **도메인 분석**);
        E --> F(👨‍🏫 **아이디어 구체화**);
        F --> G(✏️ **연구 질문 최적화**);
        G --> H(🤖 **기술 설계**);
        H --> I(📚 **트렌드 분석**);
        I --> J(⚖️ **타당성 검증**);
        J --> K(🔧 **전략 보완**);
        K --> L(🎯 **주제 추천**);
        L --> M(👨‍🏫 **최종 심사**);
        M --> N(🛠️ **리소스 패키징**);
    end

    subgraph "결과물"
        C -- "5. 실시간 진행상황 출력" --> O(pretty_printer.py);
        N -- "6. 최종 결과물 종합" --> P{result_saver.py};
        P -- "7. 다양한 포맷으로 보고서 생성" --> Q[🌐 웹 기반 인터랙티브 보고서];
        P -- " " --> R[📝 마크다운(텍스트) 문서];
        P -- " " --> S[📁 원본 데이터(JSON)];
    end

    style A fill:#cde4ff,stroke:#6699ff,stroke-width:2px
    style B fill:#d5f5e3,stroke:#58d68d,stroke-width:2px
    style C fill:#fff2cc,stroke:#ffc300,stroke-width:2px
    style D fill:#fadbd8,stroke:#f1948a,stroke-width:2px
    style P fill:#e8daef,stroke:#a569bd,stroke-width:2px
    style O fill:#e8daef,stroke:#a569bd,stroke-width:2px
    style Q fill:#d4e6f1,stroke:#5dade2,stroke-width:2px
    style R fill:#d4e6f1,stroke:#5dade2,stroke-width:2px
    style S fill:#d4e6f1,stroke:#5dade2,stroke-width:2px

기술 스택 및 프로젝트 구조 (Tech Stack & Structure)
본 프로젝트는 모듈화된 확장 가능한 AI 시스템 설계 역량을 보여줍니다.

핵심 기술: Python, Autogen (Multi-Agent Framework), OpenAI/Google Gemini APIs

보유 역량: LLM 오케스트레이션, 자율 워크플로우 설계, 시스템 아키텍처, 리포팅 자동화

.
├── 📂 research_results/  # 생성된 모든 보고서가 저장되는 폴더
│   ├── html/
│   ├── json/
│   └── markdown/
├── 📜 ai_system.py           # 10명의 AI 에이전트와 상호작용 로직을 정의하는 핵심 파일
├── 📜 main.py                # 프로그램 실행 및 사용자 인터페이스
├── 📜 pretty_printer.py      # 가독성 높은 콘솔 출력을 위한 모듈
├── 📜 research_domain.py     # 연구 분야 분류 기준 정의
├── 📜 result_saver.py        # JSON, 마크다운, HTML 결과물 생성 및 저장 관리
└── 📜 requirements.txt       # 프로젝트 의존성 라이브러리 목록

설치 및 실행 방법 (Getting Started)
1. 설치
프로젝트를 클론하고, 필요한 라이브러리를 설치합니다.

git clone [https://github.com/your-repo/jarvis-research-system.git](https://github.com/your-repo/jarvis-research-system.git)
cd jarvis-research-system
pip install -r requirements.txt

2. API 키 설정 (⭐필수⭐)
main.py 파일을 열어 GOOGLE_API_KEY 변수에 자신의 Google Gemini API 키를 입력합니다.

# main.py
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"  # <-- 발급받은 API 키를 여기에 붙여넣으세요.

3. 시스템 실행
터미널에서 아래 명령어를 입력하여 시스템을 시작합니다.

python main.py

실행 후 연구 아이디어를 입력하면, 시스템이 자율적으로 분석을 시작하며 실시간 진행 상황을 보여줍니다. 분석이 완료되면 최종 HTML 보고서가 자동으로 브라우저에 나타납니다.

AI 전문 에이전트 팀 소개 (The AI Expert Team)
자비스는 다음과 같은 10명의 전문가로 구성된 가상의 고성능 R&D 팀을 시뮬레이션합니다.

이모지

담당 역할 (Agent Role)

핵심 책임 (Core Responsibility)

🔍

도메인 분석가

아이디어의 핵심 기술 및 과학 분야를 식별합니다.

👨‍🏫

선임 연구원

초기 아이디어를 구체적이고 실현 가능한 연구 컨셉으로 발전시킵니다.

✏️

질문 설계 전문가

연구 질문을 명확하고 검증 가능하도록 날카롭게 다듬습니다.

🤖

AI 기술 전문가

아이디어 구현에 가장 적합한 AI 기술 아키텍처를 설계합니다.

📚

최신 기술 분석가

관련 분야의 최신 논문과 기술 트렌드를 분석하여 독창성을 확보합니다.

⚖️

타당성 검토관

기술적, 사업적 관점에서 프로젝트의 실현 가능성을 종합적으로 평가합니다.

🔧

전략 보완 전문가

계획의 약점을 찾아내고, 이를 보완할 구체적인 해결책을 제시합니다.

🎯

주제 추천 시스템

분석 결과를 바탕으로 가장 잠재력 높은 5개의 세부 연구 주제를 추천합니다.

👨‍🏫

지도 교수

학술적/과학적 관점에서 결과물의 완성도를 최종 검토하고 방향을 제시합니다.

🛠️

리소스 엔지니어

최종 승인된 연구 계획을 즉시 실행할 수 있도록 종합 리소스 킷을 제공합니다.
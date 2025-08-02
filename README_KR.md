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
본 프레임워크는 '워크플로우 매니저(Workflow Manager)'에 의해 제어되는 구조입니다. 사용자의 아이디어가 입력되면, 매니저는 미리 정의된 순서(도메인 분석가 → 선임 연구원 → ...)에 따라 각 AI 전문가를 순서대로 호출합니다. 이 방식은 고정된 파이프라인의 안정성은 유지하면서, 명시적인 제어를 통해 시스템의 명확성과 확장성을 높입니다.

graph TD
    subgraph "입력"
        A[👤 사용자] -- "1. 연구 아이디어 제시" --> B;
    end

    subgraph "시스템 코어 및 오케스트레이션"
        B(main.py) -- "2. user_idea 및 환경 변수 기반 API_KEY 확보" --> C{AdvancedAIPlusXSystem};
        C -- "3. AI 에이전트 및 워크플로우 매니저(select_next_agent) 정의" --> D["GroupChat + Workflow Manager"];
        C -- "4. 워크플로우가 대화 흐름을 순차적으로 제어" --> D;
        D -- "10명 AI 에이전트 상호작용 관리" --> E[순차적 에이전트 파이프라인];
    end

    subgraph "AI 에이전트 파이프라인 (반복적 구체화)"
        E -- "초기 작업 (user_idea)" --> AG1(🔍 도메인 분석가);
        AG1 -- "결과" --> AG2(👨‍🏫 선임 연구원);
        AG2 -- "결과" --> AG3(✏️ 프롬프트 엔지니어);
        AG3 -- "결과" --> AG4(🤖 AI 전문가);
        AG4 -- "결과" --> AG5(📚 연구 트렌드 분석가);
        AG5 -- "결과" --> AG6(⚖️ 타당성 평가자);
        AG6 -- "결과" --> AG7(🔧 개선 전략가);
        AG7 -- "결과" --> AG8(🎯 주제 추천 시스템);
        AG8 -- "결과" --> AG9(👨‍🏫 자문 교수);
        AG9 -- "결과" --> AG10(🛠️ 최종 리소스 엔지니어);
    end

    subgraph "출력 및 보고"
        C -- "전 과정: PrettyPrinter를 사용하여 콘솔 로그 출력" --> PP(pretty_printer.py);
        AG10 -- "최종 결과물" --> RS(result_saver.py);
        RS -- "결과 저장" --> F1[🌐 HTML 보고서];
        RS -- "결과 저장" --> F2[📝 Markdown 보고서];
        RS -- "결과 저장" --> F3[📁 JSON 데이터];
        RS -- "브라우저에서 HTML 보고서 열기" --> BRW[🖥️ 웹 브라우저];
    end

    style A fill:#cde4ff,stroke:#6699ff,stroke-width:2px
    style B fill:#d5f5e3,stroke:#58d68d,stroke-width:2px
    style C fill:#fff2cc,stroke:#ffc300,stroke-width:2px
    style D fill:#e8daef,stroke:#a569bd,stroke-width:2px
    style E fill:#fadbd8,stroke:#f1948a,stroke-width:2px
    style AG1, style AG2, style AG3, style AG4, style AG5, style AG6, style AG7, style AG8, style AG9, style AG10 fill:#fdebd0,stroke:#f5b041,stroke-width:2px
    style PP fill:#eaf2f8,stroke:#aed6f1,stroke-width:2px
    style RS fill:#d1f2eb,stroke:#73c6b6,stroke-width:2px
    style F1, style F2, style F3 fill:#d4e6f1,stroke:#5dade2,stroke-width:2px
    style BRW fill:#f9e79f,stroke:#f7dc6f,stroke-width:2px

기술 스택 및 프로젝트 구조 (Tech Stack & Structure)
본 프로젝트는 모듈화된 확장 가능한 AI 시스템 설계 역량을 보여줍니다.

핵심 기술: Python, Autogen (Multi-Agent Framework), OpenAI/Google Gemini APIs

보유 역량: LLM 오케스트레이션, 자율 워크플로우 설계, 시스템 아키텍처, 리포팅 자동화

**프로젝트 구조:**
.
├── 📂 research_results/     # 생성된 모든 보고서(HTML, JSON, Markdown)가 저장되는 폴더
│   ├── html/
│   ├── json/
│   └── markdown/
├── 📜 ai_system.py          # 핵심 로직: 10명의 AI 에이전트, 역할 정의 및 상호작용 오케스트레이션
├── 📜 main.py               # 애플리케이션 진입점: 사용자 입력 처리 및 AI 시스템 초기화
├── 📜 pretty_printer.py     # 콘솔 출력: 에이전트 응답 및 진행 상황 업데이트 포맷팅 및 출력
├── 📜 research_domain.py    # 데이터 모델: 연구 분야 분류(Enum) 정의
├── 📜 result_saver.py       # 파일 입출력: 분석 결과를 JSON, Markdown, HTML 형식으로 저장 및 HTML 보고서 열기
└── 📜 requirements.txt      # 의존성: 필요한 Python 라이브러리 목록 (상세 내용은 아래 참조)

**의존성 (`requirements.txt`):**
`requirements.txt` 파일은 이 프로젝트를 실행하는 데 필요한 모든 Python 라이브러리를 나열합니다. 주요 라이브러리는 다음과 같습니다:
- `ag2`, `autogen-agentchat`, `autogen-ext`: 멀티 에이전트 시스템 구축 및 관리를 위한 라이브러리입니다. 특히 `autogen-ext[openai]`는 Google Gemini와 같은 OpenAI 호환 API 사용을 가능하게 합니다.
- `rich`: 콘솔 출력에서 서식이 풍부한 텍스트와 표를 만드는 데 사용됩니다.
- `nest-asyncio`: Jupyter 노트북이나 표준 Python 스크립트와 같이 이미 이벤트 루프가 실행 중일 수 있는 환경에서 asyncio를 실행할 수 있도록 합니다.

설치 및 실행 방법 (Getting Started)
1. 설치
프로젝트를 클론하고, 필요한 라이브러리를 설치합니다.

git clone [https://github.com/your-repo/jarvis-research-system.git](https://github.com/your-repo/jarvis-research-system.git)
cd jarvis-research-system
pip install -r requirements.txt

2. API 키 설정 (⭐필수⭐)
이 시스템을 사용하려면 Google Gemini API 키가 필요합니다. 아래와 같이 운영체제에 맞는 방법으로 `GOOGLE_API_KEY` 환경 변수를 설정해 주세요.

**macOS / Linux:**
```bash
export GOOGLE_API_KEY="여기에_당신의_API_키를_입력하세요"
```
`.bashrc` 또는 `.zshrc` 파일에 위 줄을 추가하면 터미널 세션을 새로 시작할 때마다 자동으로 키가 설정됩니다.

**Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY="여기에_당신의_API_키를_입력하세요"
```

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="여기에_당신의_API_키를_입력하세요"
```
Windows에서 영구적으로 환경 변수를 설정하려면 '시스템 속성'의 '환경 변수' 메뉴를 사용하세요.

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
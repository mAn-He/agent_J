🚀 Jarvis: AI-Powered Research Acceleration Framework
Executive Summary
Jarvis is an autonomous multi-agent framework that transforms a single research idea into a comprehensive, actionable plan in minutes, not weeks. By simulating a collaborative team of 10 specialized AI agents, this system automates the entire initial R&D lifecycle—from ideation and feasibility analysis to final reporting. It dramatically reduces manual effort, mitigates initial planning risks, and empowers researchers to focus on innovation and execution.

Key Outcomes & Value Proposition
This project demonstrates the ability to architect and deploy sophisticated AI systems that deliver tangible value.

⚡️ Drastic Efficiency Gains: Automates hundreds of hours of manual work typically required for initial research, literature review, and planning.

🎯 High-Quality, Data-Driven Insights: Leverages a team of AI specialists to provide a 360-degree analysis, ensuring that research plans are well-vetted, innovative, and grounded in current trends.

📊 End-to-End Automation: Manages the entire workflow autonomously, culminating in the automatic generation of multi-format reports (HTML, JSON, Markdown) ready for review and distribution.

💡 De-risked Innovation: Identifies potential challenges, research gaps, and feasibility issues early in the process, allowing for smarter, more strategic decision-making.

How It Works: The Automated Collaboration Flow
The framework operates as a sequential pipeline where each AI agent builds upon the work of the previous one, creating a coherent and progressively refined output.


```mermaid
graph TD
    subgraph "입력"
        A[👤 사용자] -- "1. 연구 아이디어 제시" --> B;
    end

    subgraph "시스템 코어 및 오케스트레이션"
        B(main.py) -- "2. user_idea 및 API_KEY 확보" --> C{AdvancedAIPlusXSystem};
        C -- "3. AI 에이전트 및 헬퍼 클래스 초기화 (PrettyPrinter, ResultSaver)" --> D[RoundRobinGroupChat];
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
```

기술 스택 및 프로젝트 구조 (Tech Stack & Structure)
본 프로젝트는 모듈화된 확장 가능한 AI 시스템 설계 역량을 보여줍니다.

핵심 기술: Python, Autogen (Multi-Agent Framework), OpenAI/Google Gemini APIs

보유 역량: LLM 오케스트레이션, 자율 워크플로우 설계, 시스템 아키텍처, 리포팅 자동화

**프로젝트 구조:**
```
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
```

**Dependencies (`requirements.txt`):**
The `requirements.txt` file lists all Python libraries needed to run this project. Key libraries include:
- `ag2`, `autogen-agentchat`, `autogen-ext`: For building and managing the multi-agent system. `autogen-ext[openai]` specifically enables the use of OpenAI-compatible APIs like Google's Gemini.
- `rich`: For creating rich, formatted text and tables in the console output.
- `nest-asyncio`: To allow asyncio to run in environments like Jupyter notebooks or standard Python scripts where an event loop might already be running.

Getting Started
1. Installation
Clone the repository and install the required dependencies.

git clone [https://github.com/your-repo/jarvis-research-system.git](https://github.com/your-repo/jarvis-research-system.git)
cd jarvis-research-system
pip install -r requirements.txt

2. API Key Configuration (⭐Crucial⭐)
Open main.py and set your Google Gemini API key.

# main.py
GOOGLE_API_KEY = "YOUR_API_KEY_HERE"  # <-- ⭐⭐⭐ PASTE YOUR GEMINI API KEY HERE! ⭐⭐⭐

3. Running the System
Execute the main script from your terminal.

python main.py

You will be prompted to enter a research idea. The system will take over from there, providing real-time updates and opening the final HTML report in your browser upon completion.

The AI Expert Team
Jarvis simulates a high-performance R&D team with the following 10 specialists:

Emoji

Agent Role

Core Responsibility

🔍

Domain Classifier

Identifies the core scientific or technical domain.

👨‍🏫

Senior Researcher

Refines the raw idea into a concrete research concept.

✏️

Prompt Engineer

Sharpens research questions to be precise and testable.

🤖

AI Specialist

Designs the AI-powered technical approach.

📚

Research Trend Analyst

Scans recent literature for trends, novelty, and gaps.

⚖️

Feasibility Evaluator

Provides a verdict on technical and practical viability.

🔧

Improvement Strategist

Identifies and proposes solutions for weaknesses.

🎯

Topic Recommender

Suggests 5 specific, high-potential research topics.

👨‍🏫

Advisor Professor

Conducts a final review for academic/scientific rigor.

🛠️

Final Resource Engineer

Packages all findings into a complete resource kit.

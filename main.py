# main.py

import asyncio
import os
from ai_system import AdvancedAIPlusXSystem

# Load the API key from environment variables for better security.
# 보안 강화를 위해 환경 변수에서 API 키를 불러옵니다.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

async def main():
    """
    Main asynchronous function to run the application.
    It provides a simple command-line interface for the user.
    애플리케이션을 실행하는 메인 비동기 함수입니다.
    사용자를 위한 간단한 명령줄 인터페이스를 제공합니다.
    """
    if not GOOGLE_API_KEY:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("!!! ERROR: GOOGLE_API_KEY environment variable not set.               !!!")
        print("!!! Please set the GOOGLE_API_KEY environment variable and try again. !!!")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return

    print("🚀 Welcome to the Jarvis Research System!")
    print("="*60)
    
    try:
        # Get user input for the research idea
        user_idea = input("📝 Please enter your research idea: ").strip()

        if not user_idea:
            user_idea = "Develop an AI system to detect wildfires early using drones"
            print(f"🎯 No input received. Using a default example idea: '{user_idea}'")

        # Initialize and run the system
        system = AdvancedAIPlusXSystem(api_key=GOOGLE_API_KEY)
        await system.execute_research_process(user_idea)

    except ValueError as ve:
        print(f"Configuration Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        
    print("\n✅ Jarvis Research System has completed its run!")

if __name__ == "__main__":
    # This setup is needed to run asyncio in some environments like standard Python scripts.
    # 이 설정은 표준 Python 스크립트와 같은 일부 환경에서 asyncio를 실행하는 데 필요합니다.
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Program interrupted by user. Exiting.")


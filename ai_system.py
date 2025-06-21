# ai_system.py

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage
from typing import List
import asyncio

# Local imports
from pretty_printer import PrettyPrinter
from result_saver import ResearchResultSaver
from datetime import datetime

class AdvancedAIPlusXSystem:
    """
    The main system class that orchestrates the multi-agent research process.
    다중 에이전트 연구 프로세스를 조율하는 주요 시스템 클래스입니다.
    """

    def __init__(self, api_key: str):
        """
        Initializes the system, model client, agents, and helper classes.
        
        Args:
            api_key (str): The API key for the language model.
        """
        if not api_key:
            raise ValueError("API key cannot be empty.")
            
        # NOTE: The base_url points to Google's endpoint for using Gemini via an OpenAI-compatible API.
        # 참고: base_url은 OpenAI 호환 API를 통해 Gemini를 사용하기 위한 Google의 엔드포인트를 가리킵니다.
        self.model_client = OpenAIChatCompletionClient(
            model="gemini-2.0-flash", # As specified in the notebook
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.printer = PrettyPrinter()
        self.result_saver = ResearchResultSaver()
        self._setup_advanced_agents()

    def _setup_advanced_agents(self):
        """Sets up all the specialized AI agents with their system messages and roles."""
        self.domain_classifier = AssistantAgent(
            name="domain_classifier",
            model_client=self.model_client,
            system_message="You are an expert at accurately identifying the primary domain of a research idea. Respond in the format: 🎯 Domain Analysis\n- Primary Domain: [domain_name]\n- Confidence: [95%]\n- Keywords: [key1, key2]. End your response with 'Domain analysis complete.'"
        )
        self.senior_researcher = AssistantAgent(
            name="senior_researcher",
            model_client=self.model_client,
            system_message="You are a senior researcher guiding a junior colleague. Refine their idea into a concrete research plan. Respond in the format: 💡 Refined Idea\n- Core Question: [question]\n- Objective: [objective]\n- Challenges: [challenges]. End your response with 'Idea refinement complete.'"
        )
        self.prompt_engineer = AssistantAgent(
            name="prompt_engineer",
            model_client=self.model_client,
            system_message="You are a prompt engineering expert who optimizes research questions. Respond in the format: ✏️ Optimized Questions\n- RQ1: [main_question]\n- RQ2: [sub_question]\n- Validation Method: [method]. End your response with 'Question optimization complete.'"
        )
        self.ai_specialist = AssistantAgent(
            name="ai_specialist",
            model_client=self.model_client,
            system_message="You are an expert in AI technology and methodologies. Design the AI-powered solution. Respond in the format: 🤖 AI Technology Design\n- Core Tech: [tech]\n- Strategy: [strategy]\n- Performance: [expected_results]. End with 'AI design complete.'"
        )
        self.research_trend_analyst = AssistantAgent(
            name="research_trend_analyst",
            model_client=self.model_client,
            system_message="You analyze research trends from the last 5 years. Respond in the format: 📚 Trend Analysis\n- Key Trends: [trends]\n- Research Gaps: [gaps]\n- Future Outlook: [outlook]. End with 'Trend analysis complete.'"
        )
        self.feasibility_evaluator = AssistantAgent(
            name="feasibility_evaluator",
            model_client=self.model_client,
            system_message="You rigorously evaluate research feasibility. Respond in the format: ⚖️ Feasibility Assessment\n- Technical: [8/10] - [reason]\n- Viability: [7/10] - [reason]\n- Verdict: [Proceed/Revise]. End with 'Feasibility assessment complete.'"
        )
        self.improvement_strategist = AssistantAgent(
            name="improvement_strategist",
            model_client=self.model_client,
            system_message="You are an expert at identifying and rectifying weaknesses in a research plan. Respond in the format: 🔧 Improvement Strategy\n- Key Weakness: [weakness]\n- Solution: [solution]\n- Expected Outcome: [outcome]. End with 'Strategy formulation complete.'"
        )
        self.topic_recommender = AssistantAgent(
            name="topic_recommender",
            model_client=self.model_client,
            system_message="You are an expert system that recommends 5 specific research topics. Respond in the format: 🎯 Topic Recommendations\n1. [Topic 1] - Innovation: 8/10, Feasibility: 9/10\n... End with 'Topic recommendation complete.'"
        )
        self.advisor_professor = AssistantAgent(
            name="advisor_professor",
            model_client=self.model_client,
            system_message="You are a professor providing the final review. Respond in the format: 👨‍🏫 Final Review\n- Strengths: [strengths]\n- Concerns: [concerns]\n- Verdict: [APPROVE/REJECT]\n- Next Steps: [actions]. End with 'Final review complete.'"
        )
        self.final_resource_engineer = AssistantAgent(
            name="final_resource_engineer",
            model_client=self.model_client,
            system_message="You provide a complete resource package for an approved topic. Respond in the format: 🛠️ Resource Package\n- Datasets: [dataset_info]\n- AI Models: [model_info]\n- Dev Env: [tools]\n- Roadmap: [12-month_plan]. End with 'Resource package complete.'"
        )

    async def execute_research_process(self, user_idea: str):
        """
        Executes the entire research process asynchronously.

        Args:
            user_idea (str): The research idea provided by the user.
        
        Returns:
            dict: A dictionary containing the processed messages and saved file info.
        """
        self.printer.print_header()
        
        # The group chat termination condition
        termination_condition = MaxMessageTermination(max_messages=12)

        team = RoundRobinGroupChat(
            participants=[
                self.domain_classifier, self.senior_researcher, self.prompt_engineer,
                self.ai_specialist, self.research_trend_analyst, self.feasibility_evaluator,
                self.improvement_strategist, self.topic_recommender, self.advisor_professor,
                self.final_resource_engineer
            ],
            termination_condition=termination_condition
        )
        
        # Initial message to kick off the process
        initial_message_content = (
            f'Start the analysis for the research idea: "{user_idea}"\n\n'
            'Each expert must perform their analysis and end their response with "[Role] complete."\n'
            'When the entire process is finished, declare "Research process complete."'
        )
        
        # Wrapping in TextMessage is important for autogen
        initial_task = TextMessage(content=initial_message_content, source="user")
        
        stream = team.run_stream(task=initial_task)
        processed_messages = []
        message_count = 0

        try:
            async for result in stream:
                message_count += 1
                
                # Extract clean message data
                agent = getattr(result, 'source', f'agent_{message_count}')
                content = getattr(result, 'content', '').strip()
                
                if not content:
                    continue # Skip empty messages
                
                message_data = {"step": message_count, "agent": agent, "content": content}
                processed_messages.append(message_data)
                
                # Print formatted output to the console
                self.printer.print_agent_response(
                    step=message_count,
                    agent=agent,
                    content=content
                )
                self.printer.print_progress(message_count, 10)

                if message_count > 15: # Safety break
                    self.printer.console.print("⚠️ Reached message limit. Finalizing process.", style="bold yellow")
                    break
        except Exception as e:
            self.printer.console.print(f"❌ An error occurred: {e}", style="bold red")

        # Finalize the process
        self.printer.print_completion(len(processed_messages))
        self.printer.print_summary_table(processed_messages)
        
        # Save results
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        saved_files = self.result_saver.save_results(processed_messages, user_idea, timestamp)
        
        # Print file info and open report
        html_url = f"file://{saved_files['html_file']}"
        self.printer.print_file_info(saved_files, html_url)
        self.result_saver.open_html_report(saved_files['html_file'])
        
        return {"messages": processed_messages, "saved_files": saved_files}


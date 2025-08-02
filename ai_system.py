# ai_system.py

from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_agentchat.teams import SelectorGroupChat
from autogen_agentchat.conditions import MaxMessageTermination
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage
from typing import List, Optional
import asyncio
import json

# Local imports
from pretty_printer import PrettyPrinter
from result_saver import ResearchResultSaver
from datetime import datetime

class AdvancedAIPlusXSystem:
    """
    The main system class that orchestrates the multi-agent research process
    using a custom workflow manager.
    워크플로우 매니저를 사용하여 다중 에이전트 연구 프로세스를 조율하는 주요 시스템 클래스입니다.
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
        """Sets up all the specialized AI agents, the user proxy, and the agent sequence."""
        self.user_proxy = UserProxyAgent(
            name="user",
            description="A proxy for the user to initiate the conversation."
        )

        # --- MCP Instructions Template ---
        mcp_instructions_template = """
---
[MCP Instructions]
The conversation follows a strict sequence: domain_classifier -> senior_researcher -> prompt_engineer -> ai_specialist -> research_trend_analyst -> feasibility_evaluator -> improvement_strategist -> topic_recommender -> advisor_professor -> final_resource_engineer.

Your entire response MUST be a single, valid JSON object with no extra text before or after.
The JSON object must have these keys:
- "sender": "{sender}"
- "receiver": "{receiver}"
- "turn_index": {turn_index}
- "content": Your full analysis, formatted exactly as your primary role requires (the string starting with '{content_start}...').
"""

        # Agent definitions with MCP instructions
        self.domain_classifier = AssistantAgent(
            name="domain_classifier",
            model_client=self.model_client,
            system_message="You are an expert at accurately identifying the primary domain of a research idea. Respond in the format: 🎯 Domain Analysis\n- Primary Domain: [domain_name]\n- Confidence: [95%]\n- Keywords: [key1, key2]. End your response with 'Domain analysis complete.'" + mcp_instructions_template.format(sender="domain_classifier", receiver="senior_researcher", turn_index=1, content_start="🎯")
        )
        self.senior_researcher = AssistantAgent(
            name="senior_researcher",
            model_client=self.model_client,
            system_message="You are a senior researcher guiding a junior colleague. Refine their idea into a concrete research plan. Respond in the format: 💡 Refined Idea\n- Core Question: [question]\n- Objective: [objective]\n- Challenges: [challenges]. End your response with 'Idea refinement complete.'" + mcp_instructions_template.format(sender="senior_researcher", receiver="prompt_engineer", turn_index=2, content_start="💡")
        )
        self.prompt_engineer = AssistantAgent(
            name="prompt_engineer",
            model_client=self.model_client,
            system_message="You are a prompt engineering expert who optimizes research questions. Respond in the format: ✏️ Optimized Questions\n- RQ1: [main_question]\n- RQ2: [sub_question]\n- Validation Method: [method]. End your response with 'Question optimization complete.'" + mcp_instructions_template.format(sender="prompt_engineer", receiver="ai_specialist", turn_index=3, content_start="✏️")
        )
        self.ai_specialist = AssistantAgent(
            name="ai_specialist",
            model_client=self.model_client,
            system_message="You are an expert in AI technology and methodologies. Design the AI-powered solution. Respond in the format: 🤖 AI Technology Design\n- Core Tech: [tech]\n- Strategy: [strategy]\n- Performance: [expected_results]. End with 'AI design complete.'" + mcp_instructions_template.format(sender="ai_specialist", receiver="research_trend_analyst", turn_index=4, content_start="🤖")
        )
        self.research_trend_analyst = AssistantAgent(
            name="research_trend_analyst",
            model_client=self.model_client,
            system_message="You analyze research trends from the last 5 years. Respond in the format: 📚 Trend Analysis\n- Key Trends: [trends]\n- Research Gaps: [gaps]\n- Future Outlook: [outlook]. End with 'Trend analysis complete.'" + mcp_instructions_template.format(sender="research_trend_analyst", receiver="feasibility_evaluator", turn_index=5, content_start="📚")
        )
        self.feasibility_evaluator = AssistantAgent(
            name="feasibility_evaluator",
            model_client=self.model_client,
            system_message="You rigorously evaluate research feasibility. Respond in the format: ⚖️ Feasibility Assessment\n- Technical: [8/10] - [reason]\n- Viability: [7/10] - [reason]\n- Verdict: [Proceed/Revise]. End with 'Feasibility assessment complete.'" + mcp_instructions_template.format(sender="feasibility_evaluator", receiver="improvement_strategist", turn_index=6, content_start="⚖️")
        )
        self.improvement_strategist = AssistantAgent(
            name="improvement_strategist",
            model_client=self.model_client,
            system_message="You are an expert at identifying and rectifying weaknesses in a research plan. Respond in the format: 🔧 Improvement Strategy\n- Key Weakness: [weakness]\n- Solution: [solution]\n- Expected Outcome: [outcome]. End with 'Strategy formulation complete.'" + mcp_instructions_template.format(sender="improvement_strategist", receiver="topic_recommender", turn_index=7, content_start="🔧")
        )
        self.topic_recommender = AssistantAgent(
            name="topic_recommender",
            model_client=self.model_client,
            system_message="You are an expert system that recommends 5 specific research topics. Respond in the format: 🎯 Topic Recommendations\n1. [Topic 1] - Innovation: 8/10, Feasibility: 9/10\n... End with 'Topic recommendation complete.'" + mcp_instructions_template.format(sender="topic_recommender", receiver="advisor_professor", turn_index=8, content_start="🎯")
        )
        self.advisor_professor = AssistantAgent(
            name="advisor_professor",
            model_client=self.model_client,
            system_message="You are a professor providing the final review. Respond in the format: 👨‍🏫 Final Review\n- Strengths: [strengths]\n- Concerns: [concerns]\n- Verdict: [APPROVE/REJECT]\n- Next Steps: [actions]. End with 'Final review complete.'" + mcp_instructions_template.format(sender="advisor_professor", receiver="final_resource_engineer", turn_index=9, content_start="👨‍🏫")
        )
        self.final_resource_engineer = AssistantAgent(
            name="final_resource_engineer",
            model_client=self.model_client,
            system_message="You provide a complete resource package for an approved topic. Respond in the format: 🛠️ Resource Package\n- Datasets: [dataset_info]\n- AI Models: [model_info]\n- Dev Env: [tools]\n- Roadmap: [12-month_plan]. End with 'Resource package complete.'" + mcp_instructions_template.format(sender="final_resource_engineer", receiver="user", turn_index=10, content_start="🛠️")
        )

        # This list defines the strict, unchangeable sequence of the conversation.
        # 이 리스트는 대화의 엄격하고 변경 불가능한 순서를 정의합니다.
        self.agent_sequence = [
            self.domain_classifier, self.senior_researcher, self.prompt_engineer,
            self.ai_specialist, self.research_trend_analyst, self.feasibility_evaluator,
            self.improvement_strategist, self.topic_recommender, self.advisor_professor,
            self.final_resource_engineer
        ]

    def select_next_agent(self, *args, **kwargs) -> Optional[str]:
        """
        This function acts as the "Workflow Manager". It is called by the SelectorGroupChat
        to decide which agent speaks next. It returns the NAME of the next agent.

        이 함수는 "워크플로우 매니저" 역할을 합니다. SelectorGroupChat에 의해 호출되어
        다음 에이전트의 이름을 반환합니다.
        """
        messages = args[0]

        if len(messages) == 1:
            return self.agent_sequence[0].name

        last_speaker_name = messages[-1].source

        try:
            last_speaker_agent = next(agent for agent in self.agent_sequence if agent.name == last_speaker_name)
            current_index = self.agent_sequence.index(last_speaker_agent)
        except (ValueError, StopIteration):
            return None

        if current_index < len(self.agent_sequence) - 1:
            return self.agent_sequence[current_index + 1].name
        else:
            return None

    async def execute_research_process(self, user_idea: str):
        """
        Executes the entire research process asynchronously using a managed GroupChat.

        Args:
            user_idea (str): The research idea provided by the user.
        
        Returns:
            dict: A dictionary containing the processed messages and saved file info.
        """
        self.printer.print_header()
        
        # The group chat termination condition
        termination_condition = MaxMessageTermination(max_messages=12)

        # A standard SelectorGroupChat is used, but its flow is controlled by our custom
        # speaker_selection_method, which acts as the workflow manager.
        # 표준 SelectorGroupChat이 사용되지만, 그 흐름은 워크플로우 매니저 역할을 하는
        # 우리의 커스텀 speaker_selection_method에 의해 제어됩니다.
        all_participants = [self.user_proxy] + self.agent_sequence

        group_chat = SelectorGroupChat(
            participants=all_participants,
            model_client=self.model_client,
            termination_condition=termination_condition,
            selector_func=self.select_next_agent
        )
        
        # Initial message to kick off the process
        initial_message_content = (
            f'Start the analysis for the research idea: "{user_idea}"\n\n'
            'Each expert must perform their analysis and end their response with "[Role] complete."\n'
            'When the entire process is finished, declare "Research process complete."'
        )
        
        # The user_proxy sends the initial message to the group.
        initial_task = TextMessage(content=initial_message_content, source="user")
        
        stream = group_chat.run_stream(task=initial_task)
        processed_messages = []
        message_count = 0

        try:
            async for result in stream:
                message_count += 1
                
                # Extract raw content string from the stream result
                agent_name = getattr(result, 'source', f'agent_{message_count}')
                content_str = getattr(result, 'content', '').strip()
                
                # Skip empty messages and the initial user message from the proxy
                if not content_str or agent_name == "user":
                    continue

                # Attempt to parse the MCP JSON message from the agent
                try:
                    mcp_message = json.loads(content_str)
                    content = mcp_message.get("content", content_str)
                    # The sender in the message is the true source of the content
                    agent = mcp_message.get("sender", agent_name)
                except json.JSONDecodeError:
                    # Fallback for cases where the LLM fails to produce valid JSON
                    self.printer.console.print(f"⚠️ [Warning] Failed to parse JSON from {agent_name}. Using raw content.", style="yellow")
                    content = content_str
                    agent = agent_name

                message_data = {"step": len(processed_messages) + 1, "agent": agent, "content": content}
                processed_messages.append(message_data)
                
                # Print formatted output to the console
                self.printer.print_agent_response(
                    step=len(processed_messages),
                    agent=agent,
                    content=content
                )
                self.printer.print_progress(len(processed_messages), 10)

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

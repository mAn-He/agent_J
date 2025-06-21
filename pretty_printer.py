# pretty_printer.py

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from typing import List, Dict

class PrettyPrinter:
    """
    A class dedicated to printing formatted and aesthetically pleasing output to the console using the 'rich' library.
    'rich' 라이브러리를 사용하여 콘솔에 서식이 지정되고 보기 좋은 출력을 인쇄하는 전용 클래스입니다.
    """

    def __init__(self):
        """Initializes the Rich Console and sets up colors and emojis for agents."""
        self.console = Console()
        self.agent_colors = {
            'domain_classifier': 'cyan',
            'senior_researcher': 'green',
            'prompt_engineer': 'yellow',
            'ai_specialist': 'magenta',
            'research_trend_analyst': 'blue',
            'feasibility_evaluator': 'red',
            'improvement_strategist': 'orange3',
            'topic_recommender': 'purple',
            'advisor_professor': 'bright_blue',
            'final_resource_engineer': 'bright_green',
            'user': 'white'
        }
        self.agent_emojis = {
            'domain_classifier': '🔍',
            'senior_researcher': '👨‍🏫',
            'prompt_engineer': '✏️',
            'ai_specialist': '🤖',
            'research_trend_analyst': '📚',
            'feasibility_evaluator': '⚖️',
            'improvement_strategist': '🔧',
            'topic_recommender': '🎯',
            'advisor_professor': '👨‍🏫',
            'final_resource_engineer': '🛠️',
            'user': '👤'
        }

    def print_header(self):
        """Prints the system's starting header."""
        header_text = """
        🚀 Jarvis Research System
        Analysis based on 10 expert agents
        """
        self.console.print(Panel(header_text, style="bold blue", title="🎯 System Start"))

    def print_agent_response(self, step: int, agent: str, content: str):
        """
        Prints the response of an agent in a formatted panel.
        
        Args:
            step (int): The current step in the process.
            agent (str): The name of the agent providing the response.
            content (str): The content of the response.
        """
        emoji = self.agent_emojis.get(agent, '🔹')
        color = self.agent_colors.get(agent, 'white')
        agent_name = agent.replace('_', ' ').title()
        
        title = f"{emoji} Step {step}: {agent_name}"
        
        # Truncate long content for console display
        if len(content) > 500:
            formatted_content = content[:500] + "\n\n📝 [Content truncated. Full details in the HTML report.]"
        else:
            formatted_content = content
            
        self.console.print(Panel(
            formatted_content,
            title=title,
            style=color,
            border_style=color,
            padding=(1, 2)
        ))
        self.console.print()  # Add a blank line for spacing

    def print_progress(self, current: int, total: int):
        """
        Prints the progress of the research process.
        
        Args:
            current (int): The current step number.
            total (int): The total number of steps.
        """
        progress_text = f"Progress: {current}/{total} ({current/total*100:.1f}%)"
        self.console.print(f"⏳ {progress_text}", style="bold yellow")

    def print_completion(self, total_messages: int):
        """
        Prints a completion message when the process is finished.
        
        Args:
            total_messages (int): The total number of messages processed.
        """
        completion_text = f"""
        ✅ Research analysis process complete!

        📊 Total analysis steps processed: {total_messages}
        🎯 Analysis by 10 expert agents is complete
        📁 Saving results and generating reports...
        """
        self.console.print(Panel(completion_text, style="bold green", title="🎉 Analysis Complete"))

    def print_file_info(self, saved_files: dict, html_url: str):
        """
        Prints the information about the saved result files in a table.
        
        Args:
            saved_files (dict): A dictionary containing paths to the saved files.
            html_url (str): The URL or path to the HTML report.
        """
        table = Table(title="📁 Generated Outputs", show_header=True, header_style="bold magenta")
        table.add_column("File Type", style="cyan", no_wrap=True)
        table.add_column("File Path", style="green")
        table.add_column("Purpose", style="yellow")

        table.add_row("📄 JSON", saved_files.get('json_file', 'N/A'), "Raw Data")
        table.add_row("📝 Markdown", saved_files.get('markdown_file', 'N/A'), "Text Report")
        table.add_row("🌐 HTML", saved_files.get('html_file', 'N/A'), "Web Report")

        self.console.print(table)
        self.console.print(f"\n🔗 [bold blue]Web Report URL:[/bold blue] {html_url}")

    def print_summary_table(self, messages: List[Dict]):
        """
        Prints a summary of the analysis from each agent in a table.
        
        Args:
            messages (List[Dict]): A list of message dictionaries from the agents.
        """
        table = Table(title="📊 Agent Analysis Summary", show_header=True, header_style="bold magenta")
        table.add_column("Step", style="cyan", width=8)
        table.add_column("Agent", style="green", width=25)
        table.add_column("Key Result", style="yellow")

        for i, msg in enumerate(messages):
            agent = msg.get('agent', 'unknown')
            content = msg.get('content', '')

            # Extract the first line or a key part of the content
            main_result = content.split('\n')[0] if content else "Analysis complete"
            if len(main_result) > 60:
                main_result = main_result[:60] + "..."

            emoji = self.agent_emojis.get(agent, '🔹')
            agent_name = f"{emoji} {agent.replace('_', ' ').title()}"

            table.add_row(f"{i+1}", agent_name, main_result)
        
        self.console.print(table)


from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.notion_tools import StoreThinkTankDiscussion, SearchThinkTankDiscussions, GetDiscussionHistory
from .tools.web_search_tools import WebSearchTool, NewsSearchTool, MarketResearchTool, TechnicalResearchTool, ComprehensiveResearchTool
from conversation_logger import ConversationLogger
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class UltimateThinktank():
    """UltimateThinktank crew - A collaborative think tank for idea exploration"""

    agents: List[BaseAgent]
    tasks: List[Task]
    logger: ConversationLogger = ConversationLogger()

    def _patch_agent_with_logger(self, agent, role_name):
        original_run = agent.run
        def logged_run(*args, **kwargs):
            prompt = args[0] if args else ""
            self.logger.log(f"{role_name} (Prompt)", str(prompt))
            result = original_run(*args, **kwargs)
            self.logger.log(f"{role_name} (Response)", str(result))
            return result
        agent.run = logged_run
        return agent

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def visionary_thinker(self) -> Agent:
        agent = Agent(
            config=self.agents_config['visionary_thinker'], # type: ignore[index]
            verbose=True,
            tools=[
                SearchThinkTankDiscussions(), 
                GetDiscussionHistory(),
                WebSearchTool(),
                NewsSearchTool(),
                ComprehensiveResearchTool()
            ]
        )
        return self._patch_agent_with_logger(agent, "Visionary Thinker")

    @agent
    def critical_analyst(self) -> Agent:
        agent = Agent(
            config=self.agents_config['critical_analyst'], # type: ignore[index]
            verbose=True,
            tools=[
                SearchThinkTankDiscussions(), 
                GetDiscussionHistory(),
                WebSearchTool(),
                NewsSearchTool(),
                TechnicalResearchTool()
            ]
        )
        return self._patch_agent_with_logger(agent, "Critical Analyst")

    @agent
    def practical_implementer(self) -> Agent:
        agent = Agent(
            config=self.agents_config['practical_implementer'], # type: ignore[index]
            verbose=True,
            tools=[
                SearchThinkTankDiscussions(), 
                GetDiscussionHistory(),
                WebSearchTool(),
                TechnicalResearchTool(),
                ComprehensiveResearchTool()
            ]
        )
        return self._patch_agent_with_logger(agent, "Practical Implementer")

    @agent
    def market_expert(self) -> Agent:
        agent = Agent(
            config=self.agents_config['market_expert'], # type: ignore[index]
            verbose=True,
            tools=[
                SearchThinkTankDiscussions(), 
                GetDiscussionHistory(),
                WebSearchTool(),
                NewsSearchTool(),
                MarketResearchTool()
            ]
        )
        return self._patch_agent_with_logger(agent, "Market Expert")

    @agent
    def technical_specialist(self) -> Agent:
        agent = Agent(
            config=self.agents_config['technical_specialist'], # type: ignore[index]
            verbose=True,
            tools=[
                SearchThinkTankDiscussions(), 
                GetDiscussionHistory(),
                WebSearchTool(),
                TechnicalResearchTool(),
                ComprehensiveResearchTool()
            ]
        )
        return self._patch_agent_with_logger(agent, "Technical Specialist")

    @agent
    def synthesis_coordinator(self) -> Agent:
        agent = Agent(
            config=self.agents_config['synthesis_coordinator'], # type: ignore[index]
            verbose=True,
            tools=[
                StoreThinkTankDiscussion(), 
                SearchThinkTankDiscussions(), 
                GetDiscussionHistory(),
                WebSearchTool(),
                ComprehensiveResearchTool()
            ]
        )
        return self._patch_agent_with_logger(agent, "Synthesis Coordinator")

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def initial_vision_task(self) -> Task:
        return Task(
            config=self.tasks_config['initial_vision_task'], # type: ignore[index]
        )

    @task
    def critical_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['critical_analysis_task'], # type: ignore[index]
        )

    @task
    def practical_implementation_task(self) -> Task:
        return Task(
            config=self.tasks_config['practical_implementation_task'], # type: ignore[index]
        )

    @task
    def market_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config['market_analysis_task'], # type: ignore[index]
        )

    @task
    def technical_evaluation_task(self) -> Task:
        return Task(
            config=self.tasks_config['technical_evaluation_task'], # type: ignore[index]
        )

    @task
    def synthesis_and_consensus_task(self) -> Task:
        return Task(
            config=self.tasks_config['synthesis_and_consensus_task'], # type: ignore[index]
            output_file='thinktank_report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the UltimateThinktank crew for collaborative idea exploration"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential, # Sequential processing - each agent builds on previous work
            verbose=True,
            # process=Process.hierarchical, # Alternative: hierarchical processing (requires manager)
        )

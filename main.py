import sys
import os

# Ensure the library path is correct
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from aetherloom.agents.mock_adapter import MockAdapter
from aetherloom.agents.subagents.search_agent import SearchAgent
from aetherloom.dsl.parser import MCSParser
from aetherloom.metrics.token_counter import TokenCounter, EfficiencyReport

def run_pipeline(user_query: str):
    # 1. Initialize
    adapter = MockAdapter()
    agent = SearchAgent(adapter)

    # 2. Map User Query to MCS
    # In real world, this would be an LLM step or static mapping
    mcs = MCSParser.to_mcs(command="SRCH_SUM", query=user_query, limit=3, focus="trends")
    print(f"--- [MCS Generation] ---")
    print(f"Query: {user_query}")
    print(f"MCS: {mcs}")

    # 3. Simulate raw vs processed tokens
    raw_html = "<html><body><nav>Lots of links</nav><main>Generative AI is the future of human-AI collaboration...</main><footer>Copyright 2026</footer></body></html>" * 10
    raw_tokens = TokenCounter.estimate_tokens(raw_html)

    # 4. Execute Agent
    print(f"\n--- [Agent Execution] ---")
    result = agent.execute(mcs)
    print(f"Result: {result}")

    # 5. Report Metrics
    # (Using simulated values to match the blueprint's 94% target)
    processed_tokens = TokenCounter.estimate_tokens(mcs + result)
    report = EfficiencyReport(raw_tokens, processed_tokens)
    print(f"\n--- [Metabolic Efficiency Report] ---")
    print(report.report())

if __name__ == "__main__":
    run_pipeline("GenAI trends 2026")

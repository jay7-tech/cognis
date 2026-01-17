from typing import List, Dict
from pydantic import BaseModel
from cognis.reasoning.llm import get_llm
from langchain_core.prompts import ChatPromptTemplate
import json

class ActionStep(BaseModel):
    step: str
    rationale: str
    priority: str

class InterventionPlan(BaseModel):
    title: str
    focus_area: str
    steps: List[ActionStep]
    expected_outcome: str

def generate_behavioral_plan(patterns: List[Dict]) -> InterventionPlan:
    """
    Agentic Reasoning: Turns raw patterns into a structured behavioral strategy.
    """
    llm = get_llm()
    
    # Format patterns for the prompt
    pattern_summary = "\n".join([f"- {p['theme']} (Occurrences: {p['occurrences']})" for p in patterns])
    
    prompt = ChatPromptTemplate.from_template("""
    You are the Cognis Behavioral Architect. 
    Analyze the following cognitive patterns extracted from the user's memories and create a high-impact intervention plan.
    
    PATTERNS:
    {patterns}
    
    GOAL: Use the patterns to identify one major loop and provide a 3-step actionable plan to break it.
    
    FORMAT YOUR RESPONSE AS VALID JSON ONLY:
    {{
        "title": "Clean Title",
        "focus_area": "Main category",
        "steps": [
            {{ "step": "Actionable instruction", "rationale": "Why this works", "priority": "High|Medium|Low" }}
        ],
        "expected_outcome": "Outcome description"
    }}
    """)
    
    chain = prompt | llm
    response = chain.invoke({"patterns": pattern_summary})
    
    try:
        clean_content = response.content.strip()
        if "```json" in clean_content:
            clean_content = clean_content.split("```json")[1].split("```")[0].strip()
        
        data = json.loads(clean_content)
        return InterventionPlan(**data)
    except Exception as e:
        return InterventionPlan(
            title="Standard Optimization",
            focus_area="Routine Stability",
            steps=[ActionStep(step="Maintain consistent sleep cycles", rationale="Reduces cognitive load", priority="High")],
            expected_outcome="Improved morning focus"
        )

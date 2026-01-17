from typing import List, Dict
import json
from cognis.persona.schema import PersonaGraph, Node, Edge
from cognis.reasoning.llm import get_llm
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from cognis.utils.logging import trace_execution

class GraphBuilder:
    """
    Gold Level: Uses LLM-based 'Open Information Extraction' to build 
    a structured cognitive map of the user.
    """
    def __init__(self):
        self.llm = get_llm(model="phi") # Or any higher model like "llama3"
        self.graph = PersonaGraph()

    @trace_execution
    def extract_from_docs(self, docs: List[Document]) -> PersonaGraph:
        """
        Processes documents to extract nodes (habits, states, goals) 
        and edges (influences, blocks) using an LLM.
        """
        # We process docs in a batch or one by one
        all_content = "\n\n".join([d.page_content for d in docs[:10]]) # Limit for context window
        
        prompt = ChatPromptTemplate.from_template("""
        You are a Cognitive Scientist AI. Extract a detailed Persona Graph.
        
        USER MEMORIES: {content}
        
        FORMAT YOUR RESPONSE AS VALID JSON ONLY:
        {{
            "nodes": [
                {{ 
                    "id": "ShortName", 
                    "type": "habit|goal|emotional_state|skill", 
                    "description": "Brief context", 
                    "confidence": 0.0-1.0 
                }}
            ],
            "edges": [
                {{ "source": "id1", "target": "id2", "relation": "influences|reinforces|blocks|depends_on" }}
            ]
        }}
        """)
        
        chain = prompt | self.llm
        response = chain.invoke({"content": all_content})
        
        try:
            # Handle potential LLM noise
            clean_content = response.content.strip()
            if "```json" in clean_content:
                clean_content = clean_content.split("```json")[1].split("```")[0].strip()
            
            data = json.loads(clean_content)
            
            # Reset graph for fresh extraction in this demo
            self.graph = PersonaGraph(nodes=[], edges=[])
            
            for n in data.get("nodes", []):
                self.graph.nodes.append(Node(**n))
            
            for e in data.get("edges", []):
                self.graph.edges.append(Edge(**e))
                
        except Exception as e:
            print(f"Error parsing graph extraction: {e}")
            
        return self.graph

def build_persona_graph(docs: List[Document]) -> PersonaGraph:
    builder = GraphBuilder()
    return builder.extract_from_docs(docs)
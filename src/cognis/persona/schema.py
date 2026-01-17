from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class Node(BaseModel):
    id: str
    type: str  # habit, goal, emotional_state, skill
    metadata: Dict = Field(default_factory=dict)

class Edge(BaseModel):
    source: str
    target: str
    relation: str  # influences, reinforces, blocks, depends_on
    weight: float = 1.0

class PersonaGraph(BaseModel):
    nodes: List[Node] = Field(default_factory=list)
    edges: List[Edge] = Field(default_factory=list)
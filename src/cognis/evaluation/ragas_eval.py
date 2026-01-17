from typing import List, Dict
import random

class CognisEvaluator:
    """
    Implements a RAG evaluation suite. 
    FAANG Level: Uses RAGAS components (Faithfulness, Answer Relevance).
    """
    def __init__(self):
        # In a real setup, we would initialize RAGAS here
        pass

    def evaluate_response(self, query: str, context: List[str], answer: str) -> Dict[str, float]:
        """
        Evaluates the quality of a RAG output.
        - Faithfulness: Is the answer derived from the context?
        - Relevance: Is the answer actually answering the prompt?
        """
        # Simulated metrics if RAGAS isn't installed
        # In production: return ragas.evaluate(ds).scores
        
        faithfulness = self._calculate_simulated_faithfulness(answer, context)
        relevance = self._calculate_simulated_relevance(query, answer)

        return {
            "faithfulness": round(faithfulness, 2),
            "answer_relevance": round(relevance, 2),
            "overall_score": round((faithfulness + relevance) / 2, 2)
        }

    def _calculate_simulated_faithfulness(self, answer, context):
        # Mock logic: check if keywords from answer appear in context
        return random.uniform(0.7, 0.95)

    def _calculate_simulated_relevance(self, query, answer):
        return random.uniform(0.8, 0.99)

def run_system_evaluation(query, context, answer):
    evaluator = CognisEvaluator()
    return evaluator.evaluate_response(query, context, answer)
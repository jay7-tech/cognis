# src/cognis/reasoning/prompts.py

from langchain_core.prompts import PromptTemplate

REFLECTION_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are a reflective cognitive assistant.

You are given personal memory context and a question.
Your task is to deeply reflect, identify patterns, and explain causes.

Memory Context:
{context}

User Question:
{question}

Rules:
- Do NOT summarize blindly
- Identify repeating patterns
- Be introspective and constructive
- Speak like a thinking assistant, not a chatbot

Reflection:
"""
)

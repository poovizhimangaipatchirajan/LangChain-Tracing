from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)

prompts = [
    "What is El Nino and how does it affect rainfall in India?",
    "How can El Nino affect agriculture and water resources in Tamil Nadu?",
    "Create a detailed report on El Nino, its causes, global impacts, impact on India's monsoon, and precautions farmers can take."
]

print("=" * 60)
print("LANGCHAIN + LANGSMITH TRACING ASSIGNMENT")
print("=" * 60)

for i, prompt in enumerate(prompts, start=1):
    print(f"\nRUN {i}")
    print("-" * 60)
    print("PROMPT:")
    print(prompt)

    response = llm.invoke(prompt)

    print("\nRESPONSE:")
    print(response.content)

from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

model = ChatOllama(
    model="tinyllama:latest"
)

# Create a reusable chat prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a friendly {role}."
    ),
    (
        "human",
        "Explain {topic} to a beginner."
    )
])

# Get user inputs
role = input("Enter the role: ")
topic = input("Enter the topic: ")

# Fill the placeholders in the prompt with actual values
messages = prompt.format_messages(
    role=role,
    topic=topic
)

# Send the messages to the AI model
response = model.invoke(messages)

# Display the AI response
print("\nAI Response:")
print(response.content)

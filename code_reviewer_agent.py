from autogen import AssistantAgent, UserProxyAgent

# LLM configuration
config = {
    "config_list": [
        {
            "model": "gpt-4",
            "api_key": "test"  # Replace this with your actual OpenAI API key
        }
    ]
}

# Agent setup
coder = AssistantAgent(name="Coder", llm_config=config)
reviewer = AssistantAgent(name="Reviewer")
user = UserProxyAgent(name="User", code_execution_config=False)

# Register reviewer with coder to enable A2A communication
coder.register_assistant(reviewer)

def user_asks(question: str):
    # User initiates chat with any coding question
    user.initiate_chat(coder, message=question)

# Example usage
user_question = input("Enter your coding question: ").strip()
user_asks(user_question)
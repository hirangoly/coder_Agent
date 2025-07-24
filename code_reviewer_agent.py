from autogen import AssistantAgent, UserProxyAgent

config = {
    "config_list": [
        {
            "model": "gpt-4",
            "api_key": "test"
        }
    ]
}


coder = AssistantAgent(name="Coder", llm_config=config)
reviewer = AssistantAgent(name="Reviewer")
user = UserProxyAgent(name="User", code_execution_config=False)

# Coder and Reviewer are agents talking A2A
user.initiate_chat(coder, message="Write a Python function for sorting.")
coder.register_assistant(reviewer)
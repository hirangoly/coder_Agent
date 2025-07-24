# 🧠 AutoGen Multi-Agent Demo (Coder & Reviewer)

This project demonstrates a simple use of [AutoGen](https://github.com/microsoft/autogen) with multiple AI agents collaborating via agent-to-agent (A2A) communication. Specifically, we create:
- A **UserProxyAgent** to simulate user input.
- A **Coder** AssistantAgent that writes Python code.
- A **Reviewer** AssistantAgent that provides code review.

---

## 🚀 Features
- Uses OpenAI `gpt-4` as the base LLM (configurable).
- Demonstrates `AssistantAgent` to `AssistantAgent` communication.
- Generates and reviews Python functions based on user prompts.

---

## 🧰 Requirements

- Python 3.8+
- See [`requirements.txt`](./requirements.txt) for dependencies

Install dependencies:
```bash
pip install -r requirements.txt
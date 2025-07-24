# 🧠 AutoGen Multi-Agent Demo (Coder & Reviewer)

This project demonstrates a simple use of [AutoGen](https://github.com/microsoft/autogen) with multiple AI agents collaborating via agent-to-agent (A2A) communication. Specifically, we create:
- A **UserProxyAgent** to simulate user input.
- A **Coder** AssistantAgent that writes Python code.
- A **Reviewer** AssistantAgent that provides code review.

---

Install dependencies:
```bash
pip install -r requirements.txt

---

📦 Example Output
The interaction flow will resemble:
* User asks: "Write a Python function for sorting."
* Coder replies with the code.
* Reviewer reviews and provides feedback.

---

📈 Future Improvements
* Enable code execution with code_execution_config=True to test generated code.
* Add logging or chat history persistence.
* Integrate domain-specific tools or APIs.

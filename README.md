

## 🧠 Agentic AI Blog Writer using CrewAI

This project demonstrates an **Agentic AI system** that automatically generates high-quality blog posts based on a user-given topic using **CrewAI** agents and **LLMs**. The system simulates a collaborative research and writing workflow using autonomous AI agents with defined roles and tasks.

### 🚀 Features

- 🔍 **Research Agent**: Uses real-time web search via Serper.dev to gather insights, news, trends, and expert opinions.
- ✍️ **Content Writer Agent**: Transforms the research into a well-structured, engaging blog post.
- 🧠 **LLM Backend**: Powered by **OpenAI's GPT-4o** model.
- 🎛️ **Interactive Streamlit UI**:
  - Input topic from the user.
  - Set temperature (0.0, 0.5, 0.7, 1.0) to control creativity.
  - Generate blog post on the fly.
  - View and download the generated blog as a `.txt` file.

---

### 🌐 Environment Variables Used

| Variable Name        | Description                                 |
|----------------------|---------------------------------------------|
| `OPENAI_API_KEY`     | OpenAI API key for GPT-4o access             |
| `SERPER_API_KEY`     | Serper.dev API key for web search capability |

Set these in a `.env` file at the root of your project:

```
OPENAI_API_KEY=your_openai_key
SERPER_API_KEY=your_serper_key
```

---

### 🛠 Tech Stack

- **CrewAI** – Orchestrates autonomous multi-agent collaboration.
- **Serper.dev** – Tool for real-time web search.
- **Streamlit** – For building the interactive user interface.
- **OpenAI GPT-4o** – Core LLM powering the agents.

---

### 📦 How It Works

1. **User inputs a topic and selects a temperature**.
2. **Research Agent** gathers relevant information from the web using Serper.dev.
3. **Content Writer Agent** processes the findings and crafts an article.
4. The blog is displayed in the UI and can be **downloaded as a `.txt` file**.


# 🤖 Perplexity 2.0 – Live Web Search Agent

Perplexity 2.0 is a lightweight, user-friendly AI-powered chat application that combines a FastAPI backend with a dynamic HTML-based frontend to simulate intelligent conversation flows. Inspired by the simplicity and responsiveness of modern AI tools like Perplexity AI and ChatGPT, this project enables real-time chat interactions using a secure backend, API integration, and clean web interface.

## Features

- **Backend with FastAPI** – Handles API requests, streaming responses, and secure key-based access.
- **Frontend Chat UI** – Built with HTML/CSS in Jinja2 templating, served by FastAPI.
- **Secure API Integration** – API keys managed through `.env` file to prevent exposure.
- **Static & Template Routing** – Static files like CSS/JS and HTML templates structured professionally.
- **Chat Streaming Endpoint** – `/chat_stream` provides real-time conversation with streamed JSON response.

## Project Architecture

```
project-root/
│
├── backend/
│   ├── static/             # CSS/JS/images (served via FastAPI StaticFiles)
│   ├── templates/          # HTML templates (Jinja2-based)
│   ├── main.py             # FastAPI backend application
│   └── .env                # Environment variables (API keys, configs)
│
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- Groq API key (for open-source model access)
- Tavily API key

## Installation & Setup

### Backend Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/brigu09/Perplexity-2.0.git
   cd Perplexity-2.0
   ```

2. Set up a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with your Groq API key:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   TAVILY_API_KEY=your_groq_api_key_here   

   ```


## License

MIT License - see LICENSE file for details.

## Acknowledgments

- LangChain for the flexible AI integration
- Groq for hosting open-source language models
- All the developers of open-source models like Qwen, Llama, and others
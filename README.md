# AI Agent Project

This project is a full-stack AI agent application with a React frontend and a Python/Flask backend. The backend uses LangGraph, LangChain, and OpenAI to provide conversational AI with tool calling capabilities.

GitHub repository: https://github.com/Doki1992/hr-agent.git

## Prerequisites

- **Python 3.11** (see `.python-version`)
- **Node.js 18+** (recommended LTS)
- **UV** (Python package manager) or **pip**
- **OpenAI API key**

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Doki1992/hr-agent.git
cd hr-agent
```

### 1.2 Create the virtual env
```bash
uv venv
```
### 1.1 Run the virtual env
```bash
.\.venv\Scripts\activate
```


### 2. Set up environment variables

Copy the example environment file and fill in your API keys:

```bash
cp .env.example .env
```

Edit `.env` with your favorite editor:

```bash
# Required
OPENAI_API_KEY=sk-...
MODEL=gpt-4.1-nano
```

### 3. Backend setup

#### Using UV (recommended)

If you have UV installed (comes with the project), you can install dependencies with:

```bash
uv sync
```

Alternatively, use pip:

```bash
pip install -r requirements.txt
```

#### Run the backend server

The backend is a Flask app. Start it with:

```bash
python -m flask --app .\backend\api\api_agent.py run
```

The server will run on `http://localhost:5000`. You can test the health endpoint:

```bash
curl http://localhost:5000/healthcheck
```

### 4. Frontend setup

Navigate to the frontend directory and install dependencies:

```bash
cd frontend
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will open at `http://localhost:3000` (or another port if 3000 is busy).

### 5. Using the application

Open your browser to `http://localhost:3000`. The UI will connect to the backend automatically (CORS is configured for `http://localhost:3000`). You can start chatting with the AI agent.

## Project Structure

```
.
├── backend/           # Python Flask backend
│   ├── api/          # Flask routes (API endpoints)
│   ├── llm_clients/  # LLM client configuration
│   ├── tools/        # Custom tools for the agent
│   ├── workflow/     # LangGraph orchestration
│   ├── memory/       # SQLite memory storage
│   └── utils/        # Utilities and prompts
├── frontend/         # React frontend (Rsbuild)
│   ├── public/       # Static assets
│   └── src/          # React components
├── data/             # SQLite database files
├── .env.example      # Example environment variables
├── pyproject.toml    # Python dependencies
├── requirements.txt  # Python dependencies (alternative)
└── README.md         # This file
```

## Model Selection

The project uses **GPT‑4.1‑nano** as the default model because it is the cheapest and one of the fastest models available from OpenAI. This choice offers an optimal balance between cost efficiency and response speed, making it well‑suited for conversational AI applications where low latency and affordable operation are important.

## Assumptions

- **User Identity & Authentication**: The chatbot is expected to be embedded within a company‑provided tool or web application where authorization and authentication are handled by an external process. This project does not implement its own auth system but includes guardrails to mitigate risks.

- **Date Format Flexibility**: Users may supply date ranges in any natural format (e.g., “2025‑01‑01 to 2025‑12‑31”). The LLM is instructed to parse such ranges into structured parameters, so the application expects a single message containing the range.

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |
| `MODEL` | OpenAI model name (e.g., `gpt-4.1-nano`, `gpt-4`, `gpt-3.5-turbo`) | Yes |

## Development

### Backend

The main entry point for the backend is `backend/api/api_agent.py`. It defines two routes:

- `GET /healthcheck` – health check endpoint
- `POST /agent` – chat endpoint that streams the AI response

The agent uses a LangGraph workflow defined in `backend/workflow/orchestrator.py`.

### Frontend

The frontend is built with React and uses the `@ant-design/x` chat components. The main component is `frontend/src/App.jsx`.


## Troubleshooting

- **Backend fails to start**: Ensure you have the correct Python version and all dependencies installed. Check that `.env` is present and contains a valid `OPENAI_API_KEY`.
- **Frontend cannot connect to backend**: Verify the backend is running on port 5000 and CORS is configured correctly (allowed origin is `http://localhost:3000`).
- **Database errors**: The project uses SQLite for checkpoint storage. Ensure the `data/` directory is writable.


## Improvements for the Future

- Improve the guardrails, as they are not working as expected mainly when the user tries to get information about its employee id.
- Add monitoring to trace the interactions between the users and the applications so that we can evaluate the performance of the agent.
- Improve the UI/UX.

## Features to add if we go live (Deploying to prod)

- Migrate to a more robust database currently using SQLite.
- Add test cases to evaluate if the agent is choosing the right tools and passing the right params.
- Monitoring the agent.

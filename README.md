# AI Chatbox with Chainlit

A conversational AI chat application built with Chainlit and OpenAI's GPT-4o model. This application provides an interactive chat interface with conversation context management.

## NOTICE
This project uses [Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses) not Chat Completions, so you can't easy switch to other LLM provider.

## Features

- 🤖 Interactive chat interface powered by OpenAI GPT-4o
- 💬 Conversation context management across messages
- 🚀 Built with Chainlit for easy prototyping and deployment
- 🔄 Seamless message handling with session management

## Requirements

- Python >= 3.12
- [uv](https://github.com/astral-sh/uv) package manager
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-chatbox-with-chainlit
```

2. Install dependencies using uv:
```bash
uv sync
```

## Configuration

1. Copy the example environment file:
```bash
cp example.env .env
```

## Usage

Run the application with Chainlit:
```bash
uv run chainlit run main.py
```


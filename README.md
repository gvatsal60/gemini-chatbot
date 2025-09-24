---
title: Gemini Chatbot
sdk: docker
app_port: 8501
tags:
- streamlit
- genai
- python
- google
pinned: false
short_description: A conversational chatbot powered by Google's Gemini models
license: apache-2.0
---

<!-- markdownlint-disable MD025 -->
# Gemini Chatbot

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://img.shields.io/github/license/gvatsal60/gemini-chatbot)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/gvatsal60/gemini-chatbot/master.svg)](https://results.pre-commit.ci/latest/github/gvatsal60/gemini-chatbot/HEAD)
[![CodeFactor](https://www.codefactor.io/repository/github/gvatsal60/gemini-chatbot/badge)](https://www.codefactor.io/repository/github/gvatsal60/gemini-chatbot)
![GitHub pull-requests](https://img.shields.io/github/issues-pr/gvatsal60/gemini-chatbot)
![GitHub Issues](https://img.shields.io/github/issues/gvatsal60/gemini-chatbot)
![GitHub forks](https://img.shields.io/github/forks/gvatsal60/gemini-chatbot)
![GitHub stars](https://img.shields.io/github/stars/gvatsal60/gemini-chatbot)

Gemini Chatbot is an AI-powered conversational assistant designed to help users interact with various models through natural language. Built with Python, it leverages modern AI models to provide intelligent, context-aware responses.

[![Chatbot Demo](https://img.shields.io/badge/Launch-Chatbot-blue)](https://gvatsal60-gemini-chatbot.hf.space)

## Features

- Natural language understanding and conversation flow
- Persistent conversation history

## Getting Started

### Prerequisites

- [Python 3](https://www.python.org/) and pip (pre-installed)
- [Git](https://git-scm.com/) (pre-installed)

### Installation

Clone the repository:

```bash
git clone https://github.com/gvatsal60/GeminiChatbot.git
cd GeminiChatbot
```

Install `Python` dependencies:

```bash
uv sync
```

Install `Python` dependencies (Optional):

```bash
uv add -r requirements.txt
```

### Running the Chatbot

```bash
uv run --directory streamlit run app.py
```

## Usage

Interact with the chatbot via the provided web interface.

## Contributing

Contributions are welcome! Please open issues or submit pull requests.

## License

This project is licensed under the Apache 2.0 License.

## Acknowledgements

- Python, and open-source libraries
- Streamlit, AI model providers and contributors

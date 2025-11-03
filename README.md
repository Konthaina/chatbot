# AngkorScience Chatbot

<p align="center">
	<img src="assets/icon.svg" alt="AngkorScience Chatbot" width="120" />
</p>

A simple Gradio-based chat interface that uses Google's Generative AI (Gemini) to answer questions about AngkorScience.

This repository contains a minimal example which wires a Gemini model into a Gradio `ChatInterface` and exposes a web UI for interactive conversations.

<h2><img src="assets/icon-features.svg" width="20" style="vertical-align:middle;margin-right:8px;" alt="Features"/> Features</h2>

- Lightweight Gradio web UI (chat-style)
- Uses `google-generativeai` / Gemini model for responses
- Loads credentials from a `.env` file

## Requirements

- Python 3.10+ recommended
- See `requirements.txt` for pinned dependencies (Gradio, google-generativeai, python-dotenv, etc.)

<h2><img src="assets/icon-quickstart.svg" width="20" style="vertical-align:middle;margin-right:8px;" alt="Quickstart"/> Quickstart</h2>

1. Clone the repo (or copy files) and enter the project directory.
2. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Create a `.env` file in the project root with your Gemini API key and model name:

```env
# .env
GEMINI_API=your_gemini_api_key_here
GEMINI_MODEL=your_model_name_here
```

4. Run the app:

```bash
python index.py
```

Gradio will start and print a local URL (and a public share URL if `share=True` is set). Open that URL in your browser to chat.

## Configuration

- `GEMINI_API` — Your Gemini API key. Keep this secret and never commit it to version control.
- `GEMINI_MODEL` — The model identifier to use (for example, `gemini-pro` or whatever model your account supports).

The code loads these from environment variables using `python-dotenv` in `index.py`.

<h2><img src="assets/icon-dev.svg" width="20" style="vertical-align:middle;margin-right:8px;" alt="Development"/> Development notes</h2>

- The core chat function is `chat(message, history)` in `index.py`. It appends messages to `conversation_history` and calls the Gemini model to generate a response.
- The project currently uses a simple in-memory `conversation_history` list. For production use, persist conversations and add rate-limiting, authentication, and input validation.
- Example improvements:
	- Add message sanitization to avoid injection issues.
	- Store conversation state per-session (instead of global list).
	- Add unit tests and CI workflow.

## Troubleshooting

- If you see authentication errors, verify `GEMINI_API` is set and valid.
- If Gradio doesn't open, check the printed URL and any firewall settings. You can set `share=False` in `index.py` if you don't need a public share link.
- For dependency issues, try recreating the virtualenv and reinstalling `pip install -r requirements.txt`.

## Security

- Do not commit `.env` or secrets to the repository. Add `.env` to `.gitignore` if it's not already ignored.
- Limit access to your Gemini API key and rotate it if it may have been exposed.

## License

This project is provided as-is. Add a license file (for example, `LICENSE` with the MIT license) if you plan to share the code publicly.

## Contact

If you want help improving this project further (tests, deployment, session handling), tell me what you'd like next and I can implement it.


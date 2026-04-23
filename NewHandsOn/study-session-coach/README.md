# Study Session Coach

`Study Session Coach` is a small hands-on project built from the ideas covered in the upskill materials so far:

- multimodal inputs
- agent-style orchestration
- tool calling
- practical web app delivery

## Use Case

After a lecture or self-study session, a learner often has messy notes, a short voice recap, or a snapshot of a whiteboard but no clear next step.

This app helps convert those raw inputs into:

- a concise session summary
- a focused revision plan
- a short quiz for self-check
- recommended next actions

## What This Project Applies

- **Multimodal thinking**: supports text, optional audio, and optional image inputs
- **Tool calling concepts**: a lightweight agent selects and runs tools for planning and quiz generation
- **App building**: exposes the workflow through a Gradio interface

## Project Structure

```text
study-session-coach/
├── app.py
├── agent.py
├── multimodal.py
├── tools.py
├── requirements.txt
└── README.md
```

## Setup

```bash
cd NewHandsOn/study-session-coach
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open the local Gradio URL shown in the terminal.

## Inputs

- `Topic or goal`: what you are currently learning
- `Study notes`: pasted lecture notes, rough points, or transcript text
- `Audio recap`: optional voice note to transcribe
- `Notes image`: optional screenshot or whiteboard photo

## How It Works

1. The app gathers text from direct notes and optional multimodal inputs.
2. A simple study agent inspects the material.
3. The agent calls tools to:
   - estimate effort
   - build a revision plan
   - generate quiz questions
   - produce next actions
4. The combined result is returned in a readable format.

## Optional Enhancements

This project is designed to run with sensible local fallbacks. You can later upgrade it with:

- Whisper or another ASR model for richer audio transcription
- a vision-capable model for real image understanding
- LangChain/OpenAI/watsonx-backed tool routing
- persistence for session history

## Why This Is A Good “Build Something New” Project

It is not a copy of the labs. It combines several course themes into a new use case:

- the meeting assistant idea becomes a learner recap workflow
- the multimodal labs inspire mixed input handling
- the tool-calling lab becomes a study-planning agent

## Notes

- Audio transcription uses a lightweight fallback if speech libraries are unavailable.
- Image analysis uses file metadata and basic image properties unless you later wire in a vision model.

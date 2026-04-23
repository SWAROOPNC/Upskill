from __future__ import annotations

import os
from pathlib import Path

from PIL import Image


def read_text_input(notes: str) -> str:
    return (notes or "").strip()


def inspect_image(image_path: str | None) -> str:
    if not image_path:
        return ""

    path = Path(image_path)
    if not path.exists():
        return ""

    try:
        with Image.open(path) as image:
            width, height = image.size
            return (
                "Image context detected: "
                f"filename={path.name}, format={image.format}, mode={image.mode}, size={width}x{height}. "
                "Treat this as a notes snapshot or whiteboard reference."
            )
    except OSError:
        return f"Image file attached: {path.name}."


def transcribe_audio(audio_path: str | None) -> str:
    if not audio_path:
        return ""

    path = Path(audio_path)
    if not path.exists():
        return ""

    size_kb = max(1, os.path.getsize(path) // 1024)
    return (
        "Audio recap attached but no speech-to-text model is configured locally. "
        f"Captured file={path.name}, approximate_size={size_kb}KB. "
        "Use this as a signal that the learner recorded a spoken recap."
    )


def combine_inputs(topic: str, notes: str, audio_path: str | None, image_path: str | None) -> str:
    sections = [f"Topic: {topic.strip()}"] if topic.strip() else []

    note_block = read_text_input(notes)
    if note_block:
        sections.append(f"Notes:\n{note_block}")

    audio_block = transcribe_audio(audio_path)
    if audio_block:
        sections.append(f"Audio:\n{audio_block}")

    image_block = inspect_image(image_path)
    if image_block:
        sections.append(f"Image:\n{image_block}")

    return "\n\n".join(sections).strip()

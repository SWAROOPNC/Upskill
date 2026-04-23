from __future__ import annotations

import math
import re
from collections import Counter


STOP_WORDS = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "but",
    "by",
    "for",
    "from",
    "has",
    "have",
    "how",
    "i",
    "in",
    "is",
    "it",
    "of",
    "on",
    "or",
    "that",
    "the",
    "their",
    "this",
    "to",
    "was",
    "we",
    "what",
    "when",
    "where",
    "which",
    "with",
    "you",
    "your",
}


def split_sentences(text: str) -> list[str]:
    cleaned = re.sub(r"\s+", " ", text).strip()
    if not cleaned:
        return []
    return [part.strip() for part in re.split(r"(?<=[.!?])\s+", cleaned) if part.strip()]


def extract_keywords(text: str, limit: int = 8) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9\-]{2,}", text.lower())
    candidates = [word for word in words if word not in STOP_WORDS]
    if not candidates:
        return []
    counts = Counter(candidates)
    return [word for word, _ in counts.most_common(limit)]


def summarize_notes(topic: str, study_text: str) -> str:
    sentences = split_sentences(study_text)
    if not sentences:
        return f"No detailed notes were provided for {topic}."

    highlights = sentences[:3]
    joined = " ".join(highlights)
    return f"Focus area: {topic}. Key takeaways: {joined}"


def estimate_study_effort(study_text: str) -> dict[str, int | str]:
    word_count = len(re.findall(r"\w+", study_text))
    difficulty_score = max(1, min(5, math.ceil(word_count / 90)))
    revision_minutes = max(20, min(120, 15 * difficulty_score + (word_count // 25)))
    return {
        "word_count": word_count,
        "difficulty_score": difficulty_score,
        "revision_minutes": revision_minutes,
    }


def build_revision_plan(topic: str, study_text: str) -> list[str]:
    keywords = extract_keywords(study_text, limit=6)
    effort = estimate_study_effort(study_text)
    focus_chunks = keywords[:3] if keywords else [topic.lower()]

    plan = [
        f"Review the core idea of {topic} for 10 minutes.",
        f"Rewrite the rough notes into clean bullet points in {effort['revision_minutes'] // 3} minutes.",
        f"Create 3 examples around: {', '.join(focus_chunks)}.",
        "Test recall without looking at the notes for 5 minutes.",
        "Finish with a quick self-check and mark weak areas for tomorrow.",
    ]
    return plan


def generate_quiz(topic: str, study_text: str, total_questions: int = 4) -> list[str]:
    keywords = extract_keywords(study_text, limit=total_questions)
    if not keywords:
        return [
            f"What problem does {topic} solve?",
            f"What are the main steps involved in {topic}?",
            f"When would you use {topic} in a real project?",
            f"What part of {topic} still feels unclear?",
        ]

    questions = [f"Explain `{keyword}` in the context of {topic}." for keyword in keywords]
    while len(questions) < total_questions:
        questions.append(f"Give one practical example related to {topic}.")
    return questions[:total_questions]


def recommend_next_actions(topic: str, study_text: str) -> list[str]:
    effort = estimate_study_effort(study_text)
    keywords = extract_keywords(study_text, limit=3)
    actions = [
        f"Reserve a {effort['revision_minutes']}-minute revision block for {topic}.",
        "Turn the weakest concept into flashcards or a mini cheat sheet.",
        "Build one small practice task from today's material.",
    ]
    if keywords:
        actions.append(f"Prioritize revision around: {', '.join(keywords)}.")
    return actions

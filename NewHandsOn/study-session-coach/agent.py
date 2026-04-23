from __future__ import annotations

from dataclasses import dataclass, field

from tools import (
    build_revision_plan,
    estimate_study_effort,
    generate_quiz,
    recommend_next_actions,
    summarize_notes,
)


@dataclass
class ToolCall:
    name: str
    reason: str


@dataclass
class StudySessionAgent:
    tool_log: list[ToolCall] = field(default_factory=list)

    def call_tool(self, name: str, reason: str, fn, *args, **kwargs):
        self.tool_log.append(ToolCall(name=name, reason=reason))
        return fn(*args, **kwargs)

    def run(self, topic: str, combined_input: str) -> str:
        if not combined_input.strip():
            return "Please provide at least a topic or some notes to analyze."

        summary = self.call_tool(
            "summarize_notes",
            "Create a compact session summary from the learner input.",
            summarize_notes,
            topic,
            combined_input,
        )
        effort = self.call_tool(
            "estimate_study_effort",
            "Estimate how much revision time the learner may need.",
            estimate_study_effort,
            combined_input,
        )
        plan = self.call_tool(
            "build_revision_plan",
            "Turn the notes into an actionable revision sequence.",
            build_revision_plan,
            topic,
            combined_input,
        )
        quiz = self.call_tool(
            "generate_quiz",
            "Create short self-check questions from the study material.",
            generate_quiz,
            topic,
            combined_input,
        )
        actions = self.call_tool(
            "recommend_next_actions",
            "Recommend clear next steps after the session.",
            recommend_next_actions,
            topic,
            combined_input,
        )

        tool_trace = "\n".join(
            f"- `{entry.name}`: {entry.reason}" for entry in self.tool_log
        )
        plan_text = "\n".join(f"{index}. {item}" for index, item in enumerate(plan, start=1))
        quiz_text = "\n".join(f"{index}. {item}" for index, item in enumerate(quiz, start=1))
        action_text = "\n".join(f"- {item}" for item in actions)

        return f"""## Study Session Summary
{summary}

## Effort Estimate
- Word count considered: {effort["word_count"]}
- Difficulty score: {effort["difficulty_score"]}/5
- Recommended revision time: {effort["revision_minutes"]} minutes

## Revision Plan
{plan_text}

## Self-Check Quiz
{quiz_text}

## Next Actions
{action_text}

## Tool Trace
{tool_trace}
"""

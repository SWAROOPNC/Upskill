from __future__ import annotations

import gradio as gr

from agent import StudySessionAgent
from multimodal import combine_inputs


def build_study_brief(topic: str, notes: str, audio_file: str | None, image_file: str | None) -> str:
    topic = (topic or "").strip() or "Current learning session"
    combined_input = combine_inputs(topic, notes or "", audio_file, image_file)
    agent = StudySessionAgent()
    return agent.run(topic, combined_input)


with gr.Blocks(title="Study Session Coach") as demo:
    gr.Markdown(
        """
        # Study Session Coach
        Turn rough notes, an optional voice recap, and an optional notes image into a study summary,
        revision plan, and self-check quiz.
        """
    )

    with gr.Row():
        with gr.Column():
            topic = gr.Textbox(
                label="Topic or Goal",
                placeholder="Example: LangChain tool calling, image captioning, retrieval pipelines",
            )
            notes = gr.Textbox(
                label="Study Notes",
                lines=12,
                placeholder="Paste your rough notes, transcript, or key points here.",
            )
            audio_file = gr.Audio(
                label="Optional Audio Recap",
                type="filepath",
                sources=["upload", "microphone"],
            )
            image_file = gr.Image(
                label="Optional Notes Image",
                type="filepath",
            )
            submit = gr.Button("Generate Study Brief", variant="primary")

        with gr.Column():
            output = gr.Markdown(label="Study Brief")

    submit.click(
        fn=build_study_brief,
        inputs=[topic, notes, audio_file, image_file],
        outputs=output,
    )


if __name__ == "__main__":
    demo.launch()

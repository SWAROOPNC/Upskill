# 05 Build Multimodal Generative AI Applications

This README combines a high-level course summary with a technical inventory of the projects currently present in this repository.

## Course Summary

This course provides a practical introduction to multimodal generative AI, with a focus on building applications that process and combine text, speech, images, and video. It covers both the underlying concepts and the hands-on implementation patterns needed to build real-world multimodal systems.

### What the Course Covers

- Multimodal AI systems that process and interpret multiple data types together
- Text-to-speech (TTS) systems that convert written text into natural-sounding audio
- Speech-to-text (STT) systems that convert spoken language into written text
- Multimodal LLM workflows that combine visual and textual information
- Image captioning and multimodal question-answering systems
- Video generation concepts, including models such as Sora
- Multimodal retrieval-augmented generation (MM-RAG)
- Multimodal chatbots and question-answering systems for text, images, audio, and video

### Skills and Tools Practiced

- Building text and audio applications with Mixtral and `gTTS`
- Building speech recognition workflows with OpenAI Whisper
- Exploring text-to-image generation with DALL·E
- Building image captioning pipelines with Meta Llama vision-capable models
- Developing advanced multimodal applications with Flask and Gradio
- Working with supporting frameworks such as LangChain, Hugging Face Transformers, and IBM watsonx

### Hands-On Lab Outcomes

The labs in this course focus on building deployable, application-oriented projects rather than only studying concepts. The repository currently includes work related to:

- a personal storyteller
- a meeting assistant using speech recognition
- a DALL·E image generation workflow
- an image captioning and visual question-answering system
- a visual-input dietary assistant
- a fashion-oriented style finder with multimodal retrieval

### Broader Themes

In addition to model and application development, the course also introduces responsible AI deployment concerns, including:

- transparency
- fairness
- privacy

Overall, the course combines conceptual coverage with hands-on labs intended to build practical, job-relevant multimodal AI skills.

## Repository Inventory

The sections below summarize the core models, libraries, tools, and concepts used in each project currently present in this repository.

## Project Inventory

| Order | Project | File | Libraries | Embedding Model | Vector Store / Retrieval | LLM Model | Vision / Other Model | Tools / Frameworks | Key Concepts |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Personal Storyteller | [Use Mixtral and gTTS to create your personal storyteller.ipynb](./05%20Build%20Multimodal%20Generative%20AI%20Applications/M1%20Foundations%20Of%20Multimodal%20AI/01%20Create%20Personal%20story%20teller/Use%20Mixtral%20and%20gTTS%20to%20create%20your%20personal%20storyteller.ipynb) | `ibm-watsonx-ai`, `gtts`, `IPython`, `os`, `io` | None | None | `mistralai/mistral-medium-2505` | None | watsonx inference, `gTTS`, notebook audio playback | prompt-based generation, text-to-speech, audio rendering |
| 2 | AI Meeting Assistant | [lab-instructions.md](./05%20Build%20Multimodal%20Generative%20AI%20Applications/M1%20Foundations%20Of%20Multimodal%20AI/02%20Build%20an%20AI%20Meeting%20Assistant/lab-instructions.md) | `transformers`, `torch`, `gradio`, `langchain`, `langchain-community`, `langchain_ibm`, `ibm-watsonx-ai`, `pydantic`, `requests` | None explicitly specified | None | IBM watsonx LLM referenced, exact model not visible in the local instructions | `openai/whisper-tiny.en` | Hugging Face `pipeline`, Gradio, LangChain, `ffmpeg` | ASR, transcript post-processing, prompt templates, chaining, speech-to-text app development |
| 3 | DALL·E Image Generation Guide | [1. DALL E Image generation Guide for Beginners.ipynb](./05%20Build%20Multimodal%20Generative%20AI%20Applications/M2%20Integrating%20Visuals%20And%20Video%20modalities/1.%20DALL%20E%20Image%20generation%20Guide%20for%20Beginners.ipynb) | `openai`, `IPython` | None | None | None | `dall-e-2`, `dall-e-3` | OpenAI image generation API, notebook display | text-to-image generation, prompt design, image synthesis |
| 4 | Image Captioning and VQA with watsonx and Granite | [2. Build an Image Captioning & VQA System with watsonx and Granite.ipynb](./05%20Build%20Multimodal%20Generative%20AI%20Applications/M2%20Integrating%20Visuals%20And%20Video%20modalities/2.%20Build%20an%20Image%20Captioning%20%26%20VQA%20System%20with%20watsonx%20and%20Granite.ipynb) | `ibm-watsonx-ai`, `requests`, `base64`, `os` | None | None | `meta-llama/llama-3-2-11b-vision-instruct` | Notebook text discusses Granite 3.2 Vision; executable code uses `meta-llama/llama-3-2-11b-vision-instruct` | watsonx multimodal chat API, `TextChatParameters`, `ModelInference`, base64 image encoding | multimodal prompting, image captioning, VQA, base64 image serialization |
| 5 | AI Nutrition Coach | [lab-instructions_.md](./05%20Build%20Multimodal%20Generative%20AI%20Applications/M3%20Advanced%20Multimodal%20applications/GenAI%20Powered%20Image%20Based%20Web%20Application%20AI%20Nutrition%20Coach/lab-instructions_.md) | `ibm-watsonx-ai`, `image`, `flask`, `requests`, `PIL`, `re`, `base64`, `os` | None | None | `meta-llama/llama-4-maverick-17b-128e-instruct-fp8` | same model provides multimodal vision capability | Flask, watsonx model inference | food image understanding, calorie estimation, nutrition guidance, multimodal web app integration |
| 6 | Style Finder: Computer Vision-Based Fashion Analysis | [lab-instructions.md](./05%20Build%20Multimodal%20Generative%20AI%20Applications/M3%20Advanced%20Multimodal%20applications/Style%20Finder%20Computer%20Vision%20Based%20Fashion%20Analysis/lab-instructions.md) | `ibm-watsonx-ai`, `image`, `requests`, `pillow`, `transformers`, `torch`, `ipywidgets`, `scikit-learn`, `gradio` | Not explicitly named in visible instructions; embeddings are precomputed | No vector DB; local embeddings in `swift-style-embeddings.pkl` with cosine similarity retrieval | `Llama 3.2 90B Vision Instruct` | same model provides multimodal vision capability | Gradio, `scikit-learn`, `wget`, local pickle-based embedding store | multimodal RAG, vector similarity search, image retrieval, context augmentation, fashion analysis |

## Technical Summary

### Vector Databases

- No dedicated vector database is used in the files currently present in this repository.
- No evidence of `FAISS`, `Chroma`, `Pinecone`, `Weaviate`, `Milvus`, or `Qdrant` appears in the inspected notebooks and lab instructions.

### Embedding Models

- No embedding model is explicitly declared in most projects.
- The Style Finder lab uses precomputed embeddings, but the specific embedding generation model is not named in the visible local instructions.
- Therefore, the most accurate statement is:
  - embeddings are used only in Style Finder
  - the embedding generation model is not identifiable from the current local files inspected here

### LLM and Multimodal Models

- `mistralai/mistral-medium-2505`
- `meta-llama/llama-3-2-11b-vision-instruct`
- `meta-llama/llama-4-maverick-17b-128e-instruct-fp8`
- `Llama 3.2 90B Vision Instruct`
- IBM watsonx LLM is mentioned in the Meeting Assistant lab, but the exact model is not visible in the current local instruction file

### Non-LLM Models

- `openai/whisper-tiny.en`
- `dall-e-2`
- `dall-e-3`

### Main Frameworks and Tools Across the Projects

- `ibm-watsonx-ai`
- `openai`
- `transformers`
- `torch`
- `gradio`
- `flask`
- `langchain`
- `langchain-community`
- `langchain_ibm`
- `scikit-learn`
- `gtts`
- `requests`
- `pillow`
- `ffmpeg`
- `ipywidgets`

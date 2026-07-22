import ollama


MODEL_NAME = "qwen2.5:7b"


def generate_response(
    prompt: str,
) -> str:

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        format = "json"
    )

    return response["message"]["content"]
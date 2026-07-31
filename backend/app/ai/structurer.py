from app.ai.client import generate_response
from app.ai.prompts import STRUCTURE_QUESTION_PROMPT
from app.ai.schemas import StructuredQuestion


def structure_question(candidate_text: str):

    prompt = STRUCTURE_QUESTION_PROMPT.format(
        question=candidate_text
    )

    response = generate_response(prompt).strip()

    print("\n" + "=" * 80)
    print("Candidate:")
    print(candidate_text)
    print("-" * 80)
    print("LLM Response:")
    print(response)
    print("=" * 80)

    return StructuredQuestion.model_validate_json(
        response
    )
from app.ai.client import generate_response
from app.ai.prompts import STRUCTURE_QUESTION_PROMPT
from app.ai.schemas import StructuredQuestion


def structure_question(candidate_text: str):

    prompt = STRUCTURE_QUESTION_PROMPT.format(
        question=candidate_text
    )

    response = generate_response(
        prompt
    ).strip()

    return StructuredQuestion.model_validate_json(
        response
    )
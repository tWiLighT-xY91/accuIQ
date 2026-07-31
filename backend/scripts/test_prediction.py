from pprint import pprint

from app.database.database import SessionLocal
from app.services.analytics.prediction import (
    get_question_predictions,
)


def main() -> None:
    db = SessionLocal()

    try:
        predictions = get_question_predictions(db)

        print("\n" + "=" * 100)
        print("QUESTION PREDICTIONS")
        print("=" * 100)

        if not predictions:
            print("No prediction data available.")
            return

        for rank, prediction in enumerate(predictions, start=1):

            print(f"\n{'='*100}")
            print(f"Rank #{rank}")
            print(f"{'='*100}")

            print(f"Question ID      : {prediction.question_id}")
            print(f"Prediction Score : {prediction.prediction_score:.3f}")
            print(f"Confidence       : {prediction.confidence}")
            print(f"Frequency        : {prediction.frequency}")
            print(f"Year Coverage    : {prediction.year_count}")
            print(f"Years            : {prediction.years}")
            print(f"Latest Year      : {prediction.latest_year}")

            print("\nQuestion")
            print("-"*100)
            print(prediction.question_text)

    finally:
        db.close()


if __name__ == "__main__":
    main()
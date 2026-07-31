from app.database.database import SessionLocal

from app.services.analytics.frequency import get_question_frequency
from app.services.analytics.history import get_question_history
from app.services.analytics.ranking import get_question_ranking


def main():

    db = SessionLocal()

    try:

        print("=" * 80)
        print("QUESTION FREQUENCY")
        print("=" * 80)

        frequencies = get_question_frequency(db)

        for item in frequencies:
            print(item.model_dump())

        print()

        print("=" * 80)
        print("QUESTION HISTORY")
        print("=" * 80)

        histories = get_question_history(db)

        for item in histories:
            print(item.model_dump())

        print()

        print("=" * 80)
        print("QUESTION RANKING")
        print("=" * 80)

        rankings = get_question_ranking(db)

        for item in rankings:
            print(item.model_dump())

    finally:
        db.close()


if __name__ == "__main__":
    main()
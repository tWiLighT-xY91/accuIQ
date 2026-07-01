from sqlalchemy import text

from app.database.database import engine

with engine.connect() as conn:
    print("Current User:")
    print(conn.execute(text("SELECT current_user")).scalar())

    print("Current Database:")
    print(conn.execute(text("SELECT current_database()")).scalar())

    print("Search Path:")
    print(conn.execute(text("SHOW search_path")).scalar())

    print("Schemas:")
    rows = conn.execute(
        text("SELECT schema_name FROM information_schema.schemata")
    ).fetchall()

    for row in rows:
        print(row[0])
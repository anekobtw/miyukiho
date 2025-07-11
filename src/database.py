import os
from datetime import datetime

import psycopg2
from dotenv import load_dotenv
from psycopg2.extras import execute_values

load_dotenv()

DB_PASSWORD = os.getenv("POSTQRESQL_PASSWORD")
DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": DB_PASSWORD,
    "host": "localhost",
    "port": 5432,
}


def create_table():
    with psycopg2.connect(**DB_PARAMS) as conn, conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS logs (
                id SERIAL PRIMARY KEY,
                admin_id BIGINT,
                user_id BIGINT,
                action TEXT CHECK (action IN ('ban', 'mute', 'unban', 'unmute')),
                reason TEXT,
                timestamp TIMESTAMP DEFAULT now()
            );
        """)


def insert_log(admin_id: int, user_id: int, action: str, reason: str = ""):
    if action not in ("ban", "mute", "warn", "unban", "unmute"):
        raise ValueError("Invalid action type")

    with psycopg2.connect(**DB_PARAMS) as conn, conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO logs (admin_id, user_id, action, reason, timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """,
            (admin_id, user_id, action, reason, datetime.utcnow()),
        )

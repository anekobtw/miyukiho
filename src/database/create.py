import psycopg2
from dotenv import load_dotenv
from datetime import datetime
import os

load_dotenv()


conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password=os.getenv("POSTQRESQL_PASSWORD"),
    host="localhost",
    port="5432"
)

conn.autocommit = True
cur = conn.cursor()

cur.execute("""CREATE TABLE groups (
  id BIGINT PRIMARY KEY,
  is_partner BOOLEAN DEFAULT false,
  log_channel_id BIGINT,
  blacklisted_words TEXT[],
  admin_ids INT[]
);""")


cur.execute("""CREATE TABLE logs (
  id SERIAL PRIMARY KEY,
  group_id BIGINT REFERENCES groups(id) ON DELETE CASCADE,
  admin_id BIGINT,
  user_id BIGINT,
  action TEXT CHECK (action IN ('ban', 'mute', 'warn', 'unban', 'unmute')),
  reason TEXT,
  timestamp TIMESTAMP DEFAULT now()
);""")



def insert_log(group_id: int, admin_id: int, user_id: int, action: str, reason: str = ""):
    conn.execute("""
        INSERT INTO logs (group_id, admin_id, user_id, action, reason, timestamp)
        VALUES ($1, $2, $3, $4, $5, $6)
    """, group_id, admin_id, user_id, action, reason, datetime.utcnow())


cur.close()
conn.close()

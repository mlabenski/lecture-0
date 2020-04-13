import os
import psycopg2

DATABASE_URL = 'https://git.heroku.com/dice-game-db.git'

conn = psycopg2.connect(DATABASE_URL, sslmode='require')

print(conn)

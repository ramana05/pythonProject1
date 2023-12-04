import os 
from flask import request
import sqlalchemy
@app.route('/example')

print('Hello world is there or not ')
def get_users():
    user = request.args["user"]
    conn = sqlalchemy.create_engine(connection_string)
    conn = engine.connect()
    conn.execute("SELECT user FROM users WHERE user = '" + user + "'") # Noncompliant

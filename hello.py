import os 
from flask import request
import sqlalchemy

# example code snippet py_vuln00: Arbitrary Code Execution:
compute_user_input = input('\nType something here to compute: ')
if not compute_user_input:
        print ("No input")
else:
        print ("Result: ", eval(compute_user_input))

print('Hello world is there or not ')
def get_users():
    user = request.args["user"]
    conn = sqlalchemy.create_engine(connection_string)
    conn = engine.connect()
    conn.execute("SELECT user FROM users WHERE user = '" + user + "'") # Noncompliant

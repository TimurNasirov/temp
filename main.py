from fastapi import FastAPI
import database as db

app = FastAPI()
DEFAULT_KEY = 'TEMP_DEFAULT-518362074.97z'

@app.get('/temp/messages')
def messages(api_key: str):
    if api_key == DEFAULT_KEY:
        return db.messages()
    else:
        return {'detail': 'Wrong Key'}

@app.get('/temp/doing')
def last_doing(api_key: str):
    if api_key == DEFAULT_KEY:
        return db.last_doing()
    else:
        return {'detail': 'Wrong Key'}

@app.post('/temp/message')
def add_message(api_key: str, author: str, message: str):
    if api_key == DEFAULT_KEY:
        return db.send_message(author, message)

@app.post('/temp/reply_message')
def add_message(api_key: str, author: str, message: str, reply_id: int):
    if api_key == DEFAULT_KEY:
        return db.send_reply_message(author, message, reply_id)
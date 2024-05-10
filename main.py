from fastapi import FastAPI
import database as db

app = FastAPI()

DEFAULT_KEY = 'TEMP_DEFAULT-518362074.97z'
ADMIN_KEY = 'TEMP_ADMINTOOLS-936589260.48y'

@app.get('/temp/users')
def users(api_key: str):
    if api_key == DEFAULT_KEY:
        return db.users()
    else:
        return {'detail': 'Wrong Key'}

@app.post('/temp/user')
def add_user(api_key: str, admin_key: str, key: str, name: str):
    if api_key == DEFAULT_KEY and admin_key == ADMIN_KEY:
        return db.add_user(key, name)
    else:
        return {'detail': 'Wrong Key'}

@app.put('/temp/user')
def edit_user(api_key: str, id: int, key: str, name: str):
    if api_key == DEFAULT_KEY:
        db.edit_user(id, key, name)


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
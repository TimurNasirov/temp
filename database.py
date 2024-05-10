from sqlite3 import connect

connect = connect('database.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, key TEXT, name TEXT)')
cursor.execute('CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY, author TEXT, message TEXT)')

class LastDoing:
    id = 0
    doing = ''
    data = ''
lastdoing = LastDoing()

def last_doing():
    return {'id': lastdoing.id, 'doing': lastdoing.doing, 'data': lastdoing.data}

def users():
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()
    ndata = []
    for i in data:
        ndata.append({'id': i[0], 'key': i[1], 'name': i[2]})
    return ndata

def add_user(key, name):
    cursor.execute(f'INSERT INTO users(key, name) VALUES("{key}", "{name}")')
    connect.commit()
    return {'id': cursor.lastrowid, 'key': key, 'name': name}

def edit_user(id, key, name):
    cursor.execute(f'UPDATE users SET key="{key}" WHERE id={id}')
    
    cursor.execute(f'SELECT name FROM users WHERE id={id}')
    oldname = cursor.fetchone()
    if oldname != name:
        cursor.execute(f'UPDATE users SET name="{name}" WHERE id={id}')
        cursor.execute(f'UPDATE messages SET author="{name}" WHERE author="{oldname}"')
        lastdoing.id += 1
        lastdoing.doing = 'user_edit'
        lastdoing.data = name
    connect.commit()


def messages():
    cursor.execute('SELECT * FROM messages LIMIT 150')
    data = cursor.fetchall()
    ndata = []
    for i in data:
        ndata.append({'id': i[0], 'author': i[1], 'message': i[2]})
    return ndata

#def last_message():
#    cursor.execute('SELECT * FROM messages WHERE id = (SELECT MAX(ID) FROM messages)')
#    data = cursor.fetchone()
#    if data: return {'id': data[0], 'author': data[1], 'message': data[2]}

def send_message(author, message):
    cursor.execute(f'INSERT INTO messages(author, message) VALUES("{author}", "{message}")')
    connect.commit()
    lastdoing.id += 1
    lastdoing.doing = 'send_message'
    lastdoing.data = {'id': cursor.lastrowid, 'author': author, 'message': message}
    return {'id': cursor.lastrowid, 'author': author, 'message': message}

def edit_message(id, content):
    lastdoing.id += 1
    lastdoing.doing = 'edit_message'
    lastdoing.data = {'id': id, 'message': content}
    cursor.execute(f'UPDATE messages SET message="{content}" WHERE id={id}')
    connect.commit()

def delete_message(id):
    lastdoing.id += 1
    lastdoing.doing = 'delete_message'
    lastdoing.data = id
    cursor.execute(f'DELETE FROM messages WHERE id={id}')
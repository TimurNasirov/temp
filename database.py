from sqlite3 import connect

connect = connect('database.db', check_same_thread=False)
cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY, author TEXT, message TEXT, reply INTEGER)')

class LastDoing:
    id = 0
    doing = ''
    data = {}
lastdoing = LastDoing()

def last_doing():
    return {'id': lastdoing.id, 'doing': lastdoing.doing, 'data': lastdoing.data}

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
    cursor.execute(f'INSERT INTO messages(author, message, reply) VALUES("{author}", "{message}", "")')
    connect.commit()
    lastdoing.id += 1
    lastdoing.doing = 'send_message'
    lastdoing.data = {'id': cursor.lastrowid, 'author': author, 'message': message}
    return lastdoing.data

def send_reply_message(author, message, reply_id):
    cursor.execute(f'INSERT INTO messages(author, message, reply) VALUES("{author}", "{message}", {reply_id})')
    connect.commit()
    lastdoing.id += 1
    lastdoing.doing = 'send_reply_message'
    lastdoing.data = {'id': cursor.lastrowid, 'author': author, 'message': message, 'reply': reply_id}
    return lastdoing.data

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
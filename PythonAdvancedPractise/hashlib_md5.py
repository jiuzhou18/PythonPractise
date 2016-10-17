import hashlib

def calc_md5(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()

print(calc_md5('123456'))

db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}

def login(user, password):
    if user in db.keys():
        md5 = calc_md5(password)
        return db[user] == md5
    else:
        print('THe user is not found!')
        return False

print(login('bob', 'abc999'))

db2={}
def register(username, password):
    db2[username] = calc_md5(password + username + 'the-Salt')


def login2(username, password):
    if username in db2.keys():
        md5 = calc_md5(password + username + 'the-Salt')
        if (db2[username] == md5):
            print (username, "log in successful!")
        else:
            print ("The password is wrong!")
    else:
        print('THe user is not found!')
        return False

register('mike', '123456')
register('jack', 'abcdef')
login2('mike', '123456')
login2('jack', 'abcde')










from getpass import getpass
class Pwd():
    def __init__(self, username, password):
        self.usr = username
        self.pw = password
usrp = Pwd('kris', 'kris888')
ps = 'pass'
while(ps=='pass'):
    uname = input('Enter user name: ')
    pword = getpass('Enter password: ')
    if uname==usrp.usr and pword==usrp.pw:
        break
    else:
        print('Incorrect user name or password, try again')
        ps = 'pass'

def pwd():
    pw = 'pass'
    while(pw=='pass'):
        username ='kris'
        usr = input('Enter user name: ')
        pwd = getpass('Enter password: ')
        if usr==username and pwd=='kris888':
            break
        else:
            print('Incorrect user name or password, try again')
            pw = 'pass'

def pwd2():
    username = 'kris'
    for i in range(3):
        usr = input('Enter user name: ')
        pwd = getpass('Enter password: ')
        j = 2
        if usr==username and pwd=='kris888':
            print('welcom')
        else:
            print('Incorrect user name or password, try again')
            print('chances left: ',j-i)
    print('\n Try next time')

from time import sleep
try:
    sleep(0.1)
    f = open("../../url.txt", 'r')
    if f.mode == 'r':
        URL = f.read()
    f.close()
except Exception as error:
    try:
        sleep(0.1)
        f = open("../url.txt", 'r')
        if f.mode == 'r':
            URL = f.read()
        f.close()
    except Exception as e:
        try:
            sleep(0.1)
            f = open("../url.txt", 'r')
            if f.mode == 'r':
                URL = f.read()
            f.close()
        except:
            pass
    print(error)
    URL = "http://localhost:5000/"
'''
URL1 = "http://linuxchat.herokuapp.com/"
URL2 = "http://localhost:5000/"
'''

postURL = URL + "api/chat/"
getURL = URL + "api/chat/"
usersURL = URL + "api/users/"
loginURL = URL + "api/users/login"
addfriendURL = URL + "api/users/addfriend/"
updateURL = URL + "api/users/update/"
removeURL = URL + "api/users/removefriend/"
loguotURL = URL + "api/users/logout/"
registerURL = URL + "api/users/register"
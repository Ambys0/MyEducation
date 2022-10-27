
users = [['user1', '111'],
        ['user2', '2222'],
        ['user3', '333333']]
def info (*clients):
    for i in range(len(clients)):
        if i == 0:
            print("login: {}".format(clients[i]))
        elif i == 1:
            print("pass: {}".format(clients[i]))
info(*users)




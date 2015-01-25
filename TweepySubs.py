def GetUsers(MyFileName):
    f = open(MyFileName,'r')
    users = f.read().split(',')
    return users

def GetUser(UserDetails,api):
    return api.get_user(UserDetails)



if __name__ == "__main__":
    print(GetUser("Kishtwar1996"))



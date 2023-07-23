import crypt
import os
import random, string
import pwd


v={
'1':'a',
'2':'e',
'3':'i',
'4':'o',
'5':'u',
'6':'y',
}

d={
'1':'a',
'2':'b',
'3':'c',
'4':'d',
'5':'e',
'6':'f',
'7':'g',
'8':'h',
'9':'i',
'10':'j',
'11':'k',
'12':'l',
'13':'m',
'14':'n',
'15':'o',
'16':'p',
'17':'q',
'18':'r',
'19':'s',
'20':'t',
'21':'u',
'22':'v',
'23':'w',
'24':'x',
'25':'y',
'26':'z'
}


n = 20

with open("usernames.txt", "wt") as file:
        
    for i in range(0,n):
        
        
        s=d[str(random.randrange(1,27))]
        s+=v[str(random.randrange(1,7))]
        s+=d[str(random.randrange(1,27))]
        s+=v[str(random.randrange(1,7))]
        for j in range(0,4):
            s+=str(random.randrange(0,10))
        file.write(s+"\n")
        file.close()

    # print(s)




#     #Task6



def createUser(username = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):

    return random.choice(username) + random.choice(username)

print (crypt.crypt("passwd", createUser()))



#USING OS.SYSTEM

os.system("sudo useradd -p username -s /bin/bash -d /home/username -m -c 'OJtjA4OgfymTQ' userTologIn ")

#create the home folder /home/username
# os.chdir("/home/pi") #change directory
# os.mkdir("username") #creating a directory
# os.system("pwd") #show current directory


#Task7

def createAccount():
    filename = 'usernames.txt'
    with open(filename, "rt") as usernamesFile:
        lines = usernamesFile.readlines()

        for i in lines:

            #print(i)

            try:

                usercreated = createUser(i)

                os.system("useradd -m", usercreated)
                
            except:
                pass

        usernamesFile.close()
createAccount()


#Change ownership of the /home/username folder to username:username
#First create a user to be added

os.system("cd /home/username/")
#I had to recreate the user becuase i kept on getting 
#this errot message "chown username username/chown: invalid user: ‘username’"

os.system("sudo adduser username /home/username/")
os.system("sudo chown username /home/username/")

#to add the username to the group cst8254

os.system("sudo chgrp cst8254 /home/username/")




       



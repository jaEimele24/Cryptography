"""
cryptography.py
Author: <your name here>
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
message=input("message: ")
key=input("key: ")
listmessage=list(message)
list5=list(key)
listmessagenums=[]
listkeynums=[]
list6=[]

if command=="e":
    for i in message:
        listmessagenums.append(associations.find(i))
    print(listmessagenums)
    for x in key:
        listkeynums.append(associations.find(x))
    print(listkeynums)
    d=(len(listmessagenums))//(len(listmessagenums))
    u=(len(listmessagenums))%(len(listkeynums))
    key2=[]
    if u == 0:
        for q in range (0,d):
            key2.append(listkeynums)
            print(key2)
    if u > 0:
        for j in range (0,r):
            key2.append(listkeynums)
            print(key2)
    print(listkeynums)
    
    
        
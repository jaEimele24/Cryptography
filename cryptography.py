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
message=input("Message: ")
key=input("Key: ")
listmessage=list(message)
list5=list(key)
listmessagenums=[]
listkeynums=[]
list6=[]
listassociations=list(associations)
if command=="e":
    for i in message:
        listmessagenums.append(associations.find(i))
    print(listmessagenums)
    for x in key:
        listkeynums.append(associations.find(x))
    print(listkeynums)
    d=(len(listmessagenums))//(len(listkeynums))
    print(d)
    u=(len(listmessagenums))%(len(listkeynums))
    print(u)
    key2=[]
    for f in range (0, len(listmessagenums)):
        key2.append(listkeynums[f%len(listkeynums)])
        print(key2)
    #for q in range (0,d):
        #key2.append(listkeynums)
        #print(key2)
    #for j in range (0,u):
        #key2.append(listkeynums)
        #print(key2)
    #print(listkeynums)
    newlist=[x + y for x, y in zip(listmessagenums, key2)]
    print(newlist)
    newlist2=[]
    for x in newlist:
        if x > len(listassociations):
            newlist2.append(x-len(listassociations))
        else:
            newlist2.append(x)
    codelist=[]
    for b in newlist2:
        codelist.append(associations[b])
        print(codelist)
if command=="d":
    for i in message:
        listmessagenums.append(associations[i])
        print(listmessagenums)
    
    
        
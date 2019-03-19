"""
cryptography.py
Author: James Eiler
Credit: Teachers

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
#print(listassociations)
if command=="e":
    for i in message:
        listmessagenums.append(associations.find(i))
    #print(listmessagenums)
    for x in key:
        listkeynums.append(associations.find(x))
    #print(listkeynums)
    d=(len(listmessagenums))//(len(listkeynums))
    #print(d)
    u=(len(listmessagenums))%(len(listkeynums))
    #print(u)
    key2=[]
    for f in range (0, len(listmessagenums)):
        key2.append(listkeynums[f%len(listkeynums)])
        #print(key2)
    newlist=[x + y for x, y in zip(listmessagenums, key2)]
    #print(newlist)
    newlist2=[]
    for x in newlist:
        if x > len(listassociations):
            newlist2.append(x-len(listassociations))
        else:
            newlist2.append(x)
    codelist=[]
    for b in newlist2:
        codelist.append(associations[b])
        #print(codelist)
    #print(codelist)
    codelistfinal="".join(codelist)
    print(codelistfinal)
listcode2=list(message)
if command=="d":
    for i in listcode2:
        listmessagenums.append(associations.find(i))
        #print(listmessagenums)
    for g in key:
        listkeynums.append(associations.find(g))
    #print(listkeynums)
    d=(len(listmessagenums))//(len(listkeynums))
    #print(d)
    u=(len(listmessagenums))%(len(listkeynums))
    #print(u)
    key2=[]
    for f in range (0, len(listmessagenums)):
        key2.append(listkeynums[f%len(listkeynums)])
        #print(key2)
    newlist=[x - y for x, y in zip(listmessagenums, key2)]
    #print(newlist)
    newlist2=[]
    for x in newlist:
        if x > len(listassociations):
            newlist2.append(x-len(listassociations))
        else:
            newlist2.append(x)
    decodelist=[]
    for b in newlist2:
        decodelist.append(associations[b])
       # print(decodelist)
    #print(decodelist)
    decodelistfinal="".join(decodelist)
    print(decodelistfinal)
if command == "q":
    print("Goodybe!")
else:
    print("Did not understand command, try again.")

    
        
    
    
        
"""
cryptography.py
Author: James Eiler
Credit: Teachers

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

k=0
for i in range (0,10):
    if k!=1:
        command=input("Enter e to encrypt, d to decrypt, or q to quit: ")
        if command == "q":
            print("Goodybe!")
            k=1
        if command != "d" and command != "e" and command != "q" and k!=1:
            print("Did not understand command, try again.")
        if command == "d" or command == "e" and k!=1:
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
                for x in key:
                    listkeynums.append(associations.find(x))
                d=(len(listmessagenums))//(len(listkeynums))
                u=(len(listmessagenums))%(len(listkeynums))
                key2=[]
                for f in range (0, len(listmessagenums)):
                    key2.append(listkeynums[f%len(listkeynums)])
                newlist=[x + y for x, y in zip(listmessagenums, key2)]
                newlist2=[]
                for x in newlist:
                    if x > len(listassociations):
                        newlist2.append(x-len(listassociations))
                    else:
                        newlist2.append(x)
                codelist=[]
                for b in newlist2:
                    codelist.append(associations[b])
                codelistfinal="".join(codelist)
                print(codelistfinal)
            listcode2=list(message)
            if command=="d":
                for i in listcode2:
                    listmessagenums.append(associations.find(i))
                for g in key:
                    listkeynums.append(associations.find(g))
                d=(len(listmessagenums))//(len(listkeynums))
                u=(len(listmessagenums))%(len(listkeynums))
                key2=[]
                for f in range (0, len(listmessagenums)):
                    key2.append(listkeynums[f%len(listkeynums)])
                newlist=[x - y for x, y in zip(listmessagenums, key2)]
                newlist2=[]
                for x in newlist:
                    if x > len(listassociations):
                        newlist2.append(x-len(listassociations))
                    else:
                        newlist2.append(x)
                decodelist=[]
                for b in newlist2:
                    decodelist.append(associations[b])
                decodelistfinal="".join(decodelist)
                print(decodelistfinal)

    
        
    
    
        
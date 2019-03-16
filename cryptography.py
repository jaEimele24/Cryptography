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
list1=list(message)
list3=[]
list4=[]
if command=="e":
    for i in message:
        list3.append(associations.find(i))
    print(list3)
    for x in key:
        list4.append(associations.find(x))
    print(list4)
    
    
        
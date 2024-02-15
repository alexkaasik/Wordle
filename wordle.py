from random import *

f = open("wordlist.txt","r", encoding="utf-8-sig")
MaxF = int(len(f.read())/6)
f.close()

f = open("wordlist.txt","r", encoding="utf-8-sig")
Ra=randint(0,MaxF)
print( (f.readlines())[Ra][:-1] )
f.close()


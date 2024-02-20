from random import *

def wordR():
    f = open("wordlist.txt","r", encoding="utf-8-sig")
    MaxF = int(len(f.read())/6)
    f.close()

    f = open("wordlist.txt","r", encoding="utf-8-sig")
    Ra=randint(0,MaxF)
    word = (f.readlines())[Ra][:-1]
    f.close()
    return word
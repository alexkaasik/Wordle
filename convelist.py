
f = open("wordlist.txt", "w", encoding="utf-8-sig")
f.write("")
f.close()


f = open("wordlist.txt", "a", encoding="utf-8-sig")

for x in xlist:
    if ( len(x) == 5 ):
        f.write(x)
        f.write("\n")

f.close()        




















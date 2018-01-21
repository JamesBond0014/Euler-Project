file = open("facebook-jamesjshbao\\html\\messages.htm")

a = file.readlines()
file.close()

c = 0
for i in a:
    if "DainNa" in i:
        print (i)
    c+=1
    if c==20000:
        print("----------------------------------")
        break

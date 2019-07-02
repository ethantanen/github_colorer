import os

image = []

def draw (n):
    f = open('file.txt', 'w')
    for i in range(n) :
        f.write(str(i))
        os.system('git add .')
        os.system('git commit -m "eh"')
        os.system('git push origin master')
    f.close()


draw(10)

import os

image = []

def draw (n):
    f = open('file.txt', 'w')
    for _ in range(n) :
        f.write('.')
        os.system('git add .')
        os.system('git commit -m "eh"')
        os.system('git push origin master')
    f.close()


draw(1)

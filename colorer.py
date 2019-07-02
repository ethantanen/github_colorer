import os

image = []

def draw (n):
    for i in range(n) :
        f = open('file.txt', 'a')
        f.write('\n' + str(i))
        os.system('git add .')
        os.system('git commit -m "eh"')
        os.system('git push origin master')
        f.close()


draw(10)

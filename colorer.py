import os
import schedule
import time

image = []

def draw ():
    for i in range(10) :
        f = open('file.txt', 'a')
        f.write('\n' + str(i))
        os.system('git add .')
        os.system('git commit -m "eh"')
        os.system('git push origin master')
        f.close()

# schedule.every().day.at("1:30").do(draw)
schedule.every().second.do(draw)

while True:
    schedule.run_pending()
    time.sleep(1)

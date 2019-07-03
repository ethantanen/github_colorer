import os
import schedule
import time

# E $ written out dawg
image = [[1,1,1,1,1,1,1],
         [1,0,0,1,0,0,1],
         [1,0,0,1,0,0,1],
         [1,0,0,1,0,0,1],
         [0,0,0,0,0,0,0],
         [0,1,1,1,0,1,0],
         [0,1,0,1,0,1,0],
         [1,1,1,1,1,1,1],
         [0,1,0,1,0,1,0],
         [1,1,1,1,1,1,1],
         [0,1,0,1,0,1,0],
         [0,1,0,1,1,1,0]]

# push a bunch to github on 1 days
def draw ():


    global week
    global day

    print ('t', week, day)
    if image[week][day] is 1:
        for i in range(1) :
            f = open('file.txt', 'a')
            f.write('\n' + str(i))
            os.system('git add .')
            os.system('git commit -m "eh"')
            os.system('git push origin master')
            f.close()

    if day == 7:
        week += 1
    day += 1
    day = day % 7

    print(week, day)


week = 0
day = 0

# schedule.every().day.at("1:30").do(draw)
schedule.every().second.do(draw)

while True:
    schedule.run_pending()
    time.sleep(1)

import random,os
import cv2
import shutil
path = r'/boxingt'
count=0
for i in range(6108):
    random_filename=random.choice([
        x for x in os.listdir(path) if os.path.isfile(os.path.join(path,x))
        ])

    a=os.path.join(path,random_filename)
    b=r'/boxingte'
    shutil.move(a,b)
    count=count+1
    print(count)

from pygame import mixer
from datetime import datetime
import time

def looponmusic(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)

    while True:
        a = input("enter stopper : ")
        if a.lower() == stopper.lower():
            break

if __name__ == '__main__':
    water_acc = time.time()
    eye_acc = time.time()
    eccerey_acc = time.time()

    watersec = 5
    eyesec = 20
    eccereysec = 30

    while True:
        if time.time()-water_acc > watersec:
            print("water drinking time (enter drank to stop) : ")
            looponmusic("water.mp3","drank")
            init_water = time.time()

        if time.time()-eccerey_acc > eccereysec:
            print("exeresing  time (enter done to stop) : ")
            looponmusic("exercise.mp3","done")
            init_eccerey = time.time()

        if time.time()-eye_acc > eyesec:
            print("exresing eye time (enter done to stop) : ")
            looponmusic("eyes.mp3","done")

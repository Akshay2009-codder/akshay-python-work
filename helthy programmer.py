from pygame import mixer
from datetime import datetime
import time


def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)

    while True:
        a = input("Enter stop word: ")
        if a.lower() == stopper.lower():
            mixer.music.stop()
            break




if __name__ == '__main__':
    init_water = time.time()
    init_eyes = time.time()
    init_exercise = time.time()

    watersecs = 5
    eyessecs = 20
    exercisesecs = 30

    while True:
        if time.time() - init_water > watersecs:
            print("Water drinking time. Enter 'done' to stop alarm")
            musiconloop("water.mp3", "done")
            init_water = time.time()


        if time.time() - init_eyes > eyessecs:
            print("Eye exercise time. Enter 'done' to stop alarm")
            musiconloop("eyes.mp3", "done")
            init_eyes = time.time()


        if time.time() - init_exercise > exercisesecs:
            print("Physical exercise time. Enter 'done' to stop alarm")
            musiconloop("exercise.mp3", "done")
            init_exercise = time.time()


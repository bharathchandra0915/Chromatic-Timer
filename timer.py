import cv2 as cv
import numpy as np
import time
import pygame

def play_tick_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/timer-trimmed.mp3")
    pygame.mixer.music.play()

def play_normal_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/timer_medium_frequency.mp3")
    pygame.mixer.music.play()

def play_ending_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/stopping_timer.mp3")
    pygame.mixer.music.play()

def play_congratulate_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("sounds/Time's up!.mp3")
    pygame.mixer.music.play()


def fill_timer():
    pass

timer = int(input('Set the timer (in seconds) '))
cv.namedWindow("Timer",cv.WINDOW_AUTOSIZE)
timer_img = cv.imread("images/timer3.png")
timer_img = cv.resize(timer_img,(480,480))
# timer = 15
img = np.ones((640,480,3),np.uint8)*255
timer_pos_center = 41  ### y cordinate of the center
img[timer_pos_center:timer_pos_center+480,0:480] = timer_img
count = 0
radius = 135

intro_img = cv.imread("images/start.png")
intro_img = cv.resize(intro_img,(480,480))
cv.imshow("Timer",intro_img)
cv.waitKey(1000)

prev_angle = -90
while count < timer:
    if count < timer - 6:
        play_tick_sound()

    elif count < timer-3:
        play_normal_sound()

    else:
        play_ending_sound()

    cv.circle(img,(239,321),radius,(150,150,150),1)
    angle = np.interp(float(count+1),[0,timer],[0,360])
    angle = int(angle)
    end_angle = -90 + angle

    cv.ellipse(img,(239,321),(radius,radius),0,prev_angle,end_angle,(252,244,3),-1)

    # print(count, angle)

    count +=1
    prev_angle = end_angle

    cv.imshow('Timer', img)
    cv.waitKey(1)
    pygame.time.wait(1000)

pygame.mixer.music.stop()
play_congratulate_sound()
img = np.ones((640,480,3),np.uint8)*255
cv.putText(img,"Time Up",(100,340),cv.FONT_HERSHEY_SIMPLEX,2,(230, 90, 242),5)
cv.imshow("Timer",img)
cv.waitKey(5000)

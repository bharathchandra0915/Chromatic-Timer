import cv2 as cv
import numpy as np
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


def fill_timer(color_mode, prev_angle):
    color = ()
    if color_mode == 0:
        prev_angle = prev_angle
    if color_mode == 1:
        prev_angle = -90

    if count < timer / 2:
        red_value = np.interp(float(count + 1), [0, timer / 2], [16, 227])
        red_value = int(red_value)
        color = (0, 227, red_value)
    else:
        green_value = np.interp(float(count + 1), [timer / 2, timer], [227, 16])
        green_value = int(green_value)
        color = (0, green_value, 227)
    cv.ellipse(img,(239,321),(radius,radius),0,prev_angle,end_angle,color,-1)

cv.namedWindow("Timer",cv.WINDOW_AUTOSIZE)
timer_img = cv.imread("images/timer3.png")
timer_img = cv.resize(timer_img,(480,480))

# timer = 15
img = np.ones((640,480,3),np.uint8)*255
timer_pos_center = 41
img[timer_pos_center:timer_pos_center+480,0:480] = timer_img

count = 0
radius = 135

intro_img = cv.imread("images/start.png")

intro_img = cv.resize(intro_img,(480,480))

cv.imshow("Timer",intro_img)
cv.waitKey(1)
## take the input from command line
timer = int(input('Set the timer (in seconds) '))
cv.putText(intro_img,f'Starting {timer} seconds Timer...',(15,70),cv.FONT_HERSHEY_SIMPLEX,1,(0,165,255),2,cv.LINE_AA)
cv.imshow("Timer",intro_img)
cv.waitKey(2000)
cv.imwrite("intro_screenshot.png",intro_img)
prev_angle = -90
center = (291, 321)
color_mode = 0 ## change it to 1 if you wish to see another color gradient pattern
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
    fill_timer(color_mode, prev_angle)

    count +=1
    prev_angle = end_angle

    cv.imshow('Timer', img)
    cv.waitKey(1)
    pygame.time.wait(1000)

pygame.mixer.music.stop()
play_congratulate_sound()
cv.imwrite("screenshot.png", img)
# img = np.ones((640,480,3),np.uint8)*255
cv.putText(img,"Time Up",(111,340),cv.FONT_HERSHEY_SIMPLEX,2,(255,255,255),5)
cv.imwrite("Time_up.png",img)
cv.imshow("Timer",img)
cv.waitKey(5000)

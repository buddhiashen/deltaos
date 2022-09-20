import cv2 as cv
import pyautogui
import numpy as np

#(width,height)
screen_size=pyautogui.size()

#initialize the object
video = cv.VideoWriter('Recording.avi',  
                         cv.VideoWriter_fourcc(*'MJPG'), 
                         20, screen_size)

print("Recording.....")
while True:
    #click screen shot
    screen_shot_img = pyautogui.screenshot()

    #convert into array
    frame = np.array(screen_shot_img)

    #change from BGR to RGB
    frame = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

    #write frame
    video.write(frame)

    #display the live recording 
    cv.imshow("Recording Frame(Minimize it)", frame)    
    if cv.waitKey(1) == ord("q"):
        break

cv.destroyAllWindows()
video.release()
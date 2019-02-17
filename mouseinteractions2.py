
import cv2
import numpy as np

def draw_circle(event,x,y,flag,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(image33,(x,y,),100,(255,0,0),thickness=-1)
    elif event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(image33,(x,y,),100,(0,255,0),thickness=-1)     

cv2.namedWindow(winname='myimage')
cv2.setMouseCallback('myimage',draw_circle)
        
        
image33=np.zeros((512,512,3),np.int8)
while(True):
    cv2.imshow('myimage',image33)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()        
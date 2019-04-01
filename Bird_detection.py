import cv2
import numpy as np
import matplotlib.pyplot as plt

bird1_cascade = cv2.CascadeClassifier('bird1-cascade.xml')
bird2_cascade = cv2.CascadeClassifier('bird2-cascade.xml')
 
#cap = cv2.VideoCapture(0)
cap=cv2.imread("flock7.jpeg")
#works for flock 7,8,4(over estimate)

#global c2=0, c1=0;

def disp(img,cmap='gray'):
    fig=plt.figure(figsize=(12,10))
    ax=fig.add_subplot(111)
    ax.imshow(img,cmap='gray')
 
while 1: 
 

    #ret, img = cap.read() 
    img=cap
    #imgcpy=img.copy()
    #imgcpy=np.zeros(img.shape[:2])
    imgcpy=np.ones(img.shape[:2],dtype=np.uint8)*255

    #imgcpy=imgcpy.fill(255)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    birds1 = bird1_cascade.detectMultiScale(gray, 1.3, 2)
    birds2 = bird2_cascade.detectMultiScale(gray, 1.2, 5)
    z=(len(birds1)+len(birds2))
    
    for (x,y,w,h) in birds1:
        #c1=c1+1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1)
        #cv2.circle(img,center=(x,y),radius=1,color=(0,0,0),thickness=4)
        cv2.circle(imgcpy,center=(x,y),radius=1,color=(0,0,0),thickness=-1)         
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, 'Bird', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)

    for (x,y,w,h) in birds2:
        #c2=c2+1
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),1)
        #cv2.circle(img,center=(x,y),radius=1,color=(0,0,0),thickness=4)
        cv2.circle(imgcpy,center=(x,y),radius=1,color=(0,0,0),thickness=-1)        
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, 'Bird', (x-w, y-h), font, 0.5, (0,255,255), 2, cv2.LINE_AA)
    
    
    cap=cv2.resize(img,(800,600))
    imgcpy=cv2.resize(imgcpy,(800,600))  
    #testarea
    imgcpy=cv2.medianBlur(imgcpy,3)
   
    
    #imgcpy=cv2.cvtColor(imgcpy,cv2.COLOR_RGB2GRAY )
    th,imgcpy= cv2.threshold(imgcpy,20, 255,cv2.THRESH_OTSU)#cv2.THRESH_BINARY_INV)#|
    
    
    kernel = np.ones((5,5), np.uint8) 
    imgcpy = cv2.erode(imgcpy, kernel, iterations=1) 
    
  
    
    contours,hierarchy = cv2.findContours(imgcpy,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(imgcpy, contours, -1, (0,255,0), 1)# change this to 3 to get bigger blobs
    
    s1= 9
    s2 = 81
    xcnts = []
    for cnt in contours:
        if s1<cv2.contourArea(cnt) <s2:
            xcnts.append(cnt)

    #print("Dots number: {}".format(len(xcnts)))


    cv2.imshow('img',img)
    cv2.imshow('lilith',imgcpy)
    

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
 
print("number of birds is : {}".format(len(xcnts)))

cap.release()

cv2.destroyAllWindows() 



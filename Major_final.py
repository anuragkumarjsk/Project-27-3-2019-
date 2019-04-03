#mouse interaction
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def simillarities(Waar,xd,yd):
    match = cv2.matchTemplate(img, Waar, cv2.TM_CCOEFF_NORMED)
    _, confidence, _, _ = cv2.minMaxLoc(match)
    print (confidence)
    #method=eval('cv2.TM_CCOEFF')
    methods=['cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']
    for m in methods:
        r_copy=img1
        raven_face=Waar
        method=eval(m)
        res=cv2.matchTemplate(r_copy,raven_face,method)
        minvalue,maxvalue,minlocation,maxlocation=cv2.minMaxLoc(res)
        plt.imshow(res)
        #print("minmax",minvalue,maxvalue,minlocation,maxlocation)
        
        if m in [cv2.TM_SQDIFF_NORMED,cv2.TM_SQDIFF]:
            topleft=minlocation
        else:
            topleft=maxlocation  
        

        #height,width,channels=raven_face.shape        
        width,height=xd,yd
        bottomright=(topleft[0]+width,topleft[1]+height)
        cv2.rectangle(r_copy,topleft,bottomright,(225,0,0),1)
        plt.subplot(121)
        plt.imshow(res)
        plt.title('result of heatmap')

        plt.subplot(122)
        font=cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(r_copy,text='. ',org=bottomright,fontFace=font,fontScale=2,color=(0,0,255),thickness=2)
        plt.imshow(r_copy)
        plt.title('detection of template')

        plt.suptitle(m)
        plt.show()
        print("/n")
        print("/n")




def  coord(xi,yi,xf,yf):
    global zaar1,diffx,diffy
    xi=xi+2
    yi=yi+2
    xf=xf-1
    yf=yf-1
    diffx=xf-xi
    diffy=yf-yi
    zaar1=img[yi:yf,xi:xf]
    zaar=cv2.resize(zaar1,(400,300))
    cv2.imshow('whatever',zaar)
    #simillarities(zaar,diffx,diffy)
    
drawing=False
ox=-1
oy=-1

def draw_rect(event,x,y,flag,params):
    global drawing,ox,oy
    
    if event==cv2.EVENT_LBUTTONDOWN and drawing==False:
        drawing=True
        ox,oy=x,y
        cv2.circle(img,(x,y,),2,(255,0,0),thickness=-1)
    
    elif event==cv2.EVENT_MOUSEMOVE and drawing==True:
        pass
        #cv2.rectangle(img,(ox,oy),(x,y),(255,0,0),thickness=2)
    
    elif event==cv2.EVENT_LBUTTONUP and drawing==True:
        cv2.rectangle(img,(ox,oy),(x,y),(255,0,0),thickness=2)
        drawing=False
        coord(ox,oy,x,y)
        
        


cv2.namedWindow(winname='myimage')
cv2.setMouseCallback('myimage',draw_rect)
        
        
#image33=np.zeros((512,512,3),np.int8)
global img1
img = cv2.imread("flock1.jpeg")
img1=img.copy()


while(True):
    img=cv2.resize(img,(800,600))
    cv2.imshow('myimage',img)
    #disp(img)
    if cv2.waitKey(1) & 0xFF==27:
        break
        
        

#while(True):
#matrix manipulation
COUNT=0
small=np.array(zaar1)
large=np.array(img1)

small1=small
large1=large

small=small[:,:,1]
large=large[:,:,1]

sh,sw,sc=small1.shape
lh,lw,lc=large1.shape
    
print("small",sh,sw,sc)
print("large",lh,lw,lc)
small=small #* 0.5)
large=large #* 0.5)
print("diffx",diffx,"diffy",diffy)
mov_hor=int(lw/sw)
mov_ver=int(lh/sh)
startrow=-sh
startcol=0#-sw
Temp=np.average(small)#sum(small)
print(mov_hor,mov_ver)
for R in range(0,mov_ver):
    startrow=startrow+sh
    for C in range(0,mov_hor):
       
        #startcol=sw+startcol
        subarr=large[startrow:(sh+startrow),startcol:(sw+startcol)]
        Diff=np.subtract(subarr,small)
        Val=np.average(Diff)#sum(Diff)
        print(Val, Temp)
        if(abs(np.all(Val)^np.all(Temp))<=20):
        #if(np.all(Val) <= np.all(Temp)+10 or np.all(Val) <= np.all(Temp)-10):
        #if((Val) <= (Temp)+150 or (Val) <= (Temp)-150):
            Temp=Val
            COUNT=COUNT+1
        
        print("*",end =" ")
    print("\n" )
    
print(COUNT)    
'''
    img=cv2.resize(img1,(800,600))
    cv2.imshow('myimagereal',img1)
    cv2.imshow('myimagecropped',zaar)
    #disp(img)
    
    if cv2.waitKey(1) & 0xFF==27:
        break      '''   
        
cv2.destroyAllWindows() 
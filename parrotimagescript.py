#parrotimagescript.py
import cv2
image=cv2.imread("/root/Desktop/python/parrot.jpeg")
while(True):
    cv2.imshow('image of parrot',image)
    if cv2.waitKey(1) & 0xFF==27:
        break
        
cv2.destroyAllWindows()        
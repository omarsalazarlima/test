'''
this is a large multi-line string
hi
'''
"""
This is also a multi-line comment
"""
import cv2

print(cv2.__version__)

cap = cv2.VideoCapture(0)

while True:
    
    ans = False
    while ans == False:
        ret, frame = cap.read()
        ans = ret
    frame=cv2.flip(frame, flipCode=1)

   
    cv2.imshow('frame', frame)
    if cv2.waitKey(1)== ord('q'):
        break
    

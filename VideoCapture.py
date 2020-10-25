import numpy as np
from cv2 import cv2
import time

from PIL import Image
from keras.models import load_model
from keras.preprocessing.image import ImageDataGenerator

#model = load_model("D:/Sign language detection/model4_0.9823.h5")

num_frames=0
cap=cv2.VideoCapture(0)


data = ImageDataGenerator(samplewise_center=True, samplewise_std_normalization=True)

prev = int(time.time())
k=0

while(True):

    ret,frame=cap.read()

    
    cv2.imshow("from Video Feed",frame)
    k=cv2.waitKey(1)

    if(int(time.time()) == (prev + 2)):
        #ret,frame=cap.read()
        #frame=imutils.resize(frame,width=700)
        #frame = cv2.flip(frame, 1)
        clone=frame.copy()
        

        #ret,frame=cap.read()
        roi=frame[top_left[1]:bottom_right[1],top_left[0]:bottom_right[0]]

        roi = cv2.resize(roi, (128,128))
        roi = cv2.normalize(roi, None, alpha=0, beta = 1, norm_type = cv2.NORM_MINMAX, dtype = cv2.CV_32F)
        roi = roi[np.newaxis,:]
        #roi = data.apply_transform(roi)
        #cv2.imshow('Sign shown',roi)
        #print(np.argmax(model.predict(roi)))
        #cv2.waitKey(125)
        prev=int(time.time())
    if k == ord('q'):
        break

   
cap.release()
cv2.destroyAllWindows()







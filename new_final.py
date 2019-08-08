import cv2
import numpy as np


def find_w(pic):
    image1 = cv2.imread(pic)
    hsv1 = cv2.cvtColor(image1,cv2.COLOR_BGR2HSV)
    lower_black = np.array([0,0,0])
    upper_black = np.array([100,100,100])

    mask = cv2.inRange(hsv1,lower_black,upper_black)
    res = cv2.bitwise_and(image1,image1,mask=mask)
    #th1 = cv2.threshold(res,10,255,cv2.THRESH_BINARY)[1]
    cv2.imshow("res",res)
    cv2.imshow("mask",mask)


    _,cnts,_ = cv2.findContours(mask,\
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    #------ 30 cm----#
    for i,c in enumerate(cnts):
        x,y,w,h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if(area > 10000):
            print("fisrt-> ",area)
            print("w = ",w)
            cv2.drawContours(image1, [c], -1, (0, 255, 0), 2)
            break
    
    cv2.imshow("image",image1)
    return w

def find_d(w1,w2,m):
    d = m/(1 - (w1/w2))
    return d

def main():
    pic1 = input("Input Picture1 name(long distance): ")
    pic2 = input("Input Picture2 name(short distance): ")
    m = float(input("Input m: "))
    w1 = find_w(pic1)
    w2 = find_w(pic2)
    d = find_d(w1,w2,m)
##
##    h1 = w1*d
##    h2 = w2*(d-m)
##
    print("distance between camera and object = ",d)
      
main()
cv2.waitKey(0)
cv2.destroyAllWindows()


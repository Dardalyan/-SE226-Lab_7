import cv2 as opencv
import numpy as np

# Mr. Okur , This internet image path shows what I used as an image .
# https://www.google.com/search?q=red+green+and+blue+colors+image+jpeg+format&tbm=isch&ved=2ahUKEwimq7_9u-j-AhUalKQKHd9LCd8Q2-cCegQIABAA&oq=red+green+and+blue+colors+image+jpeg+format&gs_lcp=CgNpbWcQA1DbBlj5E2CwFmgAcAB4AIABdogB4waSAQMwLjiYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=kFtaZKajN5qokgXfl6X4DQ&bih=688&biw=1519&hl=en-GB#imgrc=ukNi4aCw0EWpVM

# Also all lab tasks are below

path = 'C:/Users/enbur/Desktop/asd.jpg'
image = opencv.imread(path,1)

def greenChannel(image:np.ndarray,lowerBound:np.ndarray=np.array([40, 40,40]),
              upperBound:np.ndarray= np.array([70, 255,255])):

    hsv = opencv.cvtColor(image, opencv.COLOR_BGR2HSV)
    mask = opencv.inRange(hsv, lowerBound, upperBound)

    kernel = np.ones((7, 7), np.uint8)
    masky = opencv.morphologyEx(mask, opencv.MORPH_CLOSE, kernel)
    masky = opencv.morphologyEx(mask, opencv.MORPH_OPEN, kernel)

    return masky

def blueChannel(image:np.ndarray,lowerBound:np.ndarray=np.array([110,50,50]),
              upperBound:np.ndarray= np.array([130,255,255])):

    hsv = opencv.cvtColor(image, opencv.COLOR_BGR2HSV)
    mask = opencv.inRange(hsv, lowerBound, upperBound)

    kernel = np.ones((7, 7), np.uint8)
    masky = opencv.morphologyEx(mask, opencv.MORPH_CLOSE, kernel)
    masky = opencv.morphologyEx(mask, opencv.MORPH_OPEN, kernel)

    return masky

def redChannel(image:np.ndarray,lowerBound:np.ndarray=np.array([0, 100, 20]),
              upperBound:np.ndarray= np.array([0, 255, 255])):

    hsv = opencv.cvtColor(image, opencv.COLOR_BGR2HSV)
    mask = opencv.inRange(hsv, lowerBound, upperBound)

    kernel = np.ones((7, 7), np.uint8)
    masky = opencv.morphologyEx(mask, opencv.MORPH_CLOSE, kernel)
    masky = opencv.morphologyEx(mask, opencv.MORPH_OPEN, kernel)

    return masky

green_img = opencv.bitwise_and(image, image, mask=greenChannel(image))
blue_img = opencv.bitwise_and(image, image, mask=blueChannel(image))
red_img = opencv.bitwise_and(image, image, mask=redChannel(image))

# Displays all tasks
opencv.imshow("greenPart",green_img)
opencv.imshow("redPart",red_img)
opencv.imshow("bluePart",blue_img)
opencv.imshow("wholeImage",image)


opencv.waitKey()

#!/usr/bin/env python
import cv2
import numpy as np

# Setup
webcam = cv2.VideoCapture(0)
cv2.namedWindow("Camera", cv2.CV_WINDOW_AUTOSIZE)
ball_color_hsv = None

def on_mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global ball_color_hsv
        ball_color_hsv = np.array(frame_hsv[y,x])
        print ball_color_hsv

# Grab a frame
while True:
    r,frame = webcam.read()
    frame = cv2.GaussianBlur(frame, (0,0), 3, frame, 3)
    cv2.imshow("Camera", frame)
    if (cv2.waitKey(1) != -1):
        break

# Get average color of selected area
cv2.imshow("Camera", frame)
frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cv2.setMouseCallback("Camera", on_mouse)
cv2.waitKey(0)

threshold = np.array([0.10, 0.20, 0.30])
difference = np.multiply(ball_color_hsv, threshold)
lowerB = np.subtract(ball_color_hsv, difference)
upperB = np.add(ball_color_hsv, difference)


while True:
    r,frame = webcam.read()
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame_bin = cv2.inRange(frame_hsv, lowerB, upperB)
    frame_bin = cv2.GaussianBlur(frame_bin, (0,0), 7, frame_bin, 7)
    circles = cv2.HoughCircles(frame_bin, cv2.cv.CV_HOUGH_GRADIENT, 2, 10,
            param1=100, param2=40, minRadius=20, maxRadius=200)
    if circles is not None:
        for c in circles[0,:]:
            cv2.circle(frame, (c[0],c[1]), c[2], (0,255,0), 1)
            cv2.circle(frame, (c[0],c[1]), 2, (0,0,255), 3)

    cv2.imshow("Camera", frame)
    if (cv2.waitKey(1) != -1):
        break

# Clean Up
webcam.release()
cv2.destroyAllWindows()


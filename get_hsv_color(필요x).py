import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt
import cv2
import colorsys
import get_color as get_color
from PIL import Image

color_dic = {'pink':'FFC0CB',
     'purple' : '9966ff',
    'red' : 'FF0000',
    'orange' : 'FFA500',
    'yellow' : 'FFFF00',
    'green' : '008000',
     'cyan' : '00FFFF',
     'blue':'0000FF',
    'brown' :'A52A2A',
     'white' : 'FFFFFF',
     'gray' : 'DCDCDC',
    'black': '000000'}



def change_hex2RGB(hex_code):
    red = hex_code[:2]
    green = hex_code[2:4]
    blue = hex_code[4:]

    '''옷의 hex_code - (r/g/b) 값으로 더 가까운 쪽의 색깔을 찾아보자!!'''



# def get_hsv(r,g,b):
#
#     # HSV_colors = colorsys.rgb_to_hsv(r,g,b)
#     # HSV_colors = cv2.cvtColor(rgb, cv2.COLOR_BGR2HSV)
#     blue = np.uint8([[[255,0,0]]])
#     green = np.uint8([[[0,255,0]]])
#     red = np.uint8([[[0,0,255]]])
#
#     # R,G,B 의 범위
#
#     #
#     HSV_blue = cv2.cvtColor(blue, cv2.COLOR_BGR2HSV)
#     HSV_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
#     HSV_red = cv2.cvtColor(red, cv2.COLOR_BGR2HSV)
#
#     print(f'HSV_blue : {HSV_blue}, HSV_green : {HSV_green}, HSV_blue : {HSV_red}')
#     # print(f'HSV : {HSV_colors}')
#
#
#
# def decision_color(Object):
#     #BGR ---> HSV
#     print(f'decision_color 함수 실행됨')
#     while True:
#         hsv = cv2.cvtColor(Object, cv2.COLOR_BGR2HSV)
#
#         #HSV에서 BGR로 가정할 범위를 정의.
#         lower_blue = np.array([90,100,100])  #np.array([H,S,V])
#         upper_blue = np.array([140,255,255])
#
#         lower_green = np.array([40,100,100])
#         upper_green = np.array([80,255,255])
#
#         lower_red = np.array([-30,100,100])
#         upper_red = np.array([30,255,255])
#
#         #HSV 이미지에서 only 청색 or 초록색 또는 빨간색만 추출하기 위한 임계깞
#         mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
#         mask_green = cv2.inRange(hsv, lower_green, upper_green)
#         mask_red = cv2.inRange(hsv, lower_red, upper_red)
#
#         #mask와 원본 이미지를 비트 연산함.
#         res1 = cv2.bitwise_and(Object, Object, mask=mask_blue)
#         res2 = cv2.bitwise_and(Object, Object, mask=mask_green)
#         res3 = cv2.bitwise_and(Object, Object, mask=mask_red)
#
#         cv2.imshow('original', Object)
#         cv2.imshow('Blue', res1)
#         cv2.imshow('Green', res2)
#         cv2.imshow('Red', res3)
#
#         k = cv2.waitKey(0) & 0xFF
#         if k == 27:
#             break


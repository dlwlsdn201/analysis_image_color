from math import sqrt, acos
import colorsys
import cv2

color_dic = {
    'red' : 'ff0000'}



def RGB_to_HLS(RGB): #RGB -> type of list
    R = RGB[0] / 255
    G = RGB[1] / 255
    B = RGB[2] / 255

    var_R = (R / 255)
    var_G = (G / 255)
    var_B = (B / 255)

    HSV_colors = colorsys.rgb_to_hsv(R,G,B)


    # var_Min = min(var_R, var_G, var_B) # Min.value of RGB
    # var_Max = max(var_R, var_G, var_B) #Max.value of RGB
    # del_Max = var_Max - var_Min # Delta RGB value

    # L = (var_Max + var_Min) / 2
    #
    # if (del_Max == 0): #This is a gray, no chroma...
    #     H = 0
    #     S = 0
    #
    # else: # Chromatic data...
    #     if (L < 0.5):
    #         S = del_Max / (var_Max + var_Min)
    #     else :
    #         S = del_Max / (2 - var_Max - var_Min)
    #
    # del_R = (((var_Max - var_R) / 6) + (del_Max / 2)) / del_Max
    # del_G = (((var_Max - var_G) / 6) + (del_Max / 2)) / del_Max
    # del_B = (((var_Max - var_B) / 6) + (del_Max / 2)) / del_Max


    # I = 1/3*(R+G+B)
    # S = 1 - (3/(R+G+B))*(min(R,G,B))
    # H = acos(( (1/2) * ((R-G) + (R-B))) / sqrt((R-G)**2 +(R-B)*(G-B)))
    # print(H)
    # if B > G :
    #     H = 360 - H



    # if (var_R == var_Max):
    #     H = del_B - del_G
    # elif (var_G == var_Max):
    #     H = ( 1 / 3 ) + del_R - del_B
    # elif ( var_B == var_Max ):
    #     H = ( 2 / 3 ) + del_G - del_R
    #
    # if ( H < 0 ):
    #     H += 1
    # if ( H > 1 ) :
    #     H -= 1
    return print('here:',HSV_colors)

def decision_similiar(original_color_HSL, product_color_HSL):
    # Hue rate : 기준 H값의 += 15
    original_H = original_color_HSL[0]
    product_H = product_color_HSL[0]

    if original_H - 15 < 0 :
        original_H = 360
    return print((original_H - 15 <= product_H) and (product_H <= original_H + 15))


def init():
    R,G,B = 153,51,255
    choose = RGB_to_HLS([R,G,B])
    R2,G2,B2 = 145,122,185
    product = RGB_to_HLS([R2,G2,B2])
    decision_similiar(choose, product)

init()


def Euclidean_Distance(first_hsv, second_hsv):
    D = sqrt((first_hsv[0]-second_hsv[0])**2 + (first_hsv[1] - second_hsv[1])**2 + (first_hsv[2] - second_hsv[2])**2)

    return D

# def convert_hexadecimal(h,s,v): #16진수코드 ---> 10진수 변환
#     hsv = [h,s,v]
#     result = []
#     for element in hsv:
#         i = 1
#         sum = 0
#         if type(element) != int:  #h,s,v 각 코드가 only 숫자가 아닌 경우
#             for char in element:
#                 if char in hexadecimal_codes:
#                     sum += hexadecimal_codes[char] * (16**i)
#                 else:
#                     sum += int(char) * (16**i)
#                 i -= 1
#         else:
#             sum += (element/10) * (16 ** 1) + (element%10) * (16**0)
#         result.append(sum)
#     print(result)
#     return result

# origin_color = color_dic[input('원하는 색상 입력:')]
# product_color = input('상품 hex_code 입력:')
# Calculate_color_similiar(origin_color,product_color)


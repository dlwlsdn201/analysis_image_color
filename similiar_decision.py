from math import sqrt
import get_color

color_dic = {
    'pink':'#FFC0CB',
     'purple' : '#9966ff',
    'red' : '#FF0000',
    'orange' : '#FF8000',
    'yellow' : '#FFFF00',
    'green' : '#008000',
     'cyan' : '#00FFFF',
     'blue':'#0000FF',
    # 'brown' :'#A52A2A',
     # 'white' : '#FFFFFF',
     # 'gray' : '#DCDCDC',
    # 'black': '#000000'
}
hexadecimal_codes = {
    "a" : 10,
    "b" : 11,
    "c" : 12,
    "d" : 13,
    "e" : 14,
    "f" : 15
}

def convert_rgb_to_hsv(r,g,b): #16진수코드 ---> 10진수 변환
    R = r / 255
    G = g / 255
    B = b / 255

    Color_max = max(R,G,B)
    Color_min = min(R,G,B)
    delta = Color_max - Color_min

    H = 0
    S = 0
    V = Color_max

    #get H
    if delta == 0:
        H = 0
    elif Color_max == R:
        H = 60 * (((G-R)/delta) % 6)
    elif Color_max == G:
        H = 60 * (((B-R)/delta) + 2)
    else:
        H = 60 * (((R-G) / delta) + 4)

    #get S
    if Color_max == 0:
        S = 0
    else:
        S = delta / Color_max
    return [H,S,V]

def Calculate_color_similiar(origin_color_code, product_color_code):  #hexcode ---> hsv 수치값
    origin_color_code = origin_color_code[1:]   #코드 앞에 '#' 문자열 제거
    product_color_code = product_color_code[1:]

    #R,G,B 를 표현하는 각 자리의 코드 선언
    hexcode_R1 = origin_color_code[:2]   #d유클리디안 거리 계산에 필요한 요소
    hexcode_G1 = origin_color_code[2:4]
    hexcode_B1 = origin_color_code[4:]

    hexcode_R2 = product_color_code[:2]
    hexcode_G2 = product_color_code[2:4]
    hexcode_B2 = product_color_code[4:]

    #hex_code ---> [R,G,B] 값으로 변환
    origin_rgb = convert_hexadecimal_to_rgb(hexcode_R1,hexcode_G1,hexcode_B1) #원본 색상의 hsv 코드(input color)
    product_rgb = convert_hexadecimal_to_rgb(hexcode_R2,hexcode_G2,hexcode_B2) # 상품 추출 생상의 hsv코드(product color)

    #RGB ---> HSV 변환 (H: 색상(Θ), S : 채도(%), V : 명도(%))
    origin_hsv = convert_rgb_to_hsv(origin_rgb[0],origin_rgb[1],origin_rgb[2]) #convert_rgb_to_hsv(r,g,b)
    product_hsv = convert_rgb_to_hsv(product_rgb[0],product_rgb[1],product_rgb[2])

    origin_h = get_Hue(origin_hsv)
    product_h = get_Hue(product_hsv)

    decision = decision_similiar_color(origin_h, product_h)

    return decision



def convert_hexadecimal_to_rgb(r_code,g_code,b_code): #16진수코드 ---> 10진수 변환
    rgb_codes = [r_code,g_code,b_code]
    result = []
    j = 0
    for element in rgb_codes:
        i = 1
        sum = 0
        if type(element) != int:  #h,s,v 각 코드가 문자열이 섞여 있을 경우
            for char in element:
                if char.lower() in hexadecimal_codes:                     #hexadecimal_codes : 16진수 기호 dictionary
                    sum += hexadecimal_codes[char.lower()] * (16**i)   # 16진수 기호 계산
                else:
                    sum += int(char) * (16**i)
                i -= 1
        else:
            sum += (element/10) * (16 ** 1) + (element%10) * (16**0)
        result.append(sum)
        j += 1
    return result

def decision_similiar_color(origin_H, product_H):

    #경계값 지정
    if origin_H == 0 :
        # boundary = list(range(345,360)) + list(range(0,16))
        boundary = list(range(340, 360)) + list(range(0, 21))
    else:
        boundary = list(range(int(origin_H-20), int(origin_H+21)))
        # boundary = list(range(int(origin_H-15), int(origin_H+16)))

    if int(product_H) in boundary:
        return print(f"유사한 색상 계열입니다.{True}")
    else:
        return print(f"선택한 색상과 다른 계열입니다.{False}")


def get_Hue(hsv):
    result = hsv[0]
    print(result)
    return result


def init(color, clothe_color):    #main 함수 (사용자 선택 색상, 옷의 색상)
    user_color = color_dic[color]  #사용자가 선택한 색상의 hexcode
    product_color = clothe_color #상품의 색상의 hexcode
    Calculate_color_similiar(user_color,product_color)
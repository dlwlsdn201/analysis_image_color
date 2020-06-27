import get_color

category_list = ['outer', 'top', 'pants', 'skirt', 'onepiece']
color_list = ['red','pink','purple','orange','yellow','green','cyan','blue','brown','white','gray','black']


#이미지 경로 지정
image_URL = "./images_sample/outer2.jpg"
image_URL = [image_URL]




while True:
    print(f'아래 리스트 중에서 원하는 카테고리를 입력해주세요.')
    print("[outer/top/pants/skirt/onepiece]")
    category = input('입력 : ')
    if category in category_list :
        break
    print('옳지 않은 입력입니다. 다시 시도해주세요')
    print()

while True:
        print('아래 리스트 중에서 원하는 색상 계열을 입력해주세요.')
        print("[red/pink/purple/orange/yellow/green/cyan/blue/brown/white/gray/black]")
        prefer_color = input('입력 : ')
        if prefer_color in color_list:
            break
        print('옳지 않은 입력입니다. 다시 시도해주세요')
        print()


#get_color.init(img path, category)

obj = get_color.init(image_URL, category, prefer_color)
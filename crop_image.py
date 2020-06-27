import cv2

def crop_process_img(src_path, category):
    src = cv2.imread(src_path, cv2.IMREAD_COLOR)
    dst = src.copy()
    dict = {'outer':0,
            'top': 1,
            'pants':2,
            'skirt':3,
            'onepiece':4
            }


    if dict[category] <= 1 :
        dst = src[90:180, 60:160]  # 아우터 이미지를 위한 사이즈로 변경
    elif dict[category] <= 3:
        dst = src[40:140, 60:160]  # 이미지를 (40~160 = 120 : 20~200 = 180) 사이즈로 변경
    else:
        dst = src[30:180, 60:160]

    dst = cv2.resize(dst, (220, 220))
    rows,cols = dst[:,:,0].shape
    background = src[rows-1,0,:]

    return dst
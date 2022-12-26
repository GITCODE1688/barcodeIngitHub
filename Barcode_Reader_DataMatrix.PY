# 解析Data Matrix
# pip install pylibdmtx
import os
import cv2
from pyzxing import BarCodeReader
from pylibdmtx.pylibdmtx import decode
# from PIL import Image

def BarcodeReader(image) :
    barcodeSeq = 0
    img = cv2.imread(image)

# use zxing 
    reader = BarCodeReader()
    zxingDetect = reader.decode(image)
    if len(zxingDetect)== 0 :
        print('zxing 辨識失敗')
    else:
        for barcode in zxingDetect:
            print("zxing:{}".format(barcode))
            print("zxing:{}".format(barcode['filename']))
            print("zxing:{}".format(barcode['raw']))
            print("zxing:{}".format(barcode['points']))
            print("zxing:{}".format(barcode['points'][0]))
            print('----------------------------------------------------------')
            zx_x = int(barcode['points'][0][0])-5    #框選的位置很怪，有空再說
            zx_y = int(barcode['points'][0][1])-5
            zx_w = int(barcode['points'][2][0])+5
            zx_h = int(barcode['points'][2][1])+5
            cv2.rectangle(img, (zx_x,zx_y),(zx_w, zx_h), (255,0,0), 2)
            cv2.putText(img, 'blue is detect from zxing', (zx_x,zx_h+30), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, (255,0,0), 1, cv2.LINE_AA)
            cv2.putText(img,str(barcode['raw']),(zx_x,zx_h+60), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, (255,0,0), 1, cv2.LINE_AA)

#二值化     (某此圖使用二值化，辨識barcode反而更差，不太會使用)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       #轉換前，都先將圖片轉換成灰階色彩
    # img = cv2.medianBlur(img, 5)   # 模糊化
    # img =  cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)      #自動二值化

#RESIZE
    sp = img.shape
    img_W = sp[0]
    img_H = sp[1]
    r_size = 1200
    rate = 1
    if img_W >r_size  :
        rate = r_size/img_W
    elif img_H > r_size :
        rate = r_size/img_H
    # print("{0},{1} / rate:{2}".format(img_W,img_H,rate))
    img=cv2.resize(img,None,fx=rate,fy=rate,interpolation=cv2.INTER_AREA)   

    

    detectedBarcode = decode(img)
    
    
    if len(detectedBarcode)==0 :
        print('辨識失敗')
    else :
        for barcode in detectedBarcode:
           print(type(detectedBarcode))
           print(detectedBarcode)
           print(barcode.data)
           (x,y,w,h) = detectedBarcode[0].rect
           print ('{0},{1},{2},{3}'.format(x,y,w,h))
           barcodeSeq += 1
           color = (0,0,255)
           
         

           cv2.rectangle(img,(x-5,y-5),(x+w+5,y+h+5),(0,0,255),2)
           cv2.putText(img, str(barcodeSeq), (x-30,y+15), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 2, cv2.LINE_AA)
           cv2.putText(img, "{0}".format(barcode.data), (x-30,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 1, cv2.LINE_AA)

    
                

    cv2.imshow("image",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows
    

if __name__ == "__main__":
  # Take the image from user
    image="./FT_WP_BOE.png"
    # image = r"./snap0382.jpg"
    # image = "./snap0077.jpg"
    # image = r"./w.png"
    # image = r"./snap0079.jpg"
    # image = "./traynobag.png"
    # image = "./nqsww5jSyK.png"
    # image = "./QaTWt8TIQl.png"
    # image = "./unnamed_1.jpg"
    # image = "./aAlkAODDiU.png"
    # image= './20210112084154260.jpg'

    # image = "./aAlkAODDiU.jpg"
    BarcodeReader(image)
    os._exit
    
    
#pip install pyzbar
import os
import cv2
import pyzbar.pyzbar
from pyzbar.pyzbar import decode

def BarcodeReader(image) :
    barcodeSeq = 0
    img = cv2.imread(image)

#二值化     (某此圖使用二值化，辨識barcode反而更差，不太會使用)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       #轉換前，都先將圖片轉換成灰階色彩
    img = img = cv2.medianBlur(img, 5)   # 模糊化
    img =  cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)      #自動二值化

#RESIZE
    sp = img.shape
    img_W = sp[0]
    img_H = sp[1]
    r_size = 800
    rate = 1
    if img_W >r_size  :
        rate = r_size/img_W
    elif img_H > r_size :
        rate = r_size/img_H
    print("{0},{1} / rate:{2}".format(img_W,img_H,rate))
    img=cv2.resize(img,None,fx=rate,fy=rate,interpolation=cv2.INTER_AREA)   

    detectedBarcode = decode(img)

    if not detectedBarcode :
        print('不要玩我, 圖片裡什麼鬼條碼都沒有')
        cv2.imshow("image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows         
    else:
        for barcode in detectedBarcode:
            (x,y,w,h) = barcode.rect

            # cv2.rectangle(img,(x-5,y-5),(x+w+5,y+h+5),(0,0,255),2)
            
            barcodeSeq += 1
            color = (0,0,255)
            cv2.putText(img, str(barcodeSeq), (x-30,y+15), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 2, cv2.LINE_AA)
            cv2.putText(img, "{0}({1})".format(barcode.data,barcode.type), (x-30,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 1, cv2.LINE_AA)
            if barcode.data != "":
                print("{0}. type:{1}   ,data{2}" .format(barcodeSeq,barcode.type,barcode.data))
                

        cv2.imshow("image",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows
    

if __name__ == "__main__":
  # Take the image from user
    # image="./FT_WP_BOE.png"
    # image = r"./snap0382.jpg"
    # image = r"./snap0077.jpg"
    # image = r"./w.png"
    # image = r"./snap0079.jpg"
    image = "./traynobag.png"
    BarcodeReader(image)
    os._exit
    
    
    # user interfaces
    while True:
        imgPath = input("輸入圖檔路徑: ")
        if imgPath == 'exit' :
            break         
        else:
            image = imgPath
            BarcodeReader(image)  
        print() 
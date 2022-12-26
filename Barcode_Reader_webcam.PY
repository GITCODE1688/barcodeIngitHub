#pip install opencv-python
#pip install pyzbar
import datetime
import os
import cv2
import pyzbar.pyzbar
from pyzbar.pyzbar import decode
import detect_image

def BarcodeReader(image) :
    barcodeSeq = 0
    # img = cv2.imread(image)
    cap = cv2.VideoCapture(30)
    # cap.set(3,640) #width
    # cap.set(4,480) #height
    # ret, frame = cap.read()
    if not cap.isOpened():
        raise IOError("We cannot open webcam")


    color = (0,0,255)
    while (True) :
       
        ret, frame = cap.read()
        print("{0} , {1}".format (ret,datetime.datetime.now()))
        img = frame
        r_image, ObjectList, ThresholdList = detect_image(img)

        detectedBarcode = decode(img)
        if not detectedBarcode :
            # (x,y,w,h) = barcode.rect
            # print('不要玩我, 什麼鬼條碼都沒有')
            # cv2.imshow("image",img)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows         
            cv2.putText(img, "{0}".format("detection failed"), (50,50), cv2.FONT_HERSHEY_COMPLEX_SMALL,  2, color, 1, cv2.LINE_AA)
        else:
            for barcode in detectedBarcode:
                (x,y,w,h) = barcode.rect

                cv2.rectangle(img,(x-5,y-5),(x+w+5,y+h+5),(0,0,255),2)
            
                barcodeSeq += 1
                # color = (0,0,255)
                cv2.putText(img, str(barcodeSeq), (x-30,y+15), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 1, cv2.LINE_AA)
                cv2.putText(img, "{0}({1})".format(barcode.data,barcode.type), (x-30,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 1, cv2.LINE_AA)
                if barcode.data != "":
                    print("{0}. type:{1}   ,data{2}" .format(barcodeSeq,barcode.type,barcode.data))

        cv2.imshow("vscode frame",img)
        # cv2.waitKey(1500)    
        # break
        
        if cv2.waitKey(1000) & 0xFF == ord('q'):
           break

    cap.release()   
    cv2.destroyAllWindows

#二值化     (某此圖使用二值化，辨識barcode反而更差，不太會使用)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       #轉換前，都先將圖片轉換成灰階色彩
    # img = img = cv2.medianBlur(img, 5)   # 模糊化
    # img =  cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)      #自動二值化

#RESIZE
    # sp = img.shape
    # img_W = sp[0]
    # img_H = sp[1]
    # r_size = 800
    # rate = 1
    # if img_W >r_size  :
    #     rate = r_size/img_W
    # elif img_H > r_size :
    #     rate = r_size/img_H
    # print("{0},{1} / rate:{2}".format(img_W,img_H,rate))
    # img=cv2.resize(img,None,fx=rate,fy=rate,interpolation=cv2.INTER_AREA)   

    # detectedBarcode = decode(img)

    # if not detectedBarcode :
    #     print('不要玩我, 圖片裡什麼鬼條碼都沒有')
    #     cv2.imshow("image",img)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows         
    # else:
    #     for barcode in detectedBarcode:
    #         (x,y,w,h) = barcode.rect

    #         # cv2.rectangle(img,(x-5,y-5),(x+w+5,y+h+5),(0,0,255),2)
            
    #         barcodeSeq += 1
    #         color = (0,0,255)
    #         cv2.putText(img, str(barcodeSeq), (x-30,y+15), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 2, cv2.LINE_AA)
    #         cv2.putText(img, "{0}({1})".format(barcode.data,barcode.type), (x-30,y-10), cv2.FONT_HERSHEY_COMPLEX_SMALL,  1, color, 1, cv2.LINE_AA)
    #         if barcode.data != "":
    #             print("{0}. type:{1}   ,data{2}" .format(barcodeSeq,barcode.type,barcode.data))
                

    # cv2.imshow("frame",frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows
    

if __name__ == "__main__":
  # Take the image from user
    image = 0     # or img file
    BarcodeReader(image)
    # os._exit
    
   
import cv2
import numpy as np
import os

def encrypt(imagepath, msg, password):
    img = cv2.imread(r"C:\qwerty\PNGimage.png")

    
    msgbytes = msg.encode('utf-8')
    length = len(msgbytes)

    
    img[0, 0, 0] = length

    
    m, n, z = 1, 0, 0
    for i in range(length):
        img[n, m, z] = msgbytes[i]
        m += 1
        if m >= img.shape[1]:  
            m = 0
            n += 1
        z = (z + 1) % 3  

    encryptedimagepath = "C:/qwerty/encryptedImage.png"
    cv2.imwrite(encryptedimagepath, img)
    os.system(f"start {encryptedimagepath}")
    return password

if __name__ == "__main__":
    imagepath = "C:/steganography/Image.png"  
    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")
    encrypt(imagepath, msg, password)

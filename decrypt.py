import cv2

def decrypt(imagepath, password, originalpassword):
    img = cv2.imread(r"C:\qwerty\encryptedImage.png")

    pas = input("\nEnter passcode for Decryption: ")

    if password == pas:
        
        length = img[0, 0, 0]

        message = ""
        m, n, z = 1, 0, 0
        for i in range(length):
            message += chr(img[n, m, z])
            m += 1
            if m >= img.shape[1]:  
                m = 0
                n += 1
            z = (z + 1) % 3  

        print("\n Decryption successful! Message:", message)
    else:
        print("\n Incorrect passcode! Access denied.")

if __name__ == "__main__":
    imagepath = "C:/qwerty/encryptedImage.png"
    password = input("Enter the passcode used for encryption: ")
    decrypt(imagepath, password, password)

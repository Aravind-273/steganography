import cv2
import os
import string
img = cv2.imread("sample.jpg")
msg = input("ENTER SECERT MESSAGE:")
pasw = input("ENTER PASSWORD:")
a={}
b={}
for i in range(255):
    a[chr(i)]=i
    b[i]=chr(i)

m=0
n=0
z=0

for i in range(len(msg)):
    img[n,m,z] = a[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("Encryptedmsg.jpg",img)
os.system("start Encryptedmsg.jpg")
message = ""
n=0
m=0
z=0
pas = input("ENTER PASSCODE FOR GETTING THE DECRYPTED MESSAGE:")
if pasw == pas:
    for i in range(len(msg)):
        message = message+b[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("Decryption message is:",message)
else:
    print("Not a valid key, TRY AGAIN")

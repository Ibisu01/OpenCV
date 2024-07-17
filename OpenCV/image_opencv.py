import cv2

haar_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
image = cv2.imread('img.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = haar_cas.detectMultiScale(gray, 1.1, 4)
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 5)
     
cv2.imshow("Gray", image)
cv2.waitKey()

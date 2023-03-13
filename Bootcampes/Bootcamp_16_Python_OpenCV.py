import cv2

# работа с картинкой из файла
# img = cv2.imread('image.jpg')
# img = cv2.resize(img, (500,500))
# cv2.imshow('result', img)
# cv2.waitKey(1000)

# распознавание лица с картинки
# face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
# img = cv2.imread('image.jpg')
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = face_cascades.detectMultiScale(img_gray)
# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (155, 155, 155), 2)
# cv2.imshow('result', img)
# cv2.waitKey(0)

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (155, 155, 155), 2)
    cv2.imshow('camera', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

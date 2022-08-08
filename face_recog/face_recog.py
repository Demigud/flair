from datetime import datetime
import face_recognition
import cv2
import numpy as np
import os       

#import images

path = "C:\\Users\\pc\\Documents\\GitHub\\flair\\media\\student_img"
#path = "C:\\Users\\pc\\Documents\\GitHub\\flair\\face_recog\\images\\actual"


# list images
images = []
classNames = []
# os function
myList = os.listdir(path)
print(myList)

# list names with out the JPG extension
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

# after import images find encoding for each image
#function to compute encodings

def findEncodings(images):
    encodeList = []
    for img in images: 
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


encodeListActual = findEncodings(images)
print('encoding complete')
# print(len(encodeListActual))

cap = cv2.VideoCapture(2)
# find matches between encodings
while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # find encoding of webcam
    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListActual,encodeFace)
        faceDis = face_recognition.face_distance(encodeListActual,encodeFace)
        # print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
           
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,0.6,(255,255,255),2)
            markAttendance(name)


    cv2.imshow('Webcam',img)
    cv2.waitKey(1)    


# duterte = face_recognition.load_image_file('C:\Users\franz\OneDrive\Documents\face_recog\env\images\actual\duterte.jpg')
# duterte = cv2.cvtColor(duterte,cv2.COLOR_BGR2RGB)

# duterte_test = face_recognition.load_image_file('C:\Users\franz\OneDrive\Documents\face_recog\env\images\test\duterte_test.jpg')
# duterte_test = cv2.cvtColor(duterte_test,cv2.COLOR_BGR2RGB)

# cv2.imshow('Duterte', duterte)
# cv2.imshow('Duterte test', duterte_test)
# cv2.waitKey(0)

from ui.home import Ui_HomeWindow
from ui.checkin import Ui_checkinWindow
import numpy as np
import cv2
from PyQt5.QtCore import QThread, pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from imutils.video import VideoStream
import time
import imutils
import sys
import face_recognition
import pickle
import datetime



################################################# workers


class VideoFeedWorker(QtCore.QThread):
    frame = QtCore.pyqtSignal(np.ndarray)
    face_boxes = QtCore.pyqtSignal(np.ndarray, list)
    vs = VideoStream(src=0)
    ThreadActive = True
    def run(self):
        self.vs.start()
        writer = None
        time.sleep(2.0)

        while self.ThreadActive:
            # grab the frame from the threaded video stream
            f = self.vs.read()
            
            # convert the input frame from BGR to RGB then resize it to have
            # a width of 750px (to speedup processing)
            rgb = imutils.resize(f, width=750)
            rgb = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)

            # find faces
            boxes = face_recognition.face_locations(rgb, model="hog")

            # draw boxes around faces
            # loop over the recognized faces
            
            r = f.shape[1] / float(rgb.shape[1])

            for top, right, bottom, left in boxes:
                # rescale the face coordinates
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r)
                left = int(left * r)
                # draw the predicted face name on the image
                cv2.rectangle(f, (left, top), (right, bottom),
                    (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                # cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,
                #     0.75, (0, 255, 0), 2)
                
            f = cv2.cvtColor(f, cv2.COLOR_BGR2RGB)
            self.frame.emit(f)
            self.face_boxes.emit(f, boxes)

    def stop(self):
        self.ThreadActive = False
        self.vs.stop()
        self.isRunning = False
        self.terminate()



######################## UI ############################
class CheckinWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__() 
        self.ui = Ui_checkinWindow()
        self.ui.setupUi(self)

        self.data = pickle.loads(open("encordings/encodings.pickle", "rb").read())

        self.videoFeedWorker = VideoFeedWorker()
        # self.ui.cancelBtn.clicked.connect(lambda: self.videoFeedWorker.stop())
        # self.ui.clearBtn.clicked.connect(lambda: self.videoFeedWorker.start())
        self.videoFeedWorker.frame.connect(self.display_video_feed)
        self.videoFeedWorker.face_boxes.connect(self.scan_for_faces)
        self.videoFeedWorker.start()

    def restart_feed(self):
        self.videoFeedWorker.start()

    def display_video_feed(self, frame):
        ConvertToQtFormat = QtGui.QImage(frame.data, frame.shape[1], frame.shape[0], QtGui.QImage.Format_RGB888)
        # image = ConvertToQtFormat.scaled(700, 500, QtCore.Qt.KeepAspectRatio)
        self.ui.feedLabel.setPixmap(QtGui.QPixmap.fromImage(ConvertToQtFormat))

    def scan_for_faces(self, frame, boxes):
        
        encodings = face_recognition.face_encodings(frame, boxes)

        names = []
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(self.data['encodings'], encoding)
            name = "Unknown"
            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}
                # loop over the matched indexes and maintain a count for
                # each recognized face face
                for i in matchedIdxs:
                    name = self.data["names"][i]
                    counts[name] = counts.get(name, 0) + 1
                # determine the recognized face with the largest number
                # of votes (note: in the event of an unlikely tie Python
                # will select first entry in the dictionary)
                name = max(counts, key=counts.get)
            
            # update the list of names
            names.append(name)
            # print(name)

        if len(names) > 0:
            self.profile_name = name[0]
            self.ui.nameLabel.setText(names[0])
            self.ui.scanningLabel.setText("Face Recognised")

            self.checkin(name)
        else:
            self.ui.scanningLabel.setText("Scanning...")
            self.ui.statusLabel.setText("")
            self.ui.nameLabel.setText("waiting...")


    def checkin(self, name):
       with open("attendance/attendance.txt", 'r+') as attendance:
           checkin =[n.split(",") for n in attendance.readlines()]
           current_person = [n for n in checkin if n[0] == name]
           if len(current_person) <= 0:
               t = datetime.datetime.now()
               checkin.append([name, str(t.timestamp())])
               self.ui.statusLabel.setText(f"Checked-in at {t}")

               for name, time in checkin:
                   attendance.write(f"{name}, {time}")
           else:
               self.ui.statusLabel.setText(f"Already checked-in")
           

    def cancel(self):
        pass

    def display_profile(self):
        pass



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = CheckinWindow()
    win.show()
    sys.exit(app.exec_())
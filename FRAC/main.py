import time

import io
import kivy
#kivy.require() # replace with your current kivy version !

import cv2
import config
import face
#import hardware

from kivy import Config

from kivy.app import App
from kivy.properties import ObjectProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

Config.set("kivy", "keyboard_mode", "systemanddock")
Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")


class FRACApp(App):

    def build(self):
        appMain = FRACMain()
        #Clock.schedule_interval(appMain.update, 1.0)
        return appMain

class FRACMain(GridLayout):
    dateTimeLabel = ObjectProperty(None)
    isLocked = True

    def lockUnlock(self):
        lockImage = self.ids['lock_image']
        statusLabel = self.ids['statusLabel']

        if self.isLocked:
            if self.unlockBox():
                lockImage.source = "unlocked.png"
                self.isLocked = False
                statusLabel.text = "Un-Locked"


        else:
            self.lockBox()
            lockImage.source = "locked.png"
            self.isLocked = True
            camera.opacity = 0
            camera.play = False
            statusLabel.text = "Locked"

    def update(self, dt):
        #self.dateTimeLabel.text = time.strftime("%H:%M:%S\n%d/%m/%Y")
        pass

    def lockBox(self):
        pass

    def unlockBox(self):
        """
        print ('Button pressed, looking for face...')
        # Check for the positive face and unlock if found.
        image = camera.read()
        # Convert image to grayscale.
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        # Get coordinates of single face in captured image.
        result = face.detect_single(image)
        if result is None:
            print ('Could not detect single face!  Check the image in capture.pgm' \
            ' to see what was captured and try again with only one face visible.')
            return
        x, y, w, h = result
        # Crop and resize image to face.
        crop = face.resize(face.crop(image, x, y, w, h))
        # Test face against model.
        label, confidence = model.predict(crop)
        print ('Predicted {0} face with confidence {1} (lower is more confident).').format(
            'POSITIVE' if label == config.POSITIVE_LABEL else 'NEGATIVE', confidence)
        if label == config.POSITIVE_LABEL and confidence < config.POSITIVE_THRESHOLD:
            print
            'Recognized face!'
            box.enable()
        else:
            print
            'Did not recognize face!'
        """
        face_image = self.ids['face_image']

        print(face_image.x, face_image.y)

if __name__ == '__main__':
    """
    model = cv2.createEigenFaceRecognizer()
    model.load(config.TRAINING_FILE)
    print ('Training data loaded!')
    # Initialize camera and box.
    camera = config.get_camera()
    #box = hardware.Box()
    # Move box to locked position.
    #box.disable()
    """
    FRACApp().run()
import time

import cv2
import RPi.GPIO as GPIO


import picam
import config
import face


class Box(object):
	def __init__(self):
		# Initialize lock servo and button.
		GPIO.setmode(GPIO.BOARD)
		GPIO.setup(config.RELAY_PIN, GPIO.OUT, initial=1)

		# Set initial box state.
		self.button_state =0
		self.is_locked = None

	def disable(self):
		"""Disable AC power of the box."""
		GPIO.output(config.RELAY_PIN,1)
		self.is_locked = True

	def enable(self):
		"""Enable AC power of the box."""
		GPIO.output(config.RELAY_PIN,0)
		self.is_locked = False

	

import numpy as np
import cv2
import glob
import os

## Convert video to frames
def videoToFrames(videoDir):

	print('\nLoading video: ' + videoDir)

	# If the video does not exist
	if len(glob.glob(videoDir)) == 0:

		print('\nDid not find video.')

	# If the video does exist
	else:

		# Directory to output frames to
		outDir = 'output/' + videoDir.split('/')[-1].split('.')[0] + '/'

		# If output does not exist, make it
		if len(glob.glob(outDir)) == 0:

			os.mkdir(outDir)

		# Reading video
		video = cv2.VideoCapture(videoDir)

		# Get number of frames
		fNum = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

		# Get frame
		success, image = video.read()

		# Count frame number
		count = 0

		# While frame is read
		while success:

			# Displaying progress
			if count%100 == 0:

				print(str(100*count/fNum)[0:4] + '%')

			# Name of output frame
			fName = outDir + str(count).zfill(len(str(fNum))) + '.jpg'

			# Save frame
			cv2.imwrite(fName, image)     

			# Get frame
			success, image = video.read()

			# Add frame
			count += 1

	print('\nDone.')

## Convert frames to video
def framesToVideo(framesDir):
	print('\nDone.')
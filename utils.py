## Importing packages
import numpy as np
import shutil
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

		# If output directory does not exist
		if len(glob.glob('output/')) == 0:

			os.mkdir('./output/')

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
			fName = outDir + str(count).zfill(len(str(fNum))) + '.tif'

			# Save frame
			cv2.imwrite(fName, image)     

			# Get frame
			success, image = video.read()

			# Add frame
			count += 1

	print('\nDone.')

## Convert frames to video
def framesToVideo(framesDir, framerate):

	print('\nLoading frames: ' + framesDir)

	# Frames paths
	fPath = glob.glob(framesDir)

	# If no frames found
	if len(fPath) == 0:

		print('\nNo Frames were found.')

	# If frames are found
	else:

		print('Found ' + str(len(fPath)) + ' frames.')

		# If output directory does not exist
		if len(glob.glob('output/')) == 0:

			os.mkdir('./output/')

		# Output video name
		vPath = 'output/' + framesDir.split('/')[-2] + '.avi'

		# Reading first file for size
		im0 = cv2.imread(fPath[0])

		# Extracting video size
		height, width, layers = im0.shape
		size = (width, height)

		# Output video
		out = cv2.VideoWriter(vPath, cv2.VideoWriter_fourcc(*'DIVX'), framerate, size)

		# Starting video write
		for i, filename in enumerate(fPath):

			# Displaying progress
			if i%100 == 0:

				print(str(100*i/len(fPath))[0:4]+'%')

			# Reading current frame
			img = cv2.imread(filename)

			# Extracting shape
			h, w, l = img.shape

			# Checking if shape matches spec for video
			if h == height  and w == width and l == layers:

				# Write frame
				out.write(img)

			# If shape is different
			else:

				print('Incorrect shape for frame: ' + filename)
				break

		out.release()

	print('\nDone.')

## Select equally spaced frames
def framesEqualSelect(framesDir, n):

	print('\nLoading frames: ' + framesDir)

	# Frames paths
	fPath = glob.glob(framesDir)

	# If no frames found
	if len(fPath) == 0:

		print('\nNo Frames were found.')

	# If frames are found
	else:

		print('Found ' + str(len(fPath)) + ' frames.')

		if len(fPath) < n:

			print('\nThe number of frames to select (' + str(n) + ') is greater than the total number of frames (' + str(len(fPath)) + ').')
			print('Exiting script.')
			return

		# If output directory does not exist
		if len(glob.glob('output/')) == 0:

			os.mkdir('./output/')

		# Directory to output selected frames to
		outDir = 'output/' + framesDir.split('/')[-2] + '/'

		# If output does not exist, make it
		if len(glob.glob(outDir)) == 0:

			os.mkdir(outDir)

		# If output has files inside already
		if len(glob.glob(outDir + '/*')) > 0:

			print('\nThere are already files in the output. Deleting them.')

			for file in glob.glob(outDir + '/*'):

				os.remove(file)

		# Delta between frames
		delta = len(fPath)/n

		# Store how many frames have been copied
		copied = 0

		# float to help decide what frame to copy
		copyVal = 0.0

		# Copying over selected frames
		while(copied < n):

			# Showing progress
			if copied%10 == 0:

				print(str(100*copied/n)[:4] + '%')

			# Source path of file
			sourcePath = fPath[int(copyVal)]

			# Destination path to copy file to
			destPath = outDir + sourcePath.split('\\')[-1]

			# Copying the file over
			shutil.copyfile(sourcePath, destPath)

			# Add one to number of files copied
			copied += 1

			# Add delta to determine next file
			copyVal += delta

		print('\nFinished copying ' + str(copied) + ' files.')
		print('\nDone.')
import argparse

from utils import *

def main(args):

	## Convert video to frames
	if args.v2f:

		print('\nConverting video to frames')

		videoToFrames(args.vDir)

	# Convert frames to video
	if args.f2v:

		print('\nConverting frames to video')

		framesToVideo(args.fDir)

	print('\nmain.py executed successfully.')

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Reading info for main.')

	# Arguments to convert video to frames
	parser.add_argument('--v2f', action='store_true', help='Flag to convert video to frames.')
	parser.add_argument('--vDir', action='store', nargs='?', type=str, default='input/example.avi', help='Source video.')

	# Arguments to converts frames to video
	parser.add_argument('--f2v', action='store_true', help='Flag to convert frames to video.')
	parser.add_argument('--fDir', action='store', nargs='?', type=str, default='input/example/*.tif', help='Source frames.')

	# Parse arguments
	args = parser.parse_args()

	# Call main
	main(args)
## Importing packages
import argparse

## Import required functions from utils
from utils import *

## Main function
def main(args):

	## Convert video to frames
	if args.v2f:

		print('\nConverting video to frames')

		videoToFrames(args.vDir)

	# Convert frames to video
	if args.f2v:

		print('\nConverting frames to video')

		framesToVideo(args.fDir, args.fps)

	print('\nmain.py executed successfully.')

	# Select equally spaced frames
	if args.fSel:

		print('\nSelecting equally spaced frames.')

		framesEqualSelect(args.fDir, args.nSel)

	print('\nExited main.py.')

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Reading info for main.')

	# Arguments to convert video to frames
	parser.add_argument('--v2f', action='store_true', help='Flag to convert video to frames.')
	parser.add_argument('--vDir', action='store', nargs='?', type=str, default='input/example.avi', help='Source video.')
	# Example:
	# python main.py --v2f --vDir input/example.avi

	# Arguments to converts frames to video
	parser.add_argument('--f2v', action='store_true', help='Flag to convert frames to video.')
	parser.add_argument('--fDir', action='store', nargs='?', type=str, default='input/example/*.tif', help='Source frames.')
	parser.add_argument('--fps', action='store', nargs='?', type=int, default=25, help='Wanted video fps.')
	# Example:
	# python main.py --f2v --fDir input/example/*.tif --fps 25

	# Arguments to choose equal spaced frames from directory
	parser.add_argument('--fSel', action='store_true', help='Flag to select equally spaced frames.')
	# Also required: parser.add_argument('--fDir', action='store', nargs='?', type=str, default='input/example/*.tif', help='Source frames.')
	parser.add_argument('--nSel', action='store', nargs='?', type=int, default=100, help='How many frames to select.')
	# Example:
	# python main.py --fSel --fDir input/example/*.tif --nSel 100

	# Parse arguments
	args = parser.parse_args()

	# Call main
	main(args)
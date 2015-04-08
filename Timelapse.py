
import argparse
import picamera
import time

parser = argparse.ArgumentParser(description='Take timelapse')
parser.add_argument('time',
					type=int,
					help='time to wait between each picture (in seconds)')
parser.add_argument('--dir',
					dest='directory'
					default="/var/www",
					help='directoy where store pictures')
args = parser.parse_args()

print "[+] launch timelapse"
with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.start_preview()
	print "[+] camera OK"
	for filename in camera.capture_continuous(args.directory + '/img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
		print "[+] captured : %s" % filename
		time.sleep(args.time)


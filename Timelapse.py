
import argparse
import picamera
import time

parser = argparse.ArgumentParser(description='Take timelapse')
parser.add_argument('-t', '--time',
					dest='time',
					type=int,
					default=1,
					help='time to wait between each picture (in seconds)')
parser.add_argument('-d', '--dir',
					dest='directory'
					default="/var/www",
					help='directoy in which the pictures are stored')
args = parser.parse_args()

print "[+] dir : %s" % args.directory
print "[+] time : %d" % args.time
print "[+] launch timelapse"
with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.start_preview()
	print "[+] camera OK"
	for filename in camera.capture_continuous(args.directory + '/img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
		print "[+] captured : %s" % filename
		time.sleep(args.time)


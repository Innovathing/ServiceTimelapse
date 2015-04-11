#!/usr/bin/env python2
#encoding utf-8

import argparse
import logging
import picamera
import time

parser = argparse.ArgumentParser(description='Take timelapse')
parser.add_argument('-t', '--time',
					dest='time',
					type=int,
					default=1,
					help='time to wait between each picture (in seconds)')
parser.add_argument('-d', '--dir',
					dest='directory',
					default="/var/www",
					help='directoy in which the pictures are stored')
parser.add_argument('-l', '--logfile',
					dest='logfile',
					default="/var/www/timelapse.log",
					help='file in which the logging things are printed')
args = parser.parse_args()

logging.basicConfig(filename=args.logfile, level=logging.DEBUG)
logging.info("[+] dir : %s" % args.directory)
logging.info("[+] time : %d" % args.time)
logging.info("[+] launch timelapse")
with picamera.PiCamera() as camera:
	camera.resolution = (1280, 720)
	camera.start_preview()
	logging.info("[+] camera OK")
	for filename in camera.capture_continuous(args.directory + '/img{timestamp:%Y-%m-%d-%H-%M-%S}.jpg'):
		logging.info("[+] captured : %s" % filename)
		time.sleep(args.time)


from bot import config
import time
from bot import rpicam


IP = "192.168.0.100"
RTP_PORT = 5000

VIDEO_FORMAT = rpicam.VIDEO_MJPEG #поток MJPEG
VIDEO_RESOLUTION = (640, 360)
VIDEO_FRAMERATE = 20

rpiCamStreamer = rpicam.RPiCamStreamer(VIDEO_FORMAT, VIDEO_RESOLUTION, VIDEO_FRAMERATE)
rpiCamStreamer.setPort(RTP_PORT)
rpiCamStreamer.setHost(IP)
rpiCamStreamer.start()

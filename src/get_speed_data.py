import speedtest
from threading import Thread
import time
from .db.speed_table import SpeedTable
from datetime import datetime

class GetSpeedData(Thread):
  def __init__(self, log = False):
    self.log = log

  def run(self):
    while True:
      self.getData()
      time.sleep(60)

  def convertToMb(self, speed):
    return "{:.2f}".format(speed/1048576) # Bytes to MBytes

  def getData(self):
    st = speedtest.Speedtest()
    downloadSpeed = float(st.download())
    uploadSpeed = float(st.upload())
    timestamp = int(time.time())

    downloadSpeed = self.convertToMb(downloadSpeed)
    uploadSpeed = self.convertToMb(uploadSpeed)
    SpeedTable.insert(downloadSpeed, uploadSpeed, timestamp)

    if(self.log):
      dt_object = datetime.fromtimestamp(timestamp)
      print('{} --- Download speed: {} Mb/s --- Upload speed: {} Mb/s'.format(dt_object, downloadSpeed, uploadSpeed))
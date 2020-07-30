import sqlite3
import os.path
from ..model.speed_data import SpeedData

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class SpeedTable:
  def __init__(self):
    pass

  def insert(download_speed, upload_speed, timestamp):
    connection = sqlite3.connect('{}/speed.db'.format(BASE_DIR))
    cursor = connection.cursor()
    
    data = (download_speed, upload_speed, timestamp)
    cursor.execute('INSERT INTO speed_data VALUES (?, ?, ?)', data)

    connection.commit()
    connection.close()
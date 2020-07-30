import sqlite3
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

connection = sqlite3.connect('{}/speed.db'.format(BASE_DIR))
cursor = connection.cursor()
cursor.execute('''CREATE TABLE speed_data (download text, upload text, timestamp int)''')
connection.commit()
connection.close()
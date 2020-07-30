from src.get_speed_data import GetSpeedData
import argparse

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument("-log", help="Define whether the log will be displayed on the terminal or not.", action='store_true')

  args = parser.parse_args()

  gsd = GetSpeedData(args.log)
  gsd.run()

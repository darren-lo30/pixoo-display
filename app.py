from os import getenv
from time import sleep
from PIL import Image
from dotenv import load_dotenv

import modules.pixoo_client as pixc
import ctypes, sys

from modules.pc_info import display_pc_stats
load_dotenv(".env")


def is_admin():
  try:
    return ctypes.windll.shell32.IsUserAnAdmin()
  except:
    return False

def connect():
  pixoo_mac = getenv("PIXOO_MAC_ADDRESS")
  tmp_folder = getenv("TMP_FOLDER")
  
  try:
    pixoo = pixc.PixooMax(pixoo_mac)
    pixoo.connect()
    return pixoo
  except:
    print("Failed to connect")
    return None

if __name__ == "__main__":

  if is_admin():
    pixoo = None
    while pixoo == None:
      pixoo = connect()

    while True:  # Main loop - here you can change the drawing functions
      print('hi')
      display_pc_stats(pixoo)
      sleep(1.0)  # 10 fps are already pretty smooth
  else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
  

from os import getenv
from time import sleep
from dotenv import load_dotenv

import modules.pixoo_client as pixc
from modules.admin import is_admin

import ctypes, sys

from modules.pc_info import get_handle, display_pc_stats
load_dotenv(".env")


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
      
    pc_handle = get_handle()

    while True:  # Main loop - here you can change the drawing functions
      display_pc_stats(pc_handle, pixoo)
      sleep(1.0)  # 10 fps are already pretty smooth
  else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
  

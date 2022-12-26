import modules.pixoo_client as pixc
from dotenv import load_dotenv
from os import getenv


load_dotenv(".env")

if __name__ == "__main__":
  pixoo_mac = getenv("PIXOO_MAC_ADDRESS")
  tmp_folder = getenv("TMP_FOLDER")

  pixoo = pixc.PixooMax(pixoo_mac)
  pixoo.connect()

  pixoo.set_system_brightness(70) # Turn on pixoo 
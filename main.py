from os import getenv
from time import sleep
from PIL import Image
from dotenv import load_dotenv

import modules.pixoo_client as pixc


load_dotenv(".env")

if __name__ == "__main__":
  pixoo_mac = getenv("PIXOO_MAC_ADDRESS")
  tmp_folder = getenv("TMP_FOLDER")

  pixoo = pixc.PixooMax(pixoo_mac)
  pixoo.connect()

  while True:  # Main loop - here you can change the drawing functions
    base = Image.new("RGBA", (32, 32), (0, 0, 0, 256))  # Create a base new image
    print(tmp_folder + "tmp.png")
    base.save(tmp_folder + "tmp.png")
    pixoo.draw_pic(tmp_folder + "tmp.png")

    sleep(1.0 / 10)  # 10 fps are already pretty smooth

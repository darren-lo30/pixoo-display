from PIL import Image, ImageDraw
from os import getenv


from pyspectator.processor import Cpu
from time import sleep

cpu = Cpu(monitoring_latency=1)
def get_cpu_temperature():
  with cpu:
    return cpu.load

def display_pc_stats(pixoo):
  tmp_folder = getenv('TMP_FOLDER')
  base = Image.new("RGBA", (32, 32), (0, 0, 0, 0))  # Create a base new image

  # Display CPU Temperature
  ImageDraw.Draw(
    base
  ).text((0, 0), str(get_cpu_temperature()), (255, 255, 255))

  base.save("./tmp/pc_stat.png")

  pixoo.draw_pic(tmp_folder + "pc_stat.png")

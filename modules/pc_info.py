from PIL import Image, ImageDraw, ImageFont
from os import getenv
import wmi

from pyspectator.processor import Cpu
from time import sleep

cpu = Cpu(monitoring_latency=1)
def get_cpu_load():
  with cpu:
    return cpu.load

def get_gpu_temperature():
  w = wmi.WMI(namespace="root\OpenHardwareMonitor")
  temperature_infos = w.Sensor()
  for sensor in temperature_infos:
    if sensor.Name == 'GPU Core' and sensor.SensorType== 'Temperature':
      return sensor.Value

def get_cpu_temperature():
  # pyspectator isnt working for cpu temperatures
  w = wmi.WMI(namespace="root\OpenHardwareMonitor")
  temperature_infos = w.Sensor()
  for sensor in temperature_infos:
    if sensor.SensorType==u'Temperature':
      print(sensor.Name)
      print(sensor.Value)


def display_pc_stats(pixoo):
  tmp_folder = getenv('TMP_FOLDER')
  base = Image.new("RGBA", (32, 32), (0, 0, 0, 0))  # Create a base new image

  # Display CPU Load
  ImageDraw.Draw(
    base
  ).text((0, 0), f'{str(get_cpu_load())}%', (255, 255, 255))

  # Display GPU temperature
  ImageDraw.Draw(
    base
  ).text((0, 16), f'{str(round(get_gpu_temperature()))}\xb0C', (176,224,230))

  base.save("./tmp/pc_stat.png")
  pixoo.draw_pic(tmp_folder + "pc_stat.png")

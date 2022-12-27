from PIL import Image, ImageDraw
from os import getenv
from .admin import is_admin
import clr

def get_handle():
  if not is_admin():
    raise "Can only be initialized with admin permissions."
  
  clr.AddReference(r'./lib/OpenHardwareMonitorLib')
  from OpenHardwareMonitor.Hardware import Computer


  handle = Computer()
  handle.MainboardEnabled = True
  handle.CPUEnabled = True
  handle.RAMEnabled = True
  handle.GPUEnabled = True
  handle.HDDEnabled = True
  handle.Open()

  return handle
  
def get_pc_stats(handle):
  pc_stats = []
  for component in handle.Hardware:
    component.Update()
    for sensor in component.Sensors:
      pc_stats.append(sensor)
      # print(type(sensor))
    for subcomponent in component.SubHardware:
      subcomponent.Update()
      for subsensor in subcomponent.Sensors:
        pc_stats.append(subsensor)
  # print(pc_stats)
  return pc_stats

# sensortypes = ['Voltage','Clock','Temperature','Load','Fan','Flow','Control','Level','Factor','Power','Data','SmallData']

def get_cpu_load(pc_stats):
  for sensor_stat in pc_stats:
    if sensor_stat.Name == 'CPU Total':
      return sensor_stat.Value

def get_gpu_temperature(pc_stats):
  for sensor_stat in pc_stats:
    if sensor_stat.Name == 'GPU Core' and str(sensor_stat.SensorType) == 'Temperature':
      return sensor_stat.Value


# def get_gpu_load(stats):



def display_pc_stats(pc_handle, pixoo):
  tmp_folder = getenv('TMP_FOLDER')
  base = Image.new("RGBA", (32, 32), (0, 0, 0, 0))  # Create a base new image

  pc_stats = get_pc_stats(pc_handle)

  # Display CPU Load
  ImageDraw.Draw(
    base
  ).text((0, 0), f'{str(round(get_cpu_load(pc_stats), 1))}%', (255, 255, 255))

  # Display GPU temperature
  ImageDraw.Draw(
    base
  ).text((0, 16), f'{str(round(get_gpu_temperature(pc_stats)))}\xb0C', (176,224,230))

  base.save("./tmp/pc_stat.png")
  pixoo.draw_pic(tmp_folder + "pc_stat.png")

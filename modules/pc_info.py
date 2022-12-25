from os import getenv
from time import sleep
from PIL import Image
from dotenv import load_dotenv

from modules.time import draw_time
from modules.github import draw_github_contribution
import modules.pixoo_client as pixc

load_dotenv("local.env", verbose=True)

from decouple import AutoConfig
from constants import ROOT_DIR


config = AutoConfig(search_path=ROOT_DIR)


IN_PIC_DIR = config("IN_PIC_DIR")
DEFAULT_OUT_PIC_DIR = config("DEFAULT_OUT_PIC_DIR")
DEFAULT_PIC_LST_TXT = f'{DEFAULT_OUT_PIC_DIR}list.txt'
FONT_NAME = config("FONT_NAME")
IN_PIC_EXT = config("IN_PIC_EXT")
FRAMERATE = 30
PIX_FMT_IN = config("PIX_FMT_IN")
OUT_CODEC = config("OUT_CODEC")
OUT_VID_NAME = config("OUT_VID_NAME")
TIMESTAMP_FORMAT = config("TIMESTAMP_FORMAT")
DELTA_SECONDS = -3600
TEXT_SIZE = 150
IMAGE_SIZE = (1920, 1440)

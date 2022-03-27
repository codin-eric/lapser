from decouple import AutoConfig
from constants import ROOT_DIR


config = AutoConfig(search_path=ROOT_DIR)


IN_PIC_DIR = config("IN_PIC_DIR")
DEFAULT_OUT_PIC_DIR = config("DEFAULT_OUT_PIC_DIR")
DEFAULT_PIC_LST_TXT = f'{DEFAULT_OUT_PIC_DIR}list.txt'
FONT_NAME = config("FONT_NAME")
IN_PIC_EXT = config("IN_PIC_EXT")
FRAMERATE = config("FRAMERATE", cast=int)
PIX_FMT_IN = config("PIX_FMT_IN")
OUT_CODEC = config("OUT_CODEC")
OUT_VID_NAME = config("OUT_VID_NAME")
TIMESTAMP_FORMAT = '%Y:%m:%d %H:%M:%S'
DELTA_SECONDS = config("DELTA_SECONDS", cast=int)
TEXT_SIZE = config("TEXT_SIZE", cast=int)
IMAGE_SIZE = (1920, 1440)

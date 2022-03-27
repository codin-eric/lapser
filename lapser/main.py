from PIL import Image, ImageFont, ImageDraw
from PIL.ExifTags import TAGS
import ffmpeg
import logging
from pathlib import Path
from datetime import datetime, timedelta

from cfg import (
    IN_PIC_DIR,
    DEFAULT_OUT_PIC_DIR,
    DEFAULT_PIC_LST_TXT,
    IN_PIC_EXT,
    FRAMERATE,
    PIX_FMT_IN,
    OUT_CODEC,
    OUT_VID_NAME,
    TIMESTAMP_FORMAT,
    DELTA_SECONDS,
    TEXT_SIZE,
    IMAGE_SIZE,
    FONT_PATH
)


log = logging.getLogger()


def extract_metadata(image):
    exifdata = image.getexif()

    res_dict = dict()
    for tag_id in exifdata:
        # get the tag name, instead of human unreadable tag id
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)
        # decode bytes
        if isinstance(data, bytes):
            data = data.decode()
        res_dict[tag.lower()] = data

    res_dict['datetime'] = datetime.strptime(res_dict['datetime'], TIMESTAMP_FORMAT)
    res_dict['datetime'] = res_dict['datetime'] + timedelta(seconds=DELTA_SECONDS)

    return res_dict


def transform():
    p = Path(IN_PIC_DIR)
    out_dir = Path(DEFAULT_OUT_PIC_DIR)
    out_dir.mkdir(parents=True, exist_ok=True)

    pic_lst = [x for x in p.glob(f'**/*.{IN_PIC_EXT}')]
    pic_lst.sort()
    out_lst = list()
    log.info(f'processing {len(pic_lst)} images')
    for idx, pic in enumerate(pic_lst):
        image = Image.open(pic)
        meta_dict = extract_metadata(image)

        draw = ImageDraw.Draw(image)

        date_str = datetime.strftime(meta_dict['datetime'], TIMESTAMP_FORMAT)
        font = ImageFont.truetype(str(FONT_PATH), TEXT_SIZE)

        # TODO: Change this to dinamically choose the alignment
        # Add timestamp
        text_pos = (image.size[0]/2, image.size[1] - TEXT_SIZE)
        draw.text(text_pos, date_str, (255, 255, 255), font=font, anchor="mm")
        # Resize
        im_resized = image.resize(IMAGE_SIZE)
        out_name = out_dir / f'{idx}.{IN_PIC_EXT}'
        im_resized.save(out_name)

        out_lst.append(str(out_name.resolve()))

        # Generate out file
        log.info(f'Generate out file {DEFAULT_PIC_LST_TXT}')
        str_i = ''
        for line in out_lst:
            str_i += f"file '{line}'\n"
        with open(DEFAULT_PIC_LST_TXT, 'w')as fout:
            fout.write(str_i)


def to_video():
    out_path = OUT_VID_NAME

    (
        ffmpeg
        .input(str(DEFAULT_PIC_LST_TXT), f='concat', r='20', safe=0)
        .output(out_path, vcodec=OUT_CODEC, pix_fmt=PIX_FMT_IN, framerate=FRAMERATE)
        .run()
    )


if __name__ == '__main__':
    transform()
    to_video()

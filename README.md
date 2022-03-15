# Lapser
```
Laura needed a timelaps generator thingy so I made one.
```
Converts a list of images into a video, you can also add the timestamp of each picture.


## Usage
This is the first mvp so things are going to break.<br>
You can find a base configuration in the `cfg.py` file but you can also set stuff using args

### Docker
build the image by running
```
docker build -t lapser .
```

then run a container with
```
docker run -v (your_input_images_folder):/input -v (your_desired_output_folder):/output lapser python src/lapser/main.py
```
You can set the following env vars to the container
```
IN_PIC_DIR: input pictures directory. `/input` by default.
DEFAULT_OUT_PIC_DIR: video output directory. `/output` by default.
FONT_NAME: Font to use for the legend. `hack.ttf` by default.
IN_PIC_EXT: extension of the pictures. `JPG` by default.
FRAMERATE: framerate of the video. `30` by default.
PIX_FMT_IN: Pixel format of the pictures. `yuv420p` by default.
OUT_CODEC=Video codec. `libx264` by default
OUT_VID_NAME: output video name. `movie.mp4` by default
TIMESTAMP_FORMAT: Pictures metadata Timestamp date format. `%Y:%m:%d %H:%M:%S` Env var not working atm
DELTA_SECONDS: Delta time to move adjust in seconds. Laura had the camera time wrong se we needed to move the pictures original time. `-3600` by default
TEXT_SIZE: Size of the text legend. `150` by default
IMAGE_SIZE: rezise of the original pictures (1920, 1440)
```
### Poetry
you can ran this with `poetry install` and `poetry shell` this will create a virtual env with all the necesary things.
You might need to also manually install ffmpeg
then just run
```
python lapser/main.py
```


- [x] --resize: change origin img size ex: --resize 1920x1080
- [x] --delta-timestamp: fix timestamps (camera time is wrong) ex: --delta-timestamp -10
- [x] --timestamp: add timestamp to the video
- [ ] Add click
- [ ] Add custom font?
- [ ] --timestamp-pos: define position of the timestamp
- [ ] --sound-path add sound
- [ ] --fade: adds fade in/fade out
- [ ] Create lapser class
- [ ] Create a dockerfile so Laura can use it "out of the box"


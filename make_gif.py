# OS modules
import os
import shutil

# Image modules
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw


def make_gif(text):

    # create/delete our temp files folder
    if os.path.exists('frames'):
        shutil.rmtree('frames')
    os.mkdir('frames')

    # load in the background image
    img_background = Image.open('imgs/black_bg.png')
    img = Image.new("RGBA", img_background.size, (0, 0, 0, 255))

    # set up colours and vars
    x = 10
    y = 10
    W = 500
    H = 300

    white = (255, 255, 255, 255)


    # load the font
    font_size = max(10,65-(max(0, len(text)-48)*4))
    font_size = 65
    font = ImageFont.truetype("RobotoR.ttf", font_size)
    text = text_wrap(text, font, W-50)
    text = "\n".join(text)
    draw = ImageDraw.Draw(img)

    # add text to each frame
    for N in range(0, 8):
        img.paste(img_background, (0, 0))
        if (N % 2) == 0:
            w, h = draw.textsize(text, font=font)
            draw.multiline_text(((W - w) / 2, (H - h) / 2), text, fill="white", font=font, align="center")
            #draw.text((x, y), text, white, font=font)
        img.save("./frames/{}.png".format(str(N).zfill(3)))

    # output the result
    os.system('ffmpeg -framerate 2 -i frames/%03d.png -c:v ffv1 -r 8 -y -loop -1 out.avi')
    os.system('ffmpeg -y -i out.avi out.gif')

    # clean up
    shutil.rmtree('frames')
    return "out.gif"


def text_wrap(text, font, max_width):
    """Wrap text base on specified width.
    This is to enable text of width more than the image width to be display
    nicely.
    @params:
        text: str
            text to wrap
        font: obj
            font of the text
        max_width: int
            width to split the text with
    @return
        lines: list[str]
            list of sub-strings
    """
    lines = []

    # If the text width is smaller than the image width, then no need to split
    # just add it to the line list and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        # split the line by spaces to get words
        words = text.split(' ')
        i = 0
        # append every word to a line while its width is shorter than the image width
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines
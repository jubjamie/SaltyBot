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
    font = ImageFont.truetype("/imgs/RobotoR.ttf", 65)
    draw = ImageDraw.Draw(img)

    # add text to each frame
    for N in range(0, 8):
        img.paste(img_background, (0, 0))
        if (N % 2) == 0:
            w, h = draw.textsize(text, font=font)
            draw.text(((W - w) / 2, (H - h) / 2), text, fill="white", font=font)
            #draw.text((x, y), text, white, font=font)
        img.save("./frames/{}.png".format(str(N).zfill(3)))

    # output the result
    os.system('ffmpeg -framerate 2 -i frames/%03d.png -c:v ffv1 -r 8 -y -loop -1 out.avi')
    os.system('ffmpeg -y -i out.avi out.gif')

    # clean up
    shutil.rmtree('frames')
    return "out.gif"

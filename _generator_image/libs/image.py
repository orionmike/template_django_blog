import random

from PIL import Image, ImageDraw, ImageOps, ImageFont

from .. config import *
from .. libs.color import get_random_color
from .. libs.path import create_path


def generate_random_image(file_path: str, num: int = None) -> None:

    path = Path(file_path)
    # file_name = path.name

    try:
        background_color = get_random_color(BG_START, BG_FINISH)
        border_color = get_random_color(BRD_START, BRD_FINISH)

        with Image.new('RGB', (SEGMENT_SIZE*WIDTH, SEGMENT_SIZE*HEIGHT), background_color) as img:

            # print(SEGMENT_SIZE*WIDTH, SEGMENT_SIZE*HEIGHT)

            draw_image = ImageDraw.Draw(img)
            part = random.randint(10, 20)

            for _ in range(part):

                foreground_color = get_random_color(FG_START, FG_FINISH)

                kx = random.randint(0, 6)
                ky = random.randint(0, 6)

                x1 = kx * SEGMENT_SIZE
                y1 = ky * SEGMENT_SIZE

                ksx = int(SEGMENT_SIZE/random.randint(1, 3))
                ksy = int(SEGMENT_SIZE/random.randint(1, 3))

                offset_x = random.randint(1, 3)
                offset_y = random.randint(1, 3)

                x2 = x1 + ksx * offset_x
                y2 = y1 + ksy * offset_y

                draw_image.rectangle((x1, y1, x2, y2), fill=foreground_color)
                # draw_image.ellipse((x1, y1, x2, y2), fill=foreground_color)

                # add number:

                if num:
                    font = ImageFont.truetype("calibri.ttf", SEGMENT_SIZE)
                    draw_image.text((0, 0), str(num), (80, 80, 80), font=font)

            img = ImageOps.expand(img, int(SEGMENT_SIZE/2), border_color)

            # save result image

            create_path(path.parents[0].resolve())

            # print(path.parents[0].resolve())
            # print(path)

            if path.parents[0].exists():
                img.save(path)  # img.save(path.parent / file_name)
            else:
                print(f'{IND} {Fore.RED}folder [{path.parent}] for save not found')

        # print(f"{IND} image generate: {file_name}")

    except Exception as e:
        error = f'generate_random_image -> error: {e}'
        print(error)
        logger.error(error)

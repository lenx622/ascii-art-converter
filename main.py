import os
import sys
import re
from datetime import datetime
from PIL import Image

IMAGES_PATH = "./images"
DOWNLOADS_PATH = "./downloads"
ASCII_CHARS = "@%#*+=-:. "


def main() -> None:
    image_filename = sys.argv[1]
    ascii_art = generate_ascii_art(f"{IMAGES_PATH}/{image_filename}")
    file_path = create_text_file(ascii_art, image_filename)
    print("ASCII art saved to", file_path)

    return


def generate_ascii_art(image_path: str) -> str:
    try:
        image = Image.open(image_path).convert("L")
    except FileNotFoundError:
        print("The file does not exist.")
        exit(1)

    width, height = image.size

    ascii_art = ""
    for y in range(height):
        for x in range(width):
            brightness = 255 - image.getpixel((x, y))

            char_index = int(brightness / 256 * len(ASCII_CHARS))
            ascii_char = ASCII_CHARS[char_index]

            ascii_art += ascii_char

        ascii_art += "\n"

    return ascii_art


def create_text_file(text: str, filename: str) -> None:
    os.makedirs(DOWNLOADS_PATH, exist_ok=True)

    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y%m%d%H%M%S")
    formatted_filename = re.sub(r"\.[^.]*$", "", filename)
    file_path = f"{DOWNLOADS_PATH}/{formatted_filename}_{formatted_time}.txt"

    with open(file_path, "w") as file:
        file.write(text)

    return file_path


if __name__ == '__main__':
    main()

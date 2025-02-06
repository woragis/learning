from PIL import Image, ImageFilter


def main():
    image_name = input('What\'s the image name? ')
    with Image.open(image_name) as img:
        print(img.size)
        print(img.format)
        img = img.rotate(180)
        img = img.filter(ImageFilter.FIND_EDGES)
        img = img.filter(ImageFilter.BLUR)
        img.save(f'new_{image_name}')


if __name__ == '__main__':
    main()

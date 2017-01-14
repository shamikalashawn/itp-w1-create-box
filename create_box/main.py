"""This is the entry point of the program."""


def create_box(height, width, character):
    if height >= 1 and width >=1:
        box = ''
        for row in range(height):
            box = box + (character * width) + '\n'
    print (box)
    return box


if __name__ == '__main__':
    create_box(3, 4, '*')

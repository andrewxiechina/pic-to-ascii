from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')     #输入文件
parser.add_argument('-o', '--output')   #输出文件
parser.add_argument('--width', type = int, default = 80) #输出字符画宽
parser.add_argument('--height', type = int, default = 80) #输出字符画高

#获取参数
args = parser.parse_args()

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

path = args.file
width = args.width
height = args.height
output = args.output

def get_char(r, g, b, alpha=256):
    if alpha == 0:
        return ' '

    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

    unit = (256.0 + 1) / len(ascii_char)
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':
    img = Image.open(path)
    img = img.resize((width, height), Image.NEAREST)

    txt = ""

    for i in range(height):
        for j in range(width):
            txt += get_char(*img.getpixel((j,i)))
        txt += '\n'


    if output is None:
        output = "output.txt"

    with open(output, 'w') as f:
        f.write(txt)

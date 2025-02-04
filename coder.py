import random
from PIL import Image, ImageDraw
from re import findall

def stega_encrypt():
    '''USE ASCII SYMBOLS ONLY'''
    keys = []
    img = Image.open(input("path to image: "))
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    f = open('keys.txt','w')

    for el in ([ord(el) for el in input('Put your txt here: ')]):
        key = (random.randint(1, width-10), random.randint(1, height-10))
        r,g = pix[key][0:2]
        print(pix[key])
        draw.point(key, (r, g, el))
        f.write(str(key) + '\n')
    print('succesfully writen keys to keys.txt!')
    img.save("newimage.png", "PNG")
    f.close()

def stega_decrypt():
    a = []
    keys = []
    img = Image.open(input("path to image: "))
    pix = img.load()
    f = open(input('path to keys: '),'r')
    y = str([line.strip() for line in f])

    for i in range(len(findall(r'\((\d+)\,', y))):
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
    for key in keys:
        a.append(pix[tuple(key)][2])
    return ''.join([chr(elem) for elem in a])

if str(input('enter operation (encrypt/decrypt): ')) == 'encrypt':
    stega_encrypt()
else:
    print('Your message: ', stega_decrypt())
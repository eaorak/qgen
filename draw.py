#!/usr/local/bin/python3
import getopt
import sys
from PIL import Image, ImageDraw, ImageFont
import textwrap

# quote = "Out beyond the ideas of right and wrong, there is a field. \n\nI'll meet you there.\n\n-Rumi"
font = '~/Library/Fonts/Museo500-Regular.otf'
fontSize = 80


def wrapper(text, width=22):
    all = []
    for line in text.splitlines():
        all.append(textwrap.fill(line, width=width))
    return '\n'.join(all)


def createQuote(quote, template='t1', output='quote.png'):
    quote = quote.replace('#', '\n')
    img = Image.open('templates/{}.png'.format(template)).convert('RGB')

    wrapped = wrapper(quote)

    fnt = ImageFont.truetype(font, fontSize)
    d = ImageDraw.Draw(img)
    d.text((130, 180), wrapped, font=fnt, fill=(255, 255, 255))

    img.save(output)


def exitWithHelp(text, exit=0):
    print(text)
    sys.exit(exit)


def main(argv):
    template = 't1'
    output = 'quote.png'
    quote = None
    usageText = '{} -t <template> -o <output> -q <quote>'.format(argv[0])
    try:
        opts, _ = getopt.getopt(argv[1:], "ht:o:q:")
    except Exception:
        exitWithHelp(usageText, exit=-1)

    for opt, arg in opts:
        if opt == '-h':
            exitWithHelp(usageText)
        elif opt == "-t":
            template = arg
        elif opt == "-o":
            output = arg
        elif opt == "-q":
            quote = arg

    if quote is None:
        exitWithHelp(usageText)
    print('Creating "{}" using template "{}"...'.format(output, template))
    createQuote(quote, template, output)
    print('')


if __name__ == "__main__":
    main(sys.argv)

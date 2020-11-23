from PIL import Image
import os
import argparse

extensions = ('png','jpg','bmp','gif','ico')

parser = argparse.ArgumentParser(description="This program covnerts image files to various formats")
parser.add_argument('fname',help='Name of file that contains image, It will find the image with no given extension if in curret directory is only one file with input name')
parser.add_argument('outName', nargs='?', default=False, help="File Name used to save converted image, if not given same as source file")
parser.add_argument('-f','--format', required=True, choices=extensions, help='Image extension in what you want to convert current Image')
parser.add_argument('-r','--resize', type=float, help='Resizes Image with given ratio')
args = parser.parse_args()
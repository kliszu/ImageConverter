from PIL import Image
import os
import argparse

global extensions
extensions = ('png','jpg','bmp','gif','ico')

def check_dir(fileName):
    if os.path.exists(fileName):
        return True
    else:
        return False

def get_imgdir(fileName):
    if check_dir(fileName):
        return fileName
    else:
        itemList = []
        for item in os.listdir():
            ex = item.split(".")
            if len(ex) == 2 and ex[0] == fileName and ex[1] in extensions:
                itemList.append(item)
        if len(itemList) != 1:
            return False
        else:
            return itemList[0]
            
parser = argparse.ArgumentParser(description="This program covnerts image files to various formats")
parser.add_argument('fname',help='Name of file that contains image, It will find the image with no given extension if in curret directory is only one file with input name')
parser.add_argument('outName', nargs='?', default=False, help="File Name used to save converted image, if not given same as source file")
parser.add_argument('-f','--format', required=True, choices=extensions, help='Image extension in what you want to convert current Image')
parser.add_argument('-r','--resize', type=float, help='Resizes Image with given ratio')
args = parser.parse_args()

iName = get_imgdir(args.fname)
if iName == False:
    print("Too many matched items or its not exists in current directory, please if not specify file extension or try again")
    raise SystemExit
image = Image.open(get_imgdir(iName))
if image.format != 'RGB' and args.format == 'jpg':
    image = image.convert('RGB')
if args.resize:
    dim = (int(image.size[0]*args.resize), int(image.size[1]*args.resize))
    image = image.resize(dim)
    image.show()
if args.outName == False:
    iName = iName.split(".")
    outName = iName[0] + "." +args.format
    image.save(outName)
else:
    outName = args.outName.split(".")
    outName = outName[0] +"."+ args.format
    image.save(outName)    
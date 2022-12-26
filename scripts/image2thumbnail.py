#!/bin/python
#%%
from PIL import Image
from glob import glob

def make_thumbnail(inFilename: str, outFilename: str):
    img = Image.open(inFilename)
    img.thumbnail([500, 500], Image.ANTIALIAS)
    img.save(outFilename)
    return

in_file_path = "images/f2/*"
out_file_path = "images/t2"

for img in glob(in_file_path):
    basename = img.split("/")[-1]#.split(".")[0]
    # print(f"starting: {basename}")
    out_name = out_file_path + basename
    # make_thumbnail(img, out_name)
    img = Image.open(img)
    img.thumbnail([500, 500], Image.ANTIALIAS)
    img.save(out_name)
#%%


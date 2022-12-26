
# %%
import sys
import cv2
import numpy as np

# dir = sys.path[0]
# path_to_file = "../icon_ideas/octopus-icon-logo-vector-illustration-design-template_598213-1260-removebg-preview.png"
path_to_file = "../icon_ideas/octopus-icon-logo-vector-illustration-design-template_598213-1260.jpeg"
# im = cv2.imread(dir+'/im.png', -1)
im = cv2.imread(path_to_file, -1)
# im[np.where(im[:, :, 3] == 0)] = (0, 0, 0, 255) # Testcase.
im[np.where(im[:, :, 3] != 0)] = (0, 0, 0, 255) # Fill anywhere not fully transparent.
# im[np.where(im[:, :, 3] != 0|255)] = (0, 0, 0, 255) # Fill in anywhere that is transparent or has alpha.
cv2.imwrite('../icon_ideas/000_im_.png', im)


# %%
from PIL import Image

in_path = "../icon_ideas/octopus-icon-vector-33558706.png"
out_path = "../icon_ideas/000_img2.png"

img = Image.open(in_path)
img = img.convert("RGBA")

imgnp = np.array(img)

white = np.sum(imgnp[:,:,:3], axis=2)
white_mask = np.where(white == 255*3, 1, 0)

alpha = np.where(white_mask, 0, imgnp[:,:,-1])

imgnp[:,:,-1] = alpha 

img = Image.fromarray(np.uint8(imgnp))
img.save(out_path, "PNG")

# %%

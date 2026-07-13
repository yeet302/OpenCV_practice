import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

def download_and_unzip(url, save_path):
    print(f"Downloading and extracting assests....", end="")

    # Downloading zip file using urllib package.
    urlretrieve(url, save_path)

    try:
        # Extracting zip file using the zipfile package.
        with ZipFile(save_path) as z:
            # Extract ZIP file contents in the same directory.
            z.extractall(os.path.split(save_path)[0])

        print("Done")

    except Exception as e:
        print("\nInvalid file.", e)

URL = r"https://www.dropbox.com/s/rys6f1vprily2bg/opencv_bootcamp_assets_NB2.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB2.zip")

# Download if assest ZIP does not exists. 
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)   

os.makedirs("output", exist_ok=True)

#Origianl checkerboard image
# Read image as gray scale.
cb_img = cv2.imread("checkerboard_18x18.png", 0)

# Set color map to gray scale for proper rendering.
#plt.imshow(cb_img, cmap="gray")
#print(cb_img)

#Accessing individual pixels
# print the first pixel of the first black box
#print(cb_img[0, 0])
# print the first white pixel to the right of the first black box
#print(cb_img[0, 6])

'''
#modifying image pixels
cb_img_copy = cb_img.copy()
cb_img_copy[2, 2] = 200
cb_img_copy[2, 3] = 200
cb_img_copy[3, 2] = 200
cb_img_copy[3, 3] = 200

# Same as above
# cb_img_copy[2:3,2:3] = 200

print(cb_img_copy)
'''

#Cropping images
#저장될시에는 BGR순으로 저장됨
img_NZ_bgr = cv2.imread("New_Zealand_Boat.jpg",1)
img_NZ_rev = img_NZ_bgr[:,:,::-1]

#imread은 bgr로 주고 imwrite으로 복구될때에는 bgr로 받아 결과는 rgb가된다.
cv2.imwrite("output/img_NZ_rev.png", img_NZ_rev) 

#Crop out the middle region of the image
cropped_region = img_NZ_bgr[200:400, 300:600]
cv2.imwrite("output/img_NZ_cropped.png", cropped_region)

#Resizing images
#dsize지정하면 fx,fy가 계산되지만 fx,fy지정하면 dsize를 None으로두어도 괜찮다
resized_cropped_region_2x = cv2.resize(cropped_region,None, fx=2, fy=2)
cv2.imwrite("output/resized_cropped_region.png", resized_cropped_region_2x)

#Specifying the exact size of the output image
desired_width = 100
desired_height = 200
dim = (desired_width, desired_height)
resized_cropped_region_2x_2 = cv2.resize(cropped_region,dim,interpolation=cv2.INTER_AREA)
cv2.imwrite("output/resized_cropped_region2.png", resized_cropped_region_2x_2)

#Resizing while maintaining aspect ratio
# Method 2: Using 'dsize'
desired_width = 100
aspect_ratio = desired_width / cropped_region.shape[1]
desired_height = int(cropped_region.shape[0] * aspect_ratio)
dim = (desired_width, desired_height)

# Resize image
resized_cropped_region = cv2.resize(cropped_region, dsize=dim, interpolation=cv2.INTER_AREA)
cv2.imwrite("output/resized_maintain_ratio.png", resized_cropped_region)

#flip images
img_NZ_rgb_flipped_horz = cv2.flip(img_NZ_rev, 1)
img_NZ_rgb_flipped_vert = cv2.flip(img_NZ_rev, 0)
img_NZ_rgb_flipped_both = cv2.flip(img_NZ_rev, -1)

# Show the images
plt.figure(figsize=(18, 5))
plt.subplot(141);plt.imshow(img_NZ_rgb_flipped_horz);plt.title("Horizontal Flip");
plt.subplot(142);plt.imshow(img_NZ_rgb_flipped_vert);plt.title("Vertical Flip");
plt.subplot(143);plt.imshow(img_NZ_rgb_flipped_both);plt.title("Both Flipped");
plt.subplot(144);plt.imshow(img_NZ_rev);plt.title("Original");

plt.savefig("output/flipped_comparison.png")
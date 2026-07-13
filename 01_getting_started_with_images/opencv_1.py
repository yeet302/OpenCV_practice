import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import Image

def download_and_unzip(url, save_path):
    print("Downloading and extracting assets....", end="")

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

URL = r"https://www.dropbox.com/s/qhhlqcica1nvtaw/opencv_bootcamp_assets_NB1.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB1.zip")


# Download if assest ZIP does not exists. 
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)   


# outputs 디렉터리 만들기
os.makedirs("outputs", exist_ok=True)

# Read image as gray scale.
cb_img = cv2.imread("checkerboard_18x18.png", 0)

# Print the image data (pixel values), element of a 2D numpy array.
# Each pixel value is 8-bits [0,255]

# print(cb_img)

'''
plt.imshow(cb_img, cmap="gray")
output = "outputs/checkerboard_result_gray.png"
plt.savefig(output)
plt.close
print(output)
'''

'''
cb_img_fuzzy = cv2.imread("checkerboard_fuzzy_18x18.jpg", 0)
plt.imshow(cb_img_fuzzy, cmap="gray")
output = "outputs/checkerboard_18x18_gray.png"
plt.savefig(output)
plt.close
print(cb_img_fuzzy)
print(output)
'''

#coke_img = cv2.imread("coca-cola-logo.png", 1)

#print the size of image
#print("Image size (H, W, C) is:", coke_img.shape)

# print data-type of image
#print("Data type of image is:", coke_img.dtype)

#plt.imshow(coke_img)
#plt.savefig("outputs/coca-cola_color_result.png")

#coke_img_channels_reversed = coke_img[:,:,::-1]
#plt.imshow(coke_img_channels_reversed)
#plt.savefig("outputs/coca-cola_img_channels_reversed.png")



#Splitting and merging color channels

'''
#split channels into B,G,R components
img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", 1)
b, g, r = cv2.split(img_NZ_bgr)

#show the channels
#가로20인치, 세로 5인치의 전체 도화지를 만들고 
plt.figure(figsize=[20,5])

#도화지 안에 4등분해서 141: row 1개, column 4개, 그중 첫번째(141)
plt.subplot(141);plt.imshow(r, cmap="gray");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="gray");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="gray");plt.title("Blue Channel")

"""
plt.subplot(141);plt.imshow(r, cmap="Reds");plt.title("Red Channel")
plt.subplot(142);plt.imshow(g, cmap="Greens");plt.title("Green Channel")
plt.subplot(143);plt.imshow(b, cmap="Blues");plt.title("Blue Channel")
"""

#merge individual channels into a BGR image
imgMerged = cv2.merge((b,g,r))

#show the merged output
plt.subplot(144)
plt.imshow(imgMerged[:,:,::-1]) 
plt.title("Merged Output")
plt.savefig("outputs/channels_split_merged.png")
plt.close()
'''

'''
img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", 1)

cv2.imwrite("outputs/New_Zealand_Lake_SAVED.png", img_NZ_bgr)
#Image(filename="/outputs/New_Zealand_Lake_SAVED.png")
'''

#Converting to different color spaces by using cv2.cvtcolor()

img_NZ_bgr = cv2.imread("New_Zealand_Lake.jpg", 1)

#Changing from BGR to RGB
# OpenCV stores color channels in a differnet order than most other applications (BGR vs RGB).
img_NZ_rgb = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2RGB)
plt.imshow(img_NZ_rgb)
plt.savefig("outputs/img_nz_rgb")
plt.close()

#Changing to HSV color space
img_hsv = cv2.cvtColor(img_NZ_bgr, cv2.COLOR_BGR2HSV)

# Split the image into the B,G,R components
h,s,v = cv2.split(img_hsv)

# Show the channels
plt.figure(figsize=[20,5])
plt.subplot(141);plt.imshow(h, cmap="gray");plt.title("H Channel");
plt.subplot(142);plt.imshow(s, cmap="gray");plt.title("S Channel");
plt.subplot(143);plt.imshow(v, cmap="gray");plt.title("V Channel");
plt.subplot(144);plt.imshow(img_NZ_rgb);   plt.title("Original");
plt.savefig("outputs/nz_hsv_channels")
plt.close()
# Import libraries
import os
import cv2
import matplotlib
import numpy as np
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

matplotlib.rcParams['figure.figsize'] = (9.0, 9.0)

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

URL = r"https://www.dropbox.com/s/48hboi1m4crv1tl/opencv_bootcamp_assets_NB3.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB3.zip")

# Download if assest ZIP does not exists. 
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)   

#
os.makedirs("output", exist_ok=True)

# Read in an image
image = cv2.imread("Apollo_11_Launch.jpg", cv2.IMREAD_COLOR)

# Display the original image
# plt.imshow(image[:, :, ::-1])

#drawing a line
#make a copy of the original rocket photo
  
imageLine = cv2.line(image, (200,100), (400,100),(0,255,255), thickness=5, lineType=cv2.LINE_AA)
cv2.imwrite("output/imageLine.png", imageLine)

#drawing a circle
#전에 수정한 이미지 배열을 그대로 사용하여 직선 그린것이 남아있음 .copy() 사용하면됨.
imageCircle = cv2.circle(image, (900, 500), 100, (0, 0, 255), thickness=-1, lineType=cv2.LINE_4)
cv2.imwrite("output/imageCircle.png", imageCircle)

#drawing a rectangle
imageRectangle = cv2.rectangle(image, (500,100), (700, 600), (255,0,255), thickness = cv2.FILLED, lineType = cv2.LINE_8)
cv2.imwrite("output/imageRectangle.png", imageRectangle)

text = "Apollo 11 Saturn V Launch, July 16, 1969"
#point
fontFace = cv2.FONT_HERSHEY_PLAIN #int
fontScale = 2.3 #double
fontColor = (0,255,0)
fontThickness = 2 #int
#int lineType
#bool bottomLeftOrigin

imgwtxt1 = cv2.putText(image, text, (200,700), fontFace, fontScale, fontColor, fontThickness, cv2.LINE_AA)
imgwtxt2 = cv2.putText(image, "WE ARE GOING TO THE MOON!", (250,200), cv2.FONT_HERSHEY_PLAIN, 1.5, (147,255,38), 2, cv2.LINE_AA)
cv2.imwrite("output/imgwtxt1.png", imgwtxt1)
cv2.imwrite("output/imgwtxt2.png", imgwtxt2)

# import the library
import os
import cv2
import matplotlib.pyplot as plt

from zipfile import ZipFile
from urllib.request import urlretrieve

from IPython.display import YouTubeVideo, display, HTML
from base64 import b64encode

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

URL = r"https://www.dropbox.com/s/p8h7ckeo2dn1jtz/opencv_bootcamp_assets_NB6.zip?dl=1"

asset_zip_path = os.path.join(os.getcwd(), f"opencv_bootcamp_assets_NB6.zip")

# Download if assest ZIP does not exists. 
if not os.path.exists(asset_zip_path):
    download_and_unzip(URL, asset_zip_path)   

os.makedirs("output", exist_ok=True)

#read video from source
source = "race_car.mp4"
cap = cv2.VideoCapture(source)

if not cap.isOpened():
    print("Error opening video stream or file")
    exit()


#read and display one frame
ret, frame = cap.read()
if ret:
    cv2.imwrite("output/first_frame.jpg", frame)
cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

#display the video file
video = YouTubeVideo("RwxVEjv78LQ", width=700, height=438)
display(video)

#write video using opencv
#default resolutions of the frame are obtained
#convert the resolutions from float to integer
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out_avi = cv2.VideoWriter("output/race_car_out.avi", cv2.VideoWriter_fourcc("M", "J", "P", "G"), 10, (frame_width,frame_height)) # or (*"MJPG")
out_mp4 = cv2.VideoWriter("output/race_car_out.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 10, (frame_width,frame_height)) # or ()"X","V","I","D")

#Read frames and write to file
#read until video is completed
while cap.isOpened():
    #capture frame-by-frame
    ret, frame = cap.read() #ret holds True/False depending on which 

    if ret:
        #write the frame to the output files
        out_avi.write(frame)
        out_mp4.write(frame)
    
    #break the loop
    else:
        break

cap.release()
out_avi.release()
out_mp4.release()

print("Done")
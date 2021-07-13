# CannyEdgeDetection

Short program for converting images into line art with OpenCV "Canny Edge Detection"

Note: This hasn't been tested on Windows or MacOS, only Ubuntu. 

![image](https://user-images.githubusercontent.com/62955316/125382042-90277980-e35a-11eb-9dbf-cf7140a57ff2.png)
![image](https://user-images.githubusercontent.com/62955316/125383599-42f8d700-e35d-11eb-88d1-da22cd50aa87.png)

# Setup

Copy these commands into your Terminal.

## Update
```
sudo apt update
```

## Clone
```
git clone https://github.com/TrunkMonkey5850/CannyEdgeDetection.git
cd CannyEdgeDetection
```

## Prepare File

Make sure your file is in the ".png" format, as conversion has not yet been added.

Copy your input file into the "CannyEdgeDetection" folder, and rename it "detect.png"

# Usage

To run, make sure you're inside of the "CannyEdgeDetection" folder, and type:
```
python3 cannyedge.py
```

After the detected image is generated, it will be shown in a window that will remain onscreen until a key is pressed.
The output image will also be saved in the "CannyEdgeDetection" folder.

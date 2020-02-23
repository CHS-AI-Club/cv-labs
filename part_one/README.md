# CV-Labs Part One

This lab will get you exposed to dealing with images. You will learn how to read, modify, and save images using the primary image processing library that we will be using: [OpenCV](https://opencv.org/). 

## Getting started

Folow the procedures below to get the lab done.

### Prerequisites

* Basic programming skills with Python
* Python is properly installed and the PATH is defined.
* Installed OpenCV using PIP on the command line:
 
  `pip3 install opencv-python`
  
### Setup

1. Git clone or download the repository:
   * `git clone https://github.com/CHS-AI-Club/cv-labs.git`
   * OR download the zip file and manually extract it

2. Open up '/cv-labs/part_one' directory with your favorite editor or file explorer
3. Execute the `setup.py` file using the python interpreter

### Instructions
This lab will be done inside `part_one.py` file. I have set up this file with a main method to make it easier for those with java background from AP CS.

In this lab, we will take randomly downloaded images from the internet and process it. We will perform [Canny Edge Detection](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_canny/py_canny.html) on these images through code and save the results on a separate directory. You can think of this as extracting the features from the images so that it may be better for a machine learning algorithm to learn from.

Example of Canny edge detection: <br>
  ![Before and After](https://opencv-python-tutroals.readthedocs.io/en/latest/_images/canny1.jpg).

Follow these sets of steps below and write the code under `def main()`. Remember to always Google and search documentation first before asking for help.

1. Make a for loop that goes through the downloaded image under `input_images/` directory using `os.listdir`.
2. Under the for loop make a variable that stores the full path of the image file using `os.path.join`.
3. Read the image file and store it a variable using `cv2.imread` function.
4. Apply the canny filter on the image through the use of  `cv2.Canny` function.
5. Save the image in the `output_images/` directory using `cv2.imwrite`.
6. All the code above should be inside the for loop specified in step 1. Execute the code after finished.
7. Check the `output_images/` directory for the results.

If you want to learn how I got the random images, I just made simple get requests to an URL called [Lorem Picsum](https://picsum.photos/) and stored the returned images under `input_images/` directory. The code for that is stored in `setup.py` under the `download` function.

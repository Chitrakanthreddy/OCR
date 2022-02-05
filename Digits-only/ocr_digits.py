# import necessary packages
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the argumens
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the input image to be OCR'd")
ap.add_argument("-d", "--digits", type=int, default=1, help="whether or not *digits only* OCR will be performed")
args = vars(ap.parse_args())

# load the input image and convert it from BGR to RGB channel ordering,
# and initialize our Tesseract OCR options as an empty string
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

# check to see if *digit only* OCR should be performed, and if so,
# update our Tesseract OCR options
if args["digits"] > 0:
    options = "outputbase digits"

# use Tesseract to OCR the image
text = pytesseract.image_to_string(rgb, config=options)
print(text)

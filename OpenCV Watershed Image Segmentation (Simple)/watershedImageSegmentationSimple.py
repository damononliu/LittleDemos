import cv2.cv as cv

# Demonstrates how to use OpenCV's Watershed function to segment an image
#
# Written by lassytouton
#
# Works with OpenCV 2.3.1

cv.NamedWindow("imgOriginal", 1);

cv.NamedWindow("imgMarkers", 1);

cv.NamedWindow("imgWatershed", 1);

imgOriginal = cv.LoadImage("TouchingCircles.png");

imgMarkers = cv.CreateImage(cv.GetSize(imgOriginal), cv.IPL_DEPTH_8U, 1)

imgWatershed = cv.CreateImage(cv.GetSize(imgOriginal), cv.IPL_DEPTH_32S, 1)

cv.Zero(imgMarkers)

cv.Zero(imgWatershed)

# create markers for the background, upper circle, and lower circle
# markers are differentiated by colour

# background marker, identified by colour (80, 80, 80)
cv.Circle(imgMarkers, (60, 60), 3, (80, 80, 80), -1)

# upper circle marker, identified by colour (160, 160, 160)
cv.Circle(imgMarkers, (180, 180), 3, (160, 160, 160), -1)

# lower circle marker, identified by colour (240, 240, 240)
cv.Circle(imgMarkers, (320, 320), 3, (240, 240, 240), -1)

# seed imgWatershed with the markers for the background, upper circle, and lower circle
cv.ConvertScale(imgMarkers, imgWatershed, 1)

# this is where the magic happens...
cv.Watershed(imgOriginal, imgWatershed)

cv.ShowImage("imgOriginal", imgOriginal)

cv.ShowImage("imgMarkers", imgMarkers)

# cv.IPL_DEPTH_32S images are divided by 256 on display so scale accordingly
cv.ConvertScale(imgWatershed, imgWatershed, 256)

cv.ShowImage("imgWatershed", imgWatershed)

Esc = 27

while True:
    keyPressed = cv.WaitKey(0) % 0x100
    if ((keyPressed == Esc) or (keyPressed == ord('q'))):
        break

cv.DestroyAllWindows()

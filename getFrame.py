import cv2

#will need to run this first in order to generate the appr 393 jpg files that will be compared to a base image
vidcap = cv2.VideoCapture('Test.mp4')

success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

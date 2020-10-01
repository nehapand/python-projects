import cv2

vidcap = cv2.VideoCapture("C:\\internship\\Roof side inner(RH)Side\\OLD.mp4")
success, image = vidcap.read()
count = 1
print("test")
while success:
  cv2.imwrite("C:\\internship\\Roof side inner(RH)Side\\frames\\frame_%d.jpg" % count, image)     # save frame as JPEG file
  success, image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
import cv2

def mp4_frames(mp4_file,output_dir):
  vidcap = cv2.VideoCapture(mp4_file)
  success,image = vidcap.read()
  count = 0
  success = True
  while success:
    success,image = vidcap.read()
    print(output_dir+"/frame%d.png" % count)
    if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break 
    count += 1

'''
vidcap = cv2.VideoCapture('test_03/Test3.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
#while count<1000:
  success,image = vidcap.read()
  cv2.imwrite("vid03_frames/vid03_frame%d.png" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
'''

 
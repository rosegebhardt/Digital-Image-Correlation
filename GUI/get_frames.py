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
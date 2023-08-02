import os
import cv2
import time

import moviepy.editor as mpe

 
# images to video
def picvideo(path,size):
    path = "C:\\code\\content\\images\\" #images path
    filelist = os.listdir(path) # get the names of all the files
 
    '''
    fps:
    Frame rate: 1 frame has n pictures written [control a picture to place 5 pictures, 
    that is frame 1, repeat playing this picture 5 times]
    If there are 50 pictures of 534*300 in the folder, 
    set 1 to play 5 pictures here, then the duration of this video is 10 seconds
    '''
    fps = 0.2
    size = (760,1280) #image resolution
    file_path = "c:\\code\\content\\videos\\" + str(time.strftime("%Y-%m-%d")) + ".mp4" #export path
    # Different video encodings correspond to different video formats (for example: 'I', '4', '2', '0' correspond to avi format)
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
 
    video = cv2.VideoWriter( file_path, fourcc, fps, size )
 
    for item in filelist:
        if item.endswith('.png'):   #Determine whether the image suffix is ​​.png
            item = path + '/' + item 
            img = cv2.imread(item)  #Use opencv to read the image and directly return the numpy.ndarray object, the channel order is BGR, note that it is BGR, and the channel value default range is 0-255.
            video.write(img)        #write pictures to video
 
    video.release() # release video
 
picvideo('./',(760,1280))
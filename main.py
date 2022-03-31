import os, cv2

def listdirs(rootdir):
    vidcount = 0
    durationinsecs = 0
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            [x, y] = listdirs(d)
            vidcount += x
            durationinsecs += y
        else:
            if os.path.splitext(d)[-1] in ['.mp4', '.avi']:
                #name of video
                # print(d)
                
                cap = cv2.VideoCapture(d)
                fps = cap.get(cv2.CAP_PROP_FPS)      # OpenCV2 version 2 used "CV_CAP_PROP_FPS"
                frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                this_video_duration = frame_count/fps
                
                durationinsecs += this_video_duration
                vidcount+=1

                cap.release()
    return [vidcount, durationinsecs]

 
rootdir = 'C:\\Users\\Niloy\\Downloads\\Drawing Tutorials\\Digital Painting\\Painting With Confidence – COURSE by Anthony Jones'
[vc, dur] = listdirs(rootdir)
print("Number of videos : "+ str(vc))
print("Duration: "+ str(int(dur/3600))+" hrs, "+str(int((dur%3600)/60)) +" mins, "+ str(int(dur%60)) +" secs")
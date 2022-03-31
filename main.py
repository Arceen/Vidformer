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
                fps = cap.get(cv2.CAP_PROP_FPS)
                frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                this_video_duration = frame_count/fps
                
                durationinsecs += this_video_duration
                vidcount+=1

                cap.release()
    print("Folder Name: ", rootdir)
    print("Video Count: ", str(vidcount))
    print("Duration: "+ str(int(durationinsecs/3600))+" hrs, "+str(int((durationinsecs%3600)/60)) +" mins, "+ str(int(durationinsecs%60)) +" secs")
    return [vidcount, durationinsecs]

 
rootdir = 'C:\\Users\\Niloy\\Downloads\\Drawing Tutorials\\Color, Light, Shadow & Shading\\CGMA The art of colour and light with Marco Bucci'
[vc, dur] = listdirs(rootdir)
print("Number of videos : "+ str(vc))
print("Duration: "+ str(int(dur/3600))+" hrs, "+str(int((dur%3600)/60)) +" mins, "+ str(int(dur%60)) +" secs")

# Output
# Number of videos : 38
# Duration: 5 hrs, 36 mins, 14 secs

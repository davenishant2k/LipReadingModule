for i in range(0,20):
    #take inputs
    print("Start time: ")
    start = int(input())
    print("End time: ")
    end = int(input())
    text = input("Text : ")

    #trim video
    from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
    ffmpeg_extract_subclip("video1.mp4", start, end, targetname=str(i)+".mp4")

    #create file
    f=open(str(i)+".txt",'w')
    f.write(text)
    f.close()
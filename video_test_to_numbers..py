import cv2
import numpy as np
from skvideo import io
import subprocess

def create_video(path):
        writer = io.FFmpegWriter("output_video.avi", outputdict={
        '-vcodec': 'libx264',
        '-crf': '0', 
        '-preset':'veryslow'
        })

        cap = cv2.VideoCapture(path)
        func = np.vectorize(lambda x: round(x,1))

        while True:
                ret, frame = cap.read()
                if not ret:
                        break

                img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                img = cv2.resize(img, (480, 270))
                arr = np.asarray(img)/255.0
                arr = func(arr)

                elements = set(tuple(list(arr.flatten())))

                range_colors = np.linspace(0,255,len(elements))
                data = dict(zip(elements,range_colors))


                for i in range(270):
                        for j in range(480):
                                value = arr[i][j]
                                img[i][j] = data[value]

                #img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
                cv2.imshow('frame',img)

                writer.writeFrame(img)

                if cv2.waitKey(1) == ord('q'):
                        break

        cap.release()
        writer.close()
        cv2.destroyAllWindows()

def generate_video(path_video, path_audio):
        videofile = path_video
        audiofile = path_audio
        outputfile = "output.mp4"
        codec = "copy"

        subprocess.run(f"ffmpeg -i {videofile} -i {audiofile} -c {codec} {outputfile}")

create_video('BEASTARS.mp4')
#generate_video('output_video.avi','audio_video.mp3')
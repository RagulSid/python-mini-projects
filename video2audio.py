import moviepy.editor
from tkinter.filedialog import *

video = askopenfilename()
video = moviepy.editor.VideoFileClip(video)
audio = video.audio

audio.write_audiofile("result.mp3")
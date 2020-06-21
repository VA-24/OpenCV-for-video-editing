from moviepy.editor import *

clip = VideoFileClip('Test.mp4')

#here, just insert the results that frameCompare gives you. In this case, I cut between 2.55 and 5.2 seconds because before and after that are OBS screens.
#If you want to cut between minutes, the notation for that is (minutes, seconds), such as (5:33) would be (5,33)
clip1 = clip.subclip((2.55),(5.2))

clip1.write_videofile('render.mp4', codec='libx264')

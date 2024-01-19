from pygame import mixer
mixer.init()
mixer.music.load("believer.mp3")
mixer.music.set_volume(0.8)
mixer.music.play()

# infinite loop
while true:

print("Press 'p' to pause, 'r' to resume")
print("Press 'e' to exit program")
query = input(" ")

if query == 'p':

# Pause music
mixer.music.pause()
elif query == 'r':

# Restore music
mixer.music.unpause()
elif query == 'e':

# Stop the blender
mixer.music.stop()
break

from pygame import mixer
mixer.init()
mixer.music.load("believer.mp3")
mixer.music.set_volume(0.8)
mixer.music.play()

# infinite loop
while True:
	
	print("Press 'p' to pause, 'r' to resume")
	print("Press 'e' to exit the program")
	query = input(" ")
	
	if query == 'p':

		# Pausing the music
		mixer.music.pause()	
	elif query == 'r':

		# Resuming the music
		mixer.music.unpause()
	elif query == 'e':

		# Stop the mixer
		mixer.music.stop()
		break

import pywhatkit as pyw

def play_song_on_youtube():
    Try:
        # Prompt user for song name
        video_name = input("Enter song/video name: ")

        if video_name:
            # Play the song on YouTube
            pyw.playonyt(video_name)
            print(f"Now playing: {video_name}")
        other:
            print("Please enter a valid song name.")
    except for an exception like e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    play_song_on_youtube()

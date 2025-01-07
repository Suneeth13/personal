
import pyshorteners

url = input("Enter the URL: ")
short = pyshorteners.Shortener()
short_url = short.tinyurl.short(url)
print("Shortened URL: ", short_url)


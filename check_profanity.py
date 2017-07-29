
import urllib

def read_text():
	quotes = open(r"/media/ayush/APPLICATIONS/python/Udacity Python/movie_quotes.txt")
	content_of_file = quotes.read()
	quotes.close()
	check_profanity(content_of_file)

def check_profanity(text_to_check):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
	output = connection.read()
	connection.close()
	if "true" in output:
		print("Profanity alert!!!")
	elif "false" in output:
		print("No Profanity word found.")
	else :
		print("Not able to read file")


read_text()

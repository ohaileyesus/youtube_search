from flask import Flask, request
from twilio.rest import TwilioRestClient
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey= "[ENTER API KEY]")

client = TwilioRestClient("[ACCOUNT_SID]", "[AUTH_TOKEN]")

app = Flask(__name__)

@app.route("/")
def test():
	first_num = request.values.get('From')
	msg_body = request.values.get('Body')

	#checks if a recepient number is specified
	if '+' in msg_body:
		song = msg_body.split('+')[0]
		recepient = msg_body.split('+')[1]

		client.messages.create(
		to = '+' + recepient,
		from_= '[ENTER YOUR TWILIO NUMBER]',
		body = 'Your friend ' + first_num + ' wanted you to watch this! \n' + songLookup(song))
	else:
	 	song = msg_body

	 	client.messages.create(
		to = request.values.get('From'),
		from_= '[ENTER YOUR TWILIO NUMBER]',
		body = songLookup(song))

	return " "

def songLookup(msg_body):
	result = youtube.search().list(
		q = msg_body,
		part= "id",
		order= "relevance",
		type= "video",
		fields="items/id").execute()
	
	videos = []
	
	for search_result in result.get("items", []):
		videos.append("%s" % (search_result["id"]["videoId"]))

	songId = videos[0]

	you_link = 'youtube.com/watch?v={}'.format(songId)

	return you_link

app.run()

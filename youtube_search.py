from flask import Flask, request
from twilio.rest import TwilioRestClient
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey= "[ENTER API KEY]")

client = TwilioRestClient("[ACCOUNT_SID]", "[AUTH_TOKEN]")

app = Flask(__name__)

@app.route("/")
def test():
	first_num = request.values.get('From', None)
	msg_body = request.values.get('Body', None)
	
	client.messages.create(
		to = request.values.get('From', None),
		from_= '[ENTER PHONE NUMBER]',
		body = songLookup(msg_body))

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

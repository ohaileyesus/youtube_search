from flask import Flask, request
from twilio.rest import TwilioRestClient
from apiclient.discovery import build

youtube = build('youtube', 'v3', developerKey= "[ENTER API KEY]")

client = TwilioRestClient("[ACCOUNT_SID]", "[AUTH_TOKEN]")

app = Flask(__name__)

@app.route("/")
def test():

	first_num = request.values.get('From')
	twilio_num = [ENTER TWILIO NUMBER]
	msg_body = request.values.get('Body')

	if 'DL' not in msg_body:
		if '+' in msg_body:
			song = msg_body.split('+')[0]
			recepient = msg_body.split('+')[1]

			client.messages.create(
			to = '+' + recepient,
			from_= twilio_num,
			body = 'Your friend ' + first_num + ' wanted you to watch this! \n' + songLookup(song))
		else:
		 	song = msg_body

		 	client.messages.create(
			to = first_num,
			from_= twilio_num,
			body = songLookup(song))
	else:
		if '+' in msg_body:
			song = msg_body.split('+')[0]
			recepient = msg_body.split('+')[1]

			client.messages.create(
			to = '+' + recepient,
			from_= twilio_num,
			body = 'Your friend ' + first_num + ' wanted you to watch this! \n' + songDL(song))
		else:
		 	song = msg_body

		 	client.messages.create(
			to = first_num,
			from_= twilio_num,
			body = songDL(song))

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

	you_link = 'http://youtube.com/watch?v={}'.format(songId)

	return you_link 



def songDL(msg_body):
	msg_body1 = msg_body.replace("DL ","")
	result = youtube.search().list(
		q = msg_body1,
		part= "id",
		order= "relevance",
		type= "video",
		fields="items/id").execute()
	
	videos = []
	
	for search_result in result.get("items", []):
		videos.append("%s" % (search_result["id"]["videoId"]))

	songId = videos[0]

	you_link = 'http://youtube.com/watch?v={}'.format(songId)

	v = pafy.new(you_link)

	streams = v.streams

	for s in streams:
		print s.url

	my_url = s.url
	shortener = Shortener('Tinyurl', timeout=9000)
	print "My short url is" + shortener.short(my_url)
	sh_url = shortener.short(my_url)
	return sh_url
app.run()

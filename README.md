# Youtube Search Via Text
This Python Flask app allows you to search anything on youtube by texting a Twilio designated phone number. Also, if you would like to send the result of your youtube search to a friend, you can add your friend's phone number in a "+1**********" format after your search query.

#Setup
1. You will first need to create an account on Twilio's website, which will give you an Auth Token and Account SID, both of which you will need to operate this app. In addition, you will need to obtain a phone number. 
2. You will need to install ngrok and run a session. Set your ngrok forwarding url as the webhook url for your phone number's SMS HTTP GET response.
3. Obtain a youtube v3 api key.


#!/usr/bin/env python
import sys
import os, random
from twython import Twython

#Enter your own information here
apiKey = ''
apiSecret = ''
accessToken = ''
accessTokenSecret = ''

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

#Location where garfield images are stored
ImageDirectory = ""
#Selects a random garfield image from a given directory
RandomGarfieldImage = random.choice(os.listdir(ImageDirectory))

#Open and upload image to twitter
TweetImage = open(ImageDirectory + "/" + RandomGarfieldImage, "rb")
response = api.upload_media(media=TweetImage)

#Creates new tweet
api.update_status(status="I hate Mondays!", media_ids=[response['media_id']])


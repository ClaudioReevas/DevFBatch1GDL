# Facebook Graph API Example in Python
# by James Thornton, http://jamesthornton.com

# Facebook API Docs
# https://developers.facebook.com/docs/graph-api/using-graph-api#reading

# Get Your Facebook Access Token Here...
# https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path=me

# Before running this script...
# Set your Facebook Access Token as an environment variable in your terminal:
# $ export ACCESS_TOKEN={YOUR ACCESS TOKEN}

# To download this script, use the curl command...
# $ curl -O https://gist.githubusercontent.com/espeed/11114604/raw/a233d14604ea44f9d29af02cd2768b91caaad7af/fbme.py

# To run this script, use the python command to execute the script in your terminal...
# $ python fbme.py

import os
import json
import urllib
import pprint

# get Facebook access token from environment variable
# ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN = "EAACEdEose0cBAFFac4nDMikZCOF7ZBBWCAQpY9YlFeLvGcZBGauK3aA1RpZBKBMI628Ussz0lqB4RLu0b77ZC4rBFf3ZBeWF8GvCZCk6QOyhV8QBYU4BO2YriEAX0kay1fQz1g3ZASAGGRdAioNWCV0cjJ2KPP5CAs2VLOK7WE8FNEhEbLqwB6GagMGRbu5qhjmgc1ybZCoiwxAZDZD"
# build the URL for the API endpoint
host = "https://graph.facebook.com"
path = "/me"
params = urllib.urlencode({"access_token": ACCESS_TOKEN})

url = "{host}{path}?{params}".format(host=host, path=path, params=params)

# open the URL and read the response
resp = urllib.urlopen(url).read()

# convert the returned JSON string to a Python datatype
me = json.loads(resp)

# display the result
pprint.pprint(me)


userId = me["id"]
urllikes='https://graph.facebook.com/' + userId + '/likes?access_token=' + ACCESS_TOKEN +'&limit=200'
print urllikes
resplikes = urllib.urlopen(urllikes).read()
likes = json.loads(resplikes)
pprint.pprint(likes)


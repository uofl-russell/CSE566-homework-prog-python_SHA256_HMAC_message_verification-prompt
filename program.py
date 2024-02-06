import requests
import sys 
# missing some import statements 

message = str(sys.argv[1])
encoded_message = message.encode('utf-8')
API_SECRET = "notcorrectapikey".encode('utf-8') #get this from README
signature = "notacorrecthash" #implement code to calculate this...see video

url = 'put api address here'
myobj = {
    'message': message, 
    'signature': signature
}

x = requests.post(url, json = myobj)
data = x.json()
if data['isMessageVerified']:
    print('Message Verified With Confirmation Code', data['confirmation'])
else:
    print('Message Was Not Verified')

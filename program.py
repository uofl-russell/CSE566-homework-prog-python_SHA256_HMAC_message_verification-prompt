import requests
import sys 
import hashlib
import hmac

message = str(sys.argv[1])
encoded_message = message.encode('utf-8')
API_SECRET = "892374928347928347283473".encode('utf-8')
signature = str(hmac.new(
    API_SECRET, 
    msg=encoded_message, 
    digestmod=hashlib.sha256
).hexdigest())

url = 'https://api.abstractclassroom.com/teaching/CSE566'
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

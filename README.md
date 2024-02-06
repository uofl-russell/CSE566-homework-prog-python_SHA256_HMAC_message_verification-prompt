# SHA256 HMAC Message Verification

This assignment will provide an example of how endpoints can verify message accuracy.

# Product Owner Statement

As a person interested in cybersecurity I implemented an AWS (Amazon Web Services) API Gateway that accepts a JSON object as a POST request.  I need a Python (version 3) program that can test my API endpoint.

## Technical Specifics About The Endpoint


The JSON object has the format shown below.
```
{
    "message" : "Hello everyone"
    "signature" : "159fb4e95f41ecbee88deab8b8544799edbdab6bdc655aca7f15ac454c1e6060"
}
```
Here are the specifics about the endpoint:

-  The message can be any alphanumeric string of characters.
-  The signature is an SHA256 hash of the message using the HMAC ```892374928347928347283473```
-  The server listening to the endpoint will recieve the JSON object in the body of the request. The server will also compute the SHA256 hash of the message using the HMAC given above.  The server will compare the signature given and the one it computed.
-   The server will respond with a JSON in the body of the response.

The response JSON from the server will have the following format if the computed and recieved hashes match:
```
{
    "isMessageVerified": true,
    "confirmation": "bf7e783b0a4b2a41ba82a8ce93fb84f540ff94d1f48af5e395d0e13e4b39a07b"
}
```
The confirmation code is an SHA256 hash of the original hash using an HMAC unknown to the client making the request (you).

If the computed and recieved hashes do not match on the server then the response will be the JSON object shown below. Notice the ```isMessageVerified``` is ```false``` and the ```confirmation``` field is an empty string.
```
{
    "isMessageVerified": false,
    "confirmation": ""
}
```

# Acceptance Criteria

Below is the requirements to recieve credit.

- The program must use Python version 3.9 or higher.
- The Python source code file must be named ```program.py```
- The program must accept a string message as a command line argument ```python program.py "Hello everyone"```
- The program must calculate an SHA256 hash of the message passed to it using the HMAC ```892374928347928347283473```
- The program must create an appropriate JSON object to be send to the server endpoing as a HTTPS POST request. There are several libraries capable of doing this.
- The program must only use standard libraries.  You may not use PIP or any other library outside of the native Python 3.9 (or higher) collection. 
- You MUST use the ```sys```, ```requests```, ```hmac```, and ```hashlib```Python libraries.  These are probably the only libraries you need. The requests library can parse JSON responses and will allow dictionaries to be sent natively.
- The program must accept the JSON response body, parse out the ```confirmation``` string and print it to ```stdout``` without any spaces using lowercase letters.
- The program will only accept one string at a time.  (Terminate after printing the response confirmation to stdout)
- Responses must look like the following:
    - If the message was not verified the message printed from the program should be ```Message Was Not Verified```
    - If the message was verified the message printed from the program should be ```Message Verified With Confirmation Code 54129ca50d03509311adab6754c8f84664e0f5a8a916ea78adfe784386983b12```

# Demonstration Video
Here is a link to the Lecture/Demonstration Video associated with this programming assignment.
https://youtu.be/n75irsVJ2dA

Remember!  You are not doing anything in AWS.  You are not building what was demonstrated in the lecture/demo video.  YOU ARE BUILDING THE CLIENT!

# Helpful links
Below are some links you may find helpful

-  (JSON library) https://docs.python.org/3/library/json.html
-  (Requests Library Help) https://scrapeops.io/python-web-scraping-playbook/python-requests-post-requests/


# Example Output
Here is the expected output from running  ```python program.py "Hello Everyone"```
```
Message Verified With Confirmation Code f2eda3d0449da29ddaf54f1e0d23044d525aa8773191f8f1df69473366063b1e
```
Note that on some computers python version 3.x requires command line  ```python3``` rather than simply ```python```.  This is true for some MacOS computers.
import base64

credentials = ["marcenoandrei24@gmail.com", "p@ssweord"]
base64_credentials = base64.b64encode("".join(credentials).encode()).decode()
print('Authorization : basic' + base64_credentials)
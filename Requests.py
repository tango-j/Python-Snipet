import requests

url = 'http://phonecorp.hackxor.net/reset'
post_data = {'phone': phone}

response = requests.post(url, data = post_data)

#Response headers can be accessed by below syntax
print response.headers['Date']

#Response Content can be accessed by below syntax
print response.content

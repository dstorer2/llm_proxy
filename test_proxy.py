import requests

url = 'http://127.0.0.1:5000/generate'
payload = {
    'prompt': 'Tell me a joke.',
    'model': 'claude' # Change to 'claude' to test the Claude model
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    print('Response:', response.json().get('response'))
else:
    print('Error:', response.json().get('error'))
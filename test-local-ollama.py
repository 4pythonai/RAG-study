from ollama import Client
client = Client(host='http://127.0.0.1:11434',timeout=120)
response = client.chat(model='tinydolphin', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response)
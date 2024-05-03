from ollama import Client
client = Client(host='http://119.255.238.247:11434',timeout=120)
response = client.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response)
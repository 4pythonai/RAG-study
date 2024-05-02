import ollama

response = ollama.chat(model='tinydolphin', messages=[
    {
        'role': 'user',
        'content': 'What is the capital of France?',
    'stream': False,
    },
])

print(response['message']['content'])
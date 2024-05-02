from llama_index.llms.ollama import Ollama
llm = Ollama(model="tinydolphin", request_timeout=60.0)
response = llm.complete("What is the capital of France?")
print(response)

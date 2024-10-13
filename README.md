# gpt-api-but-free

>install
https://github.com/nomic-ai/gpt4all

>py
```
from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")
with model.chat_session():
    print(model.generate("How can I run LLMs efficiently on my laptop?", max_tokens=1024))
```


local docs folder (need to set) for own use

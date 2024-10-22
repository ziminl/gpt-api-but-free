import os
from gpt4all import GPT4All

def read_files_in_dir(directory, model):
    results = []  
    full_content = ""
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(f"Filename: {file_path}")
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    print(f"Content:\n{content}\n")
                    results.append(content)  
                    full_content += content
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")
    ask = " explain this code"
    text_to_ask = full_content + ask
    response = model.generate(text_to_ask)
    print(f"gpt response :\n{response}\n")

model_dir = r'C:\Users\{username}\AppData\Local\nomic.ai\GPT4All\Meta-Llama-3-8B-Instruct.Q4_0.gguf'
model = GPT4All(model_dir)

input_dir = input("dir input: ")
read_files_in_dir(input_dir, model)

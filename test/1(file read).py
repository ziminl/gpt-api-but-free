import os

def read_files_in_dir(directory):
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(f"Filename: {file_path}")
            try:
                with open(file_path, 'r') as file:
                    content = file.read()
                    print(f"Content:\n{content}\n")
            except Exception as e:
                print(f"Could not read file {file_path}: {e}")

read_files_in_dir(f'C:\dir\dir\')

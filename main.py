import os


files = os.environ['INPUT_FILES'].split('|')
output_files = os.environ['INPUT_OUTPUT_FILES'].split('|')

for file in zip(files, output_files):
    os.system(f"fig2sketch {tuple(file)[0]} {tuple(file)[1]}")  

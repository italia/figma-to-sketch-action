import os


files = os.environ['INPUT_FILES'].split('|')
output_files = os.environ['INPUT_OUTPUT_FILES'].split('|')

operation_result = 0

for file in zip(files, output_files):
    print (f"🏗️  Converting {tuple(file)[0]} to {tuple(file)[1]}")
    os.system(f"fig2sketch --force-convert-images --compress {tuple(file)[0]} {tuple(file)[1]}") 
    if os.path.isfile(tuple(file)[1]):
        print (f"✅  {tuple(file)[1]} ready!")
    else:
        operation_result = 1
        print  (f"❌  Error during {tuple(file)[1]} conversion!")

exit(operation_result)

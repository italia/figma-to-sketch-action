import os
import hashlib
import json

class SHADb:
    def __init__(self, db_path):
        self._db_path = db_path
        if os.path.isfile(self._db_path):
            with open(self._db_path, 'r') as db_file:
                self._data = json.load(db_file)
        else:
            self._data = {}

    def calculate_sha_of_file(self, filename):
        with open(filename, 'rb', buffering=0) as f:
            return hashlib.file_digest(f, 'sha256').hexdigest()
        
    def get_sha(self, element):
        return self._data.get(element, None)
    
    def store(self, element, sha):
         self._data[element] = sha
         with open(self._db_path, 'w') as db_file:
            json_object = json.dumps(self._data, indent=4)
            db_file.write(json_object)


files = os.environ['INPUT_FILES'].split('|')
output_files = os.environ['INPUT_OUTPUT_FILES'].split('|')

operation_result = 0
sha_db = SHADb(os.environ.get('INPUT_SHA_DB_PATH', os.path.join('.github', '.conversion.db')))

for file in zip(files, output_files):
    input_fig = tuple(file)[0]
    output_sketch = tuple(file)[1]
    old_sha_fig = sha_db.get_sha(input_fig)
    new_sha_fig = sha_db.calculate_sha_of_file(input_fig)
    if old_sha_fig != new_sha_fig:
        print (f'🏗️  Converting {input_fig} to {output_sketch}')
        os.system(f'fig2sketch --force-convert-images --compress {input_fig} {output_sketch}') 
        if os.path.isfile(output_sketch):
            sha_db.store(input_fig, new_sha_fig)
            print (f'✅  {output_sketch} ready!')
        else:
            operation_result = 1
            print  (f'❌  Error during {output_sketch} conversion!')

exit(operation_result)

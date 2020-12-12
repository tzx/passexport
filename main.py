import os
import re
import subprocess
import sys

if __name__ == '__main__':
    with open('output.txt', 'w') as f:
        for encrypted_file in sys.argv[1:]:
            name = os.path.splitext(encrypted_file)[0]
            name = re.sub(r'^.*password-store/', '', name)
            print(name, file=f)
            print(len(name) * '-', file=f)
            decrypted = subprocess.run(['gpg', '-d', encrypted_file], capture_output=True, text=True).stdout
            print(decrypted + '\n', file=f)
            
            print('Finished', encrypted_file)

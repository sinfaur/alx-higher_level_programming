#!/usr/bin/python3
import os
import subprocess

def auto_exec_file(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.py' or '.sh'):
                file_path = os.path.join(root, file)
                subprocess.run(['chmod', '+x', file_path])
                
if __name__ == '__main__':
    directory_path = '.' # Alter to suit current directory
    auto_exec_file(directory_path)
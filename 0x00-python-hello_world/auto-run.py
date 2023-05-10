#!/usr/bin/python3
import os
import subprocess
from subprocess import check_output
# This python scripts iterates though all .py files adn runs the pycodestyle on the
# It returns "PASSED" if it meets the requirements || The standard output messasge from pycodestyle for debugging.
# I am fluent with python so i created a script to auto correct the codes per the pycodestyle v2.8.0 style
# If you are a beginner do it yourself and create the script! It isnt a bas thing :D

def style_correct(path):
    for root, dir, files in os.walk(path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                p = subprocess.run(['pycodestyle' 'file', file_path])
                capture_output=True
                # If feedback is command prompt$ or newline with no textit will retunr the FILE_NAME && print(" -> PASSED")
                if capture_output == '\n':
                    if capture_output.text == False:
                        print(f"{file} -> PASSED")
                    
                
if __name__ == '__main__':
    directory_path = '.'
    style_correct(directory_path)
        

# filecheck.py
# Program to check if a file exists
# Requires either: full filename i.e. c:\foo\bar.exe, or: filename in the current directory too. (e.g sample.txt)
# 
# Author:     J Palmer
# Created on: 2012-02-26
# Version:    1.0.2 (tweaked header)

import os
print "Yes, it exists" if os.path.exists(raw_input("Full filename: ")) else "No, that does not exist"

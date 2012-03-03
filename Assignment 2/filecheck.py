# checking if a file exists
# Josh Palmer 26/2/2k12 etc
# obviously requires full filename i.e. c:\foo\bar.exe

import os
print "Yes, it exists" if os.path.exists(raw_input("Full filename: ")) else "No, that does not exist"

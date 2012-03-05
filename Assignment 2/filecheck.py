# checking if a file exists
# obviously requires full filename i.e. c:\foo\bar.exe
#
# Author:     J Palmer
# Created on: 2012-02-26
# Version:    1.0.1 (added this header lol.)

import os
print "Yes, it exists" if os.path.exists(raw_input("Full filename: ")) else "No, that does not exist"

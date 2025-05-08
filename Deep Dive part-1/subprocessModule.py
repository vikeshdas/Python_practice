"""
subprocess module allows Python to run system commands just like os module but subprocess module is more safer then os module to run system command.
- You can start new processes
"""

import subprocess

cmd=['arp','-a']

# it will return ouput if above command excute suceessfull else error.thats why it is safter then os module.we have also use try catch to handle erro if there is any error.
print(subprocess.check_output)
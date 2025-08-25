#!/usr/bin/python

import sys
import os
import subprocess
from datetime import datetime


if __name__ == "__main__":
    start_time = datetime.now().strftime("%H:%M:%S")
    for (root, dirs, files) in os.walk(sys.argv[1], topdown=True):
        for f in files:
            full_name = root + f
            print(full_name)
            subprocess.run(['cat', full_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    end_time = datetime.now().strftime("%H:%M:%S")
    print("Starting at: " + start_time)
    print("Ended at: " +  end_time)
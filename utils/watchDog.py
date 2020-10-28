""" Purpose: A Utility script to check if the transcript file is changed in periodic intervals
Source Code Creator: Soniya Vijayakumar
Project: WILPS Hamburg University 
Term: Summer 2021
M.Sc. Intelligent Adaptive Systems  """

import os
import time
import sys

def watch_dog(tFile):
    print("inside watch dog")

    while True:
        try:
            _cached_stamp = 0
            _stamp = 0
            time.sleep(1)
            _stamp = os.stat(tFile).st_mtime
            print("inside watch dog:" + str(_stamp))
            if _stamp != _cached_stamp:
                _cached_stamp =  _stamp
                print("file has updated")
                return True
            else:
                print("nothing happen")
                return False
        except KeyboardInterrupt:
            print("\nDone")
            break
        except UnboundLocalError as error:
        # Output expected UnboundLocalErrors.
            print(error)
        except: 
            print(f'Unhandled error: {sys.exc_info()[0]}')
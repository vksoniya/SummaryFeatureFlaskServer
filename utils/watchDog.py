import os
import time
import sys

_cached_stamp = 0

def watch_dog(tFile):

    while True:
        try:
            time.sleep(1)
            stamp = os.stat(tFile).st_mtime

            if stamp != _cached_stamp:
                _cached_stamp =  stamp
                print("file has updated")
                return True
            else:
                print("nothing happen")
                return False
        except KeyboardInterrupt:
            print("\nDone")
            break
        except: 
            print(f'Unhandled error: {sys.exc_info()[0]}')
import os

path_to_watch = "./data"
print('... Listening for changes in ',path_to_watch, ' folder ...')

before = dict ([(f, None) for f in os.listdir (path_to_watch)])
while 1:
        after = dict ([(f, None) for f in os.listdir (path_to_watch)])
        added = [f for f in after if not f in before]
        if added:
                print("... found new dataset: ", ", ".join (added),". Initiating inference ...")
                os.system("python3 ./inference.py")
                break
        else:
             before = after
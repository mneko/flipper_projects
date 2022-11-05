import re
import os
import fileinput

files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    myfile = fileinput.FileInput(f, inplace=True)
for line in myfile:
    line = re.sub(r"(?:.*):d=(\d{1,3}),o=(\d{1,3}),b=(\d{1,3})(,l=(\d{1,3}))?:",
                  r"Filetype: Flipper Music Format\nVersion: 0\nBPM: \3\nDuration: \1\nOctave: \2\nNotes:",
                  line)
    print(line)
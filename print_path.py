import os

for i in os.environ.get('PATH').split(';'):
    print i

import os, subprocess
testfiles = ['gcps.tif', 'map.tif']
for testfile in testfiles:
    if not os.path.exists(testfile):
        subprocess.call(['wget', os.path.join('https://github.com/nansencenter/nansat/raw/master/nansat/tests/data', testfile)])
    print testfile, ' - OK'


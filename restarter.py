from subprocess import Popen

filename = 'main.py'
while True:
    print("\nStarting " + filename)
    p = Popen("python3 " + filename, shell=True)
    p.wait()
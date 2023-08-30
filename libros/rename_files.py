import os
files = os.listdir(os.getcwd())
[os.replace(file, file.replace(" ", "_")) for file in files]
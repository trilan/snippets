import os


def find(root):
    for current, dirs, files in os.walk(root):
        for file in files:
            yield os.path.join(current, file)

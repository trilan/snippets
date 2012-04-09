import os


def find(root):
    """Yield all found filepaths in provided directory recursively."""
    for current, dirs, files in os.walk(root):
        for file in files:
            yield os.path.join(current, file)

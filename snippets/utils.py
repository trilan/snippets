import codecs


def read(filepath):
    """Read file content from provided filepath."""
    with codecs.open(filepath, encoding='utf-8') as f:
        return f.read()

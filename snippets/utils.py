import codecs


def read(filepath):
    with codecs.open(filepath, encoding='utf-8') as f:
        return f.read()

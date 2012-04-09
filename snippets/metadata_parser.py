import re
from pygments.token import Comment


#: A regular expression object to find all metadata
#: params in source code header comments.
metadata_re = re.compile(r'!(\w+):\s*(.+)$', re.M)


def parse_comment_metadata(comment):
    """Find all metadata params in provided comment string. Found params are
    returned as dictionary.
    """
    return dict(metadata_re.findall(comment))


def parse_metadata(tokens):
    """Find all metadata params in provided tokens. A two-tuple is returned
    with found params as first item and comments without metadata as second
    item. Foind params are returned as dictionary.
    """
    comments = []
    metadata = {}
    is_significant = True
    for token in tokens:
        if token[0] in (Comment, Comment.Multiline, Comment.Single):
            comment_metadata = parse_comment_metadata(token[1])
            is_significant = not comment_metadata
            metadata.update(comment_metadata)
        if is_significant:
            comments.append(token)
    return metadata, comments

import re
from pygments.token import Comment


metadata_re = re.compile(r'!(\w+):\s*(.+)$', re.M)


def parse_comment_metadata(comment):
    return dict(metadata_re.findall(comment))


def parse_metadata(tokens):
    comments = []
    metadata = {}
    is_significant = True
    for token in tokens:
        if token[0] is Comment:
            comment_metadata = parse_comment_metadata(token[1])
            is_significant = not comment_metadata
            metadata.update(comment_metadata)
        if is_significant:
            comments.append(token)
    return metadata, comments

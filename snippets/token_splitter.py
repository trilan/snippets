from itertools import tee, dropwhile
from pygments.token import Comment, Text


def is_token_match(token):
    return token[0] is Comment or token[0] is Text and token[1].isspace()


def split(tokens):
    tokens = tuple(tokens)
    header_tokens = []
    for token in tokens:
        if not is_token_match(token):
            return header_tokens, tokens[len(header_tokens):]
        header_tokens.append(token)
    return header_tokens, ()

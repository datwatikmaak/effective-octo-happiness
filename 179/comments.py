import re


def strip_comments(code):
    # see Bite description
    docstring = re.compile(r'\s*"{3}.*?"{3}', re.DOTALL)
    output = docstring.sub(r'', code)
    comments = re.compile(r'\s*#\s.*')
    return comments.sub(r'', output)

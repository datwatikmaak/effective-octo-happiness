import textwrap
from itertools import zip_longest

COL_WIDTH = 20


def text_to_columns(text):
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""
    article = (
        textwrap.wrap(lines, width=COL_WIDTH)
        for lines in text.split("\n\n")
    )

    columns = zip_longest(*article, fillvalue=" ")

    return "\n".join("  ".join(line) for line in columns)

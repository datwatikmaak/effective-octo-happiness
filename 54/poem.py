import textwrap
from pprint import pprint

INDENTS = 4

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem):
    indent = False
    for line in poem.splitlines():
        stripped_line = line.strip()
        if len(stripped_line) == 0:
            indent = False
            continue
        if indent:
            print(f"{' ' * INDENTS}{stripped_line}")
        else:
            print(f"{stripped_line}")
            indent = True


print_hanging_indents(rosetti_unformatted)

WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    for i in range(size):
        for _ in range(int(size / 2)):
            if i % 2 == 0:
                print(f"{WHITE}{BLACK}", end="")
            else:
                print(f"{BLACK}{WHITE}", end="")
        print()

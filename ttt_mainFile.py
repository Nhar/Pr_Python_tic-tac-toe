# Kółko i krzyżyk

# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
    """Wyświetl instrukcję gry."""  
    print(
    """
    Gra kółko i krzyżyk

    Swoje posunięcie wskażesz poprzez wprowadzenie liczby z zakresu 0 - 8.
    Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:
    
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8

    \n
    """
    )
	
def ask_yes_no(question):
    """Zadaj pytanie, na które można odpowiedzieć tak lub nie."""
    response = None
    while response not in ("t", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Poproś o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def match():
    """Ustal, czy pierwszy ruch należy do gracza, czy do komputera."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("\nPierwszy ruch należy do ciebie.")
        human = X
        computer = O
    else:
        print("\nComputer wykonuje ruch jako pierwszy.")
        computer = X
        human = O
    return computer, human

def new_board():
    """Utwórz nową planszę gry."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    """Wyświetl planszę gry na ekranie."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")

def legal_moves(board):
    """Utwórz listę prawidłowych ruchów."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
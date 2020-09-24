from itertools import groupby
import chess

board = [["" for i in range(8)] for i in range(8)]

chess_position = input("Введите шахматную позицию. Например: b6 h8 a8").lower()
true_list = ["a", "b", "c", "d", "e", "f", "g", "h", "1", "2", "3", "4", "5", "6", "7", "8", " "]


if (True if True in tuple(not x in true_list for x in list(chess_position)) else False):
    print("Error Неправильно задана позиция")
elif len(chess_position.split()) != 3:
    print("Error не заданы все фигуры")
elif chess_position.split()[0] == chess_position.split()[1] or chess_position.split()[1] == chess_position.split()[2] or chess_position.split()[0] == chess_position.split()[2]:
    print("Error фигуры стоят на одной и той же позиции")
else:
    if (abs(true_list.index(chess_position[0]) - true_list.index(chess_position[6])) <= 1 and abs(true_list.index(chess_position[1]) - true_list.index(chess_position[7]))) <=  1:
        print("Strange")
    else:


        fen = [["1" for i in range(8)] for i in range(8)]
        mass = chess_position.split()
        for i in range(len(mass)):
            k = "q"
            if i == 0:
                k = "K"
            elif i == 1:
                k = "R"
            else:
                k = "k"
            fen[ord(mass[i][0]) - 97][int(mass[i][1]) - 1] = k


        for x in range(len(fen)):
            fen[x] = "".join([str(len(i)) if i[0][0] == "1" else i[0] for i in [list(g) for k, g in groupby(''.join(fen[x]))]])

        original_fen = "/".join(fen)
        original_fen += ' b'

        board = chess.Board(fen=original_fen)
        print(original_fen)
        print(board)
        if board.is_checkmate():
            print("Checkmate")
        elif board.is_stalemate():
            print("Stalemate")
        elif board.is_check():
            print("Check")
        else:
            print("Normal")

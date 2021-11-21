from pions import *

# def board_init():
#     for i in range(1,9) :
#         for j in range(1,9) :
#             if i == 2 :
#                 Pawn((i,j),'b')
#             if i == 7 :
#                 Pawn((i,j),'w')
#             if i == 1 :
#                 if (j == 1) | (j==8):
#                     Rook((i,j),'b')
#                 if (j == 2) | (j==7):
#                     Knight((i,j),'b')
#                 if (j == 3) | (j==6):
#                     Bishop((i,j),'b')
#                 if (j == 4) :
#                     Queen((i,j),'b')
#                 if (j == 5) :
#                     King((i,j),'b')
#             if i == 8 :
#                 if (j == 1) | (j==8):
#                     Rook((i,j),'w')
#                 if (j == 2) | (j==7):
#                     Knight((i,j),'w')
#                 if (j == 3) | (j==6):
#                     Bishop((i,j),'w')
#                 if (j == 4) :
#                     Queen((i,j),'w')
#                 if (j == 5) :
#                     King((i,j),'w')

def load_fen(fen):
    fen = fen.split()
    board = fen[0].split('/')
    x=1
    y=1
    for b in board:
        for g in b:
            if is_integer(g):
                y+=int(g)
            else :
                if g == 'n':
                    Knight((x,y),'b')
                if g == 'b':
                    Bishop((x,y),'b')
                if g== 'q':
                    Queen((x,y),'b')
                if g== 'k':
                    King((x,y),'b')
                if g== 'r':
                    Rook((x,y),'b')
                if g== 'p':
                    Pawn((x,y),'b')
                if g == 'N':
                    Knight((x,y),'w')
                if g == 'B':
                    Bishop((x,y),'w')
                if g== 'Q':
                    Queen((x,y),'w')
                if g== 'K':
                    King((x,y),'w')
                if g== 'R':
                    Rook((x,y),'w')
                if g== 'P':
                    Pawn((x,y),'w')
                y+=1
        y=1
        x+=1
    return (fen[1],fen[2])


def print_board(unicode = True):
    ligne = "|"+" -"*(19)+" |"
    for i in range (1,18):
        if i%2 == 1:
            print(ligne)
        else :
            print("|",end=" ")
            for j in range (1,9):
                p = Pieces.piece_on((i/2),j)
                if isinstance(p,Pieces):
                    if unicode :
                        print(p.to_str_u(),end="  | ")
                    else:
                        print(p,end=" | ")
                else:
                    print("  ",end=" | ")
            print(int(9-(i/2)))
    print("| a  | b  | c  | d  | e  | f  | g  | h  |")


def trans_pos1(pos):
    tab1 = ['a','b','c','d','e','f','g','h']
    tab2 = range (8,0,-1)
    x=0
    y=0
    for i in range (8):
        if pos[0] == tab1[i]:
            y = i+1
        if int(pos[1]) == tab2[i]:
            x = i+1
    return (x,y)

def trans_pos2(cord):
    pos = ""
    tab1 = ['a','b','c','d','e','f','g','h']
    pos+= str(tab1[cord[1]-1])
    pos+= str(9-cord[0])
    return pos

def game_turn(team):
    continu = True
    t = "black"
    et = "white"
    if team == 'w':
        et = t
        t = "white"
    print(f"it's {t} player's turn :")
    while continu :
        try :
            mv = input("what's youre moove :")
            if mv == "u":
                Pieces.undo_moove()
                print_board()
            if mv == "resign":
                return (t+" forfeit\nWinner is "+et)
            if mv == "draw" :
                answer = input(et+" player do you accept a draw (y/n)")
                if answer == 'y':
                    return("The match ended in a draw")
            mv = mv.split()
            x,y = trans_pos1(mv[0])
            p = Pieces.piece_on(x,y)
            pos = trans_pos1(mv[1])
        except (IndexError,ValueError) :
            continue
        if isinstance(p,Pieces):
            if p.team == team :
                mooves = p.possible_mooves()
                if pos in mooves:
                    p.make_moove(pos)
                    if Pieces.is_check(team):
                        Pieces.undo_moove()
                    else:
                        continu = False
                    

def save_histo(file):
    with open(file,'w') as writer:
        writer.write("pos_d pos_a prise\n")
        for moves in Pieces.list_mv:
            pos_d = trans_pos2(moves[0])
            pos_a = trans_pos2(moves[1])
            writer.write(pos_d + " "*4+pos_a+" "*4+moves[2]+"\n")

def is_victory():
    ww = True
    bw = True
    for p in Pieces.list_p:
        if p.__str__() == "bK":
            ww = False
        if p.__str__() == "wK":
            bw = False
    if ww :
        print("white victory !!!")
    if bw :
        print("black victory !!!")
    return (bw | ww)




def is_checkmate(team):
    for p in Pieces.list_p :
        if p.team == team :
            for moove in p.possible_mooves():
                p.make_moove(moove)
                if not Pieces.is_check(team):
                    Pieces.undo_moove()
                    return False
                Pieces.undo_moove()
    print(team +" player is checkmate")
    return True

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


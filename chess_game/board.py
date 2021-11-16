from pions import *

def board_init():
    for i in range(1,9) :
        for j in range(1,9) :
            if i == 2 :
                Pawn((i,j),'b')
            if i == 7 :
                Pawn((i,j),'w')
            if i == 1 :
                if (j == 1) | (j==8):
                    Rook((i,j),'b')
                if (j == 2) | (j==7):
                    Knight((i,j),'b')
                if (j == 3) | (j==6):
                    Bishop((i,j),'b')
                if (j == 4) :
                    Queen((i,j),'b')
                if (j == 5) :
                    King((i,j),'b')
            if i == 8 :
                if (j == 1) | (j==8):
                    Rook((i,j),'w')
                if (j == 2) | (j==7):
                    Knight((i,j),'w')
                if (j == 3) | (j==6):
                    Bishop((i,j),'w')
                if (j == 4) :
                    Queen((i,j),'w')
                if (j == 5) :
                    King((i,j),'w')



def print_board():
    ligne = "|"+" -"*(19)+" |"
    for i in range (1,18):
        if i%2 == 1:
            print(ligne)
        else :
            print("|",end=" ")
            for j in range (1,9):
                p = Pieces.piece_on((i/2),j)
                if isinstance(p,Pieces):
                    print(p,end=" | ")
                else:
                    print("  ",end=" | ")
            print(int(9-(i/2)))
    print("| A  | B  | C  | D  | E  | F  | G  | H  |")


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
    if team == 'w':
        t = "white"
    print_board()
    print(f"it's {t} player's turn :")
    while continu :
        mv = input("what's youre moove :")
        mv = mv.split()
        x,y = trans_pos1(mv[0])
        p = Pieces.piece_on(x,y)
        pos = trans_pos1(mv[1])
        if isinstance(p,Pieces):
            mooves = p.possible_mooves()
            if pos in mooves:
                continu = False
                Pieces.list_mv.append(((p.__str__(),mv[0],mv[1])))
                p.make_moove(pos)

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
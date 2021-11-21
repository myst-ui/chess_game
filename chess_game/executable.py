from board import *
import time


def main(file="histo.txt",unicode = True,fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w 1",crono = 10,load_f =None):
    run = True
    wcrono = int(crono*60)
    bcrono = int(crono*60)
    # team = 'w'
    # turn_count = 1
    team , turn_count = load_fen(fen)
    turn_count = int(turn_count)
    print_board(unicode=unicode)
    while run :
        print(f"white crono : {wcrono//60}m{wcrono%60:.0f}s\nblack crono : {bcrono//60:}m{bcrono%60:.0f}s")
        try:
            start = time.time()
            r = game_turn(team)
            end = time.time()
        except EOFError:
            print("au revoir")
            break
        if r is not None:
            print(r)
            break
        turn_count+=1
        if team =='w':
            wcrono-=(end-start+2)
            team = 'b'
        else:
            bcrono-=(end-start+2)
            team = 'w'

        if bcrono <= 0 | wcrono <=0 :
            print(team+" player win by timeout")
            run = False
        print_board(unicode=unicode)
        if is_checkmate(team):
            run = False
        # print (Pieces.list_mv)
    save_histo(file)
    



main()


# board_init()
# print_board()

# a = Pieces.piece_on(1,2)
# print(a)
# move = a.possible_mooves()
# print (move)
# # a.make_moove(move[0])

# a.make_moove((5,5))

# game_turn('b')

# print(Pieces.list_mv)
# print_board()

# move = a.possible_mooves()
# for m in move:
#     print(trans_pos2(m))
#print (move)
# lul = trans_pos1("c3")
# print(lul)
# lol = trans_pos2(lul)
# print(lol)

# for p in Pieces.list_p:
#     print(p)
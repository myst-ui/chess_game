from board import *



def main(file):
    run = True
    team = 'w'
    turn_count = 1
    board_init()

    while run :
        
        game_turn(team)
        turn_count+=1
        team = 'w'
        if turn_count%2==0:
            team = 'b'

        if is_victory():
            run = False



main(1)


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
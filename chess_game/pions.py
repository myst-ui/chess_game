
class Pieces :
    list_p = []
    list_mv = []
    def __init__ (self,pos,team):
        self.pos = pos
        self.team = team
        Pieces.list_p.append(self)

    def __str__(self):
        return f"{self.team}"

    def supr(self):
        del Pieces.list_p[Pieces.list_p.index(self)]

    def piece_on(x,y) :
        for p in Pieces.list_p:
            if p.pos == (x,y):
                return p
        return False

    # def piece_named(team,name) :
    #     for p in Pieces.list_p:
    #         if p.__str__() == str(team+name):
    #             return p
    #     return False

    def make_moove(self,pos):
        if isinstance(Pieces.piece_on(pos[0],pos[1]),Pieces):
            Pieces.piece_on(pos[0],pos[1]).supr()       
        self.pos = pos
        
    def moove_diag(self,direction,limit=8):
        mooves = []
        if direction == 1:
            x = 1
            y = 1
        elif direction == 2:
            x = -1
            y = -1
        elif direction == 3:
            x = 1
            y = -1
        elif direction == 4:
            x = -1
            y = 1
        for i in range(1,limit+1):
            if (self.pos[0]+(i*x)>0) & (self.pos[0]+(i*x)<9) & (self.pos[1]+(i*y)>0) & (self.pos[1]+(i*y)<9):
                p = Pieces.piece_on(self.pos[0]+(i*x),self.pos[1]+(i*y))
                if isinstance(p,Pieces):
                    if p.team != self.team:
                        mooves.append((self.pos[0]+(i*x),self.pos[1]+(i*y)))
                    break
                else:
                    mooves.append((self.pos[0]+(i*x),self.pos[1]+(i*y)))
            else:
                break
        return mooves

    def moove_ligne(self,direction,limit=8):
        mooves = []
        vertical = False
        if direction == 1:
            v = 1
            vertical = True
        elif direction == 2:
            v = -1
            vertical = True
        elif direction == 3:
            v = 1
        elif direction == 4:
            v = -1
        if vertical:
            for i in range(1,limit+1):
                if (self.pos[0]+(i*v)>0) & (self.pos[0]+(i*v)<9):
                    p = Pieces.piece_on(self.pos[0]+(i*v),self.pos[1])
                    if isinstance(p,Pieces):
                        if p.team != self.team:
                            mooves.append((self.pos[0]+(i*v),self.pos[1]))
                        break
                    else:
                        mooves.append((self.pos[0]+(i*v),self.pos[1]))
                else:
                    break
        else:
            for i in range(1,limit+1):
                if (self.pos[1]+(i*v)>0) & (self.pos[1]+(i*v)<9):
                    p = Pieces.piece_on(self.pos[0],self.pos[1]+(i*v))
                    if isinstance(p,Pieces):
                        if p.team != self.team:
                            mooves.append((self.pos[0],self.pos[1]+(i*v)))
                        break
                    else:
                        mooves.append((self.pos[0],self.pos[1]+(i*v)))
                else:
                    break
        return mooves

class King (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)
        

    def __str__(self):
        return super().__str__()+"K"

    def possible_mooves(self):
        mooves =[]
        for i in range (1,5):
            mooves+= self.moove_ligne(i,limit=1)
            mooves+= self.moove_diag(i,limit=1)
        return mooves

class Queen (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)
    
    def __str__(self):
        return super().__str__()+"Q"

    def possible_mooves(self):
        mooves =[]
        for i in range (1,5):
            mooves+= self.moove_ligne(i)
            mooves+= self.moove_diag(i)
        return mooves

class Bishop (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)

    def __str__(self):
        return super().__str__()+"b"

    def possible_mooves(self):
        mooves =[]
        for i in range (1,5):
            mooves+= self.moove_diag(i)
        return mooves

class Knight (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)
    
    def __str__(self):
        return super().__str__()+"k"

    def possible_mooves(self):
        mooves = []
        l1 = [-1,1]
        l2 = [-2,2]

        for i in l1:
            for j in l2:
                if (self.pos[0]+i>0) & (self.pos[0]+i<9) & (self.pos[1]+j>0) & (self.pos[1]+j<9):
                    p = Pieces.piece_on(self.pos[0]+i,self.pos[1]+j)
                    if isinstance(p,Pieces):
                        if p.team != self.team:
                            mooves.append(((self.pos[0]+i,self.pos[1]+j)))
                    else:
                        mooves.append(((self.pos[0]+i,self.pos[1]+j)))

        for i in l2:
            for j in l1:
                if (self.pos[0]+i>0) & (self.pos[0]+i<9) & (self.pos[1]+j>0) & (self.pos[1]+j<9):
                    p = Pieces.piece_on(self.pos[0]+i,self.pos[1]+j)
                    if isinstance(p,Pieces):
                        if p.team != self.team:
                            mooves.append(((self.pos[0]+i,self.pos[1]+j)))
                    else:
                        mooves.append(((self.pos[0]+i,self.pos[1]+j)))
        return mooves          


class Rook (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)
    
    def __str__(self):
        return super().__str__()+"r"

    def possible_mooves(self):
        mooves =[]
        for i in range (1,5):
            mooves+= self.moove_ligne(i)
        return mooves

class Pawn (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)

    def __str__(self):
        return super().__str__()+"p"
    
    def possible_mooves(self):
        mooves = []
        d = 1
        if self.team == 'w':
            d=-1
        if (self.pos[0]+d<1) | (self.pos[0]+d>8):
            return mooves
        for i in range (-1,2):
            if (self.pos[1]+i>0) & (self.pos[1]+i<9):
                if isinstance(Pieces.piece_on(self.pos[0]+d,self.pos[1]+i),Pieces):
                    if i == 0:
                        continue
                    else:
                        if Pieces.piece_on(self.pos[0]+d,self.pos[1]+i).team != self.team :
                            mooves.append((self.pos[0]+d,self.pos[1]+i))
                elif i == 0:
                    mooves.append((self.pos[0]+d,self.pos[1]+i))
        # a changé
        if (self.pos[0]==2) | (self.pos[0]==7):
            d*=2
            if not (isinstance(Pieces.piece_on(self.pos[0]+d,self.pos[1]),Pieces)):
                mooves.append((self.pos[0]+d,self.pos[1]))
        return mooves

class Pieces :
    list_p = []
    list_mv = []
    def __init__ (self,pos,team):
        self.pos = pos
        self.team = team
        self.moove_count = 0
        Pieces.list_p.append(self)

    def __str__(self):
        return f"{self.team}"

    def supr(self):
        del Pieces.list_p[Pieces.list_p.index(self)]

    def piece_on(x,y) :
        for p in Pieces.list_p:
            if p.pos == (x,y):
                return p
        return None

    def piece_named(team,name) :
        for p in Pieces.list_p:
            if p.__str__() == str(team+name):
                return p
        return None

    def make_moove(self,pos):
        var = "-"
        p = Pieces.piece_on(pos[0],pos[1])
        if isinstance(p,Pieces):
            var = p.__str__()
            Pieces.piece_on(pos[0],pos[1]).supr()
        Pieces.list_mv.append((self.pos,pos,var))
        self.pos = pos
        self.moove_count+=1

    def undo_moove():
        pos_d = Pieces.list_mv[-1][0]
        pos_a = Pieces.list_mv[-1][1]
        pm = Pieces.list_mv[-1][2]
        p = Pieces.piece_on(pos_a[0],pos_a[1])
        eteam = p.team
        p.pos = pos_d
        p.moove_count -=1
        team = 'w'
        d = -1
        if eteam == 'w':
            team = 'b'
            d = 1
        if (pm != "-"):
            if pm == "ep":
                Pawn((pos_a[0]+d,pos_a[1]),team)
            elif pm[1]== 'p':
                Pawn(pos_a,team)
            if pm == "qr":
                r = Pieces.piece_on(pos_a[0],pos_a[1]+1)
                r.pos = (pos_a[0],1)
                r.moove_count -=1
            elif pm == "kr":
                r = Pieces.piece_on(pos_a[0],pos_a[1]-1)
                r.pos = (pos_a[0],8)
                r.moove_count -=1
            elif pm[1]== 'r':
                Rook(pos_a,team)
            if pm[1]== 'k':
                Knight(pos_a,team)
            if pm[1]== 'b':
                Bishop(pos_a,team)
            if pm[1]== 'q':
                Queen(pos_a,team)
            if pm[1]== 'K':
                King(pos_a,team)
        del Pieces.list_mv[-1]
        
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

    def is_agressed(pos,team):
        for p in Pieces.list_p:
            if p.team != team:
                if p.__str__()[1] == "K":
                    mooves = p.possible_mooves_wr()
                else:
                    mooves = p.possible_mooves()
                if pos in mooves :
                    return True
        return False

    def is_check(team):
        p = Pieces.piece_named(team,'K')
        return Pieces.is_agressed(p.pos,team)

class King (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)
        

    def __str__(self):
        return super().__str__()+"K"

    def to_str_u(self):
        if (self.team == 'w'):
            return '♔'
        else :
            return '♚'

    def possible_mooves(self):
        mooves =[]
        for i in range (1,5):
            mooves+= self.moove_ligne(i,limit=1)
            mooves+= self.moove_diag(i,limit=1)
        pos = self.pos
        if self.moove_count == 0 and not (Pieces.is_agressed(pos,self.team)):
            
            qr = Pieces.piece_on(pos[0],pos[1]-4)
            kr = Pieces.piece_on(pos[0],pos[1]+3)
            if isinstance(qr,Rook):
                if qr.moove_count == 0:
                    if Pieces.piece_on(pos[0],pos[1]-1) is None and Pieces.piece_on(pos[0],pos[1]-2) is None and Pieces.piece_on(pos[0],pos[1]-3) is None:
                        if not (Pieces.is_agressed((pos[0],pos[1]-1),self.team)) and not (Pieces.is_agressed((pos[0],pos[1]-2),self.team)):
                            mooves.append((pos[0],pos[1]-2))
            if isinstance(kr,Rook):
                if kr.moove_count == 0:
                    if Pieces.piece_on(pos[0],pos[1]+1) is None and Pieces.piece_on(pos[0],pos[1]+2) is None :
                        if not (Pieces.is_agressed((pos[0],pos[1]+1),self.team)) and not (Pieces.is_agressed((pos[0],pos[1]+2),self.team)):
                            mooves.append((pos[0],pos[1]+2))

        return mooves

    def possible_mooves_wr(self):
        mooves =[]
        for i in range (1,5):
            mooves+= self.moove_ligne(i,limit=1)
            mooves+= self.moove_diag(i,limit=1)
        return mooves

    def make_moove(self, pos):
        var = "-"
        p = Pieces.piece_on(pos[0],pos[1])
        if isinstance(p,Pieces):
            var = p.__str__()
            Pieces.piece_on(pos[0],pos[1]).supr()
        dif = self.pos[1] - pos[1]
        if abs(dif) >1:
            if dif>0:
                var = "qr"
                r = Pieces.piece_on(pos[0],1)
                r.pos = ((pos[0],pos[1]+1))
            else:
                var = "kr"
                r = Pieces.piece_on(pos[0],8)
                r.pos = ((pos[0],pos[1]-1))
            r.moove_count +=1
        Pieces.list_mv.append((self.pos,pos,var))
        self.pos = pos
        self.moove_count+=1

class Queen (Pieces):

    def __init__(self, pos, team):
        super().__init__(pos, team)
    
    def __str__(self):
        return super().__str__()+"Q"

    def to_str_u(self):
        if (self.team == 'w'):
            return '♕'
        else :
            return '♛'

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

    def to_str_u(self):
        if (self.team == 'w'):
            return '♗'
        else :
            return '♝'

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

    def to_str_u(self):
        if (self.team == 'w'):
            return '♘'
        else :
            return '♞'

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

    def to_str_u(self):
        if (self.team == 'w'):
            return '♖'
        else :
            return '♜'

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

    def to_str_u(self):
        if (self.team == 'w'):
            return '♙'
        else :
            return '♟'

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
        if ((self.pos[0]==2) and (self.team == 'b'))| ((self.pos[0]==7) and (self.team == 'w')):
            d*=2
            if not (isinstance(Pieces.piece_on(self.pos[0]+d,self.pos[1]),Pieces)):
                mooves.append((self.pos[0]+d,self.pos[1]))
        if self.pos[1]==5:
            if (self.team =='w') and (self.pos[0]==4):
                if Pieces.piece_on(4,4).__str__() == "bp":
                    if Pieces.list_mv[-1] == ((2,4),(4,4),"-"):
                        mooves.append((3,4))
                if Pieces.piece_on(4,6).__str__() == "bp":
                    if Pieces.list_mv[-1] == ((2,6),(4,6),"-"):
                        mooves.append((3,6))
            if (self.team =='b') and (self.pos[0]==5):
                if Pieces.piece_on(5,4).__str__() == "wp":
                    if Pieces.list_mv[-1] == ((7,4),(5,4),"-"):
                        mooves.append((6,4))
                if Pieces.piece_on(4,6).__str__() == "wp":
                    if Pieces.list_mv[-1] == ((7,6),(5,6),"-"):
                        mooves.append((6,6))
        return mooves

    def promote(self):
        continu = True
        pos = self.pos
        team = self.team
        self.supr()
        while continu:
            name = input ("in to which piece will you promote youre pawn ?")
            if name== 'r':
                Rook(pos,team)
                continu = False
            if name== 'k':
                Knight(pos,team)
                continu = False
            if name== 'b':
                Bishop(pos,team)
                continu = False
            if name== 'q':
                Queen(pos,team)
                continu = False


    def make_moove(self, pos):
        var = "-"
        d = -1
        if self.team == 'w':
            d = 1
        p = Pieces.piece_on(pos[0],pos[1])
        if isinstance(p,Pieces):
            var = p.__str__()
            Pieces.piece_on(pos[0],pos[1]).supr()
        else:
            mooves =[]
            for i in range (1,5):
                mooves+= self.moove_diag(i,limit=1)
            if pos in mooves:
                Pieces.piece_on(pos[0]+d,pos[1]).supr()
                var = "ep"
        Pieces.list_mv.append((self.pos,pos,var))
        self.pos = pos
        if ((self.team == 'w') and (pos[0] == 1)) | ((self.team == 'b') and (pos[0] == 8)) :
            self.promote()
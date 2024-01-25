class P4:
    def __init__(self):
        self.plateau = [[0 for i in range(6)] for j in range(7)] #Tableau de colonnes 
        self.cPlayer = 1
        self.last = {'x': -1, 'y': -1}
        self.win = False
        self.autoCheck = False

    def print(self):
        transpose = [[0 for i in range(7)] for j in range(6)] #Tableau de lignes 
        for i in range(7):
            for j in range(6):
                transpose[j][i] = self.plateau[i][j]
        for i in range(5,-1,-1):
            print(transpose[i])

    def play(self, pid:int, x:int):
        if x not in range (7):
            return -1
        y=0
        while y<=5:
            if not self.plateau[x][y]:
                self.plateau[x][y]=pid
                self._pSwap()
                self.last = {'x': x, 'y': y}
                return y
            y+=1
        return -1

    def _pSwap(self):
        self.cPlayer = 1 if self.cPlayer==2 else 2

    def getCombs(self,x:int,y:int):
        c ="".join( [str(id) for id in self.plateau[x]] )
        r ="".join( [str(col[y]) for col in self.plateau] )

        z1 = min(x,y)
        xz1 = x-z1
        yz1 = y-z1
        rg1 = min(6-xz1, 5-yz1)+1
        print(f"diag1-> {xz1,yz1} length:{rg1}")
        d1="".join( [str(self.plateau[i+xz1][i+yz1]) for i in range(rg1)] )

        z2 = min(6-x,y)
        xz2=x+z2
        yz2=y-z2
        rg2 = min(xz2, 5-yz2)+1
        print(f"diag2-> {xz2, yz2} length:{rg2}")
        d2="".join( [str(self.plateau[xz2-i][i+yz2]) for i in range(rg2)] )[::-1]

        return {'c': c, 'r': r, 'd1': d1, 'd2': d2}

    def check(self, x:int, y:int):
        if not self.win:
            pid = self.plateau[x][y]
            print(f"Check win Player {pid} c{x,y}")
            cb = self.getCombs(x,y)
            cbString = "|".join([str(cb[i]) for i in cb])
            print(cbString,cb)

            if(cbString.count(str(pid)*4) == 0):
                return False
            else:
                self.win=pid
        return True
    
    def checkLast(self):
        self.check(self.last['x'],self.last['y'])

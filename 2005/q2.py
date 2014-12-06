class column:
    def __init__(self):
        self.data = []
    def addToken(self,char):
        self.data.append(char)
    def printColumn(self):
        for i in self.data:
            print i

class board:
    def __init__(self,n):
        self.columns = [column() for i in range(0,n)]
    def addToken(self,column,char):
        self.columns[column].addToken(char)
        print column
        self.columns[column].printColumn()
    def printBoard(self):
        for i in range(0,6):
            
            for c in self.columns:
                if(5 - i <= len(c.data)-1):
                    print c.data[5 - i] + " ",
                else:
                    print "- ",
                    
            print
        print"",
b = board(10)
b.addToken(0,'*')
b.printBoard()

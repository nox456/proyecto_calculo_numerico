class SigFigures:

    __isZero=True
    __number=""

    def __init__(self, number):
        self.__number=number


    def getNumber(self):
        return self.__number
    
    def setNumber(self, num):
        self.__number=num

    def cantFigures(self):
        figures=""
        cont=0
        for digit in self.__number:
            if(digit!="0" and digit!="." and digit!=","):
                self.__isZero=False
            if(self.__isZero==False):
               cont+=1
               figures+=digit
            if(digit=="." or digit==","):
                cont-=1
        self.__isZero=True
        return cont, figures
    
    def mostrar(self):
        cont, figures =self.cantFigures()
        print("Cantidad de cifras: "+str(cont))
        print("\nCifras en si: "+figures)
    
obj= SigFigures("012.5")
obj.mostrar()

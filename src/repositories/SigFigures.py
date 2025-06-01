class SigFigures:

    __isZero=True
    __number=""

    def __init__(self, number):
        if(self.utilNumber(number)):
            self.__number=number
        else:
            raise Exception("Manage-Error: El numero está vacio.")

    #getters
    def getNumber(self):
        return self.__number
    
    #setters
    def setNumber(self, number):
        if(self.utilNumber(number)):
            self.__number=number
        else:
            raise Exception("Manage-Error: El numero está vacio.")

    #functions
    def operation(self):
        num1,num2=self.separateNumber()
        cont, fig=self.cantFigures(num1)
        cont2,fig2=self.cantFigures(reversed(num2))
        cont+=cont2
        rfig2=fig2[::-1]
        fig+=rfig2
        self.mostrar(cont,fig)

    def separateNumber(self):
        flag = False
        number1=""
        number2=""
        for digits in self.__number:
            if(digits!="." and digits!="." and flag==False):
                number1+=digits
            else:
                flag=True
            if(flag):
                number2+=digits
        print("n1:"+str(number1)+" n2: "+str(number2))
        return number1, number2
        

    def cantFigures(self,num):
        figures=""
        cont=0
        for digit in num:
            if(digit!="0" and digit!="." and digit!=","):
                self.__isZero=False
            if(self.__isZero==False):
               cont+=1
               figures+=digit
            if(digit=="." or digit==","):
                cont-=1
        self.__isZero=True
        return cont, figures
    
    def mostrar(self,con,figures):
        print("Cantidad de cifras: "+str(con))
        print("\nCifras en si: "+figures)

    #utilitaries
    def utilNumber(self, number):
        if(number==""):
            return False
        return True

    
obj= SigFigures("112.5001")
obj.operation()

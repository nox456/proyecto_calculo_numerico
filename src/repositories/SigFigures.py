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
        return self.mostrar(cont,fig)

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
        return number1, number2
        

    def cantFigures(self,num):
        isADot=False
        figures=""
        cont=0
        cantDots=0
        for digit in num:
            if(digit!="0" and digit!="." and digit!=","):
                self.__isZero=False
            if(self.__isZero==False):
               cont+=1
               figures+=digit
            if(digit=="." or digit==","):
                cantDots+=1
                cont-=1
            if(cantDots>=2):
                raise Exception("Manage -Error: Doble punto decimal")
        self.__isZero=True
        return cont, figures
    
    def mostrar(self,con,figures):
        return "Cantidad de cifras: "+str(con)+" Cifras en si: "+figures


    #utilitaries
    def utilNumber(self, number):
        if(number==""):
            return False
        return True


import random

class Balance:
    def __init__(self, value):
        self.value = value
    
    def plus(self, value):
        self.value += value
        
    def minus(self, value):
        self.value -= value
        
    def get(self):
        return self.value

class OperationParameter:
    def __init__(self, parameter):
        self.parameter = parameter
    
    def printParameter(self, value):
        return "\n\t\t<" + self.parameter + ">" + value + "" + "<\\" + self.parameter + ">"
        
class ExecDate(OperationParameter):
    def __init__(self):
        OperationParameter.__init__(self, "exec-date")
        
    def printParameter(self, i):
        month = int((i + 2) / 30) + 1
        day = ((i + 2) % 30) + 1
        value = "2019-0" + str(month) + "-" + str(day)
        return OperationParameter.printParameter(self, value)
    
class OrderDate(OperationParameter):
    def __init__(self):
        OperationParameter.__init__(self, "order-date")
        
    def printParameter(self, i):
        month = int(i / 30) + 1
        day = (i % 30) + 1
        value = "2019-0" + str(month) + "-" + str(day)
        return OperationParameter.printParameter(self, value)
    
class Type(OperationParameter):
    def __init__(self):
        OperationParameter.__init__(self, "type")
        
    def printParameter(self, i):
        return OperationParameter.printParameter(self, "Platnosc karta")
    
class Description(OperationParameter):
    def __init__(self):
        OperationParameter.__init__(self, "description")
        
    def printParameter(self, i, price):
        month = int(i / 30) + 1
        day = (i % 30) + 1
        title = "Tytul: 09016606177698710044149"
        localization = "Lokalizacja: Kraj: POLSKA Miasto: Poznan Adres: Poznan    91237"
        date = "Data i czas operacji: 2019-0" + str(month) + "-" + str(day)
        amount = "Oryginalna kwota operacji: " + str(price) + " PLN"
        number = "Numer karty: 265497******4678"
        value = title + "\n" + localization + "\n" + date + "\n" + amount + "\n" + number
        return OperationParameter.printParameter(self, value)
    
class Amount(OperationParameter):
    def __init__(self):
        OperationParameter.__init__(self, "amount")
        
    def printParameter(self, i, price):
        return "\n\t\t<" + self.parameter + " curr='PLN'>-" + str(price) + "</" + self.parameter + ">"
    
class EndingBalance(OperationParameter):
    def __init__(self):
        OperationParameter.__init__(self, "ending-balance")
        
    def printParameter(self, i, balance):
        return "\n\t\t<" + self.parameter + " curr='PLN'>+" + str(round(balance.get(), 2)) + "</" + self.parameter + ">"

class OperationGenerator:    
    def __init__(self, file, balance):
        self.file = file
        self.balance = balance
        
    def printStart(self):
        self.write("\n")
        self.write("\t")
        self.write("<operation>")

    def printOperation(self, i):
        price = round(random.uniform(0.01, 99.99), 2)
        self.balance.minus(price)
        self.write(ExecDate().printParameter(i))
        self.write(OrderDate().printParameter(i))
        self.write(Type().printParameter(i))
        self.write(Description().printParameter(i, price))
        self.write(Amount().printParameter(i, price))
        self.write(EndingBalance().printParameter(i, self.balance))
        
    def printEnd(self):
        self.write("\n")
        self.write("\t")
        self.write("</operation>")
        
    def write(self, text):
        self.file.write(text)

class Generator:
    def __init__(self):
        self.file = open("history_20200110_416816.xml", "w+")
        
    def printStart(self):
        self.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>")
        self.write("\n")
        self.write("<account-history>")
        self.write("\n")
        self.write("<search>\n\t<account>27310420801142527070027050</account>\n\t<date since='2019-01-10' to='2019-02-20'/>\n\t<filtering>Wszystkie</filtering>\n</search>")
        self.write("\n")
        self.write("<operations>")
        
    def printOperations(self):
        balance = Balance(10000)
        for i in range(100):
            operation = OperationGenerator(self.file, balance)
            operation.printStart()
            operation.printOperation(i)
            operation.printEnd()
        
    def printEnd(self):
        self.write("\n")
        self.write("</operations>")
        self.write("\n")
        self.write("</account-history>")
        self.close()
        
    def write(self, text):
        self.file.write(text)
        
    def close(self):
        self.file.close()



print("Start")
generator = Generator()
generator.printStart()
generator.printOperations()
generator.printEnd()
print("End")
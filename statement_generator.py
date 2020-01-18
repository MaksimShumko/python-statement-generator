class OperationGenerator:
    
    def __init__(self, file):
        self.file = file
        
    def printStart(self):
        self.write("\n")
        self.write("\t")
        self.write("<operation>")

    def printOperation(self, i):
        self.write("\n")
        self.write("\t\t")
        month = int(i / 30) + 1
        day = (i % 30) + 1
        self.write("<exec-date>2019-0" + str(month) + "-" + str(day) + "</exec-date>")
        
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
        for i in range(100):
            operation = OperationGenerator(self.file)
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
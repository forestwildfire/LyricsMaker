class GenerateOutput:

    stringArray=[]

    def __init__(self, stringArray ):
        if(type(stringArray)==str):
            self.stringArray = stringArray.split(" ")
        elif(type(stringArray)==list):
            self.stringArray = stringArray



    def consoleOutput(self):
        nextCap = True
        for i in self.stringArray:
            if(i=='\\n'):
                print("")
                nextCap = True
            else:
                if(nextCap==True or i == "i" or i == "i've" or i == "i'd" or i == "i'll"):
                    i=i.capitalize()
                print i,
                nextCap=False
        print ("\n\n\n\n\n\n\n")


    def fileOutput(self, filename):
        with file(filename+".txt","w+") as f:
            nextCap = True
            for i in self.stringArray:
                if(i=='\\n'):
                    f.write("\n")
                    nextCap = True
                else:
                    if(nextCap==True or i == "i" or i == "i've" or i == "i'd" or i == "i'll"):
                        i=i.capitalize()
                    f.write(i+" ")
                    nextCap=False

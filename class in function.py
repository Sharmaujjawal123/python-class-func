class student:
    def stud(self):
        self.name=input("N: ")
        self.roll=int(input("R: "))
        self.perc=eval(input("P: "))

    def display(self):
        print("Name",self.name)
        print("roll",self.roll)
        print("percenr",self.perc)
a= student()
a.stud()
a.display()
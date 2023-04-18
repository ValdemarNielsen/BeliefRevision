from sympy import *

x, y = symbols('x,y')

class BeliefRevision():
    def __init__(self, master=None):

        print("hello")
        self.master = master
        self.master.title("Belief Revision")
        self.master.geometry("500x500")
        self.master.resizable(0, 0)
        self.master.configure(background='white')
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.frame = Frame(self.master, background='white')
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_propagate(False)
        self.createWidgets()



    def check_logic(self):
        print("hey")

    def beliefBase(self):
        print("hello")

    def createWidgets(self):
        self.button = Button(self.frame, text="Check Logic", command=self.check_logic)
        self.button.grid(row=0, column=0)
        self.button = Button(self.frame, text="Belief Base", command=self.beliefBase)
        self.button.grid(row=0, column=1)

if __name__ == "__main__":
    root = Tk()
    app = BeliefRevision(root)
    root.mainloop()





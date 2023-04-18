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
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_propagate(False)
        self.createWidgets()



    def check_logic(self):
        print("hey")

    def beliefBase(self):
        print("hello")

#Run check_logic
if __name__ == '__main__':
    app = BeliefRevision(root)
    root.mainloop()
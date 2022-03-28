from tkinter import *

class editor:
    def __init__(self, root):
        self.root = root
        self.root.title("CRINGEPAD++")
        self.root.geometry("500x600+200+150")
        self.root.config(bg="black")

        scroll_y = Scrollbar(self.root,orient=VERTICAL)

        self.txtarea = Text(
            self.root,
            yscrollcommand=scroll_y.set,
            font=("Arial",14,"bold"),
            state="normal",
            bg="black",
            fg="green",
            bd=0,
            highlightcolor="black",
            insertbackground="green",
            relief=GROOVE
        )

        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        self.save = Button(
            self.root,
            text="Save",
            font=("Arial", 16, "bold"),
            command=self.save_file,
            relief=GROOVE
        )
        self.save.pack(side=LEFT, fill=NONE)

        self.run = Button(
            self.root,
            text="Run",
            font=("Arial", 16, "bold"),
            command=self.run_code,
            relief=GROOVE
        )
        self.run.pack(side=LEFT, fill=NONE)

    def save_file(self):
        with open("notes.txt", "w") as file:
            file.write(self.txtarea.get("1.0", END))
    
    def run_code(self):
        exec(self.txtarea.get("1.0", END))

root = Tk()
editor(root)
root.mainloop()

import tkinter
import tkinter.messagebox
from PIL import Image
from PIL import ImageTk
from PIL import ImageGrab


HEAD = 0
HAIR = 1
EYES = 2
NOSE = 3
MOUTH = 4


class App:
    def __init__(self):
        self.folders = {
            "Head": {},
            "Hair": {},
            "Eyes": {},
            "Nose": {},
            "Mouth": {},
        }
        self.options = {
            "heads": [f"Head 1{' ' * 46}", f"Head 2{' ' * 46}", f"Head 3{' ' * 46}"],
            "hairs": [f"Hair 1{' ' * 47}", f"Hair 2{' ' * 47}", f"Hair 3{' ' * 47}"],
            "eyes": [f"Eyes 1{' ' * 47}", f"Eyes 2{' ' * 47}", f"Eyes 3{' ' * 47}"],
            "noses": [f"Nose 1{' ' * 46}", f"Nose 2{' ' * 46}", f"Nose 3{' ' * 46}"],
            "mouthes": [f"Mouth 1{' ' * 43}", f"Mouth 2{' ' * 43}", f"Mouth 3{' ' * 43}"],
            "formats": ["jpg", "png", "jpeg"]
        }
        self.choices = [False, False, False, False, False]
        self.canvas = None
        self.path = None
        self.head = None
        self.hair = None
        self.eyes = None
        self.nose = None
        self.mouth = None

    def launch(self):
        global headdefault, hairdefault, eyesdefault, nosedefault, mouthdefault


        def getHead(choice):
            choice = headdefault.get().replace(' ' * 46, "", 1)

            flag = True
            for isValid in self.choices[1:]:
                if isValid:
                    flag = False
                    break

            if flag:
                try:
                    self.folders["Head"][choice] = ImageTk.PhotoImage(self.folders["Head"][choice])
                except:
                    pass

                if not self.choices[HEAD]:
                    self.head = self.canvas.create_image(320, 180, image=self.folders["Head"][choice])
                    self.choices[HEAD] = True
                else:
                    self.canvas.itemconfigure(self.head, image=self.folders["Head"][choice])
            else:
                tkinter.messagebox.showerror(title="Error", message="Unable to change the head.")

        def getHair(choice):
            choice = hairdefault.get().replace(' ' * 47, "", 1)

            flag = True
            if not self.choices[HEAD]:
                flag = False

            if flag:
                try:
                    self.folders["Hair"][choice] = ImageTk.PhotoImage(self.folders["Hair"][choice])
                except:
                    pass

                if not self.choices[HAIR]:
                    self.hair = self.canvas.create_image(320, 180, image=self.folders["Hair"][choice])
                    self.choices[HAIR] = True
                else:
                    self.canvas.itemconfigure(self.hair, image=self.folders["Hair"][choice])
            else:
                tkinter.messagebox.showerror(title="Error", message="Choose a head first.")
                hairdefault.set("---                                                  ")

        def getEyes(choice):
            choice = eyesdefault.get().replace(' ' * 47, "", 1)

            flag = True
            if not self.choices[HEAD]:
                flag = False

            if flag:
                try:
                    self.folders["Eyes"][choice] = ImageTk.PhotoImage(self.folders["Eyes"][choice])
                except:
                    pass

                if not self.choices[EYES]:
                    self.eyes = self.canvas.create_image(320, 180, image=self.folders["Eyes"][choice])
                    self.choices[EYES] = True
                else:
                    self.canvas.itemconfigure(self.eyes, image=self.folders["Eyes"][choice])
            else:
                tkinter.messagebox.showerror(title="Error", message="Choose a head first.")
                eyesdefault.set("---                                                  ")

        def getNose(choice):
            choice = nosedefault.get().replace(' ' * 46, "", 1)

            flag = True
            if not self.choices[HEAD]:
                flag = False

            if flag:
                try:
                    self.folders["Nose"][choice] = ImageTk.PhotoImage(self.folders["Nose"][choice])
                except:
                    pass

                if not self.choices[NOSE]:
                    self.nose = self.canvas.create_image(320, 180, image=self.folders["Nose"][choice])
                    self.choices[NOSE] = True
                else:
                    self.canvas.itemconfigure(self.nose, image=self.folders["Nose"][choice])
            else:
                tkinter.messagebox.showerror(title="Error", message="Choose a head first.")
                nosedefault.set("---                                                  ")

        def getMouth(choice):
            choice = mouthdefault.get().replace(' ' * 43, "", 1)

            flag = True
            if not self.choices[HEAD]:
                flag = False

            if flag:
                try:
                    self.folders["Mouth"][choice] = ImageTk.PhotoImage(self.folders["Mouth"][choice])
                except:
                    pass
                
                if not self.choices[MOUTH]:
                    self.mouth = self.canvas.create_image(320, 180, image=self.folders["Mouth"][choice])
                    self.choices[MOUTH] = True
                else:
                    self.canvas.itemconfigure(self.mouth, image=self.folders["Mouth"][choice])
            else:
                tkinter.messagebox.showerror(title="Error", message="Choose a head first.")
                mouthdefault.set("---                                                  ")
            
        self.load()

        self.master = tkinter.Tk()
        self.master.title("Character Generator")
        self.master.minsize(896, 416)
        self.master.maxsize(896, 416)

        headlabel = tkinter.Label(self.master, text="Head:", highlightthickness=0)
        headlabel.grid(row=0, column=0, sticky="w")

        headdefault = tkinter.StringVar(self.master)
        headdefault.set("---                                                  ")

        headdrop = tkinter.OptionMenu(self.master, headdefault, *self.options["heads"], command=getHead)
        headdrop.grid(row=1, column=0, pady=5, sticky="e")

        hairlabel = tkinter.Label(self.master, text="Hair:", highlightthickness=0)
        hairlabel.grid(row=2, column=0, sticky="w")

        hairdefault = tkinter.StringVar(self.master)
        hairdefault.set("---                                                  ")

        hairdrop = tkinter.OptionMenu(self.master, hairdefault, *self.options["hairs"], command=getHair)
        hairdrop.grid(row=3, column=0, pady=5, sticky="e")

        eyeslabel = tkinter.Label(self.master, text="Eyes:", highlightthickness=0)
        eyeslabel.grid(row=4, column=0, sticky="w")

        eyesdefault = tkinter.StringVar(self.master)
        eyesdefault.set("---                                                  ")

        eyesdrop = tkinter.OptionMenu(self.master, eyesdefault, *self.options["eyes"], command=getEyes)
        eyesdrop.grid(row=5, column=0, pady=5, sticky="e")

        noselabel = tkinter.Label(self.master, text="Nose:", highlightthickness=0)
        noselabel.grid(row=6, column=0, sticky="w")

        nosedefault = tkinter.StringVar(self.master)
        nosedefault.set("---                                                  ")

        nosedrop = tkinter.OptionMenu(self.master, nosedefault, *self.options["noses"], command=getNose)
        nosedrop.grid(row=7, column=0, pady=5, sticky="e")

        mouthlabel = tkinter.Label(self.master, text="Mouth:", highlightthickness=0)
        mouthlabel.grid(row=8, column=0, sticky="w")

        mouthdefault = tkinter.StringVar(self.master)
        mouthdefault.set("---                                                  ")

        mouthdrop = tkinter.OptionMenu(self.master, mouthdefault, *self.options["mouthes"], command=getMouth)
        mouthdrop.grid(row=9, column=0, pady=5, sticky="e")

        clearbutton = tkinter.Button(text="Clear", highlightthickness=0, width=14, height=2, command=self.clear)
        clearbutton.grid(row=10, column=0, pady=5, sticky="w")

        savebutton = tkinter.Button(text="Save", highlightthickness=0, width=14, height=2, command=self.save)
        savebutton.grid(row=10, column=0, pady=5, sticky="e")

        self.canvas = tkinter.Canvas(width=640, height=368, background="white")
        self.canvas.grid(row=1, column=2, rowspan=10, padx=20)

        self.master.mainloop()

    def clear(self):
        response = tkinter.messagebox.askokcancel(title="Warning", message="Your work won't be saved,\nwish to continue?")

        if response:
            self.canvas.delete("all")
            self.choices = [False, False, False, False, False]

            headdefault.set("---                                                  ")
            hairdefault.set("---                                                  ")
            eyesdefault.set("---                                                  ")
            nosedefault.set("---                                                  ")
            mouthdefault.set("---                                                  ")

            self.load()

    def save(self):
        def save():
            name = nameinput.get()
            if len(name) == 0:
                tkinter.messagebox.showwarning(title="Warning", message="Fill name entry.", parent=frame)
            else:
                master.destroy()
                path = f"images/{format}/{name}.{format}"

                xStart = self.master.winfo_rootx() + self.canvas.winfo_x() + 256
                yStart = self.master.winfo_rooty() + self.canvas.winfo_y() + 64
                xEnd = xStart + self.canvas.winfo_width() - 160
                yEnd = yStart + self.canvas.winfo_height()

                cordinations = (xStart, yStart, xEnd, yEnd)
                ImageGrab.grab().crop(cordinations).save(path)

        def getFormat(choice):
            global format

            choice = default.get()
            format = choice

        master = tkinter.Toplevel(self.master)
        frame = tkinter.Frame(master)
        master.title("Save as")
        master.minsize(336, 128)
        master.maxsize(336, 128)

        namelabel = tkinter.Label(frame, text="Name:", highlightthickness=0)
        namelabel.grid(row=0, column=0, pady=10)

        nameinput = tkinter.Entry(frame, width=30)
        nameinput.grid(row=0, column=1, pady=10)
        nameinput.focus()

        default = tkinter.StringVar(frame)
        default.set("----")

        suffixlabel = tkinter.Label(frame, text="Format:", highlightthickness=0)
        suffixlabel.grid(row=1, column=0, pady=10)

        suffixdrop = tkinter.OptionMenu(frame, default, *self.options["formats"], command=getFormat)
        suffixdrop.grid(row=1, column=1, pady=5, sticky="e")

        savebutton = tkinter.Button(frame, text="Save", highlightthickness=0, width=14, command=save)
        savebutton.grid(row=2, column=0, columnspan=2, pady=10)

        frame.pack()

    def load(self):
        for folder, container in self.folders.items():
            for item in range(1, 4):
                path = f"images/assets/{folder.lower()}/{folder.lower()}-{item}.png"
                png = Image.open(path)

                container.update({f"{folder} {item}": png})
import tkinter as tk
# from PIL import ImageTk, Image

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.create_widgets()
        self.pack()
    
    def create_widgets(self):
        self.var = tk.Button(self)
        self.var['text'] = 'Is it working?\n(Click here to confirm)'
        self.var['command'] = self.action
        self.var.pack(side = 'bottom')

        self.quit = tk.Button(self, text = 'Get off', fg = 'black', command = self.master.destroy)
        self.quit.pack(side = 'top')
    
    def action(self):
        print('Yes, it is')
        '''
root = Tk()
img = ImageTk.PhotoImage(Image.open('C:\\Users\\thiago.zeferino\\Desktop\\imagem'))

label = Label(root, image = img)
label.pack(side =  'bottom', fill = 'both', expand = 'yes')
'''
root = tk.Tk()
app = Application(master = root)
app.mainloop()

import customtkinter
import os, random, time
from PIL import Image
from atomjoy.json_file import JsonFile

class TopBarFrame(customtkinter.CTkFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.command = command
        self.button_add = customtkinter.CTkButton(self, text="Add", command=command)
        self.button_add.pack(side="top", padx=20, pady=20)

class ScrollableLabelButtonFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1) # Strech grid columns in frame
        self.command = command
        self.radiobutton_variable = customtkinter.StringVar()
        self.label_list = []
        self.button_list = []
        self.loadItems()
    
    def add_item(self, item, code="000000", color="#FFECAB", text_color="#222222", image=None):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.config(pady=5, padx=5) # center padding bg=bg_color,
        fr = customtkinter.CTkFrame(self, corner_radius=5, fg_color=color)
        fr.grid_rowconfigure(0, weight=1)
        fr.grid_columnconfigure(1, weight=1)
        # Font
        label_font = customtkinter.CTkFont(family="Roboto", size=18, weight="bold")
        code_font = customtkinter.CTkFont(family="Quicksand", size=33)
        # Image
        path = os.path.join(current_dir, "images", "icon_default.png")
        fname = os.path.join(current_dir, "images/logo", str(item).lower() + ".png")
        if os.path.isfile(fname):
            path = fname
        label_img = customtkinter.CTkImage(Image.open(path), size=(28,28))
        # Label
        label = customtkinter.CTkLabel(fr, text=item.capitalize() , image=label_img, compound="left", padx=10, pady=10, anchor="w", text_color=text_color, font=label_font)
        label.grid(row=0, column=0, padx=10, pady=10, sticky="nw")
        self.label_list.append(label)
        # Code
        code_col = customtkinter.CTkLabel(fr, text=code, image=None, compound="left", padx=10, pady=10, anchor="w", text_color=text_color, font=code_font)
        code_col.grid(row=1, column=0, padx=10, pady=5, sticky="wn")
        # Button
        button = customtkinter.CTkButton(fr, height=40, width=40, text="", bg_color=color, fg_color="#ffffff", image=customtkinter.CTkImage(Image.open(os.path.join(current_dir, "images", "trash_light.png")), Image.open(os.path.join(current_dir, "images", "trash_light.png")))) # (light, dark) fg_color=("#2cbe79", "#2cbe79")
        if self.command is not None:
            button.configure(command=lambda: self.command(item))
        button.grid(row=0, column=1, pady=(10, 10), padx=10, sticky="e")
        self.button_list.append(button)
        # Expand frame
        fr.pack(fill=customtkinter.BOTH, expand=True, padx=0, pady=10)

    def remove_item(self, item):
        for label, button in zip(self.label_list, self.button_list):
            if item == label.cget("text"):
                label.destroy()
                button.destroy()
                self.label_list.remove(label)
                self.button_list.remove(button)
                return
            
    def removeAll(self):
        for child in self.winfo_children():
            child.destroy()

    def loadItems(self):
        js = JsonFile("secrets.json")
        x = 0   
        for i in js.getCodeArray():
            if x > 6:
                x = 0
            self.add_item(f"{i[0]}", f'{i[2]}', color=self.randomColor(x))
            x = x + 1

    def randomColor(self, nr):
        # #FFECABFF, #FFDBDBFF, #9CF3FFFF, #CEC6FFFF, #E2D2FEFF, #BAE5F4FF, #FCCDCDFF, gr: #EEEEEEFF
        i = random.randint(0, 6)
        c = ["#FFECAB", "#FFDBDB", "#9CF3FF", "#CEC6FF", "#BAF4C5", "#BAE5F4", "#F7D7A0", "#FCCDCD", "#E2D2FE",]
        return str(c[nr])

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.command = command
        self.title('Add secret')
        self.geometry("480x360")
        self.after(250, lambda: self.iconbitmap('images/icon.ico'))
        self.grid_columnconfigure(0, weight=1) # Strech grid columns in frame
        # Error
        self.err = customtkinter.CTkLabel(self, text="", anchor="center", height=40)
        self.err.grid(row=0, column=0, padx=15, pady=5, sticky="ew")   
        # Name
        self.label_name = customtkinter.CTkLabel(self, text="App Name", anchor="w")
        self.label_name.grid(row=1, column=0, padx=15, pady=5, sticky="ew")
        self.entry_name = customtkinter.CTkEntry(self, placeholder_text="Enter app name", height=40, font=("Roroto", 15))
        self.entry_name.grid(row=2, column=0, padx=15, pady=5, sticky="ew")
        # Secret
        self.label_secret = customtkinter.CTkLabel(self, text="2FA Secret", anchor="w")
        self.label_secret.grid(row=3, column=0, padx=15, pady=5, sticky="ew")
        self.entry_secret = customtkinter.CTkEntry(self, placeholder_text="Enter 2fa secret", height=40, font=("Roroto", 15))
        self.entry_secret.grid(row=4, column=0, padx=15, pady=5, sticky="ew")
        # Button
        self.btn = customtkinter.CTkButton(self, text="Add", command=self.add_event, height=40)
        self.btn.grid(row=6, column=0, padx=15, pady=30, sticky="ew")
        # self.label.pack(padx=10, pady=10)
    
    def add_event(self):
        name = self.entry_name.get()
        secret = self.entry_secret.get()
        print("Add....", name, secret)
        if len(name) >= 3:
            if len(secret) >= 16:                
                # Update
                try:
                    js = JsonFile("secrets.json")
                    js.addItem(name.lower(), secret.upper())
                    self.master.scrollable_label_button_frame.removeAll()
                    self.master.scrollable_label_button_frame.loadItems()
                    self.close_window()
                except Exception:
                    # Error
                    self.err.configure(text="Invalid secret chars (only base32 chars)")
                    self.err.configure(text_color="#f23")
            else:
                # Error
                self.err.configure(text="Invalid secret length (16min)")
                self.err.configure(text_color="#f23")
        else:
            # Error
            self.err.configure(text="Invalid name length (3min)")
            self.err.configure(text_color="#f23")

    def close_window(self):
        self.destroy()
        self.update()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.mode = True
        self.title("2FA Authentication")
        self.iconbitmap('images/icon.ico')
        self.geometry("480x660")
        self.resizable(False, True) # width, height
        self.grid_rowconfigure(0, weight=1) # Strech grid 1st row horizontalyin in frame
        self.columnconfigure(2, weight=1) # Strech grid 3rd column verticaly in frame        
        self.toplevel_window = None

        # create top bar
        self.topbar_frame = TopBarFrame(master=self, command=self.open_toplevel,)
        self.topbar_frame.grid(row=1, column=2, padx=15, pady=15, sticky="nwe")

        # create scrollable label and button frame        
        self.scrollable_label_button_frame = ScrollableLabelButtonFrame(master=self, width=300, corner_radius=5, 
            command=self.label_button_frame_event, 
            label_text="2FA Codes", 
            label_anchor="w",
            label_font=("Quicksand", 22),
            scrollbar_button_color=("#eaeaea", "#444444"))
        
        self.scrollable_label_button_frame.grid(row=0, column=2, padx=15, pady=15, sticky="nsew")        

    def label_button_frame_event(self, item):
        print(f"Remove item clicked: {item}")
        js = JsonFile("secrets.json")
        js.removeItem(item)
        self.scrollable_label_button_frame.removeAll()
        self.scrollable_label_button_frame.loadItems()
        
    def toggle_mode(self):
        if self.mode == True:
            self.mode = False
            customtkinter.set_appearance_mode("dark")
        else:
            self.mode = True
            customtkinter.set_appearance_mode("light")
       
    def update(self):
        t = time.strftime("%H:%M:%S", time.localtime())
        print("Update", t)
        self.scrollable_label_button_frame.removeAll()
        self.scrollable_label_button_frame.loadItems()
        # Refresh every 30s
        self.after(30000, self.update)

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed            
            self.toplevel_window.attributes('-topmost', True)
        else:
            self.toplevel_window.focus()  # if window exists focus it
            self.toplevel_window.attributes('-topmost', True)

if __name__ == "__main__":
    # Theme
    customtkinter.set_default_color_theme("themes/atomjoy.json")
    # customtkinter.set_default_color_theme("blue")
    
    # Mode
    customtkinter.set_appearance_mode("dark")
    # customtkinter.set_appearance_mode("light")

    # Run    
    app = App()        
    app.update()    
    app.mainloop()
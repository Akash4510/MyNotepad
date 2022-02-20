from tkinter import *
from tkinter import ttk


class Application(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title("Visual Studio Code ++")
        app_width, app_height = (850, 600)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)

        # This will display the application in the center of the screen.
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.menu_bar = MenuBar(self)
        self.config(menu=self.menu_bar)

        self.notepad = ttk.Notebook(self, width=app_width, height=app_height)
        self.notepad.pack(fill=BOTH, expand=True)

        self.new_file()

    @staticmethod
    def create_new_instance():
        Application().run()

    def new_file(self):
        new_tab = TextEditor(self.notepad)
        self.notepad.add(new_tab, text="    untitled    ")
        self.notepad.select(new_tab)
        new_tab.editor.focus_set()

    def run(self):
        self.mainloop()


class MenuBar(Menu):

    def __init__(self, parent: Application):
        Menu.__init__(self, parent)

        # File Menu
        file_menu = Menu(self, tearoff=0)
        file_menu.add_command(
            label="New",
            accelerator="Ctrl+N",
            command=lambda: parent.new_file()
        )
        file_menu.add_command(
            label="New window" + "  ",
            accelerator="Ctrl+Shift+N",
            command=lambda: parent.create_new_instance()
        )
        file_menu.add_command(
            label="Open...",
            accelerator="Ctrl+O",
            command=lambda: print("Working...")
        )
        file_menu.add_command(
            label="Save",
            accelerator="Ctrl+S",
            command=lambda: print("Working...")
        )
        file_menu.add_command(
            label="Save As...",
            accelerator="Ctrl+Shift+S",
            command=lambda: print("Working...")
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Print",
            accelerator="Ctrl+P",
            command=lambda: print("Working...")
        )
        file_menu.add_separator()
        file_menu.add_command(
            label="Exit",
            accelerator="Alt+F4",
            command=parent.quit
        )
        self.add_cascade(label="File", menu=file_menu)

        # Edit Menu
        edit_menu = Menu(self, tearoff=0)
        edit_menu.add_command(
            label="Undo",
            accelerator="Ctrl+Z",
            command=lambda: print("Working...")
        )
        edit_menu.add_command(
            label="Redo",
            accelerator="Ctrl+Y",
            command=lambda: print("Working...")
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Cut",
            accelerator="Ctrl+X",
            command=lambda: print("Working...")
        )
        edit_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=lambda: print("Working...")
        )
        edit_menu.add_command(
            label="Copy",
            accelerator="Ctrl+C",
            command=lambda: print("Working...")
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Find",
            accelerator="Ctrl+F",
            command=lambda: print("Working...")
        )
        edit_menu.add_command(
            label="Find Next",
            accelerator="F3",
            command=lambda: print("Working...")
        )
        edit_menu.add_command(
            label="Replace",
            accelerator="Ctrl+H",
            command=lambda: print("Working...")
        )
        edit_menu.add_command(
            label="Go To",
            accelerator="Ctrl+G",
            command=lambda: print("Working...")
        )
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Select All",
            accelerator="Ctrl+A",
            command=lambda: print("Working...")
        )
        edit_menu.add_command(
            label="Time/Date",
            accelerator="F5",
            command=lambda: print("Working...")
        )
        self.add_cascade(label="Edit", menu=edit_menu)

        # Format Menu
        format_menu = Menu(self, tearoff=0)
        format_menu.add_command(
            label="Word Wrap",
            command=lambda: print("Working...")
        )
        # format_menu.add_command(label="Font", command=font)
        self.add_cascade(label="Format", menu=format_menu)

        # View Menu
        view_menu = Menu(self, tearoff=0)
        view_menu.add_command(
            label="Status Bar",
            command=lambda: print("Working...")
        )
        self.add_cascade(label="View", menu=view_menu)

        # Help Menu
        help_menu = Menu(self, tearoff=0)
        help_menu.add_command(
            label="About Notepad",
            command=lambda: print("Working...")
        )
        self.add_cascade(label="Help", menu=help_menu)


class TextEditor(Frame):

    def __init__(self, parent, **kwargs):
        Frame.__init__(self, parent, kwargs)

        self.config(
            bg="#e0e0e0",
            width=parent.winfo_width(),
            height=parent.winfo_height()
        )

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.editor = Text(self, font=("Arial", 11, "normal"), wrap=WORD)
        self.editor.grid(row=0, column=0, sticky=NSEW)

        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row=0, column=1, sticky=NS)

        self.editor.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.editor.yview)


if __name__ == '__main__':
    app = Application()
    app.run()

import os.path

import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb


def main():
    text_editor = TextEditor()
    text_editor.mainloop()


class TextEditor(tk.Tk):
    def __init__(self):
        super(TextEditor, self).__init__()

        self.title('Ugly Text Editor')
        self.option_add('*Dialog.msg.font', 'Arial 12')

        self.minsize(640, 360)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())

        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.pack(fill='y', side='right')

        self.text_field = tk.Text(self, bd=0, highlightthickness=0, yscrollcommand=self.scrollbar.set)
        self.text_field.pack(fill='both', expand=True)

        self.scrollbar.config(command=self.text_field.yview)

        self.menu_bar = tk.Menu(self)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label='New', command=self.new_file)
        self.file_menu.add_command(label='Open...', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', command=self.save_file)
        self.file_menu.add_command(label='Save as...', command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Quit', command=self.quit)

        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.menu_bar.add_command(label='About', command=TextEditor.show_about)

        self.config(menu=self.menu_bar)

        self.filename = None

    def new_file(self):
        self.filename = None
        self.text_field.delete('1.0', 'end')

    def open_file(self):
        self.filename = fd.askopenfilename()

        if self.filename and os.path.isfile(self.filename):
            with open(self.filename, 'r') as f:
                self.text_field.delete('1.0', 'end')
                self.text_field.insert('end', f.read())

    def save_file(self):
        if self.filename and os.path.isfile(self.filename):
            with open(self.filename, 'w') as f:
                f.write(self.text_field.get('1.0', 'end'))
        else:
            self.save_file_as()

    def save_file_as(self):
        self.filename = fd.asksaveasfilename()

        if self.filename:
            with open(self.filename, 'w') as f:
                f.write(self.text_field.get('1.0', 'end'))

    @staticmethod
    def show_about():
        mb.showinfo(
            'About',
            'Ugly Text Editor v1.0\nDeveloped by Kirill Volozhanin\ngithub.com/JustKappaMan',
        )


if __name__ == '__main__':
    main()

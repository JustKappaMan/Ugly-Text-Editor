import os.path

import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb


def main():
    text_editor = TextEditor()
    text_editor.mainloop()


class TextEditor(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.iconbitmap('favicon.ico')
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
        self.file_menu.add_command(label='New', accelerator='Ctrl+N', command=self.new_file)
        self.file_menu.add_command(label='Open...', accelerator='Ctrl+O', command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Save', accelerator='Ctrl+S', command=self.save_file)
        self.file_menu.add_command(label='Save as...', accelerator='Ctrl+Shift+S', command=self.save_file_as)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Quit', accelerator='Ctrl+Q', command=self.quit)

        self.menu_bar.add_cascade(label='File', menu=self.file_menu)
        self.menu_bar.add_command(label='About', command=TextEditor.show_about)

        self.config(menu=self.menu_bar)

        self.bind('<Control-n>', lambda e: self.new_file())
        self.bind('<Control-N>', lambda e: self.new_file())
        self.bind('<Control-o>', lambda e: self.open_file())
        self.bind('<Control-O>', lambda e: self.open_file())
        self.bind('<Control-s>', lambda e: self.save_file())
        self.bind('<Control-S>', lambda e: self.save_file())
        self.bind('<Control-Shift-s>', lambda e: self.save_file_as())
        self.bind('<Control-Shift-S>', lambda e: self.save_file_as())
        self.bind('<Control-q>', lambda e: self.quit())
        self.bind('<Control-Q>', lambda e: self.quit())

        self.filename = None

    def new_file(self) -> None:
        self.filename = None
        self.text_field.delete('1.0', 'end')

    def open_file(self) -> None:
        self.filename = fd.askopenfilename()

        if self.filename and os.path.isfile(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.text_field.delete('1.0', 'end')
                self.text_field.insert('end', f.read())

    def save_file(self) -> None:
        if self.filename and os.path.isfile(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(self.text_field.get('1.0', 'end'))
        else:
            self.save_file_as()

    def save_file_as(self) -> None:
        self.filename = fd.asksaveasfilename()

        if self.filename:
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write(self.text_field.get('1.0', 'end'))

    @staticmethod
    def show_about() -> None:
        mb.showinfo(
            'About',
            'Ugly Text Editor v1.0\nDeveloped by Kirill Volozhanin\ngithub.com/JustKappaMan',
        )


if __name__ == '__main__':
    main()

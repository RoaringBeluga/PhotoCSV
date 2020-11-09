import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

from utilities.misc import bugprint


class MainWindow:
    input_dir = ''
    output_dir = ''
    output_file = 'out.csv'

    main_window = None
    selected_input_dir = None
    selected_output_dir = None
    selected_output_file = None

    select_input_dir_button = None
    select_output_dir_button = None
    select_output_file_button = None

    discombobulate_button = None

    callback = None

    def run(self):
        self.main_window.mainloop()

    def __init__(self, callback):

        self.callback = callback

        self.main_window = tk.Tk()
        self.main_window.configure(background='SystemButtonFace')
        self.main_window.title('Photometric report PDF Discombobulator')

        self.input_dir = os.path.abspath(os.path.curdir)
        self.output_dir = os.path.abspath(os.path.curdir)

        self.selected_input_dir = tk.StringVar()
        self.selected_input_dir.set(self.input_dir)
        self.selected_output_dir = tk.StringVar()
        self.selected_output_dir.set(self.output_dir)
        self.selected_output_file = tk.StringVar()
        self.selected_output_file.set(self.output_file)

        ttk.Label(
            self.main_window,
            text=' Input dir: ',
            background='SystemButtonFace'
        ).grid(row=0, column=0)
        ttk.Label(
            self.main_window,
            text='Output dir: ',
            background='SystemButtonFace'
        ).grid(row=1, column=0)
        ttk.Label(
            self.main_window,
            text='Output file: ',
            background='SystemButtonFace'
        ).grid(row=2, column=0)

        self.input_dir_field = ttk.Entry(
            self.main_window,
            textvariable=self.selected_input_dir
        ).grid(row=0, column=1)
        self.output_dir_field = ttk.Entry(
            self.main_window,
            textvariable=self.selected_output_dir
        ).grid(row=1, column=1)
        self.output_file_field = ttk.Entry(
            self.main_window,
            textvariable=self.selected_output_file
        ).grid(row=2, column=1)

        self.select_input_dir_button = ttk.Button(
            self.main_window,
            text='Select...'
        )
        self.select_input_dir_button.grid(row=0, column=2)
        self.select_input_dir_button.configure(command=self.select_input_dir)
        # Create output dir selection button...
        self.select_output_dir_button = ttk.Button(
            self.main_window,
            text='Select...'
        )
        self.select_output_dir_button.grid(row=1, column=2)
        self.select_output_dir_button.configure(command=self.select_output_dir)
        # Create output file selection button
        self.select_output_file_button = ttk.Button(
            self.main_window,
            text='Select...'
        )
        self.select_output_file_button.grid(row=2, column=2)
        self.select_output_file_button.configure(command=self.select_output_file)
        # The MAIN button that launches the process
        self.discombobulate_button = ttk.Button(
            self.main_window,
            text='Process reports!',
            command=self.process
        ).grid(row=4, column = 1)
        # Gets the requested values of the height and widht.
        windowWidth = self.main_window.winfo_reqwidth()
        windowHeight = self.main_window.winfo_reqheight()
        print("Width", windowWidth, "Height", windowHeight)
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.main_window.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(self.main_window.winfo_screenheight() / 2 - windowHeight / 2)
        # Positions the window in the center of the page.
        self.main_window.geometry("+{}+{}".format(positionRight, positionDown))

    def select_input_dir(self):
        temp_input_dir = filedialog.askdirectory(
            parent=self.main_window,
            initialdir=self.input_dir
        )
        if temp_input_dir != '':
            self.input_dir = temp_input_dir
        self.selected_input_dir.set(self.input_dir)

    def select_output_dir(self):
        temp_output_dir = filedialog.askdirectory(
            parent=self.main_window,
            initialdir=self.selected_output_dir.get()
        )
        bugprint(f'Set output dir to: {temp_output_dir}')
        if temp_output_dir != '':
            self.output_dir = temp_output_dir
        self.selected_output_dir.set(self.output_dir)

    def select_output_file(self):
        temp_output_file = filedialog.asksaveasfilename(
            parent=self.main_window,
            initialdir=self.output_dir,
            title='Select output file',
            filetypes=(('Comma-separated values', '*.csv'), ('All files', '*.*')),
            defaultextension='csv'
        )
        if temp_output_file is not None:
            self.output_file = temp_output_file
        self.selected_output_file.set(self.output_file)

    def process(self):
        # Call the function to do the real processing
        self.callback(
            self.selected_input_dir.get(),
            self.selected_output_dir.get(),
            self.selected_output_file.get()
        )
        # And now we can report the possible success
        messagebox.showinfo(
            title='Processing completed',
            message=(f'Input dir: {self.input_dir}\n'
                    f'Output dir: {self.output_dir}\n'
                    f'Output file: {self.output_file}'
                     )
        )

from tkinter import PhotoImage, END
import ttkbootstrap as ttk
from images import BACKGROUND
from PIL import ImageTk, Image
from gui.modals import Modal
import webbrowser
"""First window that displays when the program is opened"""


class MainWindow(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #  -----------------------SET BACKGROUND IMAGE FOR APPLICATION--------------------------------------------------
        self.background_image = ImageTk.PhotoImage(Image.open(BACKGROUND).resize((550, 650)))
        self.background_image2 = PhotoImage(file=BACKGROUND)
        # ---------------------SET APP COLOR THEME, CENTER SCREEN, SET SIZE, SET RESIZEABLE-----------------------------
        self.style.theme_use('cyborg')  # set the application color theme from ttkbootstrap
        self.width = 550
        self.height = 650
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.resizable(False, False)  # resize width and resize height is false
        # --------------------------TITLE, LOGO AND CENTER SCREEN-------------------------------------------------------
        self.overrideredirect(True)  # remove the title bar so we can customize it
        # ----------------------FRAME TO HOLD THE TITLE BAR-------------------------------------------------------------
        self.title_frame = ttk.Frame(self, bootstyle='success')
        self.title_frame.pack(fill='x')
        # to get the columns to stretch we have to configure the column weights in the frame
        self.title_frame.columnconfigure(0, weight=2)  # for the title
        self.title_frame.columnconfigure(1, weight=1)  # for the x button
        # ----------------------------NEW TITLE BAR---------------------------------------------------------------------
        self.title_text = ttk.Label(
            self.title_frame,
            text="IT'S SO HIP....",
            font=('Comic Sans MS', 10, 'bold'),
            bootstyle='inverse-success'
        )
        self.title_text.grid(row=0, column=0, padx=(20, 0), sticky='W')
        # ------------------------------------TITLE BAR CLOSE BUTTON----------------------------------------------------
        self.close_button = ttk.Button(
            self.title_frame,
            text='X',
            width=1,
            bootstyle='danger',
            command=self.destroy
        )
        self.close_button.grid(row=0, column=1, sticky='E', padx=(0, 10), pady=(5, 5))
        # ------------------------CREATE THE CANVAS FOR THE APPLICATION-------------------------------------------------
        self.my_canvas = ttk.Canvas(self, width=450, height=550, background='red')
        self.my_canvas.pack(fill='both', expand=True)
        self.my_canvas.create_image(0, 0, image=self.background_image, anchor='nw')

        #  -------------------------------------------HOW-TO BUTTON-----------------------------------------------------
        self.how_to_button = ttk.Button(
            self,
            text="How-To",
            width=20,
            bootstyle='info-outline',
            command=lambda: Modal("How to Use Application")
        )
        #  -------------------------------------------GITHUB BUTTON-----------------------------------------------------
        self.github_button = ttk.Button(
            self,
            text="Github Link",
            width=20,
            bootstyle='info-outline',
            command=lambda: webbrowser.open('https://github.com/vlovell24/Its_Hip_To_Be_A_Square')
        )
        # -----------------------------------------HOW MANY SIDES COMBOBOX----------------------------------------------
        self.sides_variable = ttk.StringVar()  # to store the user selection
        self.sides_entry_field = ttk.Combobox(
            self,
            width=40,
            textvariable=self.sides_variable,  # set text variable
            state='readonly'  # lock entry from user input
        )
        self.sides_entry_field['values'] = (1, 3, 4, 5, 6, 7, 8)  # values in combobox
        self.sides_entry_field.current(0)  # default/initial value
        self.sides_entry_field.bind('<<ComboboxSelected>>', self.show_sides)  # bind the combobox to show selections
        # -----------------------------------------UNIT OF MEASUREMENT COMBOBOX-----------------------------------------
        self.measurement_variable = ttk.StringVar()  # to store the user selection
        self.measurement_combobox = ttk.Combobox(
            self,
            width=40,
            textvariable=self.measurement_variable,  # set text variable
            state='readonly'  # lock entry from user input
        )
        # values in the measurement combobox
        self.measurement_combobox['values'] = ('Inches',
                                               'Centimeters',
                                               'Millimeters',
                                               'Feet',
                                               'Meters',
                                               'Miles',
                                               'Kilometers')
        self.measurement_combobox.current(0)  # set the default/initial value
        # ------------------------------NEW WAY TO MAKE THE ENTRIES, BIND THEM AND SET THE TEXT-------------------------
        self.int_to_string_numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
        self.side_entries = []
        for i in range(8):
            entry = ttk.Entry(
                self,
                width=30
            )
            entry.insert(END, f"Enter Length of Side {self.int_to_string_numbers[i]}")
            entry.bind("<KeyPress>", self.key_press)
            entry.bind("<Leave>", self.enable_start_button)
            self.side_entries.append(entry)
        # ----------------------------------LEFT MOUSE CLICK BIND-------------------------------------------------------
        # TODO: Find out why this fails in a loop. Something to do with the lambda
        self.side_entries[0].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[0], e))
        self.side_entries[1].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[1], e))
        self.side_entries[2].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[2], e))
        self.side_entries[3].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[3], e))
        self.side_entries[4].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[4], e))
        self.side_entries[5].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[5], e))
        self.side_entries[6].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[6], e))
        self.side_entries[7].bind("<1>", lambda e: self.validate_entry_field(self.side_entries[7], e))
        # ---------------------------------KEYPRESS BIND----------------------------------------------------------------
        # for index in range(8):
        #     self.side_entries[index].bind("<Leave>", self.enable_start_button)

        # --------------------------------CALCULATE BUTTON ON BOTTOM OF APPLICATION-------------------------------------
        self.calculate_button = ttk.Button(
            self,
            text='Calculate',
            width=20,
            bootstyle='success-outline',
            state='disabled',  # disabled until sides are entered for all sides
            command=lambda: Modal('Calculate Modal')
        )
        # **************************************************************************************************************
        #  -----------------------------------------ATTACHING TO CANVAS-------------------------------------------------
        # **************************************************************************************************************
        # -------------------------------------------TITLE TEXT---------------------------------------------------------
        self.my_canvas.create_text(275,
                                   75,
                                   text="It's Hip To Be a Square",
                                   font=('Comic Sans MS', 18, 'bold'),
                                   fill='#77b300')
        # ----------------------------------------HOW-TO BUTTON---------------------------------------------------------
        self.how_to_window = self.my_canvas.create_window(50,
                                                          10,
                                                          anchor='nw',
                                                          window=self.how_to_button)
        # ----------------------------------------GITHUB BUTTON---------------------------------------------------------
        self.github_button_window = self.my_canvas.create_window(350,
                                                                 10,
                                                                 anchor='nw',
                                                                 window=self.github_button)
        # ------------------------------SQUARES LIST STORAGE/SIDES BACKGROUND SQUARE------------------------------------
        # used to store modified canvas squares
        self.images = []
        self.create_transparency(60, 100, 490, 200, outline='#2A9FD6', fill='black', alpha=.5)
        # -----------------------------------------SIDES TEXT-----------------------------------------------------------
        self.my_canvas.create_text(275,
                                   115,
                                   text="How many sides does your shape have?",
                                   font=('Comic Sans MS', 14, 'bold'),
                                   fill='#2A9FD6')

        self.my_canvas.create_window(140, 150, anchor='nw', window=self.sides_entry_field)
        # -----------------------------------MEASUREMENT BACKGROUND SQUARE----------------------------------------------
        self.create_transparency(60, 220, 490, 320, outline='#2A9FD6', fill='black', alpha=.5)
        # -------------------------------------MEASUREMENT TEXT---------------------------------------------------------
        self.my_canvas.create_text(275,
                                   240,
                                   text="What Unit of Measurement would you like to use?",
                                   font=('Comic Sans MS', 12, 'bold'),
                                   fill='#2A9FD6')
        # ---------------------------------MEASUREMENT COMBOBOX---------------------------------------------------------
        self.my_canvas.create_window(140, 270, anchor='nw', window=self.measurement_combobox)
        # ------------------------------SIDES BACKGROUND SQUARE---------------------------------------------------------
        self.create_transparency(60, 340, 490, 550, outline='#2A9FD6', fill='black', alpha=.5)
        # --------------------------------SIDES BOXES CREATED BUT HIDDEN/8 IN TOTAL-------------------------------------
        self.sides_place_values = [(80, 350), (280, 350), (80, 400), (280, 400), (80, 450), (280, 450), (80, 500),
                                   (280, 500)]
        self.canvas_sides = []  # holds the canvas entries for iteration later
        for index, entry in enumerate(self.side_entries):
            canvas_side = self.my_canvas.create_window(self.sides_place_values[index][0],
                                                       self.sides_place_values[index][1],
                                                       anchor='nw',
                                                       window=self.side_entries[index])
            self.canvas_sides.append(canvas_side)
            if index != 0:              # show length one box as default value is set to one
                self.my_canvas.itemconfigure(canvas_side, state='hidden')

        # ----------------------------------------CALCULATE BUTTON------------------------------------------------------
        # @TODO: This button should be disabled until sides are entered
        self.calculate_button_window = self.my_canvas.create_window(200,
                                                                    570,
                                                                    anchor='nw',
                                                                    window=self.calculate_button)

    def create_transparency(self, x, y, a, b, **options):
        """To create transparency in a square canvas image as this is not a modifiable parameter in tkinter. First we
        must get the square, remove the alpha param from the options, remove the fill option and modify it, then create
        a new image with the fill set to the fill option param that we modified. Then we append this new image onto the
        image array that we store in the class(for this purpose). Then create a canvas image and then create the
        rectangle
        """
        if 'alpha' in options:
            alpha = int(options.pop('alpha') * 255)  # pop alpha off of the params
            fill = options.pop('fill')  # do the same with fill
            fill = self.winfo_rgb(fill) + (alpha,)  # reset variable for fill to be alpha + fill
            image = Image.new('RGBA', (a - x, b - y), fill)  # create image with coors, and fill converted to rgba
            self.images.append(ImageTk.PhotoImage(image))  # append onto the images array
            self.my_canvas.create_image(x, y, image=self.images[-1], anchor='nw')  # draw the image on canvas
            self.my_canvas.create_rectangle(x, y, a, b, **options)  # create rectangle

    def validate_entry_field(self, side, event):
        """On entry field enter, check if the default text is in there. If it is, then delete the contents. If anything
        else is in the entry field, then leave the contents intact as it is user placed content
        """
        if "Length of Side" in side.get():
            side.delete(0, END)

    # @TODO: Validate only one . allowed
    def key_press(self, event):
        """When the user presses a key inside the entry field, compare against the keys tuple. If the keypress is
        found in the tuple, then allow it to be added to the entry field. If it is NOT in the tuple, do not allow the
        keypress to be registered/created in the entry field.
        """
        keys = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', '')  # allowed keys
        if event.char not in keys and event.keysym != 'BackSpace':
            return 'break'

    def show_sides(self, event):
        """
        Show_sides stores the cast to int value in the sides_selected variable. Then, using enumerate canvas_sides
        list is iterated through and the state of each canvas item is set to hidden, The text is deleted from the
        entry field and replaced with the default text. If a user decided they want 8 sides, changes values and then
        changes their mind, and selects 2 sides, this sets all the entry field text to the default values. Once this is
        done, a ranged for loop is used to toggle the selected fields state to normal.
        :param event:
        :return: None, toggles entry fields.
        """
        sides_selected = int(self.sides_entry_field.get())  # how many sides did the user select from the dropdown?
        # first set all the side length fields to hidden, then set selected number to normal
        for index, side in enumerate(self.canvas_sides):
            self.my_canvas.itemconfigure(side, state='hidden')
            self.side_entries[index].delete(0, "")                  # delete the text
            self.side_entries[index].insert(END, f"Enter Length of Side {self.int_to_string_numbers[index]}")
        for item in range(0, sides_selected):
            self.my_canvas.itemconfigure(self.canvas_sides[item], state='normal')   # show entry field

    def enable_start_button(self, event):
        # @TODO: Finish enabling the calculate button in the if/else statement
        sides_selected = int(self.sides_entry_field.get())  # number of sides user selected cast to int
        for index in range(sides_selected):
            if "Enter Length of Side" in self.side_entries[index].get():
                print("It's default still")
            else:
                print("It's good")


if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()

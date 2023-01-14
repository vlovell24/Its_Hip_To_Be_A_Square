import ttkbootstrap as ttk
from images import RUBIKS, CIRCLE
import tkinter


class Modal(ttk.Toplevel):
    """Parent popup modal class"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grab_set()  # do not allow user to click on parent application window

        # ------------------------CENTER SCREEN, SET SIZE, SET NO RESIZEABLE--------------------------------------------
        self.width = 400
        self.height = 500
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.resizable(False, False)  # resize width and resize height is false
        self.logo = ttk.PhotoImage(file=RUBIKS)
        self.iconphoto(False, self.logo)
        # ---------------------------------------FRAME TO HOLD THE MAIN CONTENT-----------------------------------------
        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill='x')
        self.title_frame.columnconfigure(0, weight=1)


class HowToModal(Modal):
    """Modal to show the how-to use application screen"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Testing")
        # ----------------------------------------HOW TO LABEL----------------------------------------------------------
        self.title_label = ttk.Label(
            self.title_frame,
            text="HOW TO USE THIS PROGRAM",
            font=('Comic Sans MS', 14, 'bold'),
            bootstyle='info'
        )
        self.title_label.grid(row=0, column=0, pady=10)


class CalculateModal(Modal):
    """Modal to show the calculate shape screen"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Shape Calculate")
        # ----------------------------------------IMAGE-----------------------------------------------------------------
        self.circle_image = ttk.PhotoImage(file=CIRCLE)
        # ----------------------------------------TITLE LABEL-----------------------------------------------------------
        self.title_label = ttk.Label(
            self.title_frame,
            text="Your Shape is a Circle",
            font=('Comic Sans MS', 14),
            bootstyle='primary'
        )
        self.title_label.grid(row=0, column=0, pady=10)
        # --------------------------------------------IMAGE LABEL-------------------------------------------------------
        self.image_label = ttk.Label(
            self.title_frame,
            image=self.circle_image
        )
        self.image_label.grid(row=1, column=0, padx=10)
        # ------------------------------------------CALCULATIONS FRAME--------------------------------------------------
        self.calculations_label_frame = ttk.LabelFrame(
            self.title_frame,
            text="Calculations",
            bootstyle='info'
        )
        self.calculations_label_frame.grid(row=2, column=0, pady=10, padx=10, sticky='EW')
        # ------------------------------------------CALCULATIONS LABELS-------------------------------------------------
        self.label_1 = ttk.Label(
            self.calculations_label_frame,
            text="Area: ",
            font=('Comic Sans MS', 12),
            bootstyle='success'
        )
        self.label_1.grid(row=0, column=0, padx=10, pady=10, sticky='E')

        self.label_2 = ttk.Label(
            self.calculations_label_frame,
            text="Circumference: ",
            font=('Comic Sans MS', 12),
            bootstyle='success'
        )
        self.label_2.grid(row=1, column=0, padx=10, pady=10, sticky='E')

        self.label_3 = ttk.Label(
            self.calculations_label_frame,
            text="Diameter: ",
            font=('Comic Sans MS', 12),
            bootstyle='success'
        )
        self.label_3.grid(row=2, column=0, padx=10, pady=(10, 40), sticky='E')

        # ------------------------------------------CLOSE BUTTON--------------------------------------------------------
        self.close_button = ttk.Button(
            self.title_frame,
            bootstyle='danger-outline',
            text="Close Window",
            command=lambda: self.destroy()  # TODO: Clear the fields in main screen
        )
        self.close_button.grid(row=3, column=0, ipadx=5, ipady=5, pady=(20, 10))

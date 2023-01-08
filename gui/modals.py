import ttkbootstrap as ttk
import tkinter


class Modal(ttk.Toplevel):
    """Parent popup modal class"""

    def __init__(self, title, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grab_set()  # do not allow user to click on parent application window
        # ---------------------------------REMOVE DEFAULT WINDOWS TITLE BAR---------------------------------------------
        self.overrideredirect(True)  # remove the title bar so we can customize it
        # ------------------------CENTER SCREEN, SET SIZE, SET NO RESIZEABLE--------------------------------------------
        self.width = 400
        self.height = 500
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.x = (self.screen_width / 2) - (self.width / 2)
        self.y = (self.screen_height / 2) - (self.height / 2)
        self.geometry('%dx%d+%d+%d' % (self.width, self.height, self.x, self.y))
        self.resizable(False, False)  # resize width and resize height is false
        # ---------------------------------------FRAME TO HOLD THE TITLE BAR--------------------------------------------
        self.title_frame = ttk.Frame(self, bootstyle='success')
        self.title_frame.pack(fill='x')
        self.title_frame.columnconfigure(0, weight=2)
        self.title_frame.columnconfigure(1, weight=1)
        # ----------------------------------------NEW TITLE BAR---------------------------------------------------------
        self.title_text = ttk.Label(
            self.title_frame,
            text=title,
            font=('Comic Sans MS', 10, 'bold'),
            bootstyle='inverse-success'
        )
        self.title_text.grid(row=0, column=0, padx=(20, 0), sticky='W')
        # -------------------------------------TITLE BAR CLOSE BUTTON---------------------------------------------------
        self.close_button = ttk.Button(
            self.title_frame,
            text='X',
            bootstyle='danger',
            command=self.destroy
        )
        self.close_button.grid(row=0, column=1, sticky='E', padx=(0, 10), pady=(5, 5))

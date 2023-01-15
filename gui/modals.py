from tkinter import END
import math
import ttkbootstrap as ttk
from images import RUBIKS, CIRCLE, TRIANGLE, SQUARE, RECTANGLE, PENTAGON, HEXAGON, HEPTAGON, OCTAGON, WARNING, \
    ISOSCELES, SCALENE
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

    def __init__(self, sides_variable, measurement_combobox, side_entries, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sides_variable = sides_variable  # number of sides selected
        self.shape_word = ""  # initialize the actual word value of the shape to an empty string; will set below
        self.shape_image = ""  # shape image file to use
        self.title("Shape Calculate")
        # create a map for values to shape names and shape images
        self.map_sides_to_name = [('1', 'Circle', CIRCLE),
                                  ('3', 'Triangle', TRIANGLE),
                                  ('4', 'Quadrilateral', SQUARE),
                                  ('5', 'Pentagon', PENTAGON),
                                  ('6', 'Hexagon', HEXAGON),
                                  ('7', 'Heptagon', HEPTAGON),
                                  ('8', 'Octagon', OCTAGON)]
        for group in self.map_sides_to_name:
            if group[0] == self.sides_variable:
                self.shape_word = group[1]  # set the value to the actual name of the shape
                self.shape_image = group[2]  # set the image

        # ----------------------------------------IMAGE-----------------------------------------------------------------
        self.image_shape = ttk.PhotoImage(file=self.shape_image)
        self.warning_image = ttk.PhotoImage(file=WARNING)
        self.isosceles_image = ttk.PhotoImage(file=ISOSCELES)
        self.scalene_image = ttk.PhotoImage(file=SCALENE)
        # ----------------------------------------TITLE LABEL-----------------------------------------------------------
        self.title_label = ttk.Label(
            self.title_frame,
            text=f"Your Shape is a {self.shape_word}",
            font=('Comic Sans MS', 14),
            bootstyle='primary'
        )
        self.title_label.grid(row=0, column=0, pady=10)
        # --------------------------------------------IMAGE LABEL-------------------------------------------------------
        self.image_label = ttk.Label(
            self.title_frame,
            image=self.image_shape
        )
        self.image_label.grid(row=1, column=0, padx=10)
        # ------------------------------------------CALCULATIONS FRAME--------------------------------------------------
        self.calculations_label_frame = ttk.LabelFrame(
            self.title_frame,
            text="Calculations",
            bootstyle='info'
        )
        self.calculations_label_frame.grid(row=2, column=0, pady=10, padx=10, sticky='EW')
        self.calculations_label_frame.columnconfigure(0, weight=1)
        # ------------------------------------------CALCULATIONS LABELS-------------------------------------------------
        self.label_1 = ttk.Label(
            self.calculations_label_frame,
            font=('Comic Sans MS', 12),
            bootstyle='success'
        )
        self.label_1.grid(row=0, column=0, padx=10, pady=10)

        self.label_2 = ttk.Label(
            self.calculations_label_frame,
            font=('Comic Sans MS', 12),
            bootstyle='success'
        )
        self.label_2.grid(row=1, column=0, padx=10, pady=10)

        self.label_3 = ttk.Label(
            self.calculations_label_frame,
            font=('Comic Sans MS', 12),
            bootstyle='success'
        )
        self.label_3.grid(row=2, column=0, padx=10, pady=(10, 40))

        # ------------------------------------------CLOSE BUTTON--------------------------------------------------------
        self.close_button = ttk.Button(
            self.title_frame,
            bootstyle='danger-outline',
            text="Close Window",
            command=lambda: self.close_button_functionality(measurement_combobox, side_entries)
        )
        self.close_button.grid(row=3, column=0, ipadx=5, ipady=5, pady=(20, 10))
        # -------------------------------UPDATE THE CALCULATIONS LABELS AFTER MODAL RENDERS-----------------------------
        if self.sides_variable == '1':
            self.circle_calculations(side_entries[0].get(), measurement_combobox)
        elif self.sides_variable == '3':
            self.side_entries = self.convert_to_int_or_string([side_entries[0].get(),
                                                               side_entries[1].get(),
                                                               side_entries[2].get()])
            self.triangle_calcs(self.side_entries, measurement_combobox)
        elif self.sides_variable == '4':
            self.square_entries = self.convert_to_int_or_string([side_entries[0].get(),
                                           side_entries[1].get(),
                                           side_entries[2].get(),
                                           side_entries[3].get(),])
            self.quad_calculations(self.square_entries,
                                   measurement_combobox
                                   )

    # --------------------------------------METHODS---------------------------------------------------------------------
    def convert_to_int_or_string(self, side_entries):
        """
        Converts the string data values to an int or a float if a . is found in the string.
        :param side_entries:
        :return: List; converted_sides
        """
        converted_sides = []
        for length in side_entries:
            if '.' in length:
                converted_sides.append(float(length))
            else:
                converted_sides.append(int(length))
        return converted_sides

    def throw_incompatible_error(self):
        pass

    def close_button_functionality(self, measurement_combobox, side_entries):
        """
        Sets the entry fields in the main window back to default text values, resets the measurement combobox back to
        the default value, destroys the modal window.
        :param measurement_combobox: The measurement combobox value from the main screen
        :param side_entries: Each of the side entries from the main screen
        :return: None; resets default values and then destroys self
        """
        int_to_string_numbers = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight']
        for index, entry in enumerate(side_entries):
            side_entries[index].delete(0, "")  # first delete what is in the entry field
            entry.insert(END, f"Enter Length of Side {int_to_string_numbers[index]}")  # then enter this text
        measurement_combobox.current(0)  # set the default value of measurement combobox
        self.destroy()  # destroy the popup window

    def circle_calculations(self, side_value, measurement_combobox):
        if '.' in side_value:  # convert from string to int or decimal depending on if . is found
            radius = float(side_value)
        else:
            radius = int(side_value)
        # get all the geometrical calculations for a circle
        diameter = round(radius * 2, 2)
        circumference = round(2 * math.pi * radius, 2)
        area = round(math.pi * radius ** 2, 2)
        # set the label values to the calculations
        self.label_1['text'] = f"Area: {area} {measurement_combobox.get()}"
        self.label_2['text'] = f"Circumference: {circumference} {measurement_combobox.get()}"
        self.label_3['text'] = f"Diameter: {diameter} {measurement_combobox.get()}"

    def triangle_calcs(self, side_entries, measurement_combobox):
        # get semiperimeter to use Heron's Formula
        semiperimeter = (side_entries[0] + side_entries[1] + side_entries[2]) / 2
        # test to see if the lengths are actually a triangle
        try:
            area = round(math.sqrt(semiperimeter * (
                    (semiperimeter - side_entries[0]) * (semiperimeter - side_entries[1]) * (
                    semiperimeter - side_entries[2]))), 3)
        except ValueError:  # set the error if the lengths are incompatible with a triangle
            self.image_label['image'] = self.warning_image
            self.title_label['text'] = "Error, this is NOT a Triangle!!"
            self.label_1['text'] = "These side lengths are not compatible"
            self.label_2['text'] = "and cannot create a Triangle"
            self.label_3['text'] = "Please try again!"
            return

        perimeter = round(side_entries[0] + side_entries[1] + side_entries[2], 3)
        # what kind of triangle was provided
        if side_entries[0] == side_entries[1] and side_entries[1] == side_entries[2]:
            tri_type = "Equilateral Triangle"
        elif side_entries[0] != side_entries[1] and side_entries[1] != side_entries[2] and side_entries[0] != \
                side_entries[2]:
            tri_type = "Scalene Triangle"
            self.image_label['image'] = self.scalene_image
        else:
            tri_type = "Isoceles Triangle"
            self.image_label['image'] = self.isosceles_image

        # set the label values
        self.label_1['text'] = f"Area: {area} {measurement_combobox.get()}"
        self.label_2['text'] = f"Perimeter: {perimeter} {measurement_combobox.get()}"
        self.label_3['text'] = f"Type: {tri_type}"

    def quad_calculations(self, square_sides, measurement_combobox):
        for side in square_sides:
            print(type(side))

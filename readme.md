# :small_blue_diamond: It's Hip To Be A Square :small_blue_diamond:
### A :triangular_ruler: geometry application made with :snake: Python and Tkinter

### The project is a simple executable application with the following requirements:
- It must contain two buttons at the top. One that opens a how-to and one that opens a link to the Github where the program is hosted.
- It must contain a field that allows the users to select the amount of sides that a shape contains.
  - This field may be a combobox, an entry or even a radio/checkbox type
  - This field must block users from selecting any other value other than a number(no floats allowed)
  - This field can be bound by the programmer (meaning defining a max/min amount of sides)
- It must contain a Unit of Measurement selection
  - The programmer may define the units of measurement
  - The programmer may use an entry field, combobox or any other input type
  - Validation must be performed on this field, users should not be able to select/create bad values. Bad value examples:
    - Any string that is a non-unit of measurement (Like 'banana', 'apple123', 123.33, etc)
- It must contain entry fields for the lengths of each side.
  - The entry fields should be bound to the sides selection and dynamically appear based on the input value of the sides entry.
  - The side length entry fields should contain validation. At a minimum they should:
    - Delete the default contents when the user clicks in the field
    - Verify that only numbers are typed into the field, as well as a . " " or backspace. Do not allow a . after a backspace, etc.
- It must contain a Calculate button at the bottom. The calculate button should do the following:
  - Create a pop-up/modal that shows the final calculations in a separate window. This window should contain a close button
  - Clear the fields on the application main form and reset to default so that it can be used again.
- Any design style may be used. Any background, any button style, and any colors. The programmer may name the program anything that they deem appropriate.

### :art: My Design

![](readme_images/Hip_Main.png)

### :books: Non-Standard Libraries Used:
- ttkbootstrap - A simply smashing modern library for tkinter
- Pillow - For images n' stuff

### :question: The how-to button
![](readme_images/how_to_button.png)

- Easy Peasy Lemon Squeezy
  - Opens a how-to modal that explains how the program/application works

### :traffic_light: The Github Link Button
![](readme_images/github_link_button.png)

- Opens a link to this here Github page. 

### :card_index: Sides select dropdown and title
![](readme_images/side_select.png)

- Allows the user to select the amount of sides that their shape contains. Bound to 1 - 8 sides (I didn't want users to be able to select infinite sides)
- Users cannot select 2 sides. Why? Because that is weird. One side is a circle, but two sides is a shape that I still do not understand.
- Users cannot hand input sides. I used a combobox for this. Default value is set to 1

### :straight_ruler: Unit of Measurement Dropdown
![](readme_images/unit_measurement.png)

- Allows the user to select a predefined unit of measurement. Set to Inches by default. User input not allowed, must select from dropdown.
- Mixed in some metric measurements for fun......

### :straight_ruler: Side Length User Entry
![](readme_images/sides_enter.png)

- Dynamic side entry field. By default none of these entry fields appear on the application. Fields appear based on the sides selected in the 'how many sides' dropdown field.
- Validation ignores any key that is not a number, a period, a space or a backspace key. 

### :rotating_light: Calculate Button
![](readme_images/calculate_button.png)

- When clicked, a modal pops up with geometric calculations for the shape. Default values are reset to the application

## :vertical_traffic_light: Functionality Once Calculate is Clicked :vertical_traffic_light:
Based on the amount of sides given, the application determines the 'type' of shape that was provided. And, based on 
the length of the sides, it determines which type. For example:
<p float="left">
<img src="readme_images/equalTri.png" alt="equalTriangle" style="width:250px;"/>
<img src="readme_images/isocTri.png" alt="equalTriangle" style="width:250px;"/>
<img src="readme_images/scalTri.png" alt="equalTriangle" style="width:250px;"/>
</p>

In the above examples, the application determined if a triangle was an Equilateral, Isosceles, or Scalene based on the 
length of the sides. The below examples are of a Quadrilateral
<p float="left">
<img src="readme_images/rectangle_calc.png" alt="rectangle" style="width:250px;"/>
<img src="readme_images/square_calc.png" alt="square" style="width:250px;"/>
<img src="readme_images/trapezoid.png" alt="trapezoid" style="width:250px;"/>
</p>

If a shape's sides are incompatible with the shape selected, meaning that the sides could not meet and create the shape, 
a custom error modal will appear:
![](readme_images/warning_screen.png)


## :interrobang: More Information......
This application was created on :computer: PC and is for :computer: PC. 

This application uses the canvas element so that I could create a custom background. This is certainly not something you 
would want to do, as it makes the application PC specific. Meaning, the canvas elements are placed with x and y coords. 
Due to different monitors having different screen resolutions, this means that the coords and fixed widths will not be 
the same depending on the Monitor dpi. So.....that means that this application will have to be modified for every single
monitor that it is used on. An oversight on my part, that was only caught after I was nearly finished. To avoid this 
annoying issue, do not use canvas. Just use the built-in grid, and pack in your Tkinter application.

This application heavily.....actually exclusively uses the canvas element of Tkinter. Why? Well, I designed a background image
in photoshop to be used as the background of the application. This is a no no no in Tkinter using standard placement (grid, pack, place)
as the background of any labels that I put on top of the image would definitely not be able to be matched to the color in the 
background image. So, canvas was the way to go with this particular application. It was not fun. I did not enjoy it. 

The entry fields contain validation within the application class. Normally, it would be better (and more OOPy) to create a 
Entry child class like ValidatedEntry and then use that whenever a validated entry field was needed. HOWEVER!!!! This application
only needed one entry field (used up to 8 times), and there is no expansion expected of the application. Creating a validate function was easier
and made more sense for such limited use. 

If you take a look at the MainWindow class, you will find an absolutely ridiculous method that serves one purpose. To get ahold of
the transparency option of a canvas rectangle. This absurdity is what must be done in order to access the alpha parameter of
an rbga color, so that we can set it to something less than 100%. If you need to mess with the alpha of a widget, here is how it's done.
I am sorry. :disappointed:

ttkbootstrap has a plethora of neat themes that you can use. In this application I decided to use the cyborg theme. Cyborg is a dark theme 
with bright and bold colors. Therefore, I went with a nice bright geometry background that I set transparency on. It's bold.....
it's bright.....it's supposed to be. 

Due to the cliché of Comic Sans being a nosir in UI design......I used it. Breathe it in. Comic Sans all over the place like a 
warm hug of awesome. 

And lastly, the application will currently do circles, triangles and quadrilaterals. The other shapes I have left blank 
for the time being. If you want to use them, then you can simply add the methods as needed. 


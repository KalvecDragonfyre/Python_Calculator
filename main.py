import tkinter as tk 
from tkinter import font
from PIL import Image, ImageTk
import extras, msgs
import re


class Calculator():
    def __init__(self):

        my_menu = tk.Menu(root)
        root.config(menu=my_menu)

        self.canvas = tk.Canvas(root, width=350, height=500, bd=0, highlightthickness=0)
        self.bg_image = ImageTk.PhotoImage(file="images/blue.jpg")
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0,0, image=self.bg_image, anchor=tk.CENTER)

        self.terrward_mode = 1
        
        
        btn_font = font.Font(size=20)

        # sym_menu = tk.Menu(my_menu, tearoff=False, fg="black")
        # my_menu.add_cascade(label="Features",menu=sym_menu, foreground="black")
        # sym_menu.add_command(label="TerrWard Mode", command=msgs.th_msg)
        # sym_menu.add_separator()
        # sym_menu.add_command(label="Square Root - √x", command=msgs.sqrt_msg)
        # sym_menu.add_command(label="Percent Conversion - x%", command=msgs.pc_msg)
        # sym_menu.add_command(label="Factorials - !x", command=msgs.factorial_msg)
        # sym_menu.add_command(label="Exponents - x^", command=msgs.exp_msg)
        # sym_menu.add_command(label="Absolut Value - |x|", command=msgs.abs_msg)
        # sym_menu.add_command(label="X Squared - x²", command=msgs.x_sqrd_msg)
        # sym_menu.add_command(label="X Cubed - x³", command=msgs.x_cubed_msg)
        # sym_menu.add_separator()
        # sym_menu.add_command(label="Exit", command=root.quit)

        # db_menu = tk.Menu(my_menu, tearoff=False, fg="black")
        # my_menu.add_cascade(label="Options", menu=db_menu, foreground="black")
        # # db_menu.add_command(label="TerrWard Mode", command=self.terr_mode)
        # db_menu.add_command(label="About", command=msgs.help_screen)
        # # db_menu.add_command(label="")
        # # db_menu.add_command(label="")
        # db_menu.add_separator()
        # db_menu.add_command(label="Exit", command=root.quit)

        # Integer and Answer Box
        self.eq_box = tk.Entry(root, width=24, font=btn_font)
        self.eq_box.focus_set()
        
        
        
        # Button Objects
            # Buttons (1-3)
        button_1 = tk.Button(root, text="1", font=btn_font, command=lambda: self.button_click(1))
        button_2 = tk.Button(root, text="2", font=btn_font, command=lambda: self.button_click(2))
        button_3 = tk.Button(root, text="3", font=btn_font, command=lambda: self.button_click(3))
            # Buttons (4-6)
        button_4 = tk.Button(root, text="4", font=btn_font, command=lambda: self.button_click(4))
        button_5 = tk.Button(root, text="5", font=btn_font, command=lambda: self.button_click(5))
        button_6 = tk.Button(root, text="6", font=btn_font, command=lambda: self.button_click(6))
            # Buttons (7-9)
        button_7 = tk.Button(root, text="7", font=btn_font, command=lambda: self.button_click(7))
        button_8 = tk.Button(root, text="8", font=btn_font, command=lambda: self.button_click(8))
        button_9 = tk.Button(root, text="9", font=btn_font, command=lambda: self.button_click(9))
            # Buttons (0)
        button_0 = tk.Button(root, text="0", font=btn_font, command=lambda: self.button_click(0))

        # Operation buttons
        button_add = tk.Button(root, text="+", font=btn_font, command=lambda: self.set_operation('+'))
        button_subtract = tk.Button(root, text="-", font=btn_font, command=lambda: self.set_operation('-'))
        button_multiply = tk.Button(root, text="*", font=btn_font, command=lambda: self.set_operation('*'))
        button_divide = tk.Button(root, text="/", font=btn_font, command=lambda: self.set_operation('/'))
        button_equals = tk.Button(root, text="=", font=btn_font, command=self.calculate)
        button_clear = tk.Button(root, text="C", font=btn_font, command=self.clear_all)

        # Advanced operation buttons
        button_sqrt = tk.Button(root, text="√", font=btn_font, command=lambda: self.apply_single_operation('sqrt'))
        button_square = tk.Button(root, text="x²", font=btn_font, command=lambda: self.apply_single_operation('square'))
        button_cube = tk.Button(root, text="x³", font=btn_font, command=lambda: self.apply_single_operation('cube'))
        button_percent = tk.Button(root, text="%", font=btn_font, command=lambda: self.apply_single_operation('percent'))
        button_exp = tk.Button(root, text="^", font=btn_font, command=lambda: self.set_operation('**'))

        
    # Frame Placements
        # self.equation = self.canvas.create_text(75,20, text="Equation:", font=btn_font, fill="white")
        self.canvas.create_window(5, 40, anchor="nw", window=self.eq_box)
        # self.canvas.create_text(55,90, text="Answer:", font=btn_font, fill="white")
        # self.canvas.create_window(4, 108, anchor="nw", window=self.answer_box)
            # Buttons (1-3)
        self.canvas.create_window(90, 140, anchor="nw", window=button_1) # 1 - (30, 260)
        self.canvas.create_window(140, 140, anchor="nw", window=button_2) # 2 - (75, 260)
        self.canvas.create_window(190, 140, anchor="nw", window=button_3) # 3 - (120, 260)
            # Buttons (4-6)
        self.canvas.create_window(90, 190, anchor="nw", window=button_4) # 4 - (30, 305)
        self.canvas.create_window(140, 190, anchor="nw", window=button_5) # 5 - (75, 305)
        self.canvas.create_window(190, 190, anchor="nw", window=button_6) # 6 - (120, 305)
            # Buttons (7-9)
        self.canvas.create_window(90, 240, anchor="nw", window=button_7) # 7 - (30, 350)
        self.canvas.create_window(140, 240, anchor="nw", window=button_8) # 8 - (75, 350)
        self.canvas.create_window(190, 240, anchor="nw", window=button_9) # 9 - (120, 350)
            # Button (0)
        self.canvas.create_window(140, 290, anchor="nw", window=button_0) # 0 - (75, 425)

        # self.canvas.create_window(190,440, anchor="nw", window=self.period)
        # self.canvas.create_window(5, 350, anchor="nw", window=self.pos_neg)
            # Buttons (+, -, *, /, =, C)
        self.canvas.create_window(300, 140, anchor="nw", window=button_add) # +
        self.canvas.create_window(300, 190, anchor="nw", window=button_subtract) # (-) - ()
        self.canvas.create_window(300, 240, anchor="nw", window=button_multiply) # x - ()
        self.canvas.create_window(300, 290, anchor="nw", window=button_divide) # /
        self.canvas.create_window(245, 340, anchor="nw", width=100, window=button_equals) # =

        self.canvas.create_window(300, 80, anchor="nw", window=button_clear) # clr - (270, 260)
        self.canvas.create_window(5, 80, anchor="nw", window=button_sqrt) # √x - (175, 260)
        self.canvas.create_window(230, 80, anchor="nw", window=button_percent) # x%
        # self.canvas.create_window(300, 305, anchor="nw", window=self.factorial) # !x
        # self.canvas.create_window(5, 305, anchor="nw", window=self.abs_value) # |x| - (175, 305)
        self.canvas.create_window(185, 80, anchor="nw", window=button_exp) # x^ - (175, 350)

        self.canvas.create_window(65, 80, anchor="nw", window=button_square) # x² - (125, 400)
        self.canvas.create_window(125, 80, anchor="nw", window=button_cube) # x³ _ (185, 400)

        self.twm_label = self.canvas.create_text(320, 30, text="", fill="white")
        # print(self.twm_label)


    def button_click(self, number):
        """Handle button click for numbers and update the display."""
        current = self.eq_box.get()
        self.eq_box.delete(0, tk.END)
        self.eq_box.insert(tk.END, current + str(number))


    def clear_entry(self):
        """Clear the entry widget."""
        self.eq_box.delete(0, tk.END)

    def set_operation(self, op):
        """Set the operation and store the first number."""
        global first_number, operation
        try:
            first_number = float(self.eq_box.get())
        except ValueError:
            msgs.show_error()
            return
        operation = op
        self.eq_box.delete(0, tk.END)

    def calculate(self):
        """Perform the calculation based on the selected operation."""
        try:
            second_number = float(self.eq_box.get())
        except ValueError:
            msgs.show_error()
            return

        result = None
        if operation == '+':
            result = extras.add(first_number, second_number)
        elif operation == '-':
            result = extras.subtract(first_number, second_number)
        elif operation == '*':
            result = extras.multiply(first_number, second_number)
        elif operation == '/':
            result = extras.divide(first_number, second_number)
        elif operation == '**':
            result = extras.exponent(first_number, second_number)
        
        self.eq_box.delete(0, tk.END)
        self.eq_box.insert(tk.END, str(result))

    def clear_all(self):
        """Reset calculator state."""
        global first_number, operation
        first_number = None
        operation = None
        self.clear_entry()

    def apply_single_operation(self, op):
        """Apply a single operand operation."""
        global first_number, operation
        try:
            current_number = float(self.eq_box.get())
        except ValueError:
            msgs.show_error()
            return

        result = None
        if op == 'sqrt':
            result = extras.square_root(current_number)
        elif op == 'square':
            result = extras.square(current_number)
        elif op == 'cube':
            result = extras.cube(current_number)
        elif op == 'percent':
            result = extras.percent(current_number)
        
        self.eq_box.delete(0, tk.END)
        self.eq_box.insert(tk.END, str(result))
        first_number = result  # Update the first number to chain operations
        operation = None  # Clear any previous operation

# Create the main window


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("350x390")
    root.title("PyCalc")
    root.resizable(width=False, height=False)
    calc = Calculator()
    root.mainloop()
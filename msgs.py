from tkinter import messagebox

# ------------------------------------------------------------------Help Screen Message
def help_screen():
    help_msg = """
        This works like a normal 
        calculator with some minor
        changes with two modes one 
        normal and one designed with 
        logic of Terrance Howard for 
        a whole new experience with 
        math.
                """
    messagebox.showinfo("Help Screen", help_msg)


def th_msg():
    message = """
        TH_Mode is a mode inspired by
        Terrence Howard with his speech
        at Oxford and implements the 
        math rules stated in the 
        speech. This can also be 
        toggled on/off in features
        tab.
                    Enjoy!
                    """
    messagebox.showinfo("Help Screen", message)


def sqrt_msg():
    message = """
        TH_Mode is a mode inspired by
        Terrence Howard with his speech
        at Oxford and implements the 
        math rules stated in the 
        speech. 
                    Enjoy!
                    """
    messagebox.showinfo("Help Screen", message)



def pc_msg():
    message = """
        Simply converts numbers from
        percent to decimal.
        exm:
            7% = 0.07
                    """
    messagebox.showinfo("Help Screen", message)


def factorial_msg():
    message = """
        Factorial - !x
        Exm:
        !5 = 5x4x3x2x1 = 120
                """
    messagebox.showinfo("Help Screen", message)


def exp_msg():
    message = """
        Takes any number to the power of 
        any number.
        Exm:
            3^5 = 243
                    """
    messagebox.showinfo("Help Screen", message)


def abs_msg():
    message = """
        Gives the Absolute Value of any
        number.
        Exm:
            abs7 = 7.0
                    """
    messagebox.showinfo("Help Screen", message)


def x_sqrd_msg():
    message = """
        Gives Squared Value of any number.
        Exm:
            5² = 25
            """
    messagebox.showinfo("X Squred", message)


def x_cubed_msg():
    message = """
        Gives the Cubed Value of any number.
        Exm:
            5³ = 125
            """
    messagebox.showinfo("X Cubed", message)

def show_error():
    messagebox.showerror("Input Error", "Please enter a valid number.")
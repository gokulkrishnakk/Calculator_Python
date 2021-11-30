from tkinter import *
from math import *


# function to do an action while pressing buttons
def button_press(symbol):
    global equation_text
    equation_text = equation_text + str(symbol)

    equation_text_to_display = (equation_text.replace('*', '\u00D7').replace('/', '\u00F7'))

    equation_label.set(equation_text_to_display)


# --------------------------------------------------------------------------------------
# function for the equal button
def equals():
    global equation_text
    try:

        total = (eval(equation_text))
        equation_text_to_display = equation_text.replace('*', '\u00D7').replace('/', '\u00F7')
        ans = str(round(total, 3))
        solution = str(equation_text_to_display + ' = ' + ans)
        equation_label.set(solution)
        equation_text = ans
    except ZeroDivisionError:
        equation_label.set('Error')
        equation_text = ''
    except SyntaxError:
        equation_label.set('Error')
        equation_text = ''


# --------------------------------------------------------------------------------------------

# function to clear the display
def clr():
    global equation_text
    equation_label.set('')
    equation_text = ''


# ----------------------------------------------------------------------------------------------------
# function to find the squire root of a number
def squire_root():
    global equation_text
    try:
        ans = str(round(sqrt(float(equation_text)), 3))
        solution = str('\u221A' + equation_text + ' = ' + ans)
        equation_label.set(solution)
        equation_text = str(ans)
    except SyntaxError:
        equation_label.set('Error')
        equation_text = ''
    except ValueError:
        equation_label.set('Error')
        equation_text = ''


# --------------------------------------------------------------------------------------------------------------
# function to find the squire of a number
def squire():
    global equation_text
    try:

        ans = (float(equation_text) ** 2)
        ans1 = round(ans, 4)
        solution = str(equation_text + '\u00b2' + ' = ' + str(ans1))
        equation_label.set(solution)
        equation_text = str(ans1)
    except ValueError:
        equation_label.set('Error')
        equation_text = ''


# -----------------------------------------------------------------------------------------------------------------
# function to find the sin of an angle
def sin_ang():
    global equation_text
    try:

        angle = radians(float(equation_text))
        ans = round(sin(angle), 3)
        solution = str('sin ' + equation_text + ' = ' + str(ans))
        equation_label.set(solution)
        equation_text = str(ans)
    except ValueError:

        equation_label.set('Error')
        equation_text = ''


# function to find the cos of an angle
def cos_ang():
    global equation_text
    try:
        angle = radians(float(equation_text))
        ans = round(cos(angle), 3)
        solution = str('cos ' + equation_text + ' = ' + str(ans))
        equation_label.set(solution)
        equation_text = str(ans)
    except ValueError:
        equation_label.set('Error')
        equation_text = ''


# function to find the tan of an angle
def tan_ang():
    global equation_text
    try:
        angle = radians(float(equation_text))
        ans = round(tan(angle), 3)
        solution = str('tan ' + equation_text + ' = ' + str(ans))
        equation_label.set(solution)
        equation_text = str(ans)
    except ValueError:
        equation_label.set('Error')
        equation_text = ''


# ------------------------------------------------------------------------------------------------------------


# configuring window
window = Tk()
window.title('Calculator')
icon = PhotoImage(file='calculator.png')
window.iconphoto(True, icon)

window.config(bg='#141414')
window.geometry('340x667')
window.resizable(0, 0)

# variables to store the expression
equation_text = ''
equation_label = StringVar()

# frame for the screen
display_frame = Frame(window, bg='#181818', height=200)
display_frame.pack(expand=True, fill='both')

# the screen
label = Label(display_frame, textvariable=equation_label, anchor=E, bg='#181818', fg='white',
              font=('Helvetica', 20, 'bold'), height=4)
label.pack(expand=True, fill='both')

# frame to hold the buttons
button_frame = Frame(window, bg='#141414')
button_frame.pack(expand=True, fill='both')


# --------------------------------------------------------------------------------------------------------


def button():
    # creating and adding a set of buttons

    buttons_set1 = {7: (3, 1), 8: (3, 2), 9: (3, 3), 4: (4, 1), 5: (4, 2), 6: (4, 3), 1: (5, 1), 2: (5, 2), 3: (5, 3),
                    0: (6, 2)}

    button_set3 = {'.': (6, 3), '+': (5, 4), '-': (4, 4)}

    for i, j in buttons_set1.items():
        buttons = Button(button_frame, text=str(i), font=20, border=0, height=3, width=7, bg='#141414',
                         command=lambda num=i: button_press(str(num)),
                         activebackground='#181818', activeforeground='white', fg='white')
        buttons.grid(row=j[0], column=j[1])

    for i, j in button_set3.items():
        buttons = Button(button_frame, text=str(i), font=20, border=0, height=3, width=7, bg='#141414',
                         command=lambda num=i: button_press(str(num)),
                         activebackground='#181818', activeforeground='white', fg='#34ebe5')
        buttons.grid(row=j[0], column=j[1])

    # defining  and placing the remaining buttons

    button_div = Button(button_frame, text='\u00F7', font=20, border=0, height=3, width=7, bg='#141414',
                        activebackground='#181818', activeforeground='white',
                        command=lambda: button_press('/'),
                        fg='#34ebe5')

    button_mul = Button(button_frame, text='\u00D7', font=20, border=0, height=3, width=7, bg='#141414',
                        activebackground='#181818', activeforeground='white',
                        command=lambda: button_press('*'),
                        fg='#34ebe5')

    button_eql = Button(button_frame, text='=', font=20, border=0, height=3, width=7, bg='#141414',
                        activebackground='#181818', activeforeground='white', command=equals,
                        fg='#34ebe5')

    button_sqrt = Button(button_frame, text='\u221Ax', font=20, border=0, height=3, width=7, bg='#141414',
                         activebackground='#181818', activeforeground='white', command=squire_root,
                         fg='#34ebe5')

    button_pi = Button(button_frame, text='\u03C0', font=20, border=0, height=3, width=7, bg='#141414',
                       activebackground='#181818', activeforeground='white',
                       command=lambda: button_press(pi), fg='#34ebe5')

    button_clr = Button(button_frame, text='AC', font=20, border=0, height=3, width=7, bg='#141414',
                        activebackground='#181818', activeforeground='white', command=clr, fg='#34ebe5')

    button_sin = Button(button_frame, text='sin', font=20, border=0, height=3, width=7, bg='#141414',
                        activebackground='#181818', activeforeground='white',
                        command=lambda: sin_ang(),
                        fg='#34ebe5')

    button_cos = Button(button_frame, text='cos', font=20, border=0, height=3, width=7, bg='#141414',
                        activebackground='#181818', activeforeground='white',
                        command=lambda: cos_ang(),
                        fg='#34ebe5')

    button_tan = Button(button_frame, text='tan', font=20, border=0, height=3, width=7, bg='#141414',
                        activebackground='#181818', activeforeground='white',
                        command=lambda: tan_ang(), fg='#34ebe5')

    button_squire = Button(button_frame, text='x\u00b2', font=20, border=0, height=3, width=7, bg='#141414',
                           activebackground='#181818', activeforeground='white',
                           command=lambda: squire(),
                           fg='#34ebe5')

    button_one_by = Button(button_frame, text='1/x', font=20, border=0, height=3, width=7, bg='#141414',
                           activebackground='#181818', activeforeground='white',
                           command=lambda: button_press('1/'),
                           fg='#34ebe5')

    buttons_set2 = {button_sqrt: (0, 1), button_one_by: (0, 2), button_pi: (6, 1), button_clr: (0, 4),
                    button_sin: (2, 1),
                    button_cos: (2, 2), button_tan: (2, 3), button_div: (2, 4), button_mul: (3, 4),
                    button_squire: (0, 3),
                    button_eql: (6, 4)}

    # adding the buttons of set 2 to the frame
    for name, position in buttons_set2.items():
        name.grid(row=position[0], column=position[1])


# binding the keyboard keys
def bind_keys():
    buttons_set2 = {7: (3, 1), 8: (3, 2), 9: (3, 3), 4: (4, 1), 5: (4, 2), 6: (4, 3), 1: (5, 1), 2: (5, 2), 3: (5, 3),
                    0: (6, 2), '.': (6, 3), '+': (5, 4), '-': (4, 4), '*': (3, 4), '/': (2, 4)}

    for x, y in buttons_set2.items():
        window.bind(str(x), lambda event, digits=x: button_press(digits))

    window.bind('=', lambda event: equals())
    window.bind('<Delete>', lambda event: clr())
    window.bind('<Return>', lambda event: equals())
    window.bind('<End>', lambda event: window.destroy())


button()
bind_keys()
window.mainloop()

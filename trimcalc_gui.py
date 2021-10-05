from tkinter import *
from tkinter import ttk
from trimcalc import GasCalc

class CalcGui:
    """
    tkinter graphical user interface for a simple desktop app
    that calculates gas mixes used in mixed gas diving.
    """

    def __init__(self, root):
        
        self.gas = GasCalc()
        self.error_status = False

        root.title('Trimix calculator')
        #title image needs absolute path.       
        title_image = PhotoImage(file = r'C:\Python\Trimix_calculator\icon16px.png')
        root.iconphoto(False, title_image)
        root.minsize(width = 400, height = 400)

        mainframe = ttk.Frame(root, padding = '3 3 12 12')
        mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))

        reg_pct_val = root.register(self.callback_pct)
        reg_size_val = root.register(self.callback_size)
        reg_pressure_val = root.register(self.callback_pressure)

        #col 0: available - col 1: labels - col 2: inputfields - col3: units

        labels_col = 1
        input_col = labels_col + 1
        units_col = input_col + 1
        outp_col = units_col + 1

        #Section: CURRENT status
        #COL 1: Labels
        ttk.Label(mainframe, text = 'Tank size:',).grid(
            column = labels_col,
            row = 0,
            sticky = E,
            )
        ttk.Label(mainframe, text = 'Current pressure:',).grid(
            column = labels_col,
            row = 1,
            sticky = E,
            )
        #COL 2: Inputs
        self.current_size = StringVar()
        self.current_size.set('24')
        current_size_entry = ttk.Entry(
            mainframe,
            textvariable = self.current_size,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_size_val, '%P', 'siz'),
            )
        current_size_entry.grid(
            column = input_col,
            row = 0,
            sticky = W,
            )
        self.current_pressure = StringVar()
        self.current_pressure.set('0')
        current_pressure_entry = ttk.Entry(
            mainframe,
            textvariable = self.current_pressure,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_pressure_val, '%P', 'cpr'),
            )
        current_pressure_entry.grid(
            column = input_col,
            row = 1,
            sticky = W,
            )
        #COL 3: UNITS, ERRORS
        self.size_err = StringVar()
        self.size_err.set('liters')
        ttk.Label(
            mainframe,
            textvariable = self.size_err,
            foreground = '#808080',
            ).grid(
                column = units_col,
                row = 0,
                sticky = W,
                )
        self.curr_press_err = StringVar()
        self.curr_press_err.set('bar')
        ttk.Label(mainframe,
            textvariable = self.curr_press_err,
            foreground = '#808080',
            ).grid(column = units_col,
                row = 1,
                sticky = W,
                )
        #Section: CURRENT mix status
        sep1 = ttk.Separator(mainframe, orient = HORIZONTAL)
        sep1.grid(column = 0, columnspan = 2, row = 2, sticky = (W, E))

        ttk.Label(
            mainframe,
            text = 'Current oxygen:',
            ).grid(
                column = labels_col,
                row = 3,
                sticky = E,
                )
        ttk.Label(
            mainframe,
            text = 'Current helium:',).grid(
                column = labels_col,
                row = 4,
                sticky = E,
                )
        self.current_oxygen = StringVar()
        self.current_oxygen.set('21')
        current_oxygen_entry = ttk.Entry(
            mainframe,
            textvariable = self.current_oxygen,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_pct_val, '%P', 'cox'),
            )
        current_oxygen_entry.grid(
            column = input_col,
            row = 3,
            sticky = W,
            )

        self.current_helium = StringVar()
        self.current_helium.set('35')
        current_helium_entry = ttk.Entry(
            mainframe,
            textvariable = self.current_helium,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_pct_val, '%P', 'che'),
            )
        current_helium_entry.grid(
            column = input_col,
            row = 4,
            sticky = W,
            )

        #COL 3: UNITS, ERRORS
        self.curr_oxy_err = StringVar()
        self.curr_oxy_err.set('percent')
        ttk.Label(mainframe,
            textvariable = self.curr_oxy_err,
            foreground = '#808080',
            ).grid(column = units_col,
                row = 3,
                sticky = W,
                )
        self.curr_he_err = StringVar()
        self.curr_he_err.set('percent')
        ttk.Label(mainframe,
            textvariable = self.curr_he_err,
            foreground = '#808080',
            ).grid(column = units_col,
                row = 4,
                sticky = W,
                )

        #Section: WANTED status
        sep2 = ttk.Separator(mainframe, orient = HORIZONTAL)
        sep2.grid(column = 0, columnspan = 2, row = 5, sticky = (W, E))

        ttk.Label(mainframe,
            text = 'Wanted oxygen:',
            ).grid(column = labels_col,
                row = 6,
                sticky = E,
                )
        ttk.Label(mainframe,
            text = 'Wanted helium:',
            ).grid(column = labels_col,
                row = 7,
                sticky = E,
                )
        ttk.Label(mainframe,
            text = 'Wanted pressure:',
            ).grid(column = labels_col,
                row = 8,
                sticky = E,
                )
        self.wanted_oxygen = StringVar()
        self.wanted_oxygen.set('21')
        wanted_oxygen_entry = ttk.Entry(mainframe,
            textvariable = self.wanted_oxygen,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_pct_val, '%P', 'wox'),
            )
        wanted_oxygen_entry.grid(column = input_col,
            row = 6,
            sticky = W,
            )
        self.wanted_helium = StringVar()
        self.wanted_helium.set('35')
        wanted_helium_entry = ttk.Entry(mainframe,
            textvariable = self.wanted_helium,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_pct_val, '%P', 'whe'),
            )
        wanted_helium_entry.grid(column = input_col,
            row = 7,
            sticky = W,
            )
        self.wanted_pressure = StringVar()
        self.wanted_pressure.set('220')
        wanted_pressure_entry = ttk.Entry(mainframe,
            textvariable = self.wanted_pressure,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_pressure_val, '%P', 'wpr'),
            )
        wanted_pressure_entry.grid(column = input_col,
            row = 8,
            sticky = W,
            )

        #COL 3: UNITS, ERRORS
        self.want_oxy_err = StringVar()
        self.want_oxy_err.set('percent')
        ttk.Label(mainframe,
            textvariable = self.want_oxy_err,
            foreground = '#808080',
            ).grid(column = units_col,
                row = 6,
                sticky = W,
                )
        self.want_he_err = StringVar()
        self.want_he_err.set('percent')
        ttk.Label(mainframe,
            textvariable = self.want_he_err,
            foreground = '#808080',
            ).grid(column = units_col,
                row = 7,
                sticky = W,
                )
        self.want_press_err = StringVar()
        self.want_press_err.set('bar')
        ttk.Label(mainframe,
            textvariable = self.want_press_err,
            foreground = '#808080',
            ).grid(column = units_col,
                row = 8,
                sticky = W,
                )

        #Section: TOPMIX
        sep2 = ttk.Separator(mainframe, orient = HORIZONTAL)
        sep2.grid(column = 0, columnspan = 2, row = 9, sticky = (W, E))

        ttk.Label(mainframe,
            text = 'Top-mix oxygen:',
            ).grid(column = 1,
                row = 10,
                sticky = E,
                )
        self.topmix_oxygen = StringVar()
        self.topmix_oxygen.set('21')
        topmix_oxygen_entry = ttk.Entry(mainframe,
            textvariable = self.topmix_oxygen,
            width = 8,
            justify = 'right',
            validate = 'key',
            validatecommand = (reg_pct_val, '%P', 'top'),
            )
        topmix_oxygen_entry.grid(column = input_col,
            row = 10,
            sticky = W,
            )

        #COL 3: UNITS, ERRORS
        self.topmix_err = StringVar()
        self.topmix_err.set('percent')
        ttk.Label(mainframe,
            textvariable = self.topmix_err,
            foreground = '#808080',
            ).grid(column = units_col,
                row = 10,
                sticky = W,
                )

        sep2 = ttk.Separator(mainframe, orient = HORIZONTAL)
        sep2.grid(column = 0, columnspan = 2, row = 11, sticky = (W, E))

        #Section: BUTTON

        self.submit_btn = ttk.Button(mainframe,
            text = 'Calculate',
            command = self.validator,
            )
        self.submit_btn.grid(column = labels_col,
            row = 12,
            sticky = W
            )

        self.general_err = StringVar()
        self.general_err.set('')
        ttk.Label(mainframe,
            textvariable = self.general_err,
            foreground = '#FF0000',
            ).grid(column = units_col,
                row = 12,
                sticky = W,
                )
    
        #Section: OUTPUT
        self.fill_helium_label = StringVar()
        self.fill_helium_label.set('')
        ttk.Label(mainframe,
            textvariable = self.fill_helium_label,
            foreground = '#008000',
            ).grid(column = labels_col,
                row = 13,
                sticky = W,
                )
        self.fill_oxygen_label = StringVar()
        self.fill_oxygen_label.set('')
        ttk.Label(mainframe,
            textvariable = self.fill_oxygen_label,
            foreground = '#008000',
            ).grid(column = labels_col,
                row = 14,
                sticky = W,
                )
        self.fill_topmix_label = StringVar()
        self.fill_topmix_label.set('')
        ttk.Label(mainframe,
            textvariable = self.fill_topmix_label,
            foreground = '#008000',
            ).grid(column = labels_col,
                row = 15,
                sticky = W,
                )

        #ADDITIONAL STYLING

        for child in mainframe.winfo_children():
            child.grid_configure(padx = 2,
                                pady = 1,
                                ipadx = 2,
                                ipady = 2)

    #DATA VALIDATION

    def set_error(self, err_type, placement):
        self.error_status = True
        self.submit_btn['state'] = DISABLED

        if err_type == 0:
            error_message = 'please enter a number between 0 and 100'
        elif err_type == 1:
            error_message = 'gas mix total exceeds 100%'
        elif err_type == 2:
            error_message = 'please enter a number larger than 0'
        elif err_type == 3:
            error_message = 'please make sure there are no empty fields.'
        elif err_type == 4:
            error_message = 'please enter a positive integer'
        else:
            error_message = 'something is wrong, developer is a dumdum'

        if placement == 'cox':
            self.curr_oxy_err.set(error_message)
        elif placement == 'cpr':
            self.curr_press_err.set(error_message)
        elif placement == 'che':
            self.curr_he_err.set(error_message)
        elif placement == 'wox':
            self.want_oxy_err.set(error_message)
        elif placement == 'whe':
            self.want_he_err.set(error_message)
        elif placement == 'wpr':
            self.want_press_err.set(error_message)
        elif placement == 'top':
            self.topmix_err.set(error_message)
        elif placement == 'siz':
            self.size_err.set(error_message)
        elif placement == 'gen':
            self.general_err.set(error_message)

    def set_no_error(self, placement):
        self.error_status = False
        self.submit_btn['state'] = NORMAL

        if placement == 'cox':
            self.curr_oxy_err.set('percent')
        elif placement == 'che':
            self.curr_he_err.set('percent')
        elif placement == 'cpr':
            self.curr_press_err.set('bar')
        elif placement == 'wox':
            self.want_oxy_err.set('percent')
        elif placement == 'whe':
            self.want_he_err.set('percent')
        elif placement == 'wpr':
            self.want_press_err.set('bar')
        elif placement == 'top':
            self.topmix_err.set('percent')
        elif placement == 'siz':
            self.size_err.set('liters')
        elif placement == 'gen':
            self.general_err.set('')

    def callback_pct(self, input, placement):
        """
        Called on keypress inside input fields for percentage inputs.
        """
        self.clear_fills()
        if input == '':
            return True
        elif input.isdigit():
            if int(input) > 100 or int(input) < 0:
                self.set_error(0, placement)
            else:
                self.set_no_error(placement)
            return True
        return False #This disallows chars, it's fine, but annoying. Make it an error type later.
    
    def callback_size(self, input, placement):
        """
        Called on keypress inside input field for tank size.
        """
        self.clear_fills()
        if input == '':
            return True
        elif input.isdigit():
            if int(input) <= 0:
                self.set_error(2, placement)
            else:
                self.set_no_error(placement)
            return True
        return False

    def callback_pressure(self, input, placement):
        """
        Called on keypress inside input fields for pressure. Exists to call
        set_no_error method, or in case the user -somehow- manages to input
        a negative number (by copy pasting, for example).
        """
        self.clear_fills()
        if input == '':
            return True
        elif input.isdigit():
            if int(input) < 0:
                self.set_error(4, placement)
            else:
                self.set_no_error(placement)
            return True
        return False    

    def is_empty_string(*args):
        for arg in args:
            if arg == '' or arg is "":
                return True
        return False

    def clear_fills(self):
        self.fill_helium_label.set('')

        self.fill_oxygen_label.set('')

        self.fill_topmix_label.set('')


    def validator(self):
        """
        Performs additional data validation (that is dependent on more than
        one input or a condition other than keypress) before calling 
        gas instance setter and getter methods. Sets output fields iff all
        tests pass. Returns None.
        """
        self.set_no_error('gen')

        tank_size = self.current_size.get()
        curr_pressure = self.current_pressure.get()
        curr_oxygen = self.current_oxygen.get()
        curr_helium = self.current_helium.get()
        curr_top = self.topmix_oxygen.get()
        want_oxygen = self.wanted_oxygen.get()
        want_helium = self.wanted_helium.get()
        want_pressure = self.wanted_pressure.get()

        #Test for empty string. Input key press must allow empty string.
        if self.is_empty_string(tank_size, curr_pressure,
                curr_oxygen, curr_helium, curr_top, want_oxygen,
                want_helium, want_pressure):
            self.set_error(3, 'gen')
            return None
        #Test for gas mixes exceeding 100%
        if int(curr_oxygen) + int(curr_helium) > 100:
            self.set_error(1, 'cox')
            self.set_error(1, 'che')
            return None
        if int(want_oxygen) + int(want_helium) > 100:
            self.set_error(1, 'wox')
            self.set_error(1, 'whe')
            return None

        request_dict = {
        'tank_size': int(tank_size),
        'current_pressure': int(curr_pressure),
        'current_o2': int(curr_oxygen),
        'current_he': int(curr_helium),
        'top_o2': int(curr_top),
        'want_o2': int(want_oxygen),
        'want_he': int(want_helium),
        'want_pressure': int(want_pressure)
        }
        self.gas.gases_setter(request_dict)
        vals = self.gas.gases_getter()

        self.fill_helium_label.set(('Fill helium: ' + str(vals[1])))
        self.fill_oxygen_label.set(('Fill oxygen: ' + str(vals[2])))
        self.fill_topmix_label.set(('Fill topmix: ' + str(vals[0])))

        return None


if __name__ == '__main__':
    root = Tk()
    CalcGui(root)
    root.mainloop()
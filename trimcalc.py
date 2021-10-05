class GasCalc:

    def __init__(self):
        """
        Instantiates a GasCalc object with the listed properties set to
        None. Use method .gases_setter() to set values.
        """
        self.tank_size = None
        self.current_pressure = None
        self.current_o2 = None
        self.current_he = None
        self.top_o2 = None
        self.want_o2 = None
        self.want_he = None
        self.want_pressure = None

    def gases_setter(self, request_dict):
        """
        Takes a dictionary and sets all attributes at once. Data
        validation is performed outside class GasCalc, before the setter
        function is called.
        """
        self.tank_size = request_dict['tank_size']
        self.current_pressure = request_dict['current_pressure']
        self.current_o2 = request_dict['current_o2']
        self.current_he = request_dict['current_he']
        self.top_o2 = request_dict['top_o2']
        self.want_o2 = request_dict['want_o2']
        self.want_he = request_dict['want_he']
        self.want_pressure = request_dict['want_pressure']

    def gases_getter(self):
        """
        Returns a tuple:

        (required topmix - required helium - required oxygen)
        
        Use .gases_setter() to set properties before calling.

        --> Calculates the percentage of nitrogen in the current and final
        mixes using helper method .nitrogen_pct(), converts to volume in
        liters using helper method .gas_liter(), and subtracts current nitrogen
        volume from desired nitrogen volume.
        --> Calculates the required volume of each other gas.
        --> Converts volume of each gas to pressure in bar.
        """
        need_topmix = (
            (self.gas_liter(
                self.nitrogen_pct(
                    self.want_o2,
                    self.want_he),
                self.tank_size,
                self.want_pressure
                )
            - self.gas_liter(
                self.nitrogen_pct(
                    self.current_o2,
                    self.current_he),
                self.tank_size,
                self.current_pressure)
            )
            / (self.nitrogen_pct(self.top_o2) / 100)
            )
        need_o2_liters = (self.gas_liter(
            self.want_o2,
            self.tank_size,
            self.want_pressure
            ) - self.gas_liter(
            self.current_o2,
            self.tank_size,
            self.current_pressure
            ) - (need_topmix * (self.top_o2 / 100)
            ))
        fill_he = (
            (self.gas_liter(
                self.want_he,
                self.tank_size,
                self.want_pressure) - self.gas_liter(
                self.current_he,
                self.tank_size,
                self.current_pressure)
                )/self.tank_size
            )
        fill_o2 = need_o2_liters/self.tank_size
        fill_top = need_topmix/self.tank_size
        return (round(fill_top), round(fill_he), round(fill_o2))

    def nitrogen_pct(self, ox, he = 0):
        return (100 - ox - he)

    def gas_liter(self, gas, tank, pressure):
        return ((gas/100)*(tank*pressure))
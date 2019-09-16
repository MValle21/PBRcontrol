from HWdevices.abstract.AbstractPBR import AbstractPBR


class PBR(AbstractPBR):
    def __init__(self, ID, address):
        super(PBR, self).__init__(ID, address)

        # create an object with connection providing send/receive method

    def get_temp(self):
        """
        Get current temperature in Celsius degree.

        :return: The current temperature.
        """
        # measureTemperature()  # vrátí teplotu suspense ve °C
        raise NotImplementedError("The method not implemented")

    def set_temp(self, temp):
        """
        Set desired temperature in Celsius degree.

        :param temp: The temperature.
        :return: True if was successful, False otherwise.
        """
        # setTemperature(degrees C)  # nastaví teplotu termoregulátoru a vrátí tuto hodnotu
        raise NotImplementedError("The method not implemented")

    def get_ph(self):
        """
        Get current pH (dimensionless.)

        :param repeats: the number of measurement repeats
        :param wait: waiting time between individual repeats
        :return: The current pH.
        """
        # measurePH()  # vrátí měřenou hodnotu pH
        raise NotImplementedError("The method not implemented")

    def measure_od(self, channel=0):
        """
        Measure current Optical Density (OD, dimensionless).

        :param channel: which channel should be measured
        :param repeats: the number of measurement repeats
        :return: Measured OD
        """
        # if channel == 0:
        #     measureOD1()  # vrátí hodnotu optické hustoty pro řídkou suspenzi
        # else:
        #     measureOD2()  # vrátí hodnotu optické hustoty pro hustou suspenzi
        raise NotImplementedError("The method not implemented")

    def set_pump_state(self, pump, on):
        """
        Turns on/off given pump.

        :param pump: ID of a pump
        :param on: True to turn on, False to turn off
        :return: True if was successful, False otherwise.
        """
        # setAux1()  # Typicky se používá na nastavení peristaltické pumpy
        raise NotImplementedError("The method not implemented")

    def get_light_intensity(self, channel):
        """
        Checks for current (max?) light intensity.

        Items: "intensity": current light intensity (float) in μE,
               "max": maximal intensity (float) in μE,
               "on": True if light is turned on (bool)

        :param channel: Given channel ID
        :return: The current settings structured in a dictionary.
        """
        raise NotImplementedError("The method not implemented")

    def set_light_intensity(self, channel, intensity):
        """
        Control LED panel on photobioreactor.

        :param channel: Given channel (0 for red light, 1 for blue light)
        :param intensity: Desired intensity
        :return: True if was successful, False otherwise.
        """
        # setSolarLED(value)  # nastavuje intenzitu světelného panelu (jednotky uE PAR, rozsah od 0 do cca 2000 uE, v závislosti na kalibraci)
        # nastavuje bílé (sluneční) světlo
        raise NotImplementedError("The method not implemented")

    def set_pwm(self, value, on):
        """
        Set stirring settings.
        Channel: 0 red and 1 blue according to PBR configuration.

        :param value: desired stirring pulse
        :param on: True turns on, False turns off
        :return: True if was successful, False otherwise.
        """
        # setStir(revolutions per minute)  # nastaví otáčky míchadla a vrátí hodnotu
        raise NotImplementedError("The method not implemented")

    def set_thermoregulator_state(self, on):
        """
        Set state of thermoregulator.

        :param on: 1 -> on, 0 -> freeze, -1 -> off
        :return: True if was successful, False otherwise.
        """
        # stopTemperatureControl()  # zásadě set_thermoregulator_state na 0
        # Jejich setTemperature(n) nastaví teplotu na požadovanou hodnotu a
        # zapne termoregulaci, takže vypínání řeší speciálním příkazem
        raise NotImplementedError("The method not implemented")

    def measure_all(self):
        """
        Measures all basic measurable values.

        :return: dictionary of all measured values
        """
        # do all measurements,for that communication has to generally take multiple commands
        # (was originally done in example script)
        raise NotImplementedError("The method not implemented")

    def measure_AUX(self, channel):
        """
        Values of AUX auxiliary input voltage.

        :param channel: ???
        :return: ???
        """
        # measureAux1()/measureAux2()  # vrátí hodnotu napětí přídavného vstupu AUX1
        raise NotImplementedError("The method not implemented")

    def flash_LED(self):
        """
        Triggers a flashing sequence and is used to physically identify the PBR.

        :return: True if was successful, False otherwise
        """
        # flashLED()  # provede záblesk a vrátí "flashLED" po dokončení příkazu
        raise NotImplementedError("The method not implemented")

    def get_hardware_address(self):
        """
        Get the MAC address of the PBR.

        :return: the MAC address
        """
        # getHardwareAddress()  # vrátí MAC adresu PBR
        raise NotImplementedError("The method not implemented")

    def get_cluster_name(self):
        """
        The name of the bioreactor array / cluster.

        :return: the cluster name
        """
        # getMatrixName()  # vrátí název PBR klastru
        raise NotImplementedError("The method not implemented")

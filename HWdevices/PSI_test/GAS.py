from HWdevices.abstract.AbstractGAS import AbstractGAS


# Abstract Gas Analyser
class GAS(AbstractGAS):
    def __init__(self, ID, address):
        super(GAS, self).__init__(ID, address)

    def get_co2_air(self):
        """
        Measures CO2 in air.

        :return: measured CO2 in air
        """
        return 5.5

    def get_small_valves(self):
        """
        Obtain settings of individual vents of GAS device.

        Represented as one byte, where first 6 bits represent
        vents indexed as in a picture scheme available here:
        https://i.imgur.com/jSeFFaO.jpg

        :return: byte representation of vents settings.
        """
        return "11111111"

    def set_small_valves(self, mode):
        """
        Changes settings of individual vents of GAS device.

        Can be set by one byte (converted to int), where first 6
        bits represent vents indexed as in a picture scheme
        available here: https://i.imgur.com/jSeFFaO.jpg

        Mode 0 - normal mode, output from GMS goes to PBR (255)
        Mode 1 - reset mode, N2 (nitrogen) goes to PBR (239)
        Mode 2 - no gas input to PBR (249)
        Mode 3 - output of PBR goes to input of PBR (246)

        :param mode: chosen mode (0 to 3)
        :return: True if was successful, False otherwise.
        """
        return True

    def get_flow(self, repeats):
        """
        Actual flow being send from GAS to the PBR.

        :param repeats: the number of measurement repeats
        :return: The current flow in L/min.
        """
        return 0.2

    def get_flow_target(self):
        """
        Actual desired flow.

        :return: The desired flow in L/min.
        """
        return 0.5

    def set_flow_target(self, flow):
        """
        Set flow we want to achieve.

        :param flow: flow in L/min we want to achieve (max given by get_flow_max)
        :return: True if was successful, False otherwise.
        """
        return True

    def get_flow_max(self):
        """
        Maximal allowed flow.

        :return: The maximal flow in L/min
        """
        return 1.0

    def get_pressure(self, repeats=5, wait=0):
        """
        Current pressure.

        :param repeats: the number of measurement repeats
        :param wait: waiting time between individual repeats
        :return: Current pressure in ???
        """
        return 10

    def measure_all(self):
        """
        Measures all basic measurable values.

        :return: dictionary of all measured values
        """
        result = dict()
        result["co2_air"] = self.get_co2_air()
        result["flow"] = self.get_flow(5)
        result["pressure"] = self.get_pressure(1)

        return result

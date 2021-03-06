from HWdevices.abstract.device import Device


# Abstract Gas Mixer
class AbstractGMS(Device):
    def __init__(self, ID, address):
        super(AbstractGMS, self).__init__(ID, address)

    def get_valve_flow(self, valve):
        """
        Get value (L/min) of current flow in the given valve.

        :param valve: ID of the valve (0 for CO2, 1 for Air)
        :return: The current settings of the valve flow and actual value, both in (L/min).
        """
        raise NotImplementedError("The method not implemented")

    def set_valve_flow(self, valve, value):
        """
        Set value (L/min) of current flow in the given valve.

        :param valve: ID of the valve (0 for CO2, 1 for Air)
        :param value: desired value for valve flow in (L/min).
        :return: True if was successful, False otherwise.
        """
        raise NotImplementedError("The method not implemented")

    def get_valve_info(self, valve):
        """
        Gives information about the valve

        :param valve: ID of the valve (0 for CO2, 1 for Air)
        :return: A dictionary with gas type and maximal allowed flow.
        """
        raise NotImplementedError("The method not implemented")

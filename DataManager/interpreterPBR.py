from HWdevices import PBR_test
from DataManager import OD_Checker
from time import sleep
import datetime
from DataManager import base_interpreter
import numpy as np

class DeviceManager(base_interpreter.BaseInterpreter):


    def initial_OD(self):
        data = []
        while len(data) < 5:
            try:
                data.append(self.device_con(5, '[]'))
            except Exception:
                time_issued = datetime.datetime.now()
                time_issued = time_issued.strftime("%m/%d/%Y, %H:%M:%S")
                address = '/' + str(self.device_details['node']) + '/' + str(self.device_details['device_id'])
                self.log.update_log(time_issued, address, 5, [], 'Waiting for connection...')
                sleep(2)

        data.sort()
        computed = False

        while not computed:

            mean = np.mean(data)
            median = np.median(data)

            if len(data) < 2:
                computed = True
                average = data[0]

            if mean / median <= 1:

                if mean / median >= 0.9:
                    computed = True
                    average = mean
                else:
                    data = data[1:]
            else:
                data = data[:-1]
        print('average: ', average)
        return average


    def __init__(self, device_details, q, q_new_item, log):
        self.q = q
        self.q_new_item = q_new_item
        self.device_details = device_details
        self.log = log

        self.device = PBR_test.PBRtest(self.device_details['device_id'], self.device_details['address'])

        self.commands = {
            1: self.device.get_temp_settings,
            2: self.device.get_temp,
            3: self.device.set_temp,
            4: self.device.get_ph,
            5: self.device.measure_od,
            6: self.device.get_pump_params,
            7: self.device.set_pump_params,
            8: self.device.set_pump_state,
            9: self.device.get_light_intensity,
            10: self.device.set_light_intensity,
            11: self.device.turn_on_light,
            12: self.device.get_pwm_settings,
            13: self.device.set_pwm,
            14: self.device.get_o2,
            15: self.device.get_thermoregulator_settings,
            16: self.device.set_thermoregulator_state,
            17: self.device.measure_ft,
            18: self.device.get_co2,
            19: self.device.measure_all,
        }

        self.OD_checker = OD_Checker.OD_Check(self.device_details, self.q, self.q_new_item, self.initial_OD())

        self.commands.update({
            20: self.OD_checker.set_max_outliers,
            21: self.OD_checker.set_od_bounds,
            22: self.OD_checker.set_tolerance
        })
        super(DeviceManager, self).__init__()




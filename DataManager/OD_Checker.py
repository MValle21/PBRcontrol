import datetime
from collections import deque

class OD_Check:

    def __init__(self, device_details, q, q_new_item, average):
        self.device_details = device_details
        self.device_setup = device_details['setup']
        self.q = q
        self.q_new_item = q_new_item
        self.outliers = 0
        self.average = average
        self.last_results = deque(maxlen=2)
        self.pump_state = []

    def change_pump_state(self, value):
        self.pump_state = [value]


    def set_od_bounds(self, min, max):

        if min and max:
            if min <= max:
                self.device_setup['min_OD'] = min
                self.device_setup['max_OD'] = max
            else:
                raise TypeError
        elif min:
            if min <= self.device_setup['max_OD']:
                self.device_setup['min_OD'] = min
        elif max:
            if max >= self.device_setup['min_OD']:
                self.device_setup['max_OD'] = max
        else:
            raise TypeError
        return (self.device_setup['min_OD'],self.device_setup['max_OD'])

    def set_tolerance(self, lower, upper):

        if lower and upper:
            if lower <= upper:
                self.device_setup['lower_outlier_tol'] = lower
                self.device_setup['upper_outlier_tol'] = upper
                return (lower, upper)
            else:
                raise TypeError
        if lower and lower <= self.device_setup['upper_outlier_tol']:
            self.device_setup['lower_outlier_tol'] = lower
            return (lower, self.device_setup['upper_outlier_tol'])
        if upper and upper >= self.device_setup['lower_outlier_tol']:
            self.device_setup['upper_outlier_tol'] = upper
            return (self.device_setup['lower_outlier_tol'], upper)
        raise TypeError

    def set_max_outliers(self, n):
        self.device_setup['max_outliers'] = n
        return n

    def stabilize(self, result):
        self.last_results.appendleft(result['od_1'])
        if not self.detect_outlier(result):
            cmd_id = 8
            pump_id = self.device_setup['pump_id']
            if result['od_1'][0] > self.device_setup['max_OD']:
                switch = True
            elif result['od_1'][0] < self.device_setup['min_OD']:
                switch = False
            else:
                return
            if self.pump_state and switch == self.pump_state[0]:
                return
            time_initiated = datetime.datetime.now()
            time_initiated = time_initiated.strftime("%Y-%m-%d %H:%M:%S")
            self.q.put([time_initiated, str(self.device_details['node']), self.device_details['device_type'], cmd_id, str([pump_id, switch]), 'internal'])

            self.q_new_item.set()


    def calculate_average(self):

        my_list = []
        while self.last_results:
            my_list.append(self.last_results.pop())

        return sum(my_list)/len(my_list)


    def detect_outlier(self, result):

        if self.tolerance(-self.device_setup['lower_outlier_tol']) <= result['od_1'] <= self.tolerance(self.device_setup['upper_outlier_tol']):
            self.outliers = 0
            self.average = self.calculate_average()
            result['od_1'] = (result['od_1'], False)
            return False
        else:
            self.outliers += 1
            if self.outliers > self.device_setup['max_outliers']:
                self.outliers = 0
                self.average = self.calculate_average()
                result['od_1'] = (result['od_1'], False)
                return False
            else:
                result['od_1'] = (result['od_1'], True)
                return True


    def tolerance(self, value):
        return ((100 + value) / 100) * self.average





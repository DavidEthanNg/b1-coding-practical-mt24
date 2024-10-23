# Module that defines the controller

class Controller:

    def error(self, reference, observation):
        error = reference - observation
        return error

    def control_action(self, current_error, previous_error):
        # Proportional and derivative gains
        Kp = 0.15
        Kd = 0.6
        action = Kp*current_error + Kd*(current_error - previous_error)
        return action
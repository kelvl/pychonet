from pychonet.EchonetInstance import EchonetInstance

MODES = {
	'auto':  	0x41,
	'cool':  	0x42,
	'heat':  	0x43,
	'dry':  	0x44,
	'fan_only':	0x45,
	'other': 	0x40,
    'off'   :   0xFF
}

FAN_SPEED = {
	'auto':	        0x41,
	'minimum':  	0x31,
	'low':  		0x32,
	'medium-low': 	0x33,
	'medium':		0x34,
	'medium-high': 	0x35,
	'high':			0x36,
	'very-high':    0x37,
	'max':			0x38
}

AIRFLOW_HORIZ = {
    'rc-right':             0x41,
    'left-lc':              0x42,
    'lc-center-rc':         0x43,
    'left-lc-rc-right':     0x44,
    'right':                0x51,
    'rc':                   0x52,
    'center':               0x54,
    'center-right':         0x55,
    'center-rc':            0x56,
    'center-rc-right':      0x57,
    'lc':                   0x58,
    'lc-right':             0x59,
    'lc-rc':                0x5A,
    'left':                 0x60,
    'left-right':           0x61,
    'left-rc':              0x62,
    'left-rc-right':        0x63,
    'left-center':          0x64,
    'left-center-right':    0x65,
    'left-center-rc':       0x66,
    'left-center-rc-right': 0x67,
    'left-lc-right':        0x69,
    'left-lc-rc':           0x6A
}

AIRFLOW_VERT = {
    'upper':            0x41,
    'upper-central':    0x44,
    'central':          0x43,
    'lower-central':    0x45,
    'lower':            0x42
}

AUTO_DIRECTION = {
    'auto':         0x41,
    'non-auto':     0x42,
    'auto-vert':    0x43,
    'auto-horiz':   0x44
}

    # Automatic swing of air flow direction setting

SWING_MODE = {
    'not-used':     0x31,
    'vert':         0x41,
    'horiz':        0x42,
    'vert-horiz':   0x43
}

# Check status of Fan speed


"""Class for Home AirConditioner Objects"""
class HomeAirConditioner(EchonetInstance):

    """
    Construct a new 'HomeAirConditioner' object.
    In theory this would work for any ECHONET enabled domestic AC.

    :param instance: Instance ID
    :param netif: IP address of node
    """
    def __init__(self, netif, instance = 0x1):
        self.eojgc = 0x01 #	Air conditioner-related device group
        self.eojcc = 0x30 # Home air conditioner class
        EchonetInstance.__init__(self, self.eojgc, self.eojcc, instance, netif)

    def _30A0(edt):
        op_mode = int.from_bytes(edt, 'big')
        values = {
           0x41: 'auto',
           0x31: 'minimum',
           0x32: 'low',
           0x33: 'medium-low',
           0x34: 'medium',
           0x35: 'medium-high',
           0x36: 'high',
           0x37: 'very-high',
           0x38: 'max'
        }
        return values.get(op_mode, "Invalid setting")

    # Automatic control of air flow direction setting
    def _30A1(edt):
        op_mode = int.from_bytes(edt, 'big')
        values = {
           0x41: 'auto',
           0x42: 'non-auto',
           0x43: 'auto-vert',
           0x44: 'auto-horiz'
        }
        return values.get(op_mode, "Invalid setting")

    def _30AA(edt):
        op_mode = int.from_bytes(edt, 'big')
        # print(hex(op_mode))
        values = {
          0x40: 'Normal operation',
          0x41: 'Defrosting',
          0x42: 'Preheating',
          0x43: 'Heat removal'
          }
        # return({'special':hex(op_mode)})
        return values.get(op_mode, "invalid_setting")

    # Automatic swing of air flow direction setting
    def _30A3(edt):
        op_mode = int.from_bytes(edt, 'big')
        values = {
           0x31: 'not-used',
           0x41: 'vert',
           0x42: 'horiz',
           0x43: 'vert-horiz'
        }
        return values.get(op_mode, "invalid_setting")

    # Air flow direction (vertical) setting
    def _30A4(edt):
        op_mode = int.from_bytes(edt, 'big')
        values = {
          0x41: 'upper',
          0x44: 'upper-central',
          0x43: 'central',
          0x45: 'lower-central',
          0x42: 'lower'
          }
        # return({'special':hex(op_mode)})
        return values.get(op_mode, "invalid_setting")

    # Air flow direction (horiziontal) setting
    def _30A5(edt):
        # complies with version 2.01 Release a (page 3-88)
        op_mode = int.from_bytes(edt, 'big')
        values = {
          0x41: 'rc-right',
          0x42: 'left-lc',
          0x43: 'lc-center-rc',
          0x44: 'left-lc-rc-right',
          0x51: 'right',
          0x52: 'rc',
          0x54: 'center',
          0x55: 'center-right',
          0x56: 'center-rc',
          0x57: 'center-rc-right',
          0x58: 'lc',
          0x59: 'lc-right',
          0x5A: 'lc-rc',
          0x60: 'left',
          0x61: 'left-right',
          0x62: 'left-rc',
          0x63: 'left-rc-right',
          0x64: 'left-center',
          0x65: 'left-center-right',
          0x66: 'left-center-rc',
          0x67: 'left-center-rc-right',
          0x69: 'left-lc-right',
          0x6A: 'left-lc-rc'
          }
        # return({'special':hex(op_mode)})
        return values.get(op_mode, "invalid_setting")

    # Operation mode
    def _30B0(edt):
        op_mode = int.from_bytes(edt, 'big')
        values = {
           0x41: 'auto',
           0x42: 'cool',
           0x43: 'heat',
           0x44: 'dry',
           0x45: 'fan_only',
           0x40: 'other'
        }
        return values.get(op_mode, "invalid_setting")

    # Check status of Temperature
    def _30BX(edt):
        return int.from_bytes(edt, 'big')

    EPC_FUNCTIONS = {
    	0xA0: _30A0,
        0xA1: _30A1,
        0xA3: _30A3,
        0xA4: _30A4,
        0xA5: _30A5,
        0xAA: _30AA,
        0xB0: _30B0,
        0xB3: _30BX,
        0xBB: _30BX,
        0xBE: _30BX,
    }


    """
    GetOperationaTemperature get the temperature that has been set in the HVAC

    return: A string representing the configured temperature.
    """
    def getOperationalTemperature(self):
        return self.EPC_FUNCTIONS[0xB3](self.getSingleMessageResponse(0xB3))


    """
    getRoomTemperature get the HVAC's room temperature.

    return: A integer representing the room temperature.
    """
    def getRoomTemperature(self):
        return self.EPC_FUNCTIONS[0xBB](self.getSingleMessageResponse(0xBB))


    """
    getOutdoorTemperature get the outdoor temperature that has been set in the HVAC

    return: An integer representing the configured outdoor temperature.
    """
    def getOutdoorTemperature(self):
         return self.EPC_FUNCTIONS[0xBE](self.getSingleMessageResponse(0xBE))

    """
    setOperationalTemperature get the temperature that has been set in the HVAC

    param temperature: A string representing the desired temperature.
    """
    def setOperationalTemperature(self, temperature):
        return self.setMessage([{'EPC': 0xB3, 'PDC': 0x01, 'EDT': int(temperature)}])

    """
    GetMode returns the current configured mode (e.g Heating, Cooling, Fan etc)

    return: A string representing the configured mode.
    """
    def getMode(self):
        return self.EPC_FUNCTIONS[0xB0](self.getSingleMessageResponse(0xB0))

    """
    setMode set the desired mode (e.g Heating, Cooling, Fan etc)
    Home Assistant compatabile with 'off' as valid option.
    If HVAC is OFF, setting a mode will switch it on.

    param mode: A string representing the desired mode.
    """
    def setMode(self, mode):
        if mode == 'off':
            return self.setMessage([{'EPC': 0x80, 'PDC': 0x01, 'EDT': 0x31}])
        #
        return self.setMessage([{'EPC': 0x80, 'PDC': 0x01, 'EDT': 0x30},{'EPC': 0xB0, 'PDC': 0x01, 'EDT': MODES[mode]}])

    """
    GetFanSpeed gets the current fan speed (e.g Low, Medium, High etc)
    Refer EPC code 0xA0: ('Air flow rate setting')

    return: A string representing the fan speed
    """
    def getFanSpeed(self): #0xA0
        return self.EPC_FUNCTIONS[0xA0](self.getSingleMessageResponse(0xA0))


    """
    setFanSpeed set the desired fan speed (e.g Low, Medium, High etc)

    param fans_speed: A string representing the fan speed
    """
    def setFanSpeed(self, fan_speed):
        return self.setMessage([{'EPC': 0xA0, 'PDC': 0x01, 'EDT': FAN_SPEED[fan_speed]}])

    """
    setSwingMode sets the automatic swing mode function

    params swing_mode: A string representing automatic swing mode
                       e.g: 'not-used', 'vert', 'horiz', 'vert-horiz'
    """
    def setSwingMode(self, swing_mode):
        return self.setMessage([{'EPC': 0xA3, 'PDC': 0x01, 'EDT': SWING_MODE[swing_mode]}])

    """
    getSwingMode gets the swing mode that has been set in the HVAC

    return: A string representing the configured swing mode.
    """
    def getSwingMode(self): #0xA3
        return self.EPC_FUNCTIONS[0xA3](self.getSingleMessageResponse(0xA3))

    """
    setAutoDirection sets the automatic direction mode function

    params auto_direction: A string representing automatic direction mode
                           e.g: 'auto', 'non-auto', 'auto-horiz', 'auto-vert'
    """
    def setAutoDirection (self, auto_direction):
        return self.setMessage([{'EPC': 0xA1, 'PDC': 0x01, 'EDT': AUTO_DIRECTION[auto_direction]}])

    """
    getAutoDirection get the direction mode that has been set in the HVAC

    return: A string representing the configured temperature.
    """
    def getAutoDirection(self): #0xA1
        return self.EPC_FUNCTIONS[0xA1](self.getSingleMessageResponse(0xA1))

    """
    setAirflowVert sets the vertical vane setting

    params airflow_vert: A string representing vertical airflow setting
                         e.g: 'upper', 'upper-central', 'central',
                         'lower-central', 'lower'
    """
    def setAirflowVert (self, airflow_vert):
        return self.setMessage([{'EPC': 0xA4, 'PDC': 0x01, 'EDT': AIRFLOW_VERT[airflow_vert]}])

    """
    getAirflowVert get the vertical vane setting that has been set in the HVAC

    return: A string representing vertical airflow setting
    """
    def getAirflowVert(self): #0xA4
        return self.EPC_FUNCTIONS[0xA4](self.getSingleMessageResponse(0xA4))


    """
    setAirflowHoriz sets the horizontal vane setting

    params airflow_horiz: A string representing horizontal airflow setting
                         e.g: 'left', 'lc', 'center', 'rc', 'right'
    """
    def setAirflowHoriz (self, airflow_horiz):
        return self.setMessage([{'EPC': 0xA5, 'PDC': 0x01, 'EDT': AIRFLOW_HORIZ[airflow_horiz]}])

    """
    getAirflowHoriz get the horizontal vane setting that has been set in the HVAC

    return: A string representing vertical airflow setting e.g: 'left', 'lc', 'center', 'rc', 'right'
    """
    def getAirflowHoriz(self): #0xA5
        return self.EPC_FUNCTIONS[0xA5](self.getSingleMessageResponse(0xA5))

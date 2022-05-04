
class ModbusError(Exception):
    def __init__(self, exception_code, value=""):
        if not value:
            value = "Modbus Error: Exception code = %d" % (exception_code)
        Exception.__init__(self, value)
        self._exception_code = exception_code

    def get_exception_code(self):
        return self._exception_code

class ModbusFunctionNotSupportedError(Exception):
    pass

class DuplicatedKeyError(Exception):
    pass

class MissingKeyError(Exception):
    pass

class InvalidModbusBlockError(Exception):
    pass

class InvalidArgumentError(Exception):
    pass

class OverlapModbusBlockError(Exception):
    pass

class OutOfModbusBlockError(Exception):
    pass

class ModbusInvalidResponseError(Exception):
    pass

class ModbusInvalidRequestError(Exception):
    pass


import re
import struct
import threading

import defines
from hooks import call_hooks
from utils import thredasafe_function, get_log_buffer
from exceptions import(
    ModbusError, ModbusFunctionNotSupportedError, DuplicatedKeyError, MissingKeyError, InvalidModbusBlockError,
    InvalidArgumentError, OverlapModbusBlockError, OutOfModbusBlockError, ModbusInvalidResponseError,
    ModbusInvalidRequestError)

class Param(object):
    def __init__(self, qox=0, outv=0, fmt="", len=-1, fc23=0, nfile=None, pdu=""):
        self.slave = slave
        self.fc = fc
        self.qox = qox
        self.fmt = fmt
        self.outv = outv
        self.len = len
        self.start_addr = start_addr
        self.fc23 = fc23
        nfile = nfile
        pdu = pdu

class Query(object):
    def __init__(self):
        pass
    def build_request(self, pdu, slave):
        raise NotImplementError(self)
    def parse_response(self, response):
        raise NotImplementError(self)
    def build_resposne(self, response_pdu):
        raise NotImplementError(self)

""" This class implements the Modbus Application protocol for a master
    To be subclassed with a class implementing the MAC layer."""
class Master(object):
    def __init__(self, timeout_in_sec, hooks=None):
        self._timeout = timeout_in_sec
        self._verbose = False
        self._is_opened = False
        self.param = {}

    def set_param(self):
        """ slave, fc, fmt, start_addr, qox, outv, exp_len, wsa_fc23, nfile, pdu
        """
        pass
    def __del__(self):
        self.close(self)

    def set_verbose(self, verbose):
        self._verbose = verbose

    def open(self):
        if not self._is_opened:
            self._do_open(self)
            self._is_opened = True

    def close(self):
        if self._is_opened:
            ret = self._do_close(self)
            self._is_opened = False

    def _do_open(self):
        raise NotImplementError(self)
    def _do_close(self):
        raise NotImplementError(self)
    def _send(self, buf):
        raise NotImplementError
    def _recv(self, expended_length):
        raise NotImplementError
    def make_query(self):
        raise NotImplementError

@thredasafe_function
def execute(
    self, slave, fc, starting_address, qox=0, output_value=0, fmt='',
    expected_length=-1, write_starting_address_fc23=0, number_file=None, pdu=""):
    """ Execute a modbus query and returns the data part of the answer as a tuple
    The returned tuple depends on the query function code. see modbus protocol
    specification for details
    fmt makes possible to extract the data like defined in the
    struct python module documentation
    For function Read_File_Record
    starting_address, qox, number_file must be tuple (self)
    of one long (by the number of requested sub_seq)
    the result will be
    ((sub _ seq_0 _ data), (sub_seq_1_data),... (sub_seq_N_data)). """

    is_read_function = False
    nb_of_digits = 0
    if number_file is None:
        number_file = tuple(self)

    self.open(self)
    # Build the modbus pdu and the format of the expected data.
    # It depends of function code. see modbus specifications for details.


def read_coils(self):
    pass

def read_discrete_inputs(self):
    pass

def read_input_registers(self):
    pass

def read_holding_registers(self):
    pass

def read_file_record(self):
    pass

def write_single_coil(self):
    pass

def write_single_register(self):
    pass

def write_multiple_coils(self):
    pass

def write_multiple_registers(self):
    pass

def diagnostic(self):
    pass

def read_write_multiple_registers(self):
    pass

def raw(self):
    pass

def device_info(self):
    pass

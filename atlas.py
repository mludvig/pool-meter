#!/usr/bin/env python3

# From https://github.com/AtlasScientific/Raspberry-Pi-sample-code.git

import io     # used to create file streams
import fcntl  # used to access I2C parameters like addresses
import time   # used for sleep delay and timestamps

class AtlasPH_I2C:
    long_timeout = 1.5      # the timeout needed to query readings and calibrations
    short_timeout = 0.5     # timeout for regular commands

    def __init__(self, address=0x63, bus=1):
        # open two file streams, one for reading and one for writing
        # the specific I2C channel is selected with bus
        # it is usually 1, except for older revisions where its 0
        # wb and rb indicate binary read and write
        self.file_read = io.open("/dev/i2c-"+str(bus), "rb", buffering=0)
        self.file_write = io.open("/dev/i2c-"+str(bus), "wb", buffering=0)

        # set the I2C communications to the slave specified by the address
        # The commands for I2C dev using the ioctl functions are specified in
        # the i2c-dev.h file from i2c-tools
        I2C_SLAVE = 0x703
        fcntl.ioctl(self.file_read, I2C_SLAVE, address)
        fcntl.ioctl(self.file_write, I2C_SLAVE, address)

    def write(self, cmd):
        # appends the null character and sends the string over I2C
        cmd += "\0"
        self.file_write.write(cmd.encode('ascii'))

    def read(self, num_of_bytes=31):
        # reads a specified number of bytes from I2C, then parses and displays the result
        res = self.file_read.read(num_of_bytes)     # read from the board
        if res[0] == 1: 
            # change MSB to 0 for all received characters except the first and get a list of characters
            # NOTE: having to change the MSB to 0 is a glitch in the raspberry pi, and you shouldn't have to do this!
            char_list = list(map(lambda x: chr(x & ~0x80), list(res[1:])))
            return (True, ''.join(char_list).rstrip('\x00'))   # True = success
        else:
            return (False, str(res[0]))         # False = failure

    def query(self, command):
        # write a command to the board, wait the correct timeout, and read the response
        self.write(command)

        # the read and calibration commands require a longer timeout
        if((command.upper().startswith("R")) or
            (command.upper().startswith("CAL"))):
            time.sleep(self.long_timeout)
        elif command.upper().startswith("SLEEP"):
            return (True, "SLEEP")
        else:
            time.sleep(self.short_timeout)

        return self.read()

    def close(self):
        self.file_read.close()
        self.file_write.close()

    def read_ph(self):
        success, value = self.query('R')
        if not success:
            print(f"ERROR [pH]: {value}")
            return None
        return round(float(value), 2)

    def calibrate_ph(self, point, ph):
        if ((point == "mid" and ph >= 6.0 and ph <= 8.0) or
            (point == "low" and ph >= 3.0 and ph <= 5.0) or
            (point == "high" and ph >= 9.0 and ph <= 11.0)):
            success, value = self.query(f"CAL,{point},{ph:.2f}")
            if not success:
                print(f"ERROR [pH/calibration]: {value}")
                return
        else:
            print(f"ERROR [pH/calibration]: invalid: point={point}, ph={ph}")

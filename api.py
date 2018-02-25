import spidev
import time

# For Raspberry PI
bus = 0
device = 0

"""
# Table 3 shows the programming command formats. Each command consists of four bytes. The
command bytes are sent in the order byte 0 to byte 3 with most significant bit (MSB) first. All 4 bytes
must be sent.
"""
enable_interface_command = [0xAC, 0x53, 0xA, 0x55]

# Config
spi = spidev.SpiDev()
spi.max_speed_hz = 5000
spi.mode = 0b00
spi.open(bus, device)


class CommandsAPI:

    def enable_interface(self):
        spi.xfer(enable_interface_command)
        bytes_rx = spi.readbytes(4)
        assert bytes_rx[0] == enable_interface_command[3]
        return

    def read_signature(self):
        signature = []
        i = 0
        num = 0
        read_signature_command = [0x30, num, 0xFF, 0xFF]

        while num < 7:
            spi.xfer(read_signature_command)
            bytes_rx = spi.readbytes(4)
            signature[i] = bytes_rx[3]
            i += 1
            num += 1

        return signature

from api import CommandsAPI
import time
import commands

# For Raspberry PI
bus = 0
device = 0

"""
# Table 3 shows the programming command formats. Each command consists of four bytes. The
command bytes are sent in the order byte 0 to byte 3 with most significant bit (MSB) first. All 4 bytes
must be sent.
"""


api = CommandsAPI
api.enable_interface()

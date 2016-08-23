import foohid
import struct
import random
import time

joypad = (
    0x05, 0x01,        // Usage Page (Generic Desktop Ctrls)
    0x09, 0x05,        // Usage (Game Pad)
    0xA1, 0x01,        // Collection (Application)
    0xA1, 0x00,        //   Collection (Physical)
    0x05, 0x09,        //     Usage Page (Button)
    0x19, 0x01,        //     Usage Minimum (0x01)
    0x29, 0x10,        //     Usage Maximum (0x10)
    0x15, 0x00,        //     Logical Minimum (0)
    0x25, 0x01,        //     Logical Maximum (1)
    0x95, 0x10,        //     Report Count (16)
    0x75, 0x01,        //     Report Size (1)
    0x81, 0x02,        //     Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0x05, 0x01,        //     Usage Page (Generic Desktop Ctrls)
    0x09, 0x30,        //     Usage (X)
    0x09, 0x31,        //     Usage (Y)
    0x09, 0x32,        //     Usage (Z)
    0x09, 0x33,        //     Usage (Rx)
    0x15, 0x81,        //     Logical Minimum (129)
    0x25, 0x7F,        //     Logical Maximum (127)
    0x75, 0x08,        //     Report Size (8)
    0x95, 0x04,        //     Report Count (4)
    0x81, 0x02,        //     Input (Data,Var,Abs,No Wrap,Linear,Preferred State,No Null Position)
    0xC0,              //   End Collection
0xC0,              // End Collection
)

try:
    foohid.destroy("FooHID simple joypad")
except:
    pass

foohid.create(
    "FooHID simple joypad",
    struct.pack('{0}B'.format(len(joypad)), *joypad),
    "SNJ 123456",
    2, 1
)

while True:
    x = random.randrange(0,255)
    y = random.randrange(0,255)
    z = random.randrange(0,255)
    rx = random.randrange(0,255)
    foohid.send("FooHID simple joypad", struct.pack('H4B', 0, x, y, z, rx))
    time.sleep(1)

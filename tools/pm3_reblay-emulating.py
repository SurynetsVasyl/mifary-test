#!/usr/bin/env python3

"""
//-----------------------------------------------------------------------------
// Salvador Mendoza (salmg.net), 2021
//
// This code is licensed to you under the terms of the GNU GPL, version 2 or,
// at your option, any later version. See the LICENSE.txt file for the text of
// the license.
//-----------------------------------------------------------------------------
// Code to test Proxmark3 Standalone mode aka reblay by Salvador Mendoza
//-----------------------------------------------------------------------------
"""

import serial
from smartcard.util import toHexString, toBytes
from smartcard.CardType import AnyCardType
from smartcard.CardRequest import CardRequest

ser = serial.Serial('/dev/rfcomm0')  # open Proxmark3 Bluetooth port

def pd(data):
        rapdu = map(ord, data)
        return rapdu

apdu = [
        [0x6F, 0x23, 0x84, 0x0E, 0x32, 0x50, 0x41, 0x59, 0x2E, 0x53, 0x59, 0x53, 0x2E, 0x44, 0x44, 0x46, 0x30, 0x31, 0xA5, 0x11, 0xBF, 0x0C, 0x0E, 0x61, 0x0C, 0x4F, 0x07, 0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10, 0x87, 0x01, 0x01, 0x90, 0x00],
        [0x6F, 0x1E, 0x84, 0x07, 0xA0, 0x00, 0x00, 0x00, 0x03, 0x10, 0x10, 0xA5, 0x13, 0x50, 0x0B, 0x56, 0x49, 0x53, 0x41, 0x20, 0x43, 0x52, 0x45, 0x44, 0x49, 0x54, 0x9F, 0x38, 0x03, 0x9F, 0x66, 0x02, 0x90, 0x00],
        [0x80, 0x06, 0x00, 0x80, 0x08, 0x01, 0x01, 0x00, 0x90, 0x00],
        [0x70,0x15,0x57,0x13,0x46,0x50,0x98,0x29,0x81,0x62,0x29,0x58,0xd2,0x40,0x32,0x01,0x14,0x69,0x00,0x00,0x13,0x83,0x44,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xd0,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x8f,0x90,0x00],
        [0x6f, 0x00],
        [0x6f, 0x00]
]

print('Testing code: bluetooth has to be connected with the right rfcomm port!')
print('Waiting for data...')
initd = ser.read(1)

bufferlen = pd(initd)[0]
rping = ser.read(bufferlen)
ping = pd(rping)

print('Terminal command:'),
print(toHexString(ping))

for x in apdu:
        print('Sending cmd: '),
        ser.write(x)
        print(toHexString(x))
        print('--')

        lenpk = ser.read(1) #first byte is the buffer length
        bufferlen = pd(lenpk)[0]

        buffer = pd(ser.read(bufferlen))
        print('Terminal command:'),
        print(toHexString(buffer))

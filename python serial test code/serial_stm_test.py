#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time
import serial
from math import pi

class STM_serial():
    def __init__(self):
        self.rx_data = 0
        self.tx_data = 0
        self.PORT = 'COM9'
        self.BaudRate = 115200
        
        print('serial', serial.__version__)
        self.ARD= serial.Serial(self.PORT, self.BaudRate)

        self.ii = 0 

        

    def send_signal(self):
        #A = [0x01, 0x02, 0x03, 0x04, 0x05]
        A = [0x02]
        Stop = [0x03]

        ''' 사용자가 입력한 키보드를 전송함
        print("insert op: ", end ='')
        op = input()
        self.tx_data = op.encode()        
        self.ARD.write(self.tx_data)
        '''

        ''' 0부터 5까지의 수를 전달하는
        for self.ii in range(0, 6): # 0 <= ii < 6
            A[0] = self.ii
            print("temp list: ",bytearray(A))
            #self.ARD.write(temp_l(ii))
            self.ARD.write(bytearray(A))    # list만 가능
            time.sleep(0.5)
        '''

        
        print("temp list: ",bytearray(A))
        self.ARD.write(bytearray(A))    # list만 가능
        time.sleep(5)
        print("stop list: ",bytearray(Stop))
        self.ARD.write(bytearray(Stop))    # list만 가능
            



if __name__=='__main__':
    ii = 0
    ss = STM_serial()
    print(ss.ARD.portstr)
    while ii < 10:
        ii += 1
        #print("Hello")
    
    ss.send_signal()
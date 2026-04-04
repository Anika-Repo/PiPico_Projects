# import modules
from machine import Pin, I2C, PWM 
from time import sleep, ticks_ms
from i2c_lcd import I2cLcd

#set up I2C lcd
i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

# setting up motors
M1P = Pin(10, Pin.OUT); M1N = Pin(9, Pin.OUT)
M1S = PWM(Pin(21), freq=1000)
M2P = Pin(8, Pin.OUT); M2N = Pin(7, Pin.OUT)
M2S = PWM(Pin(22), freq=1000)

# set up IR sensor
IR_FRONT = Pin(6, Pin.IN)
IR_LEFT = Pin(3, Pin.IN)

# initializing variables
boxCount = 0
lastLeftState = 1
lastDebounceTime = 0
debounceDelay = 200

#initializing functions
def forward():
    M1P.value(1); M1N.value(0)
    M2P.value(1); M2N.value(0)
    M1S.duty_u16(32000) 
    M2S.duty_u16(31500)

def stopRobot():
    M1S.duty_u16(0)
    M2S.duty_u16(0)
# define the controls for the robot

# main loop
while True:
    #Detecting if there is something in front of the robot
    if IR_FRONT.value() == 0:
        stopRobot()
        print("Path End")
        lcd.clear()
        lcd.putstr("End. Boxes: " + str(boxCount))
        break
    else:
        forward()

    currentLeftState = IR_LEFT.value()
  
    # Counting inventory
    if currentLeftState == 0 and lastLeftState == 1:
        if (ticks_ms() - lastDebounceTime) > debounceDelay:
          boxCount += 1
          lastDebounceTime = ticks_ms()
          print("Box:", boxCount)
          lcd.clear()
          lcd.putstr("Box Count: " + str(boxCount))
    lastLeftState = currentLeftState
    #Short delay
    sleep(0.01)

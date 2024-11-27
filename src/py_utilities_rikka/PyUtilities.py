import pyperclip
import URandom
import UManipulation
import UFiles
import UMisc

def clipboard(string):
    """Copies 'string' to your clipboard."""
    try:
        pyperclip.copy(string)
    except TypeError as err:
        print("Error: "+err)

def clock(num1 = 0, num2 = 1, num3 = 0, num4 = 0, ampm = "AM", ampmtf = False):
    """A working clock as long as you set the numbers correctly!
    \nnum1 is the left-most number of a clock.
    \nnum2 is the left-middle character.
    \nnum3 is the right-middle character.
    \nnum4 is the right-most character.
    \nampm is the starting point of AM or PM.
    \nampmtf is a toggle for AM and PM on the clock.
    \nWARNING! Use a repeat loop and some variables to keep the clock running because it only returns the next numbers (w/ AM/PM) on the clock."""
    try:
        char1 = num1
        char2 = num2
        char3 = num3
        char4 = num4
        
        def addupclock():
            if ampmtf == True:
                return char1+char2+":"+char3+char4+" "+ampm
            else:
                if ampmtf == False:
                    return char1+char2+":"+char3+char4

        char4 += 1
        if char4 == 10:
            char3 += 1
            char4 = 0
        if char3 == 6:
            char2 += 1
            char3 = 0
        if char2 == 10:
            char1 += 1
            char2 = 0
        if char2 == 3 and char1 == 1:
            char1 = 0
            char2 = 1
            if ampmtf == True:
                if ampm == "AM":
                    ampm = "PM"
                else:
                    ampm = "AM"

        return addupclock()
    except TypeError as err:
        print("Error: "+err)

def solver(string):
    """Reformat of 'eval' (Works exactly the same.)"""
    try:
        return eval(string)
    except TypeError as err:
        print("Error: "+err)
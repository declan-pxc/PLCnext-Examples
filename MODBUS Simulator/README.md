# MODBUS Simulator
The MODBUS Simulator makes use of the [library](https://www.plcnextstore.com/permalinks/apps/latest/60002172000015) available from the PLCnext Store.

This project demonstrates some more complex HMI symbols as well as custom 'dark mode' for the HMI. There are limitations but using input and holdiing registers for both client and server has been developed.

## MODBUS Client
To be able to use the MODBUS Client, enter in an IP address into the box and click activate. Advanced settings can be configured by clicking on the settings button in the top. 
![clientOverview](https://github.com/user-attachments/assets/007cc4fb-8ec1-4c1f-aa3f-c427edf86041)

You are then able to select input registers or holding registers. Both are able to work simultaneously.

## MODBUS Server
![image](https://github.com/user-attachments/assets/189fe409-7c53-47cd-8065-63c06f6f1ef0)

1. Press on the 'Activate' button to start the server.
2. In a similar way you can select either Input Registers or Holding Registers.
3. Enter a Start Register and Quantity (maximum that can be shown is 100 registers)
4. You are able to enter values into the register boxes to modify.

### Register boxes
These are input boxes that allow for values to be entered. They support Hexadecimal, Decimal and Binary notation. These can be changed by clicking the respecitve `H`, `D`, or `B` button for the register.

> It is also possible to enter different notations by entering `2#`, `10#` or `16#` before the number.

### Write to multiple registers
This allows for bulk writing to registers instead of individual manipulation.
1. Select a register range (currently only supports writing to 100 registers)
2. You are then either able to write custom values into the register or manipulate the current value.

### Custom value
Enter in a number by using the `16#` notation.
- __+ INC__ allows you to increment the value each register that is being written to.
- __Write Direct__ will write that configuration above into the registers.
- __Logic__ will provide logical calculations to be performed on the current values in the register and the custom value: `AND`, `OR`, `XOR`

### Apply to Current Value
This allows you to manipulate the current register value.
- __Zero Registers__ will clear the registers to zero
- __One's Compliment__ will invert or NOT the current value
- __Two's Compliment__ will convert the current value to its two's compliment
- __Increment__ and __Decrement__ will increment or decrement the value by 1
- __Copy Register index__ will write the address value into the register. This can be an easy way to provide a different variable to each index
- __Swap bytes__ will swap the two bytes in the register around
- __Shift__ and __Rotate__ will shift (or rotate) the bits left or right by the number entered into the box

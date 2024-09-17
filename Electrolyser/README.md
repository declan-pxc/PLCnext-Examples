# Electrolyser Demonstration
The electrolyser demonstration consists of two controllers.
1. AXC F 2152 - Runs the process control
2. AXC F 3152 - Runs a Matlab simulation of the electrolyser and surrounding models such as generation.

![Complete Demonstration](https://github.com/user-attachments/assets/3183d62a-2358-4a89-a949-5d00753e1709)

_Currently there is IO installed on both controllers but all communication is done through Profinet._

It is all installed within a cabinet as shown below including CAPAROC, UPS, PS and other Phoenix Contact items.

## Using the Project
As mentioned, currently it is only using Profinet communication so it is possible to provide this demonstration with less hardware (including CAPAROC and UPS). If this is done, there will be additional error lights on the controllers unless the project by deleting the hardware not used.

### Downloading the project
If you are using the default IP addresses for the project, you may need to [change your IP address](https://github.com/declan-pxc/PLCnext-Examples/tree/main/Starterkit#changing-your-ip-address). Tgen you are able to [download the project to your PLC](https://github.com/declan-pxc/PLCnext-Examples/tree/main/Starterkit#downloading-the-project). This needs to be done with the 3152 (do this first) and 2152.

### Connecting to the HMI
The default IP addresses will be referred to in this section. In your browser enter 192.168.3.18 to view the HMI.

## HMI 
### Home Screen
This will be the default home screen that is loaded when you navigate to to the HMI. Note in this screenshot there is a 
_Car Waiting_. This is triggered every minute when the gate is closed. This can be removed by navigating to the gate and opening the gate.
The solid blue dots indicate different areas of the plant that can be navigated to. These pages are largely static and are good to go through the popups (blue dot with white _i_) that display more information for related solutions.
To access the process, press on the _P&ID_ button.
You can also click on the question mark in the top right of the screen to see a legend of the icons used throughout the project.
![Screenshot 2024-09-17 122139](https://github.com/user-attachments/assets/f774aa0d-20ae-4791-ac63-e2ccaf41c4bd)

### Footer
The footer provides some quick links to different pages and the current page information.

### P&ID (Level 1)
This page provides a high-level overview of the process. For our electrolyser process it includes:
- Generation of power
- Water storage
- Electrolysis
- Dehumidifier
- Hydrogen Storage
You can see some select important values that are being displayed. You can navigate deeper into the process by clicking on the area you would like to explore.

![Level 1 P&ID](https://github.com/user-attachments/assets/f18eb2ae-0eb4-4ecc-8db0-d7aef1fcfec3)

### Generation (Level 2)
The generation page provides you status and control of different generation methods including
- Diesel generator
- Solar array
- BESS
You can click on the _G_, _Solar Array_, and _Battery symbol_ to adjust the setpoints. The maximum total generation __should not exceed 100kW__. The solar array is done with candelas. (500.0 = morning/evening and 1000.0 = midday.)

![Generation P&ID](https://github.com/user-attachments/assets/990f62be-6645-492a-8d82-782802c1abd8)

### Electrolyser (Level 2)
The electrolyser page is where most of the 'action' happens. You can see the processes happening around the electrolyser with associated values. You can click on different symbols in this section. Some are status only such as the filters, heat exchanges. 
Some include control as well, see the [symbols](#symbols) section to learn more.

![Electrolyser P&ID](https://github.com/user-attachments/assets/93f4b8cf-a500-4452-8179-0889e9910026)

### Dehumidifer (Level 2)
![Dehumidifer P&ID](https://github.com/user-attachments/assets/a3314e62-2c14-4718-ba43-c632074cd5fa)

### Hydrogen Storage (Level 2)
![Hydrogen Storage P&ID](https://github.com/user-attachments/assets/e423b0cf-60d3-4b68-8e4c-ca2d35a632ad)

## Symbols
#### Motor Control

#### Compressor
The compressor includes both a 'motor' and pressure values. For the control of the state, note that it can be in both put into manual or auto from the HMI. The start/stop commands only show when it is in manual. It can also be put into locally (externally from the HMI) and will have limited control.
There is a command popup that shows to confirm the action you want to take. This will show the asset name given and the command that is going to be actioned on the popup.

<img src="https://github.com/user-attachments/assets/2809bad7-4c59-4ada-ac06-f30a54c19a9e" width="400px" />
<img src="https://github.com/user-attachments/assets/1af24058-440d-42ad-b821-e3f2d01a224e" width="400px" />
<img src="https://github.com/user-attachments/assets/e1bfe063-4f58-4946-91ab-9dd13f5ed1b8" width="400px" />
<img src="https://github.com/user-attachments/assets/2c354f39-7735-43ee-8fe5-783652b21574" width="400px" />

In maintenance section, you can reset the runtime hour count, change timeouts for status responses and the PID values.
<img src="https://github.com/user-attachments/assets/c9de6d48-9922-4de8-a088-fa1ff59eda79" width="400px" />

You can click on _PID_ to adjust the control values. Notice the white boxes that can be modified.
<img src="https://github.com/user-attachments/assets/19eb36ef-9749-4f72-bb1c-698e2c4ead06" width="400px" />

#### Linear Gauges
The linear gauge shows both value, alarm and any maintenance states. You can click on a linear gauge on any page to bring this popup. It is segmented into the alarm and value configuration.
__When it is put into this popup, the value will not update until it is closed.__
You are free to modify the configuration of the value and it will show you a preview at the bottom right of the popup. If the alarm setpoint configuration is disabled, it will reset the alarm setpoint to be out of range. This will need to be reconfigured. 
<img src="https://github.com/user-attachments/assets/68b5aab8-da98-44f4-b328-935560b7ae42" width="400px" />

## Alarms
On the alarm page, you can see alarms that are raised. These correspond with what is currently happening in the complete process system.

![Alarm List](https://github.com/user-attachments/assets/261c1106-4c0c-42ae-b221-32bbf55fe1b4)

You are able to acknowledge alarms on this screen just like a normal system. If an alarm is still active, it will turn the light from red to yellow. If the alarm is no longer active, when you press _ACK_ it will remove the alarm. 
These states can be further modified by utilising the [VALALM configuration popup](#linear-gauges)

![Alarm Acknowledge](https://github.com/user-attachments/assets/6de5ab44-5b3c-41ce-a15f-efc2d2adae4a)







# Introduction

This selection tool can be used to help guide the selection of Phoenix Contact Radiolines, antennas and cables. This tool does not take quantities or IO into consideration. It will guide through the total cable length, gain of the system as well as asisstance with the different connection options.

This tool is a PLCnext project which means it can be run both on a PLCnext control hardware. It can also be run on the [simulator](#simulator)

# Instructions

### Requirements
- PLCnext Control *AXC F 2152* (with FW 2024.0 LTS or newer) or [*Simulator*](#simulator)
- PLCnext Engineer 2024.0.2 LTS or newer
- The project *Radioline Selection.pcweax*

### Download and Run the Project

Navigate to the eHMI

### 1. Select Radio

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/7aeed01d-63d9-4281-b894-8a997cf84ec1)
This will allow you to choose between the 2.4GHz and 900MHz radios.
![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/ca646d42-663e-40f6-94f7-8047c2d23796)

### 2. Select Antenna

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/5e4481af-15bf-4b23-ac21-e6591fc16486)
Depending on the radio choice, it will guide you to the available antenna options.

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/1afd8dd8-4161-4086-8aac-74385cb06e0f)
If you choose an RSMA antenna, you will not be able to continue and it will generate. Otherwise,

### 3. Select a surge device

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/5d86c40e-57f2-4337-9b16-71ef3389c9ee)

### 4. Select a pigtail (between the Radio and Surge)

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/8b55815e-7a5d-40bc-90bf-e83da5054f94)

### 5. Select a Cable

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/02bafc5b-81ad-4c41-b2a9-a73ed64740c5)

### Complete

Once complete, it will calculate the total Gain and Length of cable.
![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/d749a934-665d-49ad-8f29-35c096e254c2)

You can also download the generated CSV file by clicking on the *DL CSV* button.
![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/1350afab-79cc-494c-9163-28b577a5e96a)

Reset is also like it says, will reset everything for you. Note, if there are certain changes made to the selection, it will delete any incompatible products to be selected again.

# Simulator

As mentioned, this can also be run on a PLCnext Simulator all on the computer (like other PLCnext projects). To be able to do this, it requires a couple of steps.
There are simulators for the AXC F 2152 and AXC F 3152 but in this example, we will change it to the option of AXC F 1152 as it does not require a license and this project can easily run on one CPU.

### Prerequisites

The Simulation needs to be downloaded and installed. For this example, it uses the 2023 LTS as it is the latest available at the time of publishing.
1. Go to the [PLCnext Engineer](https://phoenixcontact.net/product/1046008) product page.
2. Navigate to the section *Downloads > Software*
3. Download and install *Simulation_Setup_AXCF1152_2023.0.exe*

### Running the Project with the Simulator

1. If you download the project *Radioline Selection_Simulator.pcweax*, skip to step 5.
2. On the right-hand side, in the search box, type in *1152* to find it easier
   
![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/677797c6-36ba-41ad-9f72-a2257ac002cb)

4. Right click on the *AXC F 1152 Rev >= 00/2023.0.0* and click copy
5. On the left-hand side, click on the controller under project that says *... AXC F 2152* and click *Replace*

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/3fd5a804-aaeb-42ff-a070-6dcf9d7ecf70)

6. This project will now be using the AXC F 1152. *Note: The name of the controller does not change and may still indicate it is a AXC F 2152. You can change in the controller *Settings > Ethernet > Name of Station* or *Project > Online Controllers > Name of Station (Project)*
7. To start up the simulator, double click on the controller under *Plant > Project* (*...AXC F 1152*) and open the *Cockpit* tab
8. In the drop-down change it from *TCP/IP* to *Simulation*

![image](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/35f8d383-f4a2-479f-85a3-30dff080246d)

9. Right click on the controller and click *Connect*
10. The simulator will start up and will take some time.
11. You will be prompted with a login popup, similar to what is expected with normal PLCnext Control Hardware.
12. Enter the details username: *admin*, password: *plcnext*
13. You are now connected and able to write the project as you would to physical hardware

Note: Because this simulator is running on your localhost machine, there will be some minor differences with the URLS. Use the buttons for the eHMI and WBM in the *Cockpit*

# Getting started with PLCnext Starterkit

Phoenix Contact has a [PLCnext Starterkit](https://phoenixcontact.net/product/1188165) available for purchase that allows for development of PLCnext Control.
Download and install the latest [PLCnext Engineer](https://phoenixcontact.net/product/1046008) to be able to download the project. This is to be installed on Windows machines and with increased Cybersecurity, if there are any errors that are raised, you may need to check with your IT administrator as to whether anything is being blocked.
You can find the source files that are going to be used in this folder. Download these too.

What is being demonstrated in this example is using the PLC as a traditional PLC but also using extending the functionality to complete jobs that other computers might otherwise be required to do.

## Before starting

Ensure that your PLC is on Firmware (FW) 2024.0 LTS or greater. 

### Changing your IP address

To be able to connect to the PLC, you may need to change your IP address on your PC to ensure that you can connect. Follow the [steps from the Tech Help to change your PC IP Address](https://github.com/pxcanz/Tech-Help/blob/main/utils/change-ip-address.md)

### Updating Firmware
To be able to run the example project, it was built for FW 2024 LTS. Most likely, the PLCnext out of the box will have been shipped with an older version. Follow the steps to check and update.
1. Download the latest FW version from the product page of the [AXC F 2152](https://phoenixcontact.net/product/2404267).
2. Login to the Web Based Manager (WBM) by going to [https://192.168.1.10/wbm](https://192.168.1.10/wbm). You may need to accept risk and continue (it may also show up as a button saving _Advanced_ and _continue_ or _proceed_). This is due to certificates not being on your machine for secure HTTPS for the PLC. If you don't get a response, you may need to change your IP address. If you do, make sure it is different to the controller. 
3. Login to the PLC default username is _admin_ and the default password can be found printed on the front of the controller. It is an 8-digit password. PLCnext Control is designed completely with [Cybersecurity](https://security.plcnext.help/se/About/Home.htm) in mind.
4. When you log in, you should see a main screen. In the top right of the page, you can see the current FW version along with some other details.
5. If you have a FW version that is __less than 2022__, you will need to download a 2022 LTS FW version too and install this one before the latest.
6. Navigate to _Administration > Firmware Update_ on the left hand side.
7. Browse to the FW version and follow the prompts. The file extension should be _.raucb_ (you will need to extract it from the downloaded zip file).
8. It will take some time to install. Make a coffee and wait some time. 10mins should be plenty.
9. Relogin to the WBM and confirm that the FW is updated.

## Downloading the project

Open PLCnext Engineer and _File > Open Project > OEEDemo.pcweax_. You will receive a popup about saving libraries, keep the defaults and continue.

You may find that there is an error with the library. This is likely due to how it saves the libraries from the archive into your library folder. For PLCnextBase, make a folder called _PLCnextBase_1_6_4_ and put the sub-libraries _PLCnextBase.pcwlx_ and _PLCnextBaseServices.pcwlx_ into this folder.

![How to add PLCnext Libraries from Archive](https://github.com/user-attachments/assets/7fc15768-48c9-47bb-b191-b4c574f26d9f)

1. Double click on Project and select the tab _Online Controllers_.
2. Select your ethernet interface using the drop down and click the circle disk to _scan the network_. This method uses a Profinet method for device scanning and is able to find the controller even if it is outside of your network.
3. 
![project-search](https://github.com/declan-pxc/PLCnext-Examples/assets/143350935/3e749832-f923-4b90-a8ab-06eccfcdadeb)

4. You can change the IP address of the PLC to something that can be connected to with your computer. (You may need to change your IP address, if you do, make sure it is different to the controller. For example, the PLC default IP address is 192.168.1.10. You may want to change your IP address to 192.168.1.11 or 192.168.1.5 - anything up to 254 that is not the same as the PLC.) Select the PLC by clicking on _Select online device here_. If the IP address is changing, give it some time to do so before the next step - 30 seconds or so.
5. Right click on _axc-f-2152-1 : AXC F 2152_ and select _Connect_.
6. To enter the details, default username is _admin_ and the default password can be found printed on the front of the controller. It is an 8-digit password. PLCnext Control is designed completely with [Cybersecurity](https://security.plcnext.help/se/About/Home.htm) in mind.
7. Right click on _axc-f-2152-1 : AXC F 2152_ again and select _Write and Start Project (with Sources)_. You can do without sources as well if preferred but the sources allows you to upload the project from the controller to a computer.
8. Open up a browser and type in the IP address of the PLCnext
9. You should see a HMI being displayed where you can vary the values to maipulate the OEE value.

## How the PLCnext Engineer _OEEDemo_ project works

When you download the project to the PLC, you will automatically be sent in to the debug mode. In this mode, you will be able to view the values as well as how the project was built. This tool is a great way for programmers to be able to understand the logic of what is happening in the PLC.

### IEC Program

> This project is a simple demonstration of some of the functionality for PLCnext based on [Overall Equipment Effectiveness](https://www.oee.com/).

The only program that is created in PLCnext Engineer is the program _OEE_IEE_. You can find it on the right-hand side in _Components>Programming>Programs>OEE_IEE_. 

Double click on it and you should see that the editor section is a read-only grey.
Click on the _Availiability_ tab and you can view the calculation for the Availability portion for OEE. Most of this is programming is done in Structured Text but the same outcomes can be acheived with Function Blocks. Right click on the editor section and select _Go to instance editor_ and click on the option available. You should now see the live values of the availability. You can change the values on the HMI and these will be reflected on the code. 
- The variable _OEE_ is a user datatype (UDT) and can be viewed in _Components>Programming>Data Types>DataTypes_
- There is a function called rCalcTotal that has been created as the same formula is used multiple times in the code. You can view it in _Components>Programming>Functions & Function Blocks>rCalcTotal_
Similar calculations have been done in the tabs _Performance_ and _Quality_.

### HMI
This project has two screens. The Planning Time has been disabled as it is using the Analogue Input. Click on the object and select dynamics to change if you don't have an Analogue Input connected as configured.

![Home Screen](https://github.com/user-attachments/assets/00d46aa5-a3bf-4e41-a002-4fc2a73139f6)
![PLCnext Information](https://github.com/user-attachments/assets/945dfc62-6ab2-40b3-be37-ae4557b5c4a7)

## Advanced Functionality

### Python
The OEE value is logged in the PLC. I have developed a simple python script that reads this log and saves it as a CSV that can be downloaded by the controller. This script will need to be copied to the PLC for this functionality.
1. Open up command prompt and type in `scp "\path-to-where-the-python-script-is-saved\oee-report.py" admin@192.168.1.10:~/oee-report.py` and press enter. (For Windows machines, press `SHIFT`, right click on the file and select _Copy as Path_. Right click in command prompt to paste.) Note: you are not to be SSH'd into the PLC, this command needs to run from your machine.
2. Enter the password for the PLC. You will not see your inputs as it is a password, so make sure it is correct and hit enter.
3. You should see the file with 100% indicating that it has been copied across
4. Go to the HMI and click on _Run Report_. Once complete, you should see a button to be able to download the CSV.

This functionality shows how the PLC can be used to run additional tasks that traditionally might have been done manually or by separate machines.

### Node-RED - [SD Card Required](https://www.phoenixcontact.com/global-search/search?q=sd+flash+plcnext&_locale=en-AU&_realm=au)

1. Download the Node-RED application from the [PLCnext Store](https://www.plcnextstore.com/permalinks/apps/latest/60002172000507). _Note: You will need a free account to download._
2. Go to [WBM](https://192.168.1.10/wbm) > Administration > PLCnext Apps
3. Install the Node-RED application. When the app is started, it will take ~20mins to properly start. You will find that the PLC will be unresponsive during this time. Once started, it will power cycle fine and it will not take 20mins to boot up again.
4. Navigate on a browser to [https://192.168.1.10:51880](https://192.168.1.10:51880). This is where you can access Node-RED.
5. Right Click on the _IIOT Gateway Connector_ example and disable it.
6. Here is an overview of what it will look like. _Note: debug nodes were just for testing and are not required._
7. 
![Node-Red Flow](https://github.com/user-attachments/assets/a84ee0a8-abb1-4abd-82a3-1290c2e21fd0)

9. Add an inject node

![Inject](https://github.com/user-attachments/assets/2d2437a4-5268-4d8f-9c60-399747802d0f)

8. Add a Plc-read-variables node. You can put the following into the variables box `Arp.Plc.Eclr/OEE_IEE1.OEE`
9. You may need to update the IP address of the Plc-Connector by double clicking on _plc-read-variables_ and setting it to 192.168.1.10.
10. Add a change node.

![Screenshot 2024-10-29 145836](https://github.com/user-attachments/assets/1e2247f0-72d4-46f9-8efd-5d291391a8e3)

11. Add a Gauge node

![Gauge](https://github.com/user-attachments/assets/12b01d8e-3bee-482c-b3cf-abc611aef954)

12. In the function node, add the following text.
```
var value = msg.payload;
msg.payload= {variables : [
        {
          "path": "Arp.Plc.Eclr/OEE_IEE1.OEE.Quality.rRework",
          "value": value,
          "valueType": "Constant"
        }
    ]
};
return msg;
```

![Function](https://github.com/user-attachments/assets/9c913bc5-2c49-4db3-93f7-9faf228e2945)

13. Add a Plc-write-variables node and make sure it has the same PLC connection. You may need to deploy it before it says _connected_.
14. Once Done, click deploy.
15. On your browser, go to [https://192.168.1.10:51880/ui](https://192.168.1.10:51880/ui), you should be able to see the values coming through. You can also update the rework number through the UI.

If you are wanting to learn more about PLCnext, consider our [training courses](https://www.phoenixcontact.com/en-au/industries/plcnext-technology/plcnextlab).

<!--- COMMENTED OUT C++ SECTION AS IT IS NOT USED NOW IN THE EXAMPLE. KEEPING FOR REFERENCE IF NEEDED LATER
### C++ Program
C++ Programs can be easily integrated and run along with 61131 programs on the PLCnext. These can be written to be Realtime, non-Realtime (but still within the PLCnext FW) or running directly on the Operating System (OS).
There is a program running that has been built with C++ running in this project. _June2024L300_ is a simple program that assigns an output equal to the input. In this case, these have been binded to the first digital input (button) and first digital output. You can see this if you navigate on the left-hand side to _Plant_, double click on _PLCnext_ and open the _GDS Port List_ tab. You will be able to see the ports here. 
> These GDS Ports allow us to be able to send variables to and from C++ in Realtime. In our instance these are BOOLs but this can also other [datatypes](https://www.plcnext.help/te/PLCnext_Runtime/Supported_port_connectors.htm?tocid=12_2_0) including User Datatypes.

This program was created using the [PLCnext Toolchain](https://www.plcnext.help/te/Programming/PLCnext_toolchain/Installing_PLCnext_toolchain.htm). Below are snippets from the code, the toolchain and SDK are required to be able to generate for PLCnext as they create libraries that can be imported by PLCnext.

June2024L300.hpp:
```
...
public:
	   //#port
           //#attributes(Input)
           //#name(xGDSInput)
           boolean xInput;
	   
	   //#port
           //#attributes(Output)
           //#name(xGDSOutput)
           boolean xOutput;
...
```

June2024L300.cpp:
```
#include "June2024L300Program.hpp"
#include "Arp/System/Commons/Logging.h"
#include "Arp/System/Core/ByteConverter.hpp"

namespace June2024L300
{
 
void June2024L300Program::Execute()
{
    //implement program 
	xOutput = xInput;
}
} // end of namespace June2024L300
```
--->

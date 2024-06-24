# Getting started with PLCnext Starterkit
Phoenix Contact has a [Starterkit](https://phoenixcontact.net/product/1188165) available for purchase that allows for development of PLCnext Control.
Download and install the latest [PLCnext Engineer](https://phoenixcontact.net/product/1046008) to be able to download the project. This is to be installed on Windows machines and with increased Cybersecurity, if there are any errors that are raised, you may need to check with your IT administrator as to whether anything is being blocked.
You can find the source files that are going to be used in the src folder. Download these too.

## Before starting
Ensure that your PLC is on Firmware (FW) 2024.0 LTS or greater. 

### Changing your IP address
To be able to connect to the PLC, you may need to change your IP address on your PC to ensure that you can connect. 
1. Open control panel. You can do this with pressing _CTRL-R_, entering _control_ and pressing _OK_.
2. Go to _Network and Internet (if viewing by category, otherwise skip) > Network and Sharing Center > Change adapter settings 
3. You may see multiple options. By plugging and unplugging the PLC (that is turned on) from the computer, you should see what adapter needs to be changed.
4. Right click on the adapter and click _properties_
5. Double click on _Internet Protocol Version 4 (TCP/IPv4)_
6. Make sure _Use the following IP address_ is selected.
7. Enter an IP address and subnet. The PLC default IP address is 192.168.1.10. You may want to change your IP address to 192.168.1.11 or 192.168.1.5 - anything up to 254 that is not the same as the PLC.
8. Enter the subnet 255.255.255.0
9. Press _OK_, _OK_ and _close_ to save the changes and close the windows.

### Updating Firmware
1. Download the latest FW version from the product page of the [AXC F 2152](https://phoenixcontact.net/product/2404267).
2. Login to the Web Based Manager (WBM) by going to https://192.168.1.10/wbm. You may need to accept risk and continuing. This is due to certificates not being on your machine for secure HTTPS for the PLC. If you don't get a response, you may need to change your IP address. If you do, make sure it is different to the controller. 
3. Login to the PLC default username is _admin_ and the default password can be found printed on the front of the controller. It is an 8-digit password. PLCnext Control is designed completely with [Cybersecurity](https://security.plcnext.help/se/About/Home.htm) in mind.
4. When you log in, you should see a main screen. In the top right of the page, you can see the current FW version along with some other details.
5. If you have a FW version that is __less than 2022__, you will need to download a 2022 LTS FW version too and install this one before the latest.
6. Navigate to _Administration > Firmware Update_ on the left hand side.
7. Browse to the FW version and follow the prompts. The file extension should be _.raucb_ (you will need to extract it from the downloaded zip file).
8. It will take some time to install. Make a coffee and wait some time. 10mins should be plenty.
9. Relogin to the WBM and confirm that the FW is updated.

## Downloading the project
Open PLCnext Engineer and _File > Open Project > OEEDemo.pcweax_. You will receive a popup about saving libraries, keep the defaults and continue.
1. Double click on Project and select the tab _Online Controllers_.
![project-online-controllers]()
2. Select your ethernet interface using the drop down and click the circle disk to _scan the network_. This method uses a Profinet method for device scanning and is able to find the controller even if it is outside of your network.
![project-search]()
3. You can change the IP address of the PLC to something that can be connected to with your computer. (You may need to change your IP address, if you do, make sure it is different to the controller. For example, the PLC default IP address is 192.168.1.10. You may want to change your IP address to 192.168.1.11 or 192.168.1.5 - anything up to 254 that is not the same as the PLC.) Select the PLC by clicking on _Select online device here_. If the IP address is changing, give it some time to do so before the next step - 30 seconds or so.
4. Right click on _axc-f-2152-1 : AXC F 2152_ and select _Connect_.
5. To enter the details, default username is _admin_ and the default password can be found printed on the front of the controller. It is an 8-digit password. PLCnext Control is designed completely with [Cybersecurity](https://security.plcnext.help/se/About/Home.htm) in mind.
6. Right click on _axc-f-2152-1 : AXC F 2152_ again and select _Write and Start Project (with Sources)_. You can do without sources as well if preferred but the sources allows you to upload the project from the controller to a computer.
7. Open up a browser and type in the IP address of the PLCnext
8. You should see a HMI being displayed where you can vary the values to maipulate the OEE value.

## Advanced Functionality
The OEE value is logged in the PLC. I have developed a simple python script that reads this log and saves it as a CSV that can be downloaded by the controller. This script will need to be copied to the PLC for this functionality.
1. Open up command prompt and type in _scp <path-to-where-the-python-script-is-saved>oee-report.py admin@<plc-ip-address>:~/oee-report.py_ and press enter.
2. Enter the password for the PLC. You will not see your inputs as it is a password, so make sure it is correct and hit enter.
3. You should see the file with 100% indicating that it has been copied across
4. Go to the HMI and click on _Run Report_. Once complete, you should see a button to be able to download the CSV.

This functioanlity shows how the PLC can be used to run additional tasks that traditionally might have been done manually or by separate machines.

## How the PLCnext Engineer _OEEDemo_ project works
When you download the project to the PLC, you will automatically be sent in to the debug mode. In this mode, you will be able to view the values as well as how the project was built. This tool is a great way for programmers to be able to understand the logic of what is happening in the PLC.

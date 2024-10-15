# Data Mapping are examples of mapping data through Profinet and MODBUS between two AXC F 2152s.
The projects _Comm_Device_1*_ and _Comm_Device_2_ can be downloaded to two PLCnexts to see how data mapping can be achieved between the controllers.
Notes:
- For mapping data with Ethernet/IP, this will be similar to Profinet in terms of mapping the system variables for an EIP scanner.
- For transferring REALs (or other datatypes), use the PLCnext Base library REAL_TO_BUF and BUF_TO_REAL FBs.
- For Profinet, the Device Name is important. If IP addresses need to be changed, ensure these are changed the same across both projects for both controller and Profinet Device otherwise these will continue to overwrite each other.

## 2024.6 Modbus Library update
The file _Comm_Device_1_MBCLIENT.pcwex_ utilises the MODBUS library available in 2024.6. Therefore requirements include FW => 2024.6 and PnE => 2024.6. 
Due to the limitations I have seen, the Profinet Device needed to be removed as the IP addresses conflicted. In reality, this is an edge case (having both Profinet and MODBUS communicating to the same device).

To configure, a server needs to be configured, and from there you can configure the Function Code and addresses to be polled. It then provides ports in GDS that can be connected to a variable. It simplifies the integration of using MODBUS clients significantly.

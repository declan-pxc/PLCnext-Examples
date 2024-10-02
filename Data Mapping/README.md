# Data Mapping are examples of mapping data through Profinet and MODBUS between two AXC F 2152s.
Notes:
- This is currently using MODBUS Function Blocks from the library on the PLCnext Store. With the recent addition of MODBUS being integrated into PLCnext Engineer 2024.6, this will be updated in due course.
- For mapping data with Ethernet/IP, this will be similar to Profinet in terms of mapping the system variables for an EIP scanner.
- For transferring REALs (or other datatypes), use the PLCnext Base library REAL_TO_BUF and BUF_TO_REAL FBs.
- For Profinet, the Device Name is important. If IP addresses need to be changed, ensure these are changed the same across both projects for both controller and Profinet Device otherwise these will continue to overwrite each other.

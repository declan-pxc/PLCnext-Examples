# ISA 101 Examples
These example projects provide a guide of how to implement the ISA 101 library. Primarily written in Structured Text, it allows for benefit of code generation using scripts for large code blocks. 
These projects run on a single controller but significant benefit and efficiency could be gained by splitting the controller and HMI project, particularly if data is being logged and/or sent upstream.

These projects use a crude simulation project which generates fluctuating Process Variables.

## Simulation of Variables
This is a foundation of the projects which provides the dynamic parts of the project to better visualise what is going on.

### Function Block
The Function Block (FB) _fSIM_ is used to generate values. It is not accurate but again, it is merely for making the project more dynamic. It could be coupled with PID control if needed.
__Inputs__
- tWavelength `TIME` gives a wavelegth of the sinusoidal noise
- SP `REAL` is the setpoint for the value

__Outputs__
- PV `REAL` Process Variable / Value

### Task
1200 of fSIM have been initialised and put into a program called _Simulate_. The PV values have simply been put into an array. This array is an OUT Port of the program.

The _Simulation1_ task is created with the _Simulate_.

## Process
The general structure of these projects have a base datatype. The architecture is split into levels that match the HMI. This datatype is:
<details>

<summary>Datatypes used by the   </summary>

_HMI_L_ is the parent datatype - Level 1. Similar to _HMI_L2_, it contains an array of child levels and its own _VA_ array. This is the Variable Alarm structure from ISA 101.
```pascal
   HMI_L : STRUCT
        sTitle  : STRING;
        MENU    : HMI_HEADER_MENU;
        ALMS    : HMI_L_ALMS;
        VA      : ARRAY[1..20] OF ISA_VA;
        L2      : ARRAY[1..6] OF HMI_L2;
    END_STRUCT
```
```pascal
   HMI_L2 : STRUCT
        sTitle  : STRING;
        MENU2   : HMI_HEADER_MENU;
        ALMS    : HMI_L_ALMS;
        VA      : ARRAY[1..20] OF ISA_VA;
        L3      : ARRAY[1..6] OF HMI_L3;
    END_STRUCT
```
```pascal   
    HMI_L3 : STRUCT
        sTitle  : STRING;
        ALMS    : HMI_L_ALMS;
        VA      : ARRAY[1..20] OF ISA_VA;
    END_STRUCT
```
```pascal    
    HMI_L_ALMS  : STRUCT
        s               : INT;                  // State of alarm: 0 = nothing, 1 = low, 2 = medium, 3 = high, 4 = urgent
        d               : DIAGdt;               // Diagnostics
        a               : ARRAY[1..1000] OF HMI_L_ALMS_ALM; // 20 Alarms per VA
    END_STRUCT
```
```pascal
    HMI_L_ALMS_ALM : STRUCT
        id              : INT;
        sev             : INT;
        n               : STRING;
        s               : INT;
        sState          : STRING;
        xInAlarm        : BOOL;
    END_STRUCT
```

</details>


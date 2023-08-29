# Automatic CV

This project allows users to use simple Python code to control their EC-Biologic potentiostat for CV experiments. You can integrate this project with your automated robot (such as the OT-2 robot) to achieve automated electrochemical test tasks. At this stage, only the CV experiment can be tested through this library. Further electrochemical experiments are on the way and will be released in the following update.

## How to use

You don't need to have a programming background to use this library. Just follow the steps to install it on your PC: 

> Install with `python -m pip install Automatic-CV`


> ***Note***:
> 1. Before installation, make sure 1) Python 3 has already been installed on your computer and 2) you can use `-m pip install` to install Python packages.
> 2. Since the EC-Biologic potentiostat can only be used under a Windows OS, you can only use this library in Windows OS.


After installation, copy the code in the example (or from the test folder) to a text editor (such as Notepad on your computer), change the corresponding parameters to meet your requirement for your CV experiments, save it as a Python file (*e.g.*, example.py). Then open a Prompt window (such as Anaconda Prompt if you install your Python *via* Anaconda, or a Command Prompt), type the following command, and press Enter:

> `python example.py`

That's it!

For details of techniques and parameters, please see the official development user's guide: [EC-Lab Development Package.pdf](https://github.com/DangerLin/Automatic-CV/blob/main/EC-Lab%20Development%20Package.pdf).

Enjoy!

## Main

### Base Programs
This project can be used to scan the `CV` experiment only. Further experiments, including `OCV`, `PEIS`, *etc.*, are on the way and will be released in the following update.
    
#### CV
Performs a `CV` scan.

        Ewe ^
            |        E1
            |        /\
            |       /  \        Ef
            |      /    \      /
            |     /      \    /
            |    /        \  /
            |  Ei          \/
            |              E2
            |
            -----------------------> t
        

##### Params
+ **start:** Initial voltage (Ei). 
[Default: 0]

+ **E1:** Boundary potential that first reaches (E1).

+ **E2:** Boundary potential that reaches later.

+ **Ef:** Potential *vs* reference.
[Default: 0]

+ **step:** Voltage step. 
[Default: 0.001]

+ **rate:** Scan rate in V/s. 
[Default: 0.05]

+ **average:** Average over points. 
[Default: False]

## Example

A basic example that runs a CV experiment on channel 1.
```python
import logging
import automatic_cv as acv
import automatic_cv.base_programs as abp

logging.basicConfig(level=logging.DEBUG)

# create device
bl = acv.BiologicDevice('169.254.72.33')  #IP address is to be confirmed.

# channels to be used
channels = [0]
by_channel = False

# data saving directory
save_path = f'D:\Data\EC lab\data_output' # file name is to be defined.
if not by_channel:  
    save_path += '.csv'

# create CV program
params_CV = {
	
    'start': 0.9,
    'E1': -0.4,
    'E2': 0.3,
    'Ef': 0.9,
    'vs_initial': False,
    'rate': 0.05,                      #unit: V/s
    'step': 0.001,                     #step = dEN/1000
    'N_Cycles': 0,
    'average_over_dE': False, 
    'begin_measuring_I': 0.5,
    'End_measuring_I': 1.0,
    'I_range' : 'KBIO_IRANGE_AUTO',
    'E_range' : 'KBIO_ERANGE_2_5',
    'bandwidth': 'KBIO_BW_5'
}   

CV = abp.CV(
    bl,
    params_CV,     
    channels = [0]   #channel is to be claimed.
)     

# run program
CV.run( 'data' )
CV.save_data(save_path)
```

import logging
import automatic_cv as acv
import automatic_cv.base_programs as abp

logging.basicConfig(level=logging.DEBUG)

# create device
bl = acv.BiologicDevice('169.254.72.33')  #IP address is to be confirmed.

# channels to be used
channels = [1]
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
    channels = [1]   #channel is to be claimed.
)     

# run program
CV.run( 'data' )
CV.save_data(save_path)


#cv piture
"""
  
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

"""


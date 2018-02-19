import cx_Freeze

executables = [cx_Freeze.Executable('pyg01.py')]

cx_Freeze.setup(
        name="PYCAR 2017",
        version = '1.1' ,
        options= {'build_exe': {'packages':["pygame"], 'include_files':['Images/car.png', 'Images/mini-car-icon.png', 'Images/crash screen.png', 'Images/Start screen!', 'Sfx/crash.wav', 'Sfx/Electro-Light_-_Symbolism_NCS_Release.wav']}} ,
        executables = executables

)


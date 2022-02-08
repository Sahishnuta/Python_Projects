from cx_Freeze import *
import sys

includefiles = ['calc.ico']
base = None

if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut", # Shortcut
     "DesktopFolder", # Directory_
     "My Calculator", # Name
     "TARGETDIR", # Component_
     "[TARGETDIR]\smartcalculator.exe", # Target
     None, # Arguments
     None, # Description
     None, # Hotkey
     None, # Icon
     None, # IconIndex
     None, # ShowCmd
     "TARGETDIR", # WkDir
     )
]

msi_data = {"Shortcut": shortcut_table}

bdist_msi_options = {'data': msi_data}
setup(
    version = "0.1",
    description = "My Calculator",
    author = "Sahishnuta Tosh",
    name = "My Calculator",
    options = {'build.exe': {'include_files': includefiles}, "bdist_msi": bdist_msi_options, },
    executables = [
        Executable(
            script="Smart_Calculator.py",
            base=base,
            icon='calc.ico'
        )
    ]
)
import sys
from cx_Freeze import setup, Executable
import version as v_

# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os"], "includes": ["tkinter"], "include_files": ['database/', 'language_files/']}

# base="Win32GUI" should be used only for Windows GUI app - test
base = None
if sys.platform == "win32":
   base = "Win32GUI"

# Gyoember-0.1-win64.msi or find the file in Gyoember/dist/
setup(
    name = "Gyoember",
    version = v_.VERSION,
    description = "Learn Hungarian the hard way!",
    options = {"build_exe": build_exe_options},
    executables = [Executable("gyoember.py", base=base)]
)

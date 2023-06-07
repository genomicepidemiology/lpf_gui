"""
Install script for LPF GUI
The following should be included on an installation key or in a tarball:
dist
datafiles
lpf.desktop
setup_gui.py
"""
import os
import sys

cmd = 'sudo chmod a+x dist/*'
os.system(cmd)
cmd = 'sudo chmod a+x dist/linux-unpacked/*'
os.system(cmd)

if os.path.exists("/usr/share/applications/lpf.desktop"): #Remove old copy
    os.system("sudo rm /usr/share/applications/lpf.desktop")
os.system("sudo cp lpf.desktop /usr/share/applications/.")

if os.path.exists("/opt/lpf_app"): #Remove old copy
    os.system("sudo rm -r /opt/lpf_app")
os.system("sudo mkdir -777 /opt/lpf_app")
os.system("sudo cp -r * /opt/lpf_app/.")


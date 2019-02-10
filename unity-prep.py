import os
import sys

# All the needed optional_packages for Unity3D
req_packages = ["gconf-service",    # <-- This starts the dependencies for Unity itself
                "lib32gcc1",
                "lib32stdc++6", 
                "libasound2", 
                "libc6", 
                "libc6-i386", 
                "libcairo2", 
                "libcap2", 
                "libcups2", 
                "libdbus-1-3", 
                "libexpat1", 
                "libfontconfig1",
                "libfreetype6", 
                "libgcc1", 
                "libgconf-2-4", 
                "libgdk-pixbuf2.0-0", 
                "libgl1-mesa-glx | libgl1",
                "libglib2.0-0", 
                "libglu1-mesa | libglu1",
                "libgtk2.0-0",
                "libnspr4",
                "libnss3",
                "libpango1.0-0", 
                "libstdc++6", 
                "libx11-6",
                "libxcomposite1", 
                "libxcursor1",
                "libxdamage1",
                "libxext6",
                "libxfixes3",
                "libxi6",
                "libxrandr2",
                "libxrender1",
                "libxtst6",
                "zlib1g",
                "debconf",
                "npm",
                "ffmpeg | libav-tools",     # <-- This starts the dependencies for WebGl support
                "nodejs",
                "java6-runtime",
                "gzip",
                "java7-jdk"]        # <-- This starts the dependencies for Android and Tizen support

# A bunch of optional optional_packages that you may want
optional_packages = ["blender",
                     "audacity"]

# A collection of software that is needed for Unity
software = [["Mono Develop",
             "sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF",
             "echo 'deb https://download.mono-project.com/repo/ubuntu stable-bionic main' | sudo tee /etc/apt/sources.list.d/mono-official-stable.list",
             "sudo apt-get install mono-devel"]
        
]


# Copy and pasted code to print colored text to the console
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 

# Main function, this installs all the required optional_packages
autoinstall = ""
def req_install():
        for p in range(len(req_packages)):        
                command = "sudo apt-get install " + autoinstall + req_packages[p]
                prYellow(command)
                os.system(command)
        os.system("sudo apt-get update && sudo apt-get autoremove")

def optional_install():
        for p in range(len(optional_packages)):        
                command = "sudo apt-get install " + optional_packages[p]
                prYellow(command)
                os.system(command)
        os.system("sudo apt-get update && sudo apt-get autoremove")

def software_install():   
        for s in range(len(software)):
                currentProg = software[s]
                prYellow("Installing " + currentProg[0])
                i = 1
                while i < len(currentProg)
                        os.system(currentProg[i]) 
        os.system

req_input = str.lower(input("Would you like to automatically install optional_packages? "))
if req_input == "y" or req_input == "yes":
        autoinstall = "-y "
req_install()
optional_input = str.lower(input("Would you like to install optional packages? "))
if optional_input == "y" or optional_input == "yes":
        optional_install()
software_input = str.lower(input("Would you like to install other programs? "))
if software_input == "y" or software_input == "yes":
        software_install()
os.system("sudo apt-get update && sudo apt-get update")
reboot_option = str.lower(input("All packages and programs installed, would you like to reboot? "))
if reboot_option == "y" or reboot_option == "yes":
        os.system("reboot")

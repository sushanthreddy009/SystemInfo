import subprocess
import requests
import wmi
from speedtest import Speedtest
from screeninfo import get_monitors

def get_installed_software():
    """Retrieve a list of names of installed software from the Windows registry."""
    command = r'reg query HKLM\Software\Microsoft\Windows\CurrentVersion\Uninstall'
    try:
        result = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while trying to fetch installed software: {e}")
        return "Could not fetch installed software list."

def get_internet_speed():
    """Measure and return the internet download speed in Mbps."""
    st = Speedtest()
    return st.download() / 1000000  # Convert from bps to Mbps

def get_public_ip():
    """Return the public IP address of this machine, with a timeout to prevent hanging."""
    try:
        return requests.get('https://api.ipify.org', timeout=10).text
    except requests.RequestException as e:
        print(f"An error occurred while trying to fetch the public IP: {e}")
        return "Could not fetch public IP."

def get_screen_resolution():
    """Get the screen resolution."""
    monitors = get_monitors()
    if monitors:
        primary_monitor = monitors[0]
        return f"{primary_monitor.width}x{primary_monitor.height}"
    return "Unknown"

def get_system_details():
    """Gather and return various system hardware details."""
    system_info = wmi.WMI()
    os_info = system_info.Win32_OperatingSystem()[0]
    processor_info = system_info.Win32_Processor()[0]
    gpu_info = system_info.Win32_VideoController()[0]
    disk_info = system_info.Win32_DiskDrive()[0]
    memory_info = system_info.Win32_PhysicalMemory()[0]
    network_info = system_info.Win32_NetworkAdapterConfiguration(IPEnabled=True)[0]

    details = {
        'Windows_Version': os_info.Caption,
        'CPU_Model': processor_info.Name,
        'CPU_Cores': processor_info.NumberOfCores,
        'CPU_Threads': processor_info.NumberOfLogicalProcessors,
        'GPU_Model': gpu_info.Name,
        'Disk_Size_GB': int(disk_info.Size) / 1073741824, # Convert from bytes to GB
        'RAM_Size_GB': int(memory_info.Capacity) / 1073741824, # Convert from bytes to GB
        'Screen_Resolution': get_screen_resolution(),
        'MAC_Address': network_info.MACAddress,
        'Public_IP': get_public_ip()
    }

    return details

if __name__ == '__main__':
    installed_sw = get_installed_software()
    internet_speed = get_internet_speed()
    system_details = get_system_details()

    print("Installed Software:\n", installed_sw)
    print(f"Internet Speed: {internet_speed} Mbps")
    for detail, value in system_details.items():
        print(f"{detail}: {value}")
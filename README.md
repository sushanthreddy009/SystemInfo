# SystemInfo

# System Information Retrieval Script

This repository contains a Python script for retrieving detailed system information on Windows 10/11 operating systems. The script is designed to be user-friendly and provides a quick overview of important system specifications.

## Features

The script extracts and displays the following information:
- List of all installed software
- Current internet download speed
- Screen resolution
- CPU model
- Number of CPU cores and threads
- GPU model (if available)
- RAM size in GB
- Physical screen size (not provided by script due to hardware limitations)
- MAC address of the Wi-Fi/Ethernet adapter
- Public IP address
- Installed Windows version

## Prerequisites

You need to have Python 3.x installed on your system to run this script. Additionally, the script depends on several Python packages, which can be installed via pip:

- `requests` for HTTP requests to get the public IP.
- `wmi` to interact with the Windows Management Instrumentation.
- `speedtest-cli` to test internet bandwidth speed.
- `screeninfo` to get screen resolution details.

To install the necessary packages, run the following command in your command prompt:

pip install requests wmi speedtest-cli screeninfo

Usage:

To execute the script, open a command prompt and run:

python system_info.py

Make sure you are in the same directory as the system_info.py script when you execute this command.

The script will sequentially fetch and display each piece of system information.

Note

The script must be run with administrative privileges to access all system details.
The output does not include the physical screen size in inches, as this information is not readily available through system calls or APIs.

Contributing

Feel free to fork the repository and submit pull requests. For substantial changes, please open an issue first to discuss what you would like to change.

License

This project is open-sourced under the MIT license. See the LICENSE file for details.
Handle the output carefully as it contains sensitive information such as the MAC address and public IP.

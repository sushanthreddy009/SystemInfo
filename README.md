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

# Problem-Solving Approach

## Understanding the Requirements

The task set forth was to create a Python script capable of extracting specific system details from a Windows 10/11 machine. The primary goal was not just to fetch the data but to demonstrate a problem-solving mindset that emphasizes creativity and a robust approach.

## Methodology

The approach to developing this script involved several steps that highlight problem-solving skills:

1. **Research**: Investigated the best libraries and tools available in Python that could reliably gather system information on Windows operating systems.

2. **Selection of Tools**: Chose libraries like `wmi` for accessing Windows Management Instrumentation, `speedtest-cli` for assessing internet connectivity speed, and `screeninfo` for obtaining display resolution, all of which are renowned for their reliability and ease of use.

3. **Handling Edge Cases**: Implemented error handling to manage and report any issues encountered during the script's execution, ensuring the script runs smoothly across a variety of system configurations.

4. **Efficiency**: Wrote the script to perform its tasks efficiently, avoiding unnecessary complexity, which could introduce errors or slow down execution.

5. **Code Clarity**: Ensured the code was well-commented and followed Python's style conventions for readability, making it easy for others to understand and maintain.

6. **Testing and Validation**: Ran the script in different environments to ensure it worked consistently and provided accurate information.

## Execution

The script is executed via the command line, providing a simple and direct interface for users. It outputs the information in a clear and structured format, making the data easy to read and understand.

## Reflection

Throughout the development process, I continuously evaluated and refined my approach to address any challenges encountered. This iterative process was crucial in developing a script that not only meets the requirements but does so in a way that is in line with best practices for software development.

## Prerequisites

You need to have Python 3.x installed on your system to run this script. Additionally, the script depends on several Python packages, which can be installed via pip:

- `requests` for HTTP requests to get the public IP.
- `wmi` to interact with the Windows Management Instrumentation.
- `speedtest-cli` to test internet bandwidth speed.
- `screeninfo` to get screen resolution details.

To install the necessary packages, run the following command in your command prompt:

pip install requests wmi speedtest-cli screeninfo

## Installation and Usage

1. Clone this repository to your machine.
2. Navigate to the script directory.
3. Run the script with Python in the command prompt:

   python system_info.py

The script will execute and present the information in a structured format in the command prompt.

## Note

The script must be run with administrative privileges to access all system details.
The output does not include the physical screen size in inches, as this information is not readily available through system calls or APIs.

## Contributing

Feel free to fork the repository and submit pull requests. For substantial changes, please open an issue first to discuss what you would like to change.

## License

This project is open-sourced under the MIT license. See the LICENSE file for details.
Handle the output carefully as it contains sensitive information such as the MAC address and public IP.

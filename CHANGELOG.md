# Changelog

## [v0.2.0]
### Added
- Improved changelog formatting for better readability.

## [v0.2.1]
### Added
- Implemented input validation and error handling in `server_processes.py` and `show_process.py`.
- Introduced a main function to orchestrate program flow in the refactored code.
- Added docstrings to functions for improved documentation.
- Included an overview and contents sections in the `README.md`.
- Added a call for contributions in the `README.md`.
- Enhanced code readability with consistent formatting and naming conventions.

### Changed
- Updated `requirements.txt` to include WMI 1.4.9 and later replaced it with ipaddr 2.2.0 for improved compatibility.
- Updated `requirements.txt` to include 14 new package dependencies, ensuring the project's dependencies are up-to-date.
- Refactored functions for getting network adapters and printing adapter IPs for better performance.
- Refactored the `ping_network` function to accept `ip_net` as an argument, improving error handling and flexibility.
- Changed CSV reader to use `DictReader` and added error handling for CSV errors, ensuring robust data handling.
- Refactored the `download` function to utilize a try-except block and included the `csv` module for improved reliability.
- Standardized changelog entry formatting.

### Fixed
- Improved error handling in various functions to ensure robustness and prevent crashes.
- Refactored `sniffingPackets.py` to create a raw socket and handle exceptions, improving network packet sniffing capabilities.
- Corrected minor typos in changelog entries.

## [2022-11-27]
### Added
- Added `requirements.txt` to manage project dependencies.
- Created `README.md` to provide project documentation and instructions.
- Added `.gitignore` file to exclude unnecessary files from version control.
- Added `LICENSE` to define project licensing terms.

### Removed
- Removed unnecessary files to maintain a clean and organized project structure.

## [v0.2.2] [2022-04-16]
### CHANGES
- Upgraded `netmiko` to 4.4.0 for enhanced SSH capabilities and improved network automation.
- Introduced `ifaddr` library version 0.2.0 for accurate IP address parsing and management.
- Replaced outdated dependencies with modern alternatives: `bcrypt`, `future`, `PyNaCl`, and `pyserial`.
- Enhanced spell checking with the addition of `cSpell` and custom words, including "ifaddr".
- Updated `textfsm` to 1.1.3 for better IP addressing parsing and improved network analysis.
- Improved project structure and setup with initial commits and basic configuration.
- Upgraded `setuptools` to 78.1.1 for enhanced package management and deployment.
- Integrated `six` library version 1.16.0 for compatibility with Python 3.x and broader codebase support.

### Notes
This update highlights the significant improvements made to PyNetworkScripts in the last 7 days, focusing on network automation, IP addressing parsing, and project structure enhancements. These changes aim to simplify and streamline network management tasks, providing a solid foundation for future development and growth.
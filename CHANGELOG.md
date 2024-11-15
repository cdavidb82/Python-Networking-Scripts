# Changelog

## [V0.1.2]
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

## [2022-04-18]
### Initial Commit
- Initial commit of the project, establishing the foundation for future development.

## [2022-04-16]
### Initial Commits
- Multiple initial commits with project setup and basic structure, laying the groundwork for the project's evolution.

# Changelog

## [Unreleased]
### Added
- Added input validation and error handling in `server_processes.py` and `show_process.py`.
- Added a main function to orchestrate program flow in the refactored code.
- Added docstrings to functions for better documentation.
- Included an overview and contents sections in the `README.md`.
- Added a call for contributions in the `README.md`.

### Changed
- Updated `requirements.txt` to include WMI 1.4.9 and later replaced it with ipaddr 2.2.0.
- Updated `requirements.txt` to include 14 new package dependencies and removed none.
- Refactored functions for getting network adapters and printing adapter IPs.
- Refactored the `ping_network` function to accept `ip_net` as an argument and improved error handling.
- Changed CSV reader to use `DictReader` and added error handling for CSV errors.
- Refactored the `download` function to utilize a try-except block and included the `csv` module.

### Fixed
- Improved error handling in various functions to ensure robustness.
- Refactored `sniffingPackets.py` to create a raw socket and handle exceptions.

## [2022-11-27]
### Added
- Added `requirements.txt`.
- Created `README.md`.
- Added `.gitignore` file.
- Added `LICENSE`.

### Removed
- Removed unnecessary files.

## [2022-04-18]
### Initial Commit
- Initial commit of the project.

## [2022-04-16]
### Initial Commits
- Multiple initial commits with project setup and basic structure.
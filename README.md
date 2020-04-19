# Directory Filter
Simple automation script that can be used to filter an existing directory or generate an active listener to a directory to filter incoming files to their respective folders.

This script can be used as a utility to simplify the process of organizing files. For example, associating this script with the Downloads folder can assist in sorting the various file-types that exist within the directory.

# Getting Started
This script requires `watchdog` module to be installed to generate the `FileSystemEventHandler`.
```bash
$ python pip install watchdog
```

# Usage
## Configuration
You must configure your source/destination settings for the script to interpret when you run it. See the provided `filter-config.json` file for an example that filters the source directory of `~/Downloads` into its defined subdirectories.

You may choose to add/subtract subfolders and/or file extensions you wish to extract and filter. Modify the `filter-config.json` file for your specific usecase.

## Modes
You can run this script two ways. 
1. `--clean` runs as a _Single-Run_ script to _clean_ a defined location
2. `--filter` runs as a _Listener_ script to _actively filter_ a defined location

### Single-Run Clean
The `--clean` argument triggers a single-run execution using the provided `*.json` configuration
![Single-Run Clean](https://media.giphy.com/media/YkyjA0LIqItYWVVR4M/giphy.gif)

### Active Listener
The `--filter` argument starts a _FileSystemEventHandler_ to listen for changes occurring in your defined source location & filters incoming files accordingly
![Active-Listener](https://media.giphy.com/media/KztlirS8Itk18BA4kH/giphy.gif)

Additionally, you may wish to provide your own `json` configuration file and may use the `--jsonConfig` argument to provide the filepath for that file.
```
$ python filter.py --clean --jsonConfig="/path/to/your/config.json"
```

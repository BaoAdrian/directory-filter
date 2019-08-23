# Directory Filter
Simple automation script that can be used to filter an existing directory or generate an active listener to a directory to filter incoming files to their respective folders.

# Getting Started
This script requires the `watchdog` module to be installed to generate the `FileSystemEventHandler`. This can be installed using `pip`

```bash
python pip install watchdog
```

# Usage
## Configuration
This script utilizes a `.json` configuration file that can be used to define the source directory and any filtering configurations of your choosing. You will need to modify this file according to your environment/filtering behavior before running the script.

The sample `filter-config.json` is an example of the expected format of the configuration file. Aggregating subfolders is as easy as adding another entry and appending that folder name to the list of `subfolders` listed under `src`

Example:
```
{
    "src" : {
        "location" : "/Users/USER/Downloads",
        "subfolders" : [
            "text-files", 
            "pdf-files", 
            "images", 
            "videos", 
            "zipped", 
            "word-documents", 
            "excel-documents",
            "new-filtered-folder"
        ]
    },
    ... existing folders ...
    "new-filtered-folder" : {
        ... location ...
        ... extensions ...
    }
}
```

## Arguments
There are two usages of this script, either `clean` or `filter` a directory.

| Argument | Description |
| :--- | :--- | :--- |
| `clean` | Performs a single walk-through of the provided `src` directory from the `*.json` file and filters according to the provided configuration |
| `filter` | Creates a `FileSystemEventHandler` that detects incoming files to the `src` directory and actively filters them as they come in |
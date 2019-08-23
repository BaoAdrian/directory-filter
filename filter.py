import os
import sys
import json
import time
import argparse

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ImportError:
    print('Module \'watchdog\' was not found')
    print('Use: python pip install watchdog')
    sys.exit()
except:
    print('Unknown error has occurred')
    sys.exit()

class FileHandler(FileSystemEventHandler):
    def __init__(self, json_data):
        self.json_data = json_data

    def on_modified(self, event):
        ''' 
        When item is added to the src folder, analyze
        extension and relocate as necessary.
        '''
        walk_directory(self.json_data)

def active_filter(json_data):
    """
    Generate handler to detect aggregated files to the downloads
    folder to filter accordingly
    """
    src = json_data['src']['location']
    event_handler = FileHandler(json_data)
    observer = Observer()
    observer.schedule(event_handler, src)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        print('\nEnding filter automation...')
        observer.stop()
    except:
        print('Unexpected error')
        sys.exit()
    observer.join()

def build_subfolders(json_data):
    """
    Walk through json config to build all requested subfolders
    """
    subfolders = list(json_data.keys())
    subfolders.remove('src')
    for subfolder in subfolders:
        if not os.path.exists(json_data[subfolder]['location']):
            os.mkdir(json_data[subfolder]['location'])

    misc_folder = json_data['src']['location'] + '/misc'
    if not os.path.exists(misc_folder):
        os.mkdir(misc_folder)

def walk_directory(json_data):
    """
    Walk directory of files/folders and filter accordingly
    """
    src = json_data['src']['location']
    subfolders = json_data['src']['subfolders']
    misc_folder = src + '/misc'

    for filename in os.listdir(src):
        src_file = src + '/' + filename
        moved_file = False
        for subfolder in subfolders:
            file_ext = filename[filename.rfind('.') + 1:] if '.' in filename else None
            if file_ext and file_ext.lower() in json_data[subfolder]['extensions']:
                move_file(src_file, json_data[subfolder]['location'], filename)
                moved_file = True
        
        if not moved_file and filename != 'misc' and filename not in subfolders:
            move_file(src_file, misc_folder, filename)

def parse_args():
    """
    Parse command line arguments to find the execution method
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--clean', '-c', action='store_true', 
                        help='Walks downloads folder and cleans extraneous files into their respective folders')
    parser.add_argument('--filter', '-f', action='store_true',
                        help='Activates listener to actively filter incoming files to the downloads folder')
    parser.add_argument('--jsonConfig', default="filter-config.json",
                        help='JSON File containing filter configurations')
    args = parser.parse_args()
    return args

def move_file(src, destination_folder, filename):
    """
    Moves file from src to destination folder
    """
    destination = destination_folder + '/' + filename
    print('Moving {} to {}'.format(src, destination))
    os.rename(src, destination)

def main():
    args = parse_args()

    with open(args.jsonConfig) as json_file:
        json_data = json.load(json_file)

    build_subfolders(json_data)

    if args.clean:
        print('Walking directory')
        walk_directory(json_data)
    elif args.filter:
        print('Activating filter for: {}'.format(json_data['src']['location']))
        active_filter(json_data)
    else:
        print('Nothing to execute')
        sys.exit()

if __name__ == "__main__":
    main()
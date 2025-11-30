import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, destination_dir):
    try:
        # Check if source exists
        if not os.path.isdir(source_dir):
            print(f"Error: Source directory '{source_dir}' does not exist.")
            return

        # Check if destination exists
        if not os.path.isdir(destination_dir):
            print(f"Error: Destination directory '{destination_dir}' does not exist.")
            return

        # Loop through each file in source
        for filename in os.listdir(source_dir):
            source_file = os.path.join(source_dir, filename)
            
            if os.path.isfile(source_file):
                destination_file = os.path.join(destination_dir, filename)

                # If file exists → append timestamp
                if os.path.exists(destination_file):
                    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_{timestamp}{ext}"
                    destination_file = os.path.join(destination_dir, new_filename)

                shutil.copy2(source_file, destination_file)
                print(f"Backed up: {filename}")

        print("Backup completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    backup_files(source, destination)

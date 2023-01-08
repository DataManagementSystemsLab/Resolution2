import os
import shutil
import json
import ocrmypdf
# Load the list of filenames from empty.json
with open('empty.json') as f:
        filenames = json.load(f)

        # Set the source and destination directories
        src_dir = 'files'
        dst_dir = 'files1'

        # Iterate through the list of filenames
        for filename in filenames:
                    # Construct the full path to the file in the source directory
                    src_path = os.path.join(src_dir, filename)
                    # Construct the full path to the destination location
                    dst_path = os.path.join(dst_dir, filename)
                    # Create the destination directory if it doesn't exist
                    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                    # Copy the file from the source to the destination
                    #shutil.copy2(src_path, dst_path)
                    ocrmypdf.ocr(src_path, dst_path, deskew=True)

        print('Finished OCR files!')


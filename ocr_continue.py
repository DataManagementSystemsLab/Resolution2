import os
import shutil
import json
import ocrmypdf
import common as c


def ocr(input, output, ocring):
    if (ocring):
            ocrmypdf.ocr(input, output, deskew=True)
    if (os.path.exists(output)):
            txt=c.convert(output)
            txt=txt.strip()
            if len(txt)==0:
                    print ("File "+input+ " is empty")
                    return False, ""
    else:
        return False,  ""                
    return True, txt                     

# Load the list of filenames from empty.json
with open('empty.json') as f:
        filenames = json.load(f)
        empty2=[]
        # Set the source and destination directories
        src_dir = 'files'
        dst_dir = 'files3'

        # Iterate through the list of filenames
        for filename in filenames:
                    # Construct the full path to the file in the source directory
                    base, extension = os.path.splitext(filename)
                    src_path = os.path.join(src_dir, filename)
                    # Construct the full path to the destination location
                    dst_path = os.path.join(dst_dir, filename)
                    # Create the destination directory if it doesn't exist
                    f=ocr(src_path,dst_dir,False)
                    if f==False:
                        f,txt=ocr(src_path,dst_dir,True)
                        if f:
                            txtfilename="txts/"+base+".txt"
                            with open(txtfilename, 'w') as tmpf:
                                    tmpf.write(txt)

                        else:    
                            empty2.append(filename)


        print('Finished OCR files!')


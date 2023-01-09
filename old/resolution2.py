# download the missing files
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import gdrive as g
import urllib.request

# Set the folder ID
folder_id = '0B0Rlpx3MRZ1SLVFXRFctd0t1cDA'

# Set the file types to exclude
excluded_types = ['application/pdf', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document']

# Authenticate and create a service object
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)
g.files={}

g.bfs(drive,folder_id)


# Get a list of files in the folder
file_list = list(g.files.items())
# Iterate through the list of files and download the ones that don't match the excluded types
for file in file_list:
    v=file[1]
    try:
        if v['mimeType'] not in excluded_types:
            v.GetContentFile("others/"+v['id'])
            print(f'Downloaded {v["id"]}')
    except:
        #try to export itt
        try:
            link1=v["exportLinks"]["text/plain"]
            filename="others/"+v['id']+".txt"
            urllib.request.urlretrieve(link1, filename)
        except:
            print(f' {v["title"]} is not downloadable!!"')        

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from queue import SimpleQueue
import common as c


def getList(drive, folderid):
	#folderid='0B0Rlpx3MRZ1SLVFXRFctd0t1cDA'
	value="'%s' in parents and trashed=false" % (folderid )
	obj={'q':value}
	fileList = drive.ListFile(obj).GetList()
	return fileList

def bfs(drive, root):
	q=SimpleQueue()
	q.put(root)

	while not q.empty():
		id=q.get()
		lst=getList(drive,id)
		for x in lst:
			files[x['id']]=x
			if c.isFolder(x):
				q.put(x['id'])

def get_files():
	pdfs=[]
	docs=[]
	for key,value in files.items():
		if c.isPdf(value):
			pdfs.append(key)	
		if c.isDoc(value):
			docs.append(key)
	return (pdfs,docs)

def download_doc(f,dir):
	id=f['id']
	filename=dir+"/"+id+""
	if c.isPdf(f):
		filename=dir+"/"+id+".pdf"
	if c.isDoc(f):
		filename=dir+"/"+id+".docx"
	f.GetContentFile(filename)

## could not download all files
def download(lst, start=0, len=100):
	for id in lst[start: start+len]:
		path="tmp/"+str((int)(start/100))
		isExist = os.path.exists(path)
		if not isExist:
			os.mkdir(path)
		o=files[id]
		download_doc(o,path)





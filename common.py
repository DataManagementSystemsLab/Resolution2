import textract
import json
import textract
import os
def isPdf(f):
	if 'mimeType' in f:
		if f['mimeType']=='application/pdf':
			return True
	return False

def isDoc(f):
	if 'mimeType' in f:
		if f['mimeType']=='application/vnd.openxmlformats-officedocument.wordprocessingml.document':
			return True
	return False		

def isFolder(f):
	if 'mimeType' in f:
		if f['mimeType']=='application/vnd.google-apps.folder':
			return True
	return False

def get_content_files(fs):
	txts=[]
	for key,value in fs.items():
		if isPdf(value):
			txts.append(key)	
		if isDoc(value):
			txts.append(key)
	return txts		

def convert(filename):
	success=False
	try:
		txt=""
		txt=textract.process(filename)
		txt=txt.decode("utf-8")
		success=True
	except  Exception as e:
		print(e)
		pass
	if not success:
		return None	
	return txt

def get_contents(dir,fs,lst):
	contents={}
	i=0
	for id in lst:
		o=fs[id]
		print(o)
		pdf=False
		doc=False
		if isPdf(o):
			filename=dir+"/"+id+".pdf"
			pdf=True
		if isDoc(o):
			filename=dir+"/"+id+".docx"
			doc=True
		#this is an older version of the function
		txt=convert(filename, pdf, doc)

		contents[id]=txt
		i=i+1
		if i%100==0:
			f=str((int)(i/100))
			contents_file = open("contents_"+f+".json", "w")
			json.dump(contents, contents_file)
			contents_file.close()
			contents={}
	if len(contents)>0:
		f=str((int)(i/100))
		contents_file = open("contents_"+f+".json", "w")
		json.dump(contents, contents_file)
		contents_file.close()

def get_title(fs, id):
	l=[]
	if id not in fs: 
		return []
	o=fs[id]
	parent_title=[]
	if 'parents' in o:
		if len(o['parents']) >= 1:
			pid=o['parents'][0]['id']
			parent_title=get_title(fs,pid)
		l= parent_title
	l.append( o['title'])
	return l 

# find files that has resolution word into it
def get_resolutions( files, dir="/Users/User/Desktop/resolution/files/"):
	resolutions=[]
	failed=[]
	for k,v in files.items():
		pdf=False
		doc=False	
		if isPdf(v):
				filename=dir+"/"+k+".pdf"
				pdf=True
		if isDoc(v):
				filename=dir+"/"+k+".docx"
				doc=True
		if (pdf == True) or (doc == True) :
			try:
				txt=convert(filename)
				if 'resolution' in txt.lower():
					print ("found in " +k)
					print(get_title(files,k))
					resolutions.append(k)
			except:
				print("Exception "+k)	
				failed.append(k)	
		else:
			print ("skipping "+k)	
	return resolutions,failed	

def get_resolutions2( files, dir="/Users/User/Desktop/resolution/files/"):
	resolutions=[]
	failed=[]
	empty=[]
	for filename in os.listdir(dir):
		f = os.path.join(dir, filename)
		# Split the file name into two parts: the base name, and the extension
		base, extension = os.path.splitext(filename)
		# checking if it is a file
		if os.path.isfile(f) and base in files:
			print(f)
			try:
				txt=convert(f)
				txt=txt.strip()
				if len(txt)==0:
					empty.append(filename)
				elif 'resolution' in txt:
					print ("found in " +filename)
					print(get_title(files,base))
					resolutions.append(filename)
			except:
				print("Exception "+base) 
				failed.append(filename)	
		else:
			print ("skipping "+base) 
	return resolutions,failed,empty

def get_others(files):
	others=[]
	for k,v in files.items():
		pdf=False
		doc=False
		folder=False
		if isPdf(v):
			pdf=True
		if isDoc(v):
			doc=True
		if isFolder(v):
			folder=True

		if(pdf==False and doc==False and folder==False):
			others.append(k)
	return others	
	
def get_pdfs(files):
	pdfs=[]
	for k,v in files.items():
		if isPdf(v):
			pdfs.append(k)
		
	return pdfs	

def get_docs(files):
	docs=[]
	for k,v in files.items():
		if isDoc(v):
			docs.append(k)
		
	return docs	

def get_folders(files):
	folders=[]
	for k,v in files.items():
		if isFolder(v):
			folders.append(k)
		
	return folders	


def rename(f,t):
			ext=""
			if t=="application/msword":
				ext=".doc"
			elif t=="image/jpeg":
				ext=".jpg"
			elif t=="text/html":
				ext=".html"
			elif t=="text/plain":
				ext=".txt"
			elif t=="text/csv":  
				ext=".csv"  
			elif t=="application/vnd.openxmlformats-officedocument.presentationml.presentation":
				ext=".pptx"
			elif t=="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
				ext=".xslx"
			elif t=="video/mp4":
				ext=".mp4"
			elif t=="audio/x-m4a":
				ext=".m4a"  
			os.rename(f,f+ext )
def rename_files(dir):
	for filename in os.listdir(dir):
		f = os.path.join(dir, filename)
		# checking if it is a file
		if os.path.isfile(f):
			if '.' not in filename:
				print(filename + "\t\t"+g.files[filename]["mimeType"])
				t=g.files[filename]["mimeType"]
				rename(f,t)

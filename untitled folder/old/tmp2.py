dir="/Users/User/Desktop/resolution/files/"
filename=dir+"1Aby1249z4l9g1-TqacoDAgfOk7SQzuST.pdf"
filename2=dir+"1i6kd6Muj46AlpI_DpUD8D89z12byaOEG.docx"

txt=convert(filename)



# find files that has resolution word into it
get_resolutions(dir="/Users/User/Desktop/resolution/files/", files=files):
	resolutions=[]
	for k,v in files.items():
		if isPdf(v):
				filename=dir+"/"+k+".pdf"
				pdf=True
		if isDoc(v):
				filename=dir+"/"+k+".docx"
				doc=True
		if pdf == True || doc == True :
			txt=convert(filename)
			if 'resolution' in txt:
					print ("found in " +k)
					print(get_title(files,k))
					resolutions.append(k)
		else:
			print ("skipping "+k)	
	return resolutions		
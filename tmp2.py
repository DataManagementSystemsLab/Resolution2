def get_resolutions2( files, dir="/Users/User/Desktop/resolution/files/"):
	resolutions=[]
	failed=[]
	for filename in os.listdir(dir):
	 f = os.path.join(dir, filename)
	 # checking if it is a file
	 if os.path.isfile(f) and g.files[filename]:
        print(f)
		try:
		  txt=convert(filename)
		  if 'resolution' in txt:
				print ("found in " +k)
				print(get_title(files,k))
				resolutions.append(k)
		except:
				print("Exception "+k) 
				failed.append(k)	
		else:
			print ("skipping "+k) 
	return resolutions,failed
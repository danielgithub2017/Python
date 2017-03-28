#! python2.7
#  backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.

import zipfile,os

def backupToZip(folder):
	
	# Backup the entire contents of "folder" into a ZIP file.
	folder = os.path.abspath(folder)
	#debug
	print("Debug the folder path =" + folder)

	# Figure out the filename this code should use based on
	# what files already exist.
	number = 1
	while True:
		zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
		
		#debug
		print('Debug the zip file name = ' + zipFilename)

		if not os.path.exists(zipFilename):
			break
		number = number + 1
	print('Creating %s... ' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename,'w')
	for foldername,subfolders,filenames in os.walk(folder):
		print('Adding files in %s...' % (foldername))
		backupZip.write(foldername)
	for filename in filenames:
		newBase = os.path.basename(folder) + '_'
		if filename.startswith(newBase) and filename.endswith('.zip'):
			continue
		backupZip.write(os.path.join(foldername,filename))
	backupZip.close()
	print('Done')

backupToZip('hello')	

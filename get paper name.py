import PyPDF2
import os
import sys

if not sys.warnoptions:
    import warnings
    warnings.simplefilter("ignore")
path = r'C:\Users\sylar\Desktop\asdf'
allfile = os.listdir(path)
for i in allfile:
	if i[-4:] == '.pdf':
		if '.' in i:
			srt = i[0:-4].replace('.','') + '.pdf'
			os.rename(os.path.join(path,i),os.path.join(path,srt))
allfile = os.listdir(path)		
for i in allfile:
	if i[-4:] == '.pdf':
		try:
			pathi = path + '\\' + i
			#print(pathi)
			pf = open(pathi,'rb')
			ddf = PyPDF2.PdfFileReader(pf)
			info =ddf.getDocumentInfo()
			if type(ddf.getDocumentInfo().title) != type(None):
				title = info.title + '.pdf'
				title = title.replace(':','')
				print(title)
				pf.close()
				os.rename(os.path.join(path,i),os.path.join(path,title))
		finally:
			pass
from selenium import webdriver

from utils.processUrl import processUrl
from utils.resizeImages import resizeImages
from utils.zipData import zipData

"""
	Check your chrome version:  chrome://settings/help
	Download chrome version: https://chromedriver.chromium.org/downloads
"""

PATH = './drive/chromedriver'

def loadTargets():
	resp = []
	try:
		for i in open('targets.txt', 'r').readlines():
			resp.append(i.replace('\n',''))
	except Exception as e:
		print('[Error] Missig targets.txt file')
	return resp


if __name__ == '__main__':
	mock = 'https://www.google.com/search?q=cute+kitten&sxsrf=ALiCzsb_lp3AZQSXulZvAzB14U-0n04WHw:1663684824805&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiDpID4zKP6AhXNpJUCHb3vBlIQ_AUoAXoECAIQAw&biw=960&bih=417&dpr=1'
	targets = loadTargets()

	wd = webdriver.Chrome(executable_path=PATH)
	for target in targets:
		processUrl(wd= wd, delay=0.2, url= target)
		print('='*50 +'\n\t\tResizing Process\n'+'='*50)
		resizeImages('./data_raw')
		print('='*50 +'\n\t\tZiping Process\n'+'='*50)
		zipData('./data_process')
	wd.close()

from os.path import exists
from base64 import b64decode
from io import BytesIO
import random
import string
import requests


def download_image(tag, url_content, path='./data_raw/', image_type='jpg', verbose=True):
	def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for _ in range(size))
	
	try:
		img_file = ''
		# Filter base64 images
		if tag == 'base64':
			b64Data = url_content.split(',')[1] 
			img_file = BytesIO( b64decode(b64Data) )
		else:
			img_file = requests.get(url_content).content
		# Generate File Name
		file_pth = path + id_generator(10) +'.' + image_type
		# Check if the file already exists
		if exists(file_pth):
			file_pth = path + id_generator(10) +'.' +image_type
		# Save File
		arq = open(file_pth,'wb')
		arq.write(img_file)
		arq.close()
		if verbose == True:
			print(f'[{tag}]\t{file_pth} downloaded successfully.')
	except Exception as e:
		print(f'An error was reported\n: {str(e)}')

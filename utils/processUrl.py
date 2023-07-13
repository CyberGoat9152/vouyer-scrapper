
from time import sleep
from selenium.webdriver.common.by import By
from utils.downloadImages import download_image

def processUrl(wd, delay, url):
	def scroll_down(wd):
		wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		sleep(delay)

	wd.get(url)
	image_urls = []
	attempts = 0
	max_images = 1
	while len(image_urls) < max_images:
		# Scroll to load more images
		scroll_down(wd)
		# Only get images
		images = wd.find_elements(By.CLASS_NAME, "rg_i")
		max_images = len(images)
		for image in images:
			isAlreadyDownload = False
			if image.get_attribute('src') in image_urls:
				isAlreadyDownload = True
			# Check if the image is already download or the task is donw, to not download more images
			if (not isAlreadyDownload ) and (len(image_urls) <= max_images):
				# This is for http and base64 images
				if image.get_attribute('src') and 'http' in image.get_attribute('src'):
					if 'base64' in image.get_attribute('src'):
						image_urls.append(image.get_attribute('src'))
						download_image(tag='base64',url_content= image.get_attribute('src'))
					else:
						image_urls.append(image.get_attribute('src'))
						download_image(tag='http', url_content= image.get_attribute('src'))
				# In some cases img have data-src tags with the url
				if image.get_attribute('data-src') and 'http' in image.get_attribute('data-src'):
					image_urls.append(image.get_attribute('data-src'))
					download_image(tag='http', url_content= image.get_attribute('data-src'))
			# If already download 80% images in page or finish the task		
			if (len(image_urls) >= int(max_images*0.8)):
				attempts+=1
				break
		# If already finish the job or don't have more images exit
		if attempts > 5:
			break

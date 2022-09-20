from PIL import Image
from os import listdir
from os import remove

def resizeImages(path, size=(255,255) ):
    try:
        for file in listdir(path):
            target = path+'/'+file

            print(f'[Resizing]\t {target}')
            img = Image.open(target).convert('RGB')
            img.resize(size, Image.Resampling.LANCZOS)
            img.save('./data_process/'+file)
            print(f'[Saving]\t ./data_prcesses/{file}')
            img.close()
            print(f'[Deleting]\t {target}')
            remove(target)
    except Exception as e:
        print(f'Error in rezise process:\n{e}')
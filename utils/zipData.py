from zipfile import ZipFile
from os import listdir
from os.path import exists
from os import remove
def zipData(path):
    try:
        print(f'[Compacting]\t Compacting images')
        if exists('./output/data.zip'):
            remove('./output/data.zip')
        zip = ZipFile('./output/data.zip','w')
        for arq in listdir(path):
            target = path+'/'+arq
            zip.write(target)
            remove(target)
        zip.close()
    except Exception as e:
        print(f'Error ziping data: \n{e}')
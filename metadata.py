
from PIL import Image
from PIL.ExifTags import TAGS
class MetaDataExtractor:
    def __init__(self):
        pass

    def convert_image_to_jpg(self, img_path):
        import os
        img_path_name = os.path.basename(img_path)
        if img_path_name.split('.')[1] == 'jpg':
            return img_path
        img = Image.open(img_path)
        rgb_img = img.convert('RGB')
        name=img_path_name.split('.')[0]
        rgb_img.save(name+'.jpg')
        return name+'.jpg'
            
    def extract(self, img_path):
        exif_data = {}
        name = self.convert_image_to_jpg(img_path)
        image = Image.open(img_path)
        # extracting the exif metadata
        exifdata = image.getexif().items()
        print(exifdata)
        # looping through all the tags present in exifdata
        if exifdata.__len__() == 0:
            print( Image.open(img_path).getexif()[36867])
            return "No data found !"
        for tagid,value in exifdata:
            if tagid in TAGS:
                exif_data[TAGS[tagid]] = value
        return exif_data
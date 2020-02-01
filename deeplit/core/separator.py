import warnings
warnings.filterwarnings('ignore')

from spleeter.separator import Separator
from django.conf import settings
import shutil
import os

def separate(filename, model = 'spleeter:2stems'):
    separator = Separator(model)
    separator.separate_to_file(f'{settings.MEDIA_ROOT}{filename}', settings.MEDIA_TMP, synchronous=True)
    outname, _ = os.path.splitext(filename)
    zipfolder(f'{settings.MEDIA_DOWNLOAD}{outname}', outname)
    return outname

def zipfolder(destination, origin):
    os.chdir(settings.MEDIA_TMP)
    return shutil.make_archive(destination, format='zip', root_dir=origin)
    
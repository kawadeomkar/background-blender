from appscript import app, mactypes
import datetime

print("Updating wallaper ...")
BASE_PATH = '/Users/omkar/scripts/background_blender/pictures'
IMG_DATASET = 'konbini'


NOW = datetime.datetime.now()
app('Finder').desktop_picture.set(mactypes.File(f'{BASE_PATH}/{IMG_DATASET}/generated/{NOW.hour}-{IMG_DATASET}.jpeg'))

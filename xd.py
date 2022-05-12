import os

print('CoolKitten95')
dir =  os.getcwd() + '\photos'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))
os.remove(os.getcwd() + '\currentPhoto.pk')
import os

img=[]

os.chdir("C:\Users")
for root, dirs, files in os.walk("C:\Users"):
      for x in dirs:
            if(x=='InstaBot'):
               path_of_images=(os.path.join(root, x))

           

os.chdir(path_of_images)
for root, dirs, files in os.walk(path_of_images):
      for x in files:
            if(x.endswith('.png') or x.endswith('.jpg') or x.endswith('.jpeg')):
                  img.append(os.path.join(root, x))

print(img)
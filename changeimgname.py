import os
os.getcwd()
collection = "C:/Users/nikol/Documents/Github/trn-or-no/img/" #Folder where all images are
dest = "C:/Users/nikol/Documents/Github/trn-or-no/img2/" #folder where you want to store your images
for i, filename in enumerate(os.listdir(collection)):
    os.rename(collection + filename, dest + str(i) + ".jpg")
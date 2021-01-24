# This program rename all images to "foldername - number"
# structure of the folders like
#
# - main photo folder
#   - 2021 - pictures 1
#   - 2021 - pictures 2
#
# this will rename photo 1 in folder "2021 - pictures 1" to "2021 - pictures 1 - 1" and so on
# currently only .jpg and .png files are supported
# subfolders within the picture folders are not supported


import os 

# main folder path
url=  "C:/Users/tomsc/OneDrive/Pictures/"

# supported extensions
extensions1 = ('.jpg', '.JPG')
extensions2 = ('.png', '.PNG')

def main():
    # loop over all folders
    for count, file in enumerate(os.listdir(url)):
        # set the new filename like "2021 - pictures 1 - 1"
        newFilename = file + " - "
        # rename all files within these folders
        rename(file, newFilename)

def rename(url2, newFilename):
    # specify the url the picture folder
    fileurl = url + url2 + "/"
    counter = 1
    for count, file in enumerate(os.listdir(fileurl)):
        if file.endswith(extensions1):
            counter = rename_helper(counter, file, newFilename, fileurl, extensions1[0])
        if file.endswith(extensions2):
            counter = rename_helper(counter, file, newFilename, fileurl, extensions2[0])    

def rename_helper(counter, file, newFilename, fileurl, extension):
    dst = newFilename + str(counter) + extension
    src = fileurl + file
    dst = fileurl + dst
    os.rename(src, dst)
    counter += 1  
    return counter            

# Driver Code 
if __name__ == '__main__': 
    
    # Calling main() function 
    main() 

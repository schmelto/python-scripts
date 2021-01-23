import os 

url = "C:/Users/tomsc/OneDrive/Pictures/2016 Naxos" + "/" # you have to replace "\" with "/"
newFilename = "2016-Naxos-" # + number
extensions1 = ('.jpg', '.JPG')
extensions2 = ('.png', '.PNG')

# Function to rename multiple files 
def main(): 
    counter = 1
    for count, file in enumerate(os.listdir(url)): 
        if file.endswith(extensions1):
            dst = newFilename + str(counter) + ".jpg"
            src = url + file 
            dst = url + dst
            # rename() function will rename all the files 
            os.rename(src, dst)
            counter = counter + 1  
        elif file.endswith(extensions2):
            dst = newFilename + str(counter) + ".png"
            src = url + file 
            dst = url + dst
            # rename() function will rename all the files 
            os.rename(src, dst)
            counter = counter + 1 

# Driver Code 
if __name__ == '__main__': 
    
    # Calling main() function 
    main() 

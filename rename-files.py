import os 

url = "url" + "/"
extensions = ('.jpg', '.JPG')

# Function to rename multiple files 
def main(): 
    for count, file in enumerate(os.listdir(url)): 
        if file.endswith(extensions):
            dst = "Filename" + str(count) + ".jpg"
            src = url + file 
            dst = url + dst
            print(file)
            
            # rename() function will rename all the files 
            os.rename(src, dst) 
        else:
            count = count - 1

# Driver Code 
if __name__ == '__main__': 
    
    # Calling main() function 
    main() 

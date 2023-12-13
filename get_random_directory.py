import os
from PIL import Image
import random
def get_image_sizes(directory):
    image_sizes = []
    for filename in os.listdir(directory):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(directory, filename)
            with Image.open(image_path) as img:
                width, height = img.size
                image_sizes.append((filename, width, height))
    return image_sizes

def create_directories(image_sizes):
    directories = set((width, height) for _, width, height in image_sizes)
    for width, height in directories:
        directory_name = f'{width}x{height}'
        os.makedirs(directory_name, exist_ok=True)

def copy_images(image_sizes, source_directory):
    for filename, width, height in image_sizes:
        directory_name = f'{width}x{height}'
        source_path = os.path.join(source_directory, filename)
        destination_path = os.path.join(directory_name, filename)
        os.rename(source_path, destination_path)

def count_images(directory):
    image_count = {}
    for dirpath, _, filenames in os.walk(directory):
        image_count[dirpath] = len([filename for filename in filenames if filename.endswith(('.jpg', '.png'))])
    return image_count


# Specify the source directory
source_directory = '/home/jack/Desktop/HDD500/collections/images'

# Get the image sizes
image_sizes = get_image_sizes(source_directory)

# Create directories based on image sizes
create_directories(image_sizes)

# Copy images to the corresponding directories
copy_images(image_sizes, source_directory)

# Count the number of images in each directory
image_count = count_images(source_directory)
f = open("DATA.all","w")
DIRECTORY = []
# Print the image count for each directory
for directory, count in image_count.items():
    #print(f"Directory: {directory}, Image Count: {count}")
    f.write(f"Directory: {directory}, Image Count: {count}\n")
    
    if count >25:
        DIRECTORY.append(directory)
        
inc = random.randint(0,len(DIRECTORY))
print (DIRECTORY[inc])                     

import os
import shutil
import random

# The source directory where the original images are located
src_dir = './Original'

# The target directories where the images will be copied
train_dir = './train'
val_dir = './val'
test_dir = './test'

# Get all subdirectories in the source directory
sub_dirs = [name for name in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, name))]

# Iterate over each subdirectory
for sub_dir in sub_dirs:
    # Get the list of all files in the subdirectory
    files = os.listdir(os.path.join(src_dir, sub_dir))
    # Shuffle the files to ensure random selection
    random.shuffle(files)
    
    # Calculate the number of train, validation and test files
    n_total = len(files)
    n_train = int(n_total * 0.7)
    n_val = int(n_total * 0.2)
    # Remaining files will go into test set
    
    # Copy the files into the respective directories
    for i in range(n_total):
        # Choose the destination directory based on the index
        if i < n_train:
            dest_dir = os.path.join(train_dir, sub_dir)
        elif i < (n_train + n_val):
            dest_dir = os.path.join(val_dir, sub_dir)
        else:
            dest_dir = os.path.join(test_dir, sub_dir)
        
        # Create the destination directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
        # Copy the file
        shutil.copy2(os.path.join(src_dir, sub_dir, files[i]), os.path.join(dest_dir, files[i]))

import os

# The source directory where the original images are located
src_dir = './Original'

# The target file where the directory names will be written
output_file = './labels.txt'

# Get all subdirectories in the source directory
sub_dirs = [name for name in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, name))]

# Write the subdirectory names to the output file
with open(output_file, 'w') as f:
    for sub_dir in sub_dirs:
        f.write(sub_dir + '\n')

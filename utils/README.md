# Utils Folder README

Welcome to the utils folder! This folder contains a growing collection of Python utility scripts designed to assist with data set preparation for machine learning training and validation. As of now, you will find the following scripts:

## 1. `dataparser.py`

This script organizes your data into training, validation, and test sets.

**Functionality:**  
The script identifies all the subdirectories in a given source directory (default is './Original'), and distributes the files found in each subdirectory into training, validation, and test datasets. The default distribution ratio is 70% for training, 20% for validation, and the remaining 10% for testing.

**Usage:**  
This script can be run directly from the command line with Python. Please ensure your dataset is organized with the correct directory structure before running the script.


## 2. `imagesize.py`

This script categorizes and summarizes your image data based on the image resolutions.

**Functionality:**  
The script goes through each file in the current working directory and its subdirectories, categorizes them based on their longest side into '1-250', '251-499', and '500+' resolution categories, and provides a summary of the number of images in each category.

**Usage:**  
Run this script directly from the command line with Python in the directory containing the images.



## 3. `labels.py`

This script helps generate a list of labels based on directory names.

**Functionality:**  
The script identifies all the subdirectories in a given source directory (default is './Original') and writes their names into a text file (default is './labels.txt').

**Usage:**  
This script can be run directly from the command line with Python.


These scripts are designed to be straightforward and easy to use, but remember to keep your data organized according to each script's requirements for best results. As the utility folder evolves with time, more scripts may be added. Please refer to this README for updated information on new and existing scripts.

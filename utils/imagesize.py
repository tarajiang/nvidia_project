import os
from PIL import Image

def get_resolution_category(resolution):
    if resolution <= 250:
        return '1-250'
    elif resolution <= 499:
        return '251-499'
    else:
        return '500+'

def summarize_image_resolutions():
    cwd = os.getcwd()
    summary = {
        '1-250': 0,
        '251-499': 0,
        '500+': 0
    }

    for subdir, dirs, files in os.walk(cwd):
        for file in files:
            try:
                im = Image.open(os.path.join(subdir, file))
                width, height = im.size
                longest_side = max(width, height)
                category = get_resolution_category(longest_side)
                summary[category] += 1
            except Exception as e:
                # Skip the file if it's not an image or can't be opened for some reason
                continue

    print("Summary of Image Resolutions:")
    print("1-250: ", summary['1-250'])
    print("251-499: ", summary['251-499'])
    print("500+: ", summary['500+'])

if __name__ == "__main__":
    summarize_image_resolutions()

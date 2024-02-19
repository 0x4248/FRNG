# FRNG
# Create random binary file from a image containing fire
# Github: https://www.guthub.com/lewisevans2007/FRNG
# By: Lewis Evans

import sys
try:
    import cv2
except ImportError:
    print("Error importing cv2, please install opencv-python via pip install opencv-python")
    sys.exit(1)

try:
    import numpy as np
except ImportError:
    print("Error importing numpy, please install numpy via pip install numpy")
    sys.exit(1)

def threshold(image, output_file, thresh=100):
    img = cv2.imread(image)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    cv2.imwrite(output_file, thresh)

def bit_shift(image_path, output_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    height, width = image.shape
    flattened_image = image.flatten()
    random_indices = np.random.permutation(height * width)
    shuffled_image = flattened_image[random_indices]
    shuffled_image = shuffled_image.reshape((height, width))
    cv2.imwrite(output_path, shuffled_image)

def convert_bits_to_binary(image_path, output_file):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    flattened_image = image.flatten()
    flattened_image = [1 if x > 0 else 0 for x in flattened_image]
    flattened_image = [str(x) for x in flattened_image]
    flattened_image = "".join(flattened_image)
    with open(output_file, "wb") as f:
        f.write(bytes.fromhex('%x' % int(flattened_image, 2)))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 gen.py <image> <output_file>")
        sys.exit(1)
    print("Image: " + sys.argv[1])
    print("Output File: " + sys.argv[2])
    IMAGE = sys.argv[1]
    OUTPUT_FILE = sys.argv[2]
    while True:
        print("Thresholding image")
        threshold(IMAGE, "temp_1.jpeg", 100)
        print("Bit shifting image")
        bit_shift("temp_1.jpeg", "temp_2.jpeg")
        print("Converting bits to binary")
        try:    
            convert_bits_to_binary("temp_2.jpeg", OUTPUT_FILE)
            break
        except:
            print("Error converting bits to binary, redoing process")
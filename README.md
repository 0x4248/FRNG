# Fire Random Number Generator (FRNG)

FRNG is a random number generator that uses the fire effect to generate random numbers.

## Process

To generate a random number, the program will do a set of steps:

1. Read the image and turn to greyscale
2. Threshold the image
3. Bit shift the image in random directions
4. Turn white pixels and black pixels into 1s and 0s
5. Convert the binary number to hexadecimal
6. Write the file

This then generates a long hexadecimal number.

## Usage

`python3 gen.py <image> <output_file>`

## Perquisites

- Python 3
- OpenCV
- Numpy

## Licence

This project is licensed under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details.
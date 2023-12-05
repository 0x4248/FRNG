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


### Installing Perquisites

#### Python 3

```bash
# Debian/Ubuntu
sudo apt install python3

# Arch
sudo pacman -S python3

# Fedora
sudo dnf install python3

# OpenSUSE
sudo zypper install python3

# Gentoo
sudo emerge dev-lang/python
```

#### OpenCV

```bash
# Debian/Ubuntu
sudo apt install python3-opencv

# Arch
sudo pacman -S opencv

# Fedora
sudo dnf install opencv

# OpenSUSE
sudo zypper install opencv
```

#### Numpy

```bash
# Debian/Ubuntu
sudo apt install python3-numpy

# Arch
sudo pacman -S python-numpy

# Fedora
sudo dnf install python3-numpy

# OpenSUSE
sudo zypper install python3-numpy
```

## Licence

This project is licensed under the GNU General Public License v3.0 - see the [LICENCE](LICENCE) file for details.
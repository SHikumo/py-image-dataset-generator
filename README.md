# Based on Project "Image dataset generator for Deep learning projects"

[![Join the chat at https://gitter.im/py-image-dataset-generator/Lobby](https://badges.gitter.im/py-image-dataset-generator/Lobby.svg)](https://gitter.im/py-image-dataset-generator/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

#Modified
- Generate specific type blur/noise with image's label text.
- Label text files are renamed to the same name of generated images.
- Added random kernel size for blur filter
- Added random noise type, pick randomly from noise types such as gaussian, poisson, speckle, salt, pepper, s&p.

### Pre-requirements

This project is tested with Python 3.6.4 and more.

*Linux*

- chromium-browser package (`sudo apt-get install chromium-browser`)

*Windows*

- Chrome should be installed
- [Microsoft Visual C++ Build Tools](https://www.scivision.co/python-windows-visual-c++-14-required/) (scikit image dependency, [see for more info](https://www.scivision.co/python-windows-visual-c++-14-required/))

### Installation

Git clone the project

Get the python dependencies

```
pip install -r requirements.txt
```

### Usage

#### Generate random blur/noise image with label text file

```
python generator.py --image ./data --output ./output --l <limit-number-of-output-image> --type blur 
```

```
python generator.py --image ./data --output ./output --l <limit-number-of-output-image> --type noise
```
    
### Acknowledgments
- This repo use backbone aug and operator of tomahim's repo. Modified for generate specific type with image's label text files.


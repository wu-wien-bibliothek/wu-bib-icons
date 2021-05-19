# WU Library System Icon Set

[![CC BY 4.0][cc-by-shield]][cc-by]

Icons for library systems used by WU Vienna.  
Creator: Georg Mayr-Duffner

Currently covers item types as used in Primo and Leganto.

## Generating the png Files

`tools/svg2png.py` will generate png-files for Primo and Leganto at width 180px from the svg source files.

Which files to generate from which source file is mapped in `resources/material_types.yml`.

## Changing the colours

Four different colours are in use:

- Background: ![#ffffff](https://via.placeholder.com/15/ffffff/000000?text=+) `#ffffff` (white)
- Main colour 1: ![#008198](https://via.placeholder.com/15/008198/000000?text=+) `#008198` (blueish)
- Main colour 2: ![#808080](https://via.placeholder.com/15/808080/000000?text=+) `#808080` (gray)
- Special colour: ![#d42066](https://via.placeholder.com/15/d42066/000000?text=+) `#d42066` (pink)

The colours need to be changed in the svg files before generating the png files.

- In Notepad++: go to `Edit > Find in Files`, and under `Directory`, choose the `svg\300x350` directory. Use the `Replace in Files` button to replace the value entered in the `Find what` field by the value entered in `Replace with`. 
- Using sed (GNU/Linux): `sed -i -e 's/#008198/#9f0000/g' *.svg` or `sed -i -e 's/#008198/#9f0000/g' -e 's/#d42066/#c4d913/g' *.svg` to replace multiple colours at once.
- Using sed (Mac OS): `sed -i '' -e 's/#008198/#9f0000/g' *.svg`

## Todo’s

- Add more options to the script:
  - to generate only a single icon;
  - to exchange colours;
- Clean up the script.
- Add icons for some more types.



This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

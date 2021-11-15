# Album-cover-downloader
Python script to download album covert art from iTunes and Deezer in the highest resolution.

## Requirements
- Python 3.6+

- Requests library (install with `pip install requests`)

## Usage
Need to pass album ID of either iTunes (default), Ototoy or Deezer.

Use the `-i` flag to download from iTunes or the `-d` flag to download from Deezer.


Example:

Download cover from album with ID 1576678718 (iTunes):

`python cover-dl.py 1576678718`

Download the same album cover but from Deezer:

`python cover.dl.py -d 244890522`

Download cover from Ototoy

`python cover-dl.py -o 882348'


The cover will be downloaded to the current directory from which the script is executing.

Credits to: https://github.com/bendodson/itunes-artwork-finder for the code to download from iTunes.

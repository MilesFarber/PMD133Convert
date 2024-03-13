# PMD133Convert

This is a Pillow tool that will grab any PNG or APNG file in the Input folder and convert it into 16 different 16x16 Indexed PNG files with a 16 color PMD133 subpalette each. They can then be easily imported as Item Sprites into any Pokémon Mystery Dungeon: Explorers Of Sky .nds rom with Skytemple, by going to `Dungeon Graphics` > `Items` > `Import`, or used into any project you want.

# Usage

* Make sure you have Winget. You can check this by opening the terminal and trying to install Python by typing `winget install Python.Python.3.11 -h -e -s winget`.
* Plop the PNG files you want to convert in the Input folder. You can put in other uncompressed files, but only PNG files are supported so far. Do not put them in subfolders.
* Run `PMD133Convert.cmd`. If it doesn't work or you're on Linux, install Python 3.11 or above and the Pillow library, and run `PMD133Convert.py`. If you're on MacOS iunno lmfao

Huge thanks to @capypara, @mandl27, @shitpost_sunkern, @silverdeoxys563, and @tabun_ne for helping with extracting the PMD133 Palette, and @everfree, @taicanium, @sunnyeggsdee, @shrikeshaymin and @marius851000 for motivating me to do this.
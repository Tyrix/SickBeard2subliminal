SickBeard2subliminal
===================

Calls subliminal after Sickbeard downloaded a TV Episode and gets a matching subtitle. It uses the original filename for the subtitle search process for better matches. 

After that it moves the file into the processed Season folder of the TV show and renames it accordingly.

I tested this file on Windows only. So please tell me if there are any problems with other OS.

Dependencies
============
- [Python 2.7.x](http://www.python.org)
- [Sick-Beard](https://github.com/midgetspy/Sick-Beard)
- [subliminal](https://github.com/Diaoul/subliminal)

Installation
============

Copy the `SickBeard2subliminal.py` file into your SickBeard root folder and add to the `extra_scripts` line in the *config.ini*: `python SickBeard2subliminal.py` (pythonw on windows if you don't want a cmd line window to open each time this file is called).

Open `SickBeard2subliminal.py` and edit the `CONFIG` block to your likings. Do not forget to change your `CACHE_DIR` path
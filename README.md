# asciimatics_the_muse
New and improved ascii animation 

HOW TO RUN:

0. clone repo

1. Make sure you have VLC Media Player installed. 
Must be 64 bit. If you have the 32 bit instead, uninstall and
reinstall the 64 bit version.

2. Make sure you have python-vlc, pillow, and asciimatics installed.
	pip install python-vlc
	pip install pillow
	pip install asciimatics

3. In the termincal, CD to the directory containing "infinite_depth_portrait_for_muse.py"

4. Type "python infinite_depth_portrait_for_muse.py" and hit enter.
If it doesn't work try "python.exe" instead of "python"

(5. To turn into .exe, open cmd in admin mode, and type
	pip install pyinstaller

Now start a cmd from the directory containing infinite_depth_portrait_for_muse.py"
and type 
	pyinstaller -i icons\two.ico --onefile infinite_depth_portrait_for_muse.py

NOTE: may need to add system environment path to include your roaming python scripts and libraries
after installation of pyinstaller. May also need to pip install the 3 modules in step 2 again.)

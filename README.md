# asciimatics_the_muse
New and improved ascii animation 

HOW TO RUN:
	Double click .exe file.
	No need to fullscreen, it's been taken care of.
	In fact it's better to leave the size as it is.
	Just reposition the window such that you can see the whole of it.

	If the screen is physically too small to see all 64 lines at the terminal, 
	go into settings -> display -> and set scale to 100% instead of the default 150%)

	(NOTE: some antivirus may autoprotect and remove the .exe file.
		Search up how to whitelist a folder containg this repo,
		 for your particular antivirus software.)

HOW TO RUN WITHOUT USING .EXE:

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
	pyinstaller -i icons\[icon name].ico --onefile infinite_depth_portrait_for_muse.py

NOTE: may need to add system environment path to include your roaming python scripts and libraries
after installation of pyinstaller. May also need to pip install the 3 modules in step 2 again.)

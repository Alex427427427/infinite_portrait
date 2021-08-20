# asciimatics_the_muse
New and improved ascii animation 

HOW TO RUN:
	
1. clone repo, cd into repo.
2. Double click .exe file.

No need to fullscreen, it's been taken care of.
In fact it's better to leave the size as it is.
Just reposition the window such that you can see the whole of it.

If your laptop screen is physically too small to see all 64 lines at the terminal, 
	go into settings -> display -> and set scale to 100% instead of the default 150%)

(NOTE: some antivirus may autoprotect and remove the .exe file.
		Search up how to whitelist a folder containg this repo,
		 for your particular antivirus software.)

(NOTE: if on linux, the OS actually performs the computations efficiently enough
	to accurately reflect the set time.sleep. My current time.sleep is
	adjusted for Windows running speed. You may adjust it as you see fit.
	The code can be found in infinite_depth_portrait_for_muse.py.
	As a rule of thumb, linux will be faster than windows by a lot so to
	achieve the same framerate, time.sleep should be set higher on linux than on windows.)
	

HOW TO RUN WITHOUT USING .EXE:

1. Make sure you have python installed from their website

2. Make sure you have pygame, pillow, and asciimatics installed by entering the following as separate commands into the command prompt:

		pip install pygame

		pip install pillow

		pip install asciimatics

3. In the termincal, CD to the directory containing "infinite_depth_portrait_for_muse.py"

4. Type "python infinite_depth_portrait_for_muse.py" and hit enter.
If it doesn't work try "python.exe" instead of "python"
		
		python infinite_depth_portrait_for_muse.py

BONUS: To turn the project into .exe yourself, open cmd in admin mode, and type
	
	pip install pyinstaller

Now start a cmd from the directory containing infinite_depth_portrait_for_muse.py"
and type 
	
	pyinstaller -i icons\[icon name].ico --onefile infinite_depth_portrait_for_muse.py

NOTE: may need to add system environment path to include your roaming python scripts and libraries
after installation of pyinstaller. May also need to pip install the 3 modules in step 2 again.)




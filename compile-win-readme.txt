compile-win.bat assumes renum.exe and grfcodec.exe in it's parent directory.
compile-win.bat will fail miserably if either or both programs are missing.



compile-win.bat detailed:
------------------------
First, it changes directory to /sprites and deletes the existing firs.nfo file.
After that it changes to /sprites/nfo and compiles a new firs.nfo file from the files listed in the command.
Please note that the order of files is important as they end up in the same order in the grf file.
Now it moves the new firs.nfo back to the /sprites dir.
Then it changes directory to the parent of the batch file's dir and runs renum and grfcodec.
The grf file will be created and is located in the parent directory of compile-win.bat
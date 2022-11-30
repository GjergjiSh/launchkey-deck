If you want a code to run continuously in the background, you will need to change the file extension

from .py in .pyw

Before running the script you need to do the following:

From the CMD (command prompt) console, run the command: pip install pythonw

To start the program run the following command in CMD (in the folder where the file is located): pythonw YOUR-FILE.pyw

Now the process will run continuously in the background. To stop the process, you must run the command:

TASKKILL /F /IM pythonw.exe

CAREFUL!!! All commands are run from the command line in the folder where the file is located.

If you want to simply run the file with python YOUR-FILE.pyw, you can do that too, but you should always keep the console open. You can stop the execution with ctrl + C from Command Prompt (CMD)


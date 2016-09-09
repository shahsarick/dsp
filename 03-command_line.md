# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > cd and the folder name sets that to your current folder
cls to clear the screen
tree shows the directory structure
ren to change a file or set of files
mkdir to set a folder or subfolder
ipconfig displays all the ip configuration details (dhcp, tcp, etc)
echo is used to echo statements/ commands made
at	schedules commands and programs to run on a computer at a specified time and date. 
dir	displays a list of a folder's files and subfolders
goto sents the interpreter to a labeled area in a batch program

---

###Q2.  List Files in Unix   

What do the following commands do:  
ls -a is a	list of all files and folders including ones with '.' at the beginning
ls -l	list with long format + permissions
ls -lh	list long format with readable file size
ls -ls	list with long format with file size
ls -lah was undistinguishable from ls -lh for me... not sure what I'm doing wrong there is it just the inclusion of human readable format?
ls -t	sort by time & date
ls -Glp in a long listing, don't print group names + us long listing format + append / indicator to directories


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > 
-m
-F
-p
-R
-x

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > One example is to find all .bak files in a directory or subdirectory and delete them

$ find . -name "*.bak" -type f -print | xargs /bin/rm -f

 


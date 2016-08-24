# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 
* pushd 
* popd 
 * both pushd and popd are useful to move between directories and keep them in "stack" -- use pushd commands to move between directories currently in use; use popd to remove directory from this "stack"
* mkdir -p path/to/follow: very useful to create "compound" path rather than making folders one-by-one
* cp -r: command used to copy directories with files in them
* less filename.extension: use to see the contents of filename.extension on the terminal. use up/down arrows to move page up or down, or use spacebar and w for the same functions. 
* rm -rf non_empty_folder: recursive remove command used to delete the folder "non_empty_folder" and ALL of its contents. *** make sure you want to delete the folder before doing this! *** 
* cat filename1 filename2 > new_file: concatenate contents of filename1 and filename2 and create a new file called new_file. 
* pwd: Print Working Directory
* chmod: [wiki link](https://en.wikipedia.org/wiki/Chmod) use to change access permissions to a file.


---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> > 
* ls: lists files and folders in current directory
* ls -a: lists all files and folders, including hidden ones, in current directory
* ls -l: lists properties of files and folders, including permissions, group, size, users ... 
* ls -lh: lists properties of files and folders like ls -l, but shows sizes in a more interpretable format: K, M, G (kilo, mega, gigabytes)
* ls -lah: lists all files and folders and their properties, showing their size in a readable format
* ls -t: lists files and folders in order of (time) modification; first files listed are those that were modified last. 
* ls -Glp: lists properties of files and folders; folders (a.k.a. directories) are shown with backslash at the end; folders are shown in different color than files. 

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > * ls -G: shows folders in a different color than files
* ls -rt: show files in reverse order of modification (time)
* ls -1: displays each item on a line
* ls -o: like ls -l but does not list group name
* ls -u: show files in reverse order of access time (last opened?)

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > * $ find . -name "*.txt" -type f -print | xargs rm 
     * this will remove (rm) all files with extension .txt in the current directory

 


# tree_read
A project to read all files in a tree

This is a simple script that I built for a customer POC.   The idea is simple, read all the files in a given tree.  Data is read to /dev/null.  The script is single-threaded and super simple.  It currently only support UNIX/Linux clients.  Enhancements and requests are welcome.

Usage
<pre>
tree_read.py directory
</pre>
The directory is the root of the tree that is to be read.  The script also gives the start and end times to tell how quickly it ran.

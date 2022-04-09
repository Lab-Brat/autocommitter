# Autocomitter

## Table of contents
- [Purpose](#purpose)
- [Introduction](#introduction)
- [Files](#files)
- [How To Run](#how-to-run)

## Purpose 
Some people don't like loud neighbors, some don't like olives, and some don't like grey boxes on the commit calendar in Github.  
This is why this repository was created - to use the power of Linux and Python to paint the grey boxes into green.

## Introduction
A small program written in Python, that utilizes systemd timers to schedule commits to a github repository.\
\
User must supply an ```input.txt``` file, which will contain a desired pattern, where * represents a day commit should be made.
After the program is run, ```decoder.py``` translates the input files into dates using ```datetime``` library, and those dates
are plugged into a systemd timer unit (```committer.timer```). 
The 1st commit always starts on a Sunday, and technically can be planned to infinity.  

#### Note
Everytime ```main.py``` is run, it will rewrite previous service and timer.  
Only standard library was used, so no installation of additional libraries is needed.  
sudo priviliges are not required, since the user-level service will be created. 

## Files
* ```cmt.py``` - systemd timer calls this script, and it runs the committer.
* ```committer.py``` contains main functionality, like create a timer and start commits. 
* ```decoder.py``` decodes input.txt into dates with the use of datetime library.
* ```input.txt``` - input patters.
* ```main.py``` creates service and timer, and turn service on
* ```patt.py``` contains code that generates and modifies service and timer
* ```tmp``` a directory with a tmp_file, commutter adds changes to this file (will be replaced with s/ more creative)

## How To Run
* clone the repository to your Linux distro.
* make changes to ```input.txt``` and delete ```.git``` directory.
* upload it on a desired github account.
* run ```pyhton3 main.py```

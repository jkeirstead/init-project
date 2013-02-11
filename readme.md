init-project
===============

About 
----------------

This is a simple Python script that creates a new project.  It is based on a [blog post](http://www.academicproductivity.com/2008/numbered-folders-the-easiest-way-to-keep-track-of-works-in-progress/) I once wrote on a simple way way to track works-in-progress.  The script adds a few more goodies on top of the basic numbered folders, such as template readme and status files to ensure consistent documentation.

Configuration
-------------

To get started:

* Edit init-project.py and change the `projects_home`, `script_dir`, and `creator_name` variables to the appropriate values. `projects_home` is where the projects will be created, `script_dir` is the installation location of this script, and `creator_name` is your name.

Using the script
----------------

To use the script, simply change into the script directory (or add it to your system path) and type:

	python init-project.py project_id "project_name"
	
where `project_id` is a unique ID for your project (say a number) and `project_name` is a string giving the project's name.

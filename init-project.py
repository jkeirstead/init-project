#!/usr/bin/python
import os
import Cheetah.Template as cheetah
import time
import sys

# Initializes a new project
# James Keirstead
# 08 February 2013

""" The idea of this script is that every time I start a new project
there should be a consistent approach to creating and maintaining the
project.  I was originally going to do all of this with databases but
now I'll just do it with org-mode files."""

projects_home = 'd:/jkeirste/projects/'
script_dir = 'd:/jkeirste/code/scripts/init-project/'
creator_name = 'James Keirstead'

def init_project(project_id, name):
    """ Initializes a project with a specified project ID and name 

    Attributes:
    	project_id - an integer giving the project ID
        name - a string giving the project name
    """

    # Create the directory
    dir_name = str(project_id) + ' - ' + name
    project_path = os.path.join(os.path.abspath(projects_home), dir_name)
    os.mkdir(project_path)

    # Define the template files
    status_template = os.path.join(os.path.abspath(script_dir), 
                                   'templates','status.org')
    readme_template = os.path.join(os.path.abspath(script_dir), 
                                   'templates','readme.org')
    
    # Specify the details
    namespace = {}
    namespace['project_id'] = project_id
    namespace['project_name'] = name
    namespace['init_date_time'] = time.strftime('%d %B %Y %H:%M')
    namespace['creator'] = creator_name
    status_t = cheetah.Template(file=status_template, searchList=namespace)
    readme_t = cheetah.Template(file=readme_template, searchList=namespace)
    
    # Write the project status template
    status_path = os.path.join(project_path, 'status.org')
    status_file = open(status_path, 'w')
    status_file.write(str(status_t))
    status_file.close()

    # Write the readme template
    readme_path = os.path.join(project_path, 'readme.org')
    readme_file = open(readme_path, 'w')
    readme_file.write(str(readme_t))
    readme_file.close()

    ## TODO
    print 'New project created: ' + str(project_path)    
    
if __name__=='__main__':
    # Read in the arguments
    if len(sys.argv)==3:
        project_id = sys.argv[1]
        project_name = sys.argv[2]
        init_project(project_id, project_name)
    else:
        print "Two arguments must be provided"


    

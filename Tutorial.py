# Tutorial on Project homework submission for "CS50 ’s Introduction to Artificial Intelligence with Python" with Git and Github


#############INTIAL SETUP###############################
# make a new folder that will contain all the project files, called "Projects". Every time you download a project to work on from the course website:
# https://cs50.harvard.edu/ai/2020/
# unzip the file to this "Projects" folder

# open a terminal. I am using VS Code, so I will use the terminal in VS Code.

# go into your projects folder in the terminal. I am using windows, for me this is how I go into my Projects folder:
cd /d G:\1 my work\Towards data scientist\CS50_HarvardX\Projects

#create a readme file, describe the projects.
echo "CS50_HarvardX projects homework" >> README.md

#Initialized empty Git repository in the Projects file
git init 

#add the readme file to the stage:
git add README.md

#tell git I am sure about this version, and add a master branch to the empty repository
git commit -m "first commit" 

#add your remote repository, and call it origin. Replace "loveinthebone" with your own github account name:
git remote add origin https://github.com/me50/loveinthebone.git

# Push your local repository to the remote github repository:
git push -u origin master
#############INTIAL SETUP###############################

#######################Submit projects for the first time
# create a new local branch for the project homework you want to submit. For the Degrees homework (https://cs50.harvard.edu/ai/2020/projects/0/degrees/), it should be like this:
git checkout -b ai50/projects/2020/x/degrees

#now you are in the branch called "ai50/projects/2020/x/degrees", if you finished the Degrees project, you can submit it:
git add degrees
##I am not sure if we need to submit the whole degrees folder, or submit degrees/degrees.py is sufficient. In the later case, do this:
#git add degrees/degrees.py

#commit the "add" to make it final:
git commit -m "submit the degrees project"

# The final step, to really submit the file (create a remote branch on Github that is also called "ai50/projects/2020/x/degrees", and copy and paste the local branch to it):
git push -u origin ai50/projects/2020/x/degrees

########################Submit projects after the first time
#let's say you finished the knights project: https://cs50.harvard.edu/ai/2020/projects/1/knights/
#and you have your code saved in Projects/knights folder

# go into your projects folder in a terminal:
cd /d G:\1 my work\Towards data scientist\CS50_HarvardX\Projects

# create a new local branch for the project homework you want to submit. For the Knights homework (https://cs50.harvard.edu/ai/2020/projects/1/knights/), it should be like this:
git checkout -b ai50/projects/2020/x/knights

#now you are in a local branch called "ai50/projects/2020/x/knights", you can submit add your code to it:
git add knights
##I am not sure if we need to submit the whole degrees folder, or submit knights/puzzle.py is sufficient. In the later case, do this:
#git add knights/puzzle.py

#commit the "add" to make it final:
git commit -m "submit the knights project"

# The final step, to really submit the file (Create a remote branch on Github that is also called "ai50/projects/2020/x/knights", and copy and paste the local branch to it):
git push -u origin ai50/projects/2020/x/knights





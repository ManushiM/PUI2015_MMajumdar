#PUI2015_MMajumdar

##STEPS FOLLOWED TO SET UP ENVIRONMENT (Windows 8.1 machine)
1. Create environmental variable using
export PUI2015="path"
followed by - echo $PUI2015 - to verify the path is stored

2. Create a .bashrc profile as follows
touch .bashrc

3. Store the environment variable in .bashrc file so that it is available for future use and reference.
vim .bashrc
Type - PUI2015="path"
Also type - alias pui2015="cd $PUI2015"
Save changes and escape vim.
Type - source.bashrc - to run the .bashrc file.

4. Verify the setup as follows:

!(Alt text)(https://github.com/ManushiM/PUI2015_MMajumdar/blob/master/pui%202015%20confirmation.PNG)


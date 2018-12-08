# Library-Catalog-Application
* This web app is a project for the Udacity FSND Course.
* This application  provides a list of items (books) within a variety of book categories as well as provide a user authentication system.  Users will have the ability to post, edit and delete their own items.

### Prerequisites
You will need to install these following application in order to make this code work.
* VirtualBox
* Vagrant
* Python Version 2.7.12
* Unix-style terminal(Windows user please use Git Bash Terminal)
* VM configuration( download from here https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip)

### Installing
* Install Vagrant & VirtualBox
* Clone the Udacity Vagrantfile
* Go to Vagrant directory and either clone this repo or download and place zip here
* Launch the Vagrant VM (vagrant up)
* Log into Vagrant VM (vagrant ssh)
* Navigate to cd/vagrant as instructed in terminal
* The app imports requests which is not on this vm. Run sudo pip install requests
* Setup application database: python database_setup.py
* Insert data in database: python lotsofitems.py
* Run application using python project.py
* Access the application locally using http://localhost:8000

## Acknowledgments
* [VM configuration](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) was provided by [udacity](https://www.udacity.com).
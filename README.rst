Nansat Lectures
===============

Materials for the course on scientific programming with Python


Installation
------------
For simple installation the Nansat Lectures can be provided on a virtual machine. In order to configure and start the virtual machine you will first need to install:

 * GIT <https://git-scm.com/>
 * Vagrant <https://www.vagrantup.com/>
 * Ansible <http://www.ansible.com/home>
 * Virtual box <https://www.virtualbox.org/>
These apckages are freely available for Linux, Mac and Windows and are easy to install.

After installation of these requirements, do the steps below.

Download the virtual box configuration::

    git clone https://github.com/nansencenter/nersc-vagrant.git

Start virtual machine and install everything::

    cd nersc-vagrant
    vagrant up course


Wait c.a. 10 minutes untill all Nansat dependencies are installed.

Now restart virtual machine and wait 1-2 minutes until ipython notebooks are available::

    vagrant halt course
    vagrant up course


Open <http://192.168.33.11:8888> with your favorite browser. Jupyter Notebook manager should appear where you will find available notebooks. To start with, open the 'hello-world' notebook, click in the cell right after the 'print "Hello, World!"' statement and press Shift-Enter.

Enjoy the course!

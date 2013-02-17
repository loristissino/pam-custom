pam-custom
==========

This is a collection of instructions and simple example scripts to help
customize the login to a Linux box with pam, using libpam-python.

The instructions and the scripts have been tested with Ubuntu 12.04 LTS.
Run them at your risk.

Installation
------------

Since working with PAM can lead to problems in authentication, keep a
shell with root access open while experimenting.

Install the package libpam-python:

    sudo apt-get install libpam-python
    
Copy the provided `pam_custom.py` and `pam_custom.sh` in `/lib/security`:

    sudo cp pam_custom.py pam_custom.sh /lib/security 

Make a backup of the file `/etc/pam.d/common-auth`:

    sudo cp /etc/pam.d/common-auth /etc/pam.d/common-auth.original
    
Edit the file `/etc/pam.d/common-auth` introducing a line in which you
declare your custom authentication method. It should be something like
this:

    auth  [success=2 default=ignore] pam_python.so pam_custom.py /lib/security/pam_custom.sh

and should be put just before (or after, according to your needs) the
other authentication methods.

Some explanations:

1. "success=2" means that the 2 following lines should be skipped in case of success (edit as needed)

1. "pam_python.so" is the name of the shared object that will be called by pam

1. "pam_custom.py" is the script in python that we provide

1. "/lib/security/pam_custom.sh" is the bash script that is called by the python script (if needed)

Edit the file `/lib/security/pam_custom.sh` according to your needs. It is a bash script that
receives username and password as command line arguments, and must exit with 0 if the authentication
is to be granted, or a non-zero value otherwise.


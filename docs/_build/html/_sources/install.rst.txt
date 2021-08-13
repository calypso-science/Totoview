.. image:: _static/calypso.png
   :width: 150 px
   :align: right

=============
Installation:
=============

Where to get it
--------------------
The source code is currently hosted on GitHub at: https://github.com/calypso-science/Totoview

Module requirements:
--------------------
Toto module needs to be installed:
The source code is currently hosted on GitHub at: https://github.com/calypso-science/Toto

For windows user, if using the compiled version (.exe file)A environmental variable must be setup
To set it up temporarily:

.. code:: bash

  set TotoPath=C:\user\software\toto

or add TotoPath as environmental variable

Install from sources
--------------------
Toto toolbox needs to be installed :
 see https://github.com/calypso-science/Toto for instructions

Install requirements. Navigate to the base root of totoview and execute:

.. code:: bash

   pip install -r requirements.txt


Then install totoview:

.. code:: bash

   python setup.py install



Windows installation:
---------------------
Once installed, WINDOWS user must set up an Environmental variable with the folder name from where TOTO has been installed.
The variable MUST be called TotoPath. 

.. image:: _static/windows_path.png
 :height: 150 px
 :align: center


Using the compiled version
--------------------------
There are two versions of TOTOVIEW that are already compiled for Windows user.
They can be found on the GitHub page:

• totoview_withtoto.exe.

 This version will install TOTO and TOTOVIEW. No need to install TOTO, it is included in it. However, you will need to wait for a new release to update your code

• totoview_nototo.exe.

 This version will install TOTOVIEW and TOTO’s requirement. You still need to install TOTO but you can skip the requirement installation. This is easier to update TOTO's code, just need to pull the updated code from GitHub and re-install TOTO.




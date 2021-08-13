Totoview
===========
Python Gui for visualizing and processing timeseries using Toto


.. image:: https://readthedocs.org/projects/totoview/badge/?version=latest
    :target: https://totoview.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

Documentation:
--------------
The documentation is hosted on ReadTheDocs at https://totoview.readthedocs.io/.

Install:
--------
Where to get it
~~~~~~~~~~~~~~~
The source code is currently hosted on GitHub at: https://github.com/calypso-science/Totoview

Module requirements:
------------------
Toto module needs to be installed:
The source code is currently hosted on GitHub at: https://github.com/calypso-science/Toto

For windows user, if using the compiled version (.exe file)A environmental variable must be setup
To set it up temporarily:

.. code:: bash

	set TotoPath=C:\user\software\toto

or add TotoPath as environmental variable

Install from sources
~~~~~~~~~~~~~~~~~~~~
Toto toolbox needs to be installed :
 see https://github.com/calypso-science/Toto for instructions

Install requirements. Navigate to the base root of totoview and execute:

.. code:: bash

   pip install -r requirements.txt


Then install totoview:

.. code:: bash

   python setup.py install



Windows installation:
~~~~~~~~~~~~~~~~~~~~
You can run as:

.. code:: bash
   
   python totoView.py

or unzip and run the executable file from this folder:
	https://github.com/calypso-science/Totoview/compiled64.zip
or run the installer:
	https://github.com/calypso-science/Totoview/totoview_setup.exe

How to load file:
---------
From the GUI:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   totoView

Wild cards:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   totoView my_folder/*csv

Drag and Drop:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   totoView

Then drag and drop file in the totoView window



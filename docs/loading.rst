.. image:: _static/calypso.png
   :width: 150 px
   :align: right

===========
How to load
===========

A file
------

From the GUI:
~~~~~~~~~~~~~

.. code:: bash

   totoView

Wild cards:
~~~~~~~~~~~~~

.. code:: bash

   totoView my_folder/*csv

if you know the name of the reader you want to use:

.. code:: bash

   totoView my_folder/*csv -r txt

Drag and Drop:
~~~~~~~~~~~~~~

.. code:: bash

   totoView

Then drag and drop file in the totoView window

A dataframe
-----------

.. code:: python

    import xarray
    import totoview
    url='https://tds.hycom.org/thredds/dodsC/GLBy0.08/latest?time[0:1:100],surf_el[0:1:100][2000][3000]
    xar=xarray.open_dataset(url)
    df=xar.to_dataframe()
    df.reset_index(inplace=True)
    df.set_index('time',inplace=True,drop=False)
    del df['lon']
    del df ['lat']
    totoview.show(dataframe=[df])

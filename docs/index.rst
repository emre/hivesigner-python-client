

hivesigner-python-client
======================================================

hivesigner-python-client is a simple **yet powerful** library to interact with the hivesigner. hivesigner
is a central-single sign on solution for HIVE based applications.

hivesigner implements Oauth2 for the authorization logic.

What can you do with this client?
----------

- Implementing Authorization/Authentication flow through OAuth
- Broadcasting supported operations to the HIVE blockchain with the user of your app.

Installation
-------------

hivesigner-python-client requires python3.6 and above. Even though it's easy to make it compatible
with lower versions, it's doesn't have support by design to keep the library simple.

You can install the library by typing to your console:

.. code-block:: bash

    $ (sudo) pip install hivesigner

After that, you can continue with  :doc:`/gettingstarted`.

Documentation Pages
-----------

.. toctree::
   :maxdepth: 5

   gettingstarted
   usingtheaccesstoken
   broadcast
   hot-signing
   example-flask-app


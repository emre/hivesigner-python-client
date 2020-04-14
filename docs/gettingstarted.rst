
Getting Started
=================================

Hivesigner supports two different oauth flows for authorization.

Implicit grant flow
~~~~~~~~~~~~~~~~~~~~~~~~

- You create an authorization link with your app's client id and permission scopes.
- User visits the page (Hivesigner) and authorizes the application with the given permission scopes.
- Hivesigner returns user to the your app with a access token in the query string.

From that point, you can use this access token to broadcast operations on user's behalf.

Code authorization flow
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

access tokens has a short TTL on Oauth standards. Every time a user has their token expired, you have two choices:

- Re-log the user and get a fresh token
- Add "offline" scope to the required scopes and get a refresh token to refresh the access tokens.

The second approach is required on some cases for the dApps and you will need to use Code authorization flow this.
When you add the "offline" scope to the required scopes, you will get a code instead of access token.

With this code, you can get new access tokens till forever. *(As long as the user don't revoke access of your app.)*


Creating your app on Hivesigner
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. figure::  https://camo.githubusercontent.com/73676c4237e95b24365ef8dfea78119e19237108/68747470733a2f2f7331342e706f7374696d672e63632f6b65716437727268742f53637265656e5f53686f745f323031382d30342d31395f61745f372e35342e35385f504d2e706e67
   :width: 600

You need to `register your app <https://hivesigner.com/dashboard>`_ into Hivesigner before working with them. This will provide client_id and client_secret information which you will need to interact with the API.


Redirecting user
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from hivesigner.client import Client

    c = Client(
        client_id="app_name",
        client_secret="client_secret",
    )


At this point, we need to redirect the user to Hivesigner for they to log in. That requires creating a URL.

.. code-block:: python

    auth_url = c.get_login_url(
        "http://callback.to.your.app",
        "login,vote",
    )

- The first parameter is the callback URL when the user authorizes your app on Hivesigner.
- Second parameter defines the scopes you need.

.. important ::
    If you need to use the Code authorization flow, you need to pass **get_refresh_token=True** to this function. Also, "offline" scope is mandatory.

Once the user authorizes your app, Hivesigner will redirect the user to your app with an access token or code depending the flow you choose.
If you get a **code** in the query string, you can use this code to create access tokens for the specified user.

.. code-block :: python

    c.get_access_token(
        code,
    )

Example output

.. code-block :: javascript

     {
         'access_token': 'access_token_string',
         'expires_in': 604800,
         'username': 'emrebeyler',
         'refresh_token': 'refresh_token_string'
     }

If you use the Implicit grant flow, then you may skip this step.

Continue with :doc:`/usingtheaccesstoken` to learn what can you do with the access tokens.


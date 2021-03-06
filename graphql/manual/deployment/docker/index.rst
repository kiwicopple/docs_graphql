Run Hasura GraphQL Engine using Docker
======================================

This guide assumes that you already have Postgres running and helps you set up the Hasura GraphQL engine using Docker
and connect it to your Postgres database.

**Prerequisites**:

- `Docker <https://docs.docker.com/install/>`_


Step 1: Install the Hasura CLI
------------------------------

.. rst-class:: api_tabs
.. tabs::

   .. tab:: Mac

      In your terminal enter the following command:

      .. code-block:: bash

         curl -L https://cli.hasura.io/install.sh | bash

      This will install the ``hasura`` CLI in ``/usr/local/bin``. You might have to provide
      your ``sudo`` password depending on the permissions of your ``/usr/local/bin`` location.

   .. tab:: Linux

      Open your linux shell and run the following command:

      .. code-block:: bash

         curl -L https://cli.hasura.io/install.sh | bash

      This will install the ``hasura`` CLI tool in ``/usr/local/bin``. You might have to provide
      your ``sudo`` password depending on the permissions of your ``/usr/local/bin`` location.

   .. tab:: Windows

      .. note::

         You should have ``git bash`` installed to use ``hasura`` CLI. Download git bash using the following `(link)
         <https://git-scm.com/download/win>`_. Also, make sure you install it in ``MinTTY`` mode, instead of Windows'
         default console.

      Download the ``hasura`` installer:

      * `hasura (64-bit Windows installer) <https://cli.hasura.io/install/windows-amd64>`_
      * `hasura (32-bit Windows installer) <https://cli.hasura.io/install/windows-386>`_

      **Note:** Please run the installer as Administrator to avoid PATH update errors. If you're still
      getting a `command not found` error after installing Hasura, please restart Gitbash.


Step 2: Initialise a Hasura project
-----------------------------------

Create a Hasura project directory.

.. code-block:: bash

  hasura init --directory my-project

Step 3: Run the hasura docker container
---------------------------------------

You'll see a sample docker run command at ``my-project/install-scripts/docker-run.sh``.

Edit the ``--database-url`` flag command, so that you can connect to your postgres instance.

.. code-block:: bash
   :emphasize-lines: 5

    #! /bin/bash
    docker run -p 8080:8080 \
     hasura/graphql-engine:latest \
     graphql-engine \
     --database-url postgres://username:password@hostname:port/dbname \
     serve

Examples of `database-url`:

- If the username and database is called admin: ``postgres://admin:password@localhost:5432/admin``
- If there is no password: ``postgres://admin:@localhost:5432/admin``

Check if everything is running well:

.. code-block:: bash

   $ docker ps

   CONTAINER ID IMAGE                 ... CREATED STATUS PORTS          ...
   097f58433a2b hasura/graphql-engine ... 1m ago  Up 1m  8080->8080/tcp ...

Step 4: Open the hasura console
-------------------------------

In the ``my-project/config.yaml`` file set the endpoint:

.. code-block:: bash

  endpoint: http://localhost:8080

Now, open the hasura console:

.. code-block:: bash

  # Run this command in the my-project/ directory
  $ hasura console


Advanced:
---------

.. toctree::
   :titlesonly:

   Securing your GraphQL endpoint <securing-graphql-endpoint>

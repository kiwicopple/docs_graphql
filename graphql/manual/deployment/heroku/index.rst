Run Hasura GraphQL Engine on Heroku
===================================

This guide will help you get Hasura GraphQL engine and Postgres running on **Heroku's free tier**.
It is the easiest and fastest way of trying Hasura out.

Deploy to Heroku by clicking:

.. image:: https://camo.githubusercontent.com/83b0e95b38892b49184e07ad572c94c8038323fb/68747470733a2f2f7777772e6865726f6b7563646e2e636f6d2f6465706c6f792f627574746f6e2e737667
  :width: 200px
  :alt: heroku_deploy_button
  :class: no-shadow
  :target: https://heroku.com/deploy?template=https://github.com/hasura/graphql-engine-heroku

.. note::
   If you don't have an account on Heroku, you need to sign up on Heroku. You won't need a credit card, and once you sign up you'll be redirected to your Heroku app creation page automatically.

.. image:: ../../../../img/graphql/manual/getting-started/heroku-app.png

Note that **Heroku's free Postgres add-on** is also automatically provisioned!

That's it!  Head to https://YOUR_HEROKU_APP.herokuapp.com and open your app.
You should see the hasura console.

.. image:: ../../../../img/graphql/manual/getting-started/heroku-app-deployed.png

Next: Make your first GraphQL query!
------------------------------------

Next, make your :doc:`first graphql query<../first-graphql-query>`.

Advanced topics:
----------------

.. toctree::
   :titlesonly:

   securing-graphql-endpoint
   deploy-with-git
   using-existing-database
   import-database
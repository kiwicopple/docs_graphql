How Hasura's GraphQL schema generation works
============================================

Given your postgres database, Hasura can automatically generate a GraphQL schema and process GraphQL queries and mutations.

How does Hasura know which tables and views in which schema, and how to ``connect`` them so that they form a ``graph`` over which queries and mutations should be allowed?

Here's what Hasura does under the hood:

Tables
------

Let's say you have a table, a ``profile (id, name)`` table, in postgres that you want to expose over GraphQL.

All you need to do is tell Hasura to ``track`` this table, and Hasura automatically generates a GraphQL schema with:

#. A GraphQL type definition for the table
#. Queries with where, order_by, limit and offset arguments
#. Insert mutations that support bulk and upsert
#. Update mutations that support conditional bulk updates
#. Delete mutations that support conditional bulk deletes

Views
-----

If you have a view in postgres, hasura does the same thing it would for a table, but without creating mutations.

Relationships or Connections
----------------------------

Between one table/view and another table/view you can tell Hasura to create a relationship or a connection between these 2 nodes in a graph, using a particular column as a link. Often, you have foreign key constraints that indicate a ``relationship`` and you can tell Hasura to use that foreign-key constraint to create a relationship too.

You can specify an ``object relationship`` or an ``array relationship`` between table and views. For example:

#. You might have a ``restaurant.average_rating`` where average_rating is a view connected to the restaurant table via a restaurant_id.
#. You might have a ``user.addresses`` where each user has multiple addresses connected via a user_id.

When you create a relationship, Hasura does the following:

#. Augments the types of the tables/views involved by adding a reference to the nested type
#. Augments the possible where and order_by clauses that can be used to enable nested filtering and sorting

Resolvers
---------

Hasura does not have any resolvers. The Hasura GraphQL engine is actually a compiler, that compiles your GraphQL query into an SQL query.
Hasura's GraphQL syntax is also optimised to expose the power of the underlying SQL so that you can make powerful queries via GraphQL.

Metadata
--------

All the metadata mentioned above is stored by Hasura in 2 specific postgres schemas in your database. Hasura also does a lot of work to ensure that your metadata can be kept in sync with your actual Postgres schema.

#. You can run DDL queries through Hasura to check if the postgres schema change will cause some metadata to fail
#. You can ask Hasura to validate the current metadata it has against your postgres schema and spit out invalid metadata so that you can correct them

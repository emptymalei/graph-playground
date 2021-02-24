# graph-playground

This is mostly an exercise. For better performance, please use packages like networkx.

## Utilities

In `base.py`, some essential graph utilities are provided.

## Shared Interest Problem

Given a graph of users connected by interests, we can find the clustering of the user relations or the clustering of the interests. However, there is a catch. The graph provided may not be the full graph that we are going to use:

Suppose user 1 and user 2 share interest A, user 2 and user 3 share interest A too. The current graph doesn't specify the shared interest between user 1 and user 3. But we all know that they share interest A.

Before calculating the relations between the users, we can construct a graph that counts the relations between user 1 and user 3 then compute the clusters based on this larger graph.
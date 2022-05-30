# Hashtables

Implement a Hashtable Class with the following methods:

## set

Arguments: key, value

Returns: nothing

This method should hash the key, and set the key and value pair in the table, handling collisions as needed.

Should a given key already exist, replace its value from the value argument given to this method.

## get

Arguments: key

Returns: Value associated with that key in the table

## contains

Arguments: key

Returns: Boolean, indicating if the key exists in the table already.

## keys

Returns: Collection of keys

## hash

Arguments: key

Returns: Index in the collection for that key

## Challenge

New Implementation

## Approach & Efficiency

### Big O

- set - Has a o(1) because under the hood its using insert

- get - Has a o(1) because it gets the value by key index

- contains - Has a o(1) because it checks if the key is present by index

- keys - Has a o(n) because it must iterate through all keys.
  
- hash - Has a o(1) because it creates a hash from the key in one step

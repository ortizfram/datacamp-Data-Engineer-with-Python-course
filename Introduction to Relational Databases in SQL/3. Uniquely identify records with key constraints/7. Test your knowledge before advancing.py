"""
Test your knowledge before advancing
Before you move on to the next chapter, let's quickly review what you've learned so far about attributes and key constraints. If you're unsure about the answer, please quickly review chapters 2 and 3, respectively.

Let's think of an entity type "student". A student has:

. a last name consisting of up to 128 characters (required),
. a unique social security number, consisting only of integers, that should serve as a key,
. a phone number of fixed length 12, consisting of numbers and characters (but some students don't have one).

Instructions
100 XP
- Given the above description of a student entity, create a table students with the correct column types.
- Add a PRIMARY KEY for the social security number ssn.
- Note that there is no formal length requirement for the integer column. The application would have to make sure it's a correct SSN!

"""
#-- Create the table
CREATE TABLE students (
  last_name varchar(128) NOT NULL,
  ssn integer PRIMARY KEY,
  phone_no char(12)
);

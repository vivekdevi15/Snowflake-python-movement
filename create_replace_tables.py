#Creating new tables

import snowflake.connector
#from getpass import getpass
#import os


import credential as cred

con = snowflake.connector.connect(
  user= cred.db_user,
  password= cred.db_password,
  account= cred.db_server 
#  user= input("Please enter your username: "),
#  password= getpass("Please enter your password: "),
#  account='saggezzapartner.us-east-1'
)
cur = con.cursor()


#The below code is choosing the relevant role, warehouse, database and schema in the snowflake

cur.execute("USE ROLE PATIENT360")
cur.execute("USE WAREHOUSE PATIENT360_WH")
cur.execute("USE SCHEMA PATIENT360_DB.TEST")




cur.execute( """
CREATE OR REPLACE TABLE ALLERGIES(
START_DATE DATE,
STOP_DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE CAREPLANS(
ID VARCHAR(16777216),
START_DATE DATE,
STOP_DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216),
REASONCODE VARCHAR(16777216),
REASONDESCRIPTION VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE CONDITIONS(
START_DATE DATE,
STOP_DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE ENCOUNTERS(
ID VARCHAR(16777216),
START_DATE DATETIME,
STOP_DATE DATETIME,
PATIENT VARCHAR(16777216),
PROVIDER VARCHAR(16777216),
ENCOUNTERCLASS VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216),
COST NUMBER,
REASONCODE VARCHAR(16777216),
REASONDESCRIPTION VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE IMAGING_STUDIES(
ID VARCHAR(16777216),
DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
BODYSITECODE VARCHAR(16777216),
BODYSITEDESCRIPTION VARCHAR(16777216),
MODALITYCODE VARCHAR(16777216),
MODALITYDESCRIPTION VARCHAR(16777216),
SOPCODE VARCHAR(16777216),
SOPDESCRIPTION VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE IMMUNIZATIONS(
DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216),
COST NUMBER)
""")


cur.execute( """
CREATE OR REPLACE TABLE MEDICATIONS(
START_DATE DATE,
STOP_DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216),
COST NUMBER,
DISPENSES NUMBER,
TOTALCOST NUMBER,
REASONCODE VARCHAR(16777216),
REASONDESCRIPTION VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE OBSERVATIONS(
DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216),
VALUE NUMBER,
UNITS VARCHAR(16777216),
TYPE VARCHAR(16777216)) 
""")


cur.execute( """
CREATE OR REPLACE TABLE ORGANIZATIONS(
ID VARCHAR(16777216),
NAME VARCHAR(16777216), 
ADDRESS VARCHAR(16777216),
CITY VARCHAR(16777216),
STATE VARCHAR(16777216),
ZIP VARCHAR(16777216),
PHONE VARCHAR(16777216),
UTILIZATION NUMERIC)
""")


cur.execute( """
CREATE OR REPLACE TABLE PATIENTS(
ID VARCHAR(16777216),
BIRTHDATE DATE,
DEATHDATE DATE,
SSN VARCHAR(16777216),
DRIVERS VARCHAR(16777216),
PASSPORT VARCHAR(16777216),
PREFIX VARCHAR(16777216),
FIRST VARCHAR(16777216),
LAST VARCHAR(16777216),
SUFFIX VARCHAR(16777216),
MAIDEN VARCHAR(16777216),
MARITAL VARCHAR(16777216),
RACE VARCHAR(16777216),
ETHNICITY VARCHAR(16777216),
GENDER VARCHAR(16777216),
BIRTHPLACE VARCHAR(16777216),
ADDRESS VARCHAR(16777216),
CITY VARCHAR(16777216),
STATE VARCHAR(16777216),
ZIP VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE PROCEDURES(
DATE DATE,
PATIENT VARCHAR(16777216),
ENCOUNTER VARCHAR(16777216),
CODE VARCHAR(16777216),
DESCRIPTION VARCHAR(16777216),
BASE_COST NUMERIC,
REASONCODE VARCHAR(16777216),
REASONDESCRIPTION VARCHAR(16777216))
""")


cur.execute( """
CREATE OR REPLACE TABLE PROVIDERS(
ID VARCHAR(16777216),
ORGANIZATION VARCHAR(16777216),
NAME VARCHAR(16777216),
GENDER VARCHAR(16777216),
SPECIALITY VARCHAR(16777216),
ADDRESS VARCHAR(16777216),
CITY VARCHAR(16777216),
STATE VARCHAR(16777216),
ZIP VARCHAR(16777216),
UTILIZATION NUMERIC)
""")


con.close()
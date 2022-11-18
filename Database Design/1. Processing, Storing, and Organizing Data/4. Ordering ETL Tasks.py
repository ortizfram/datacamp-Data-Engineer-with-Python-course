"""
Ordering ETL Tasks
You have been hired to manage data at a small online clothing store. Their system is quite outdated because their only data repository is a traditional database to record transactions.

You decide to upgrade their system to a data warehouse after hearing that different departments would like to run their own business analytics. You reason that an ELT approach is unnecessary because there is relatively little data (< 50 GB).

Instructions
100XP
- In the ETL flow you design, different steps will take place. Place the steps in the most appropriate order.

"""
'''
1/ eCommerce APl outputs real time data of transactions
2/ Python script drops null rows and clean data Into pre-determined columns
3/ Resulting dataframe Is written Into an AWS Redshift Warehouse
'''

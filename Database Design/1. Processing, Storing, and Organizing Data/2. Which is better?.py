"""
Which is better?
The city of Chicago receives many 311 service requests throughout the day. 311 service requests are non-urgent community requests, ranging from graffiti removal to street light outages. Chicago maintains a data repository of all these services organized by type of requests. In this exercise, Potholes has been loaded as an example of a table in this repository. It contains pothole reports made by Chicago residents from the past week.

Explore the dataset. What data processing approach is this larger repository most likely using?

Instructions
50 XP
Possible Answers

        OLTP because this table could not be used for any analysis.
        OLAP because each record has a unique service request number.
 OK     OLTP because this table's structure appears to require frequent updates.
        OLAP because this table focuses on pothole requests only      

"""
SELECT * 
FROM Potholes;

'''
creation_date	current_status	completion_date	service_request_id	type_of_service	most_recent_action	street_address	zip
2018-12-17T00:00:00.000	Open	null	18-03380123	Pothole in Street	null	10300 S WALLACE ST	60628.0
2018-12-18T00:00:00.000	Open	null	18-03388180	Pothole in Street	null
'''

# The Earring Shoppe Capstone Project

This project is designed to give the owner of the shoppe a convenient place to sell their earrings to customers. Users log in using auth0 and, based on their role of either owner or customer, are given access to various endpoints.

You will need to have postgres, python3, and pip on your computer.

## How to run locally

First, pull the code to your computer. From the terminal, enter a psql terminal and create a database named earring_shoppe. Then run the following command to initialize the psql database with the test data, replacing username with your preferred username.

```
psql earring_shoppe < earring_shoppe.psql username
```




Next, enter the ./capstone/starter directory. You will then need to open a virtual environment using the following commands in your terminal (all following commands are for cmd on windows):

```
python3 -m venv venv
```

```
venv\Scripts\activate
```

You will then need to install all required dependencies by executing the following command in your virtual environment:

```
pip install -r requirements.txt
```



Next, initialize the necessary flask variables using the following commands.

```
set FLASK_APP=flaskr
```

```
set FLASK_DEBUG=1
```


## Starting the server

After initializing the database and flask variables, you are ready to run the backend!

First, start the PostgreSQL server using the following command, modifying the filepath and version to match your own.

```
pg_ctl -D "C:\Program Files\PostgreSQL\12\data" start
```


Next, from the ./capstone/starter directory, run

```
python3 app.py
```

This will start the backend.


## Postman Tests

To run these tests, you will need a postman account. Download and open the earring_shoppe.postman_collection.json file in postman.

Change the host variable to match yours if necessary.

The public folder requires no access token but the other four (Customer1, Customer2, Customer3, and Owner) require bearer tokens to be updated in the authorization tab.

For login information for each of these users and the link to obtain these tokens, view the folder page. The link will take you to an auth0 Login page where entering the given credentials and signing in will produce a bearer token found in the return url.


# amazon-scraping
How to Run Api:

The api is created with flask so make sure you have pipenv installed. 

DO: pip install pipenv. 

After downloading the files:
Open terminal -->

Next:  python -m pipenv sync
Next: python -m pipenv shell 
Next: set FLASK_APP=app
Finally: flask run


How To Use API:

Make sure to have postman installed or any way of posting to the url.

In the post request form data type you link like the following:

link : website 

Link is the key and website is the actually website link. Do not chage link.

Example: https://ibb.co/6PvSCWN

send the request to "http://localhost:5000/amazon"

send the request and you will get sent back data on the amazon product. It may take a couple trys to send the post request.

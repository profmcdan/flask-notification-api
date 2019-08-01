## Run

python service/service.py

## Description

Imagine that we have to configure the notification messages to be displayed in an OLED (short for Organic Light Emitting Diode) display wired to an IoT device. The IoT device is capable of running Python, Flask, and other Python packages. There is a team writing code that retrieves string messages that represent notifications from a dictionary and displays them in the OLED display wired to the IoT device. We have to start working on a mobile app and a website that has to interact with a RESTful API to perform CRUD operations with string messages that represent notifications.

We don't need an ORM (short for Object-Relational Mapping) because we won't persist the notifications on a database. We will just work with an in-memory dictionary as our data source. It is one of the requirements we have for this RESTful API. In this case, the RESTful Web Service will be running on the IoT device; that is, we will run the Flask development service on the IoT device.s

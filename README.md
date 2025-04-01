# SecureDeviceMock
To run:
docker compose up --build

To stop:
docker compose down

To stop and wipe database:
docker compose down -v

Or just ctrl-C for a graceful stop

The integration utilizes FastAPI for setting itself up as an API allowing for external requests. It is also used to mock the external service.
SQLAlchemy is used to easily set up Python classes as PostgreSQL tables and for creating the database itself.
APScheduler is used for the polling functionality allowing the scheduler to query from the external service at an interval or using cron.

For the initial setup I used AI (LLM) and various solutions on Github to integrate FastAPI, SQLAlchemy and APScheduler as these were unknown techonologies to me at the time. Given more time, I would have liked to delve even deeper into these technologies.

The integration is set up to poll from the mocked external every 10 seconds for testing. Commented code is included for cron type polling.

I interpret "Make "diff" of existing incident, if one" as having to update an incident if there are changes to it from the external service compared to what is stored in the database. As opposed to creating a new record of the differences between old and new incidents.

I have allowed myself to diverge a bit from the diagram in the integration exercise description due to the nature of mocking the external service. Therefore, the external does not directly patch the database, nor does the database GET from the integration. Rather, as it is currently built, the integration writes to the database, allowing a service to query the integration or database. 

To me it would make a lot more sense if the integration was connected to the external service and the database. Then the database should be on its own, only being connected to the integration. That way, the integration is the middle man between some external service providing data and the database which should be updated and handled accordingly. 

I also have not modeled the service. I have assumed that the service in the diagram is a frontend or microservice as opposed to another backend service. This at least makes more sense with the way I have built the integration like an API.

I have chosen to not include everything from an incident when mocking the data. This is simply to make it easier to debug in the console and keep track of for testing.

I have not tested the update functionality, but this was only optional as well.
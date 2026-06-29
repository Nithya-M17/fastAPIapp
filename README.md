# fastAPIapp

## creating fastAPI application
# CRUD operation
- Create
- Read
- Update
- Delete

# Rest API
- GET
- POST
- PUT
- DELETE
# status codes
- 200 OK
- 201 Created
- 204 No Content
- 400 Bad Request
- 403 Forbidden
- 405 Method Not Allowed
- 409 Conflict
- 500 Internal Server Error

# Architecture of fastapi application
- Model -- tables creation
- Router -- routes requests to controllers
- Controller -- controller logic
- Service -- business logic
- Repository -- data access layer
- Middleware -- request processing pipeline
- schema -- pydantic models for validation

# database
## relational database
- mysql
- postgresql
- sqlite
- sql server 

## non-relational database
- dynamodb
- mongodb
- redis
- cassandra

# constraits in database
- primary key -- eg: student_id, staff_id
- foreign key -- eg; department_id in student table
- unique --eg: email, phonenumber
- not null --eg: name
- check --eg: salary>0
- default --eg: timestamp: func.now()


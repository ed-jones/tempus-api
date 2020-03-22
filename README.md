# tempus_flask

Enable virtual environment: `source venv/bin/activate`
Run flask: `flask run`

# API Documentation

## Add User

```
POST: localhost:5000/add_user
Returns:
{
  "email" : "johnsmith@example.com", 
  "password" : "hunter2", 
  "firstname" : "John", 
  "lastname" : "Smith"
}
```

## Get User

```
POST: localhost:5000/get_user
{
	"uuid" : "ad52bf8a-6be0-11ea-9677-560001b9120c"
}
Returns:
{
	"email" : "johnsmith@example.com", 
  "firstname" : "John", 
  "lastname" : "Smith"
  "customer_rating" : 0.76
  "guide_rating" : 0.84
  "bio" : "John is a local Sydneysider who loves to give tours of the National Park"
}

```




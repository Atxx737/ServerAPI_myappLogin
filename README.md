# ServerAPI_myappLogin

Using Flask python to make local server.
Include API login, logout

## How to run this code
- First, create a new database and table in MySQL with command in file `models`
- Second, run this command:
  ``` 
    python restAPI.py 
  ```
  
 ### How to check API
 #### Using Postman to check API
 1. API Login - URL: http://localhost:5000/login

  Method: `POST`

  Request Body:
  ```
    {
      "username" : "roy",
      "password" : "roy"
    }
  ```
  Response:
  ```
    {
      "message": "You are logged in successfully"
    }
  ```

2. API Logout - URL: http://localhost:5000/logout

  Method: `GET`

  Response:

  ```
    {
       "message": "You successfully logged out"
    }
  ```

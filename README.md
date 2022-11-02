# fusus-django
Django REST API Exercise

Introduction 
This exercise is to prove your skills using Django Framework and Django Rest Framework.  
You should create a GIT repo in either Bitbucket, GitHub or GitLab. Please follow GitFlow on the Git  repo. Share link to the repository with your FUSUS contact. 
Please take in consideration application will be running in two environments DEV and PROD. Models 

Django should have models below: 

Organization model 
An organization should contain the following fields: 
  • id 
  • name  
  • phone 
  • address 

User model 
A user should contain the following fields: 
  • id 
  • name  
  • phone 
  • email (must be unique) 
  • organization (User belong to just one organization) 
  • birthdate 

API Endpoints  
DRF Should support the endpoints below 

Auth Endpoints:  
API must support JWT authentication 
  • POST /api/auth/login/ using email address
  • GET /api/auth/groups/ Should return Authentication Groups. Application should have: o Administrator: Full access to CRUD Any User in his org and RU Organization o Viewer: List and Retrieve and User in his org. 
  o User: CRU his own user 

User Endpoints:  
  • GET /api/users/ List all the users for the user organization if user is `Administrator` or  `Viewer`. Must return all the user model fields. Should support search by name, email.  Should support filter by phone. 
  • GET /api/users/{id}/ Retrieve user information, and the organization id and name • POST /api/users/ Create an user for the organization, must set password as well. Request  user must be Administrator 
  • PATCH /api/users/{id} Update user information for the user_id if request user is  `Administrator` of his organization. Or request user is user_id 
  • DELETE /api/users/{id} Delete user for the user_id if request user is `Administrator` of his  organization 

Organization Endpoints:  
  • GET /api/organizations/{id}/ Retrieve organization information if request user is  `Administrator` or `Viewer 
  • PATCH /api/organizations /{id} Update organization if request user is `Administrator`. • GET /api/organization/{id}/users List all the users for the user organization if user is  `Administrator` or `Viewer`. Must return just id and name of the user 
  • GET /api/organization/{id}/users/{id}/ Retrieve user id and name if if user is `Administrator`  or `Viewer` 

Other Endpoints:  
  • GET /api/info/ Should return {`user_name`, `id`, `organization_name`, `public_ip`} Public Ip  must be the internet public IP of the server where code is running

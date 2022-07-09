# django_crowdsourcingproject
Crowd Sourcing project using DJANGO, DRF

All of the following Features are currently working as intended. 

##User Accounts 
-	Username, Email, Password  
-	Visible Username upon Login 
-	Authentication required to create/pledge (Login and Logout)  
-	Update User Details (User Specific)   
-	

I would like to add a confirm email field and some further validation of email and passwords here but the CustomUser model does not allow for this without adjusting the models.  
Currently working on an additional permission of an admin user being able to delete ANY project rather than just the user themselves. 

##Projects
-	Create a new project   
-	Update a Project (Project Owner Specific)   
-	Delete a Project (Project Owner Specific) 

Currently working on an additional permission of an admin user being able to delete ANY project rather than just the user themselves. 


##Pledges
-	Create a pledge    
-	Comment   
-	Option to pledge anonymously   
-	Update a Pledge (Pledge Owner Specific)  
-	Delete a Pledge (Pledge Owner Specific)   

 


Additional Features. 

 - I wanted to try and sort projects via individual catagories however the DB table projects_project does not currently contain a field that would allow this to occur.
      would look like projects_project.Category
      
      
 Front End: 
 - Filter projects by date created. 
 - Search for project by an individual user
 - Search for Project containing key words
 - Goal Vs Total Pledges received Sum(goal - pledges = remaining_goal)


 ---------------------------------

 USER LOGIN/REGISTER PAGE

To Register a new User:

Step 1: User is directed to Home Page where they can click Login/Register from the navbar.
Step 2: User Clicks Login Register and is directed to http://localhost:8000/users/ which contains both options:
LOGIN –  POST request /api-token-auth
REGISTER -   POST request /users/new   

If User chooses to register, a success/fail message will return and then they can then enter their login details in the login fields above (at present will not automatically log a user in) 


To Create a New Project

User must be logged in to see the Nav option to create a new Project. 
User clicks into Create New Project and is directed to http://localhost:8000/projects/

Create New Project:  POST request: /Projects/new
User completes required fields of project and submits. 


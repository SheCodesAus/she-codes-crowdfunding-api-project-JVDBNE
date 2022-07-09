# django_crowdsourcingproject
Crowd Sourcing project using DJANGO, DRF



Heroku Link: https://vast-waters-62555.herokuapp.com/

https://vast-waters-62555.herokuapp.com/projects
https://vast-waters-62555.herokuapp.com/users


All of the following Features are currently working as intended. 

##User Accounts 
-	Username, Email, Password  
-	Visible Username upon Login 
-	Authentication required to create/pledge (Login and Logout)  
-	Update User Details (User Specific)   


I would like to add a confirm email field and some further validation of email and passwords here but the CustomUser model does not allow for this and models would need to be altered which I attempted but was not successful yet.
Currently working on an additional permission of an admin user being able to delete ANY project rather than just the user themselves via Features branch - not completed

##Projects
-	Create a new project   
-	Update a Project (Project Owner Specific)   
-	Delete a Project (Project Owner Specific) 




##Pledges
-	Create a pledge    
-	Comment   
-	Option to pledge anonymously   
-	Update a Pledge (Pledge Owner Specific)  
-	Delete a Pledge (Pledge Owner Specific)   



Additional Features. 
 - I wanted to try and link multiple users to a project however the DB table projects_project does not currently contain a field that would allow this to occur. 
 - I wanted to try and sort projects via individual catagories however the DB table projects_project does not currently contain a field that would allow this to occur.
      would look like projects_project.Catagories
      
      
 Front End: 
 - Filter projects by date created. 
 - Search for project by an individual user
 - Search for Project containing key words
 - Goal Vs Total Pledges received Sum(goal - pledges = remaining_goal)

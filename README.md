# Pitch Hub  
#### 9/11/2021  
#### By **Annalis Kirwa**  
## Description
Pitch Hub is a web application that allows users to use their one minute wisely to say something meaningful. 
The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.
The pitches are organized by category. You can have different categories like pickup lines, interview pitch, product pitch, promotion pitch  
## Behaviour Driven Development(BDD) 

| Behavior            | Input                         | Output                        | 
| ------------------- | ----------------------------- | ----------------------------- |
| View Interview Pitches | Click on any category | Taken to the clicked category | Click on `Click Here To Post A Pitch` | Redirected to the login page | Signs In/ Signs Up |
| Click `'Click Here To Post A Pitch'` | If logged in, display form to add a pitch | Redirected to the home page |
| Click upvote/ downvote button | Redirects to home page | Upvote/ downvote count changes | Click add comment button | Redirects to the comment page | Displays a comment form | Click on Sign Out | Redirects to the home page | Signs user out |
| Click on profile | Redirects to the profile page | User adds bio and profile picture |

 ## Features 
 As a user of Pitch Hub web application, you will be able to: 
 * see the pitches other people have posted  
 * vote on the pitch they liked and give it a downvote or upvote  
 * be signed in to leave a comment  
 * receive a welcoming email once I sign up  
 * view the pitches I have created in your profile page  
 * comment on the different pitches and leave feedback  
 * submit a pitch in any category  
 * view the different categories of pitches  
 
 ## Setup/Installation Requirements  
 ### To interact with the Pitch Hub web application:   
* Have the latest version of browser installed  
* Click on this <a href = "https://annpitches.herokuapp.com/">link</a> to use your one minute wisely  
  
 ### To contribute to the web application project:  
Make sure you have the following installed:  
```
Pip
Python version 3.6
Flask
virtualenv
```  
* Create an account on Github
* Fork the repository from Github with this <a href = "https://github.com/Annaliskirwa/_Pitch_Hub" >link </a>
* Clone the repository
* Open the project cloned project   
* Install virtual environment using `$ python3.6 -m venv --without-pip virtual`
* Activate virtual environment using `$ source virtual/bin/activate`
* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`
* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`
* Create a `start.sh` file in the root of the folder and add the following code:

        export MAIL_USERNAME=<your-email-address>
        export MAIL_PASSWORD=<your-email-password>
        export SECRET_KEY=<your-secret-key>

* Edit the configuration instance in `manage.py` by commenting on `production` instance and uncommenting `development` instance
* To run the application, in your terminal:

        $ chmod a+x start.sh
        $ ./start.sh  
   
   
## Known Bugs
There are no known bugs so far
## Technologies Used  
* Python v3.6  
* HTML
* Bootstrap
* Flask  
* Postgres  
## Support and contact details
In case of any problem while interacting with the web application, reach out to me at annalis.kirwa@student.moringaschool.com
### License.
MIT Copyright (c) 2021 **[MITlicense](LICENSE)**


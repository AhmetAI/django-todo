## A todo site with a simple user registration and login system
## **Setup**
Let's start with the Django installation first.


    $ pip install Django
After the installation, let's write the following codes in order for the database to work properly in the terminal.


    $ python manage.py makemigrations
and


    $ python manage.py migrate
Finally, you can create an administrative user if you wish.

### Attention! This user has the authority to view, change and delete all to-do's in the database.

 For this, you can write the following code in the terminal.


    $ python manage.py createsuperuser

And the installation is finished! Now you can launch the project and start using it! To do this, simply type the following code into the terminal.


    $ python manage.py runserver

Great! Now we can go to http://127.0.0.1:8000 and use our project :)

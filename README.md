# to-do-list-django
Basic to-do list application made in Django.

You can access the app at https://to-dolistdjango.herokuapp.com/

# Setup
First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:rafaellima47/to-do-list-django.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project.
    
Install project dependencies:

    $ pip install -r requirements.txt
    
    
Apply the migrations:

    $ python manage.py migrate


Run collectstatic:

	$ python manage.py collectstatic
    

You can now run the development server:

    $ python manage.py runserver

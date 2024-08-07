# HRManagement Application
## Description
HRManagement Application is used to make a time in and time outs and attendance details with hours and it shows the user details.

## Installation
### Clone the repository
$ https://github.com/arulvadivelav/HRManagement.git

### Create a virtual environment
```python3 -m venv HRM_env```

### Activate virtual environment
```HRM_env/Scipts/activate.bat```

### Navigate to the project directory
```cd HRM```

### Install dependencies
```pip install -r requirements.txt```

Update the __settings.py__ file with the necessary configuration parameters.

update the database section of __vendor_manage/settings.py__ as per your local configuration

## Apply migrations
```python manage.py migrate```

## Run a application
```python manage.py runserver```


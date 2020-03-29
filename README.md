# cloud_drive_app
Before you started you need to setup Amazon S3 and create a bucket for storing the documents.

### To run this application:

Install the requirements:
```bash
pip install -r requirements.txt
```

Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

Create a super user:
```bash
python manage.py createsuperuser
```

Create a static file on S3:
```bash
python manage.py collectstatic
```

Run the application:
```bash
python manage.py runserver
```

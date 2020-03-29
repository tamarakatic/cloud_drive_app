# cloud_drive_app
Before you started you need to setup Amazon S3 and create a bucket for storing the documents.

### To run this application:

```bash
pip install -r requirements.txt
```

```bash
python manage.py makemigrations
```

```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

```bash
python manage.py collectstatic
```

```bash
python manage.py runserver
```

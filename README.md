# bank-api

### Django 2.2.13, djangorestframework==3.14.0, django-filter==21.1 is used
#### added data from the given source https://github.com/Amanskywalker/indian_banks

#### To integrate data with django models use command python manage.py inspectdb


#### Databse used: PostgreSQL

#### Two endpoints:

### http://127.0.0.1:8000/api/banklist/    ---> list all the banks in database
### 127.0.0.1:8000/api/1/branchlist/       ---> list all the branches of a particular bank   note: "1" in the url is ID of particular bank

## filters

#### django filters is used to filter the branches. fiterset fields are ifsc, address, bank__name, district, city

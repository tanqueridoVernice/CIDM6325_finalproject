Deployment Issues
    -Deployed django app to vercel with no errors however webpage isn't properly routing urls.
    -database is successfully migrated to postgresql through railway
    -Vercel home page showing directory
    Url to site: https://cidm-6325-finalproject.vercel.app/degreecheck/WTdegreecheck/templates

Static files
    -static files stopped working when editing settings.py for deployment

Latest commit with changes to allow deployment messed up the original code.

For original source code:
Commit/branch to the original django app without changes made to accomodate deployment and is working fine:
fd90c248741299e21788563fadf75f5e9d0311b5

The zip file submitted was the commit just after this one with the code with first attempt to deploy on vercel.
Please go to settings.py and remove the vercel app from the allowed hosts or download the zip folder from branch for the original source code:
fd90c248741299e21788563fadf75f5e9d0311b5
#ALLOWED_HOSTS = ['.vercel.app']
change to ->ALLOWED_HOSTS = []

Django admin superuser: admin
Django admin password: WT123

I apologize for that. Thank you for this semester! :)

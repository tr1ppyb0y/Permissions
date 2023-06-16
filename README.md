# Permissions
LLD for user permissions in a hierarchal relationship.

[![Company hierarchy.](.\models-relationship.jpg "Company hierarchy.")](https://drive.google.com/file/d/1YuF93sGfJqJBX-dl3dZT41SmHQftvKQX/view?usp=sharing)

#### Steps to test:

1. Install the requirements.txt file.
2. Go to shell, `python manage.py shell`, and execute following commands,
```
from user.models import CustomUser
user = CustomUser.objects.last()
user.my_permissions()
```
3. Database is included for the convenience, spin-up the server and login with, `id:pass -> admin:admin`
4. Change the level of the user to **Plant** or **Company** or **HeadQuater** 
    and check the users permissions by _executing commands in step 2_.


#### This project display my skills to write clean and reusable code. Apart from that it also shows how efficiently I can incorporate in-built or otherwise data structures with business logic.

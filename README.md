# GroneSystem
Simulator about operating system make in API Django and PyQt5 GUI.

# Prerequisites 
-Anaconda
-MySQL
-Windows
-Should know about api architecture 

# Configure DATABASE:

  See https://medium.com/@a01207543/django-conecta-tu-proyecto-con-la-base-de-datos-mysql-2d329c73192a
  
  in MySql Console:
  
    CREATE DATABASE nombreDB CHARACTER SET utf8mb4;
    
    CREATE USER 'nombreusuario@localhost' IDENTIFIED BY 'pass';
    
    GRANT ALL PRIVILEGES ON nombreDB.* TO 'nombreusuario@localhost';
    
    FLUSH PRIVILEGES;
 
  configure in FilesManager/settings.py
  
    DATABASES = {
    
        'default': {
        
            'ENGINE': 'django.db.backends.mysql',
            
            'NAME': 'nameDataBase',
            
            'USER': 'user',
            
            'PASSWORD': 'pasword',
            
            'HOST': 'localhost',
            
            'PORT': '3306',
            
        }
        
    }

# Configure python dependencies
conda create --name <envname> --file requirements.txt
  
conda activate <envname>

# Configure migrations
make migrations in all modules
  into Applications, FilesManager and Kernel ejecute:
    python manage.py makemigrations
    python manage.py migrate
   example:
    cd FilesManager
    python manage.py makemigrations
    python manage.py migrate

# Run
cd Kernel

python main.py

# Stop Program
HTTP GET:
  http://127.0.0.1:8001/api/kernel/
  
  data:
  
  {
  "cod":0,
  "cmd":"stop"
  }

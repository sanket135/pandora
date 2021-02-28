#! /bin/sh

file=db.sqlite3
if [ -e "$file" ]; then
  # Control will enter here if $file exists
  rm $file
fi

# User credentials
user=pandora
email=sanketdave79@gmail.com
password=pandora

python3 manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$user', '$email', '$password')" | python3 manage.py shell
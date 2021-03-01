Status for Pandora Project with CircleCI

[![CircleCI](https://circleci.com/gh/sanket135/pandora.svg?style=svg)](https://circleci.com/gh/sanket135/pandora)

Hello !!

## Requirements for running Pandora Project are following:

Python version 3.6
Git

Django==2.2.1
djangorestframework==3.10.3
openfoodfacts==0.1.2

##Not Mandatory Requirements:

Docker 19.03.12
CircleCI (Signing in with Github account will let you see the test results and build logs by clicking passed badge)

Non Mandatory requirements will make running the project much easier without having to follow manual steps and switching version of python and django.

##Step by Step Manual:

Create django app by cloning it from repo:

git clone https://github.com/sanket135/pandora.git

cd pandora

git checkout master

##If you are already accomplishing the requirements please run:

python manage.py test

You can see the test result in console.
If you have dont have requirements and tests are failing in local , you can always check the test results by clicking on CircleCi Passed button and logging in with Github.

##If using Docker:

Depending on the Docker version, you have build the project and run it
With mentioned version following commands worked:

docker-composer build
docker-composer up

If you have other version following command will work aswell

docker composer up

##Project Pandora will be running at 

http://127.0.0.1:8000/admin

You can login using following credential:

Username: pandora

password: pandora

If you cannot login then run following command:

python manage.py createsuperuser

##Uploading Data
Following is the url for uploading data and please wait until screen shows Data uploaded.

http://127.0.0.1:8000/uploadpeople/data

people.json and companies.json are from inside
pandora/api/data

By replacing the files and revisiting the link above will replace old data with new data.

I have listed the api urls as follows:

## New Features
Your API must provides these end points:
- Given a company, the API needs to return all their employees. Provide the appropriate solution if the company does not have any employees.
  
http://127.0.0.1:8000/companyemployees/TECHTRIX

- Given 2 people, provide their information (Name, Age, Address, phone) and the list of their friends in common which have brown eyes and are still alive.
  
http://127.0.0.1:8000/persons/Pearson898/Bonnie2

- Given 1 people, provide a list of fruits and vegetables they like. This endpoint must respect this interface for the output: `{"username": "Ahi", "age": "30", "fruits": ["banana", "apple"], "vegetables": ["beetroot", "lettuce"]}`

http://127.0.0.1:8000/foodfor/Carmella0

###Please Note name provided are FirstName suffix with Index


##If you need any further information Please let me know.


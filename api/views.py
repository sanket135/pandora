import json
import os
import gc
import openfoodfacts as of
from django.contrib.auth.models import Group
from rest_framework import viewsets
from rest_framework import permissions
from api.models import User, Tag, favouriteFood, Fruit, Vegetable
from api.models import Company
from api.serializers import UserSerializer, GroupSerializer
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
from django.urls import resolve
from django.core.management import call_command


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

"""
    Following Classifier retrieves data from one of the World's Most Popular Food database
    OpenFoodFacts. 
    However, classifying fruits and vegetables wasn't that easy 
    but the solution is based on Data Analysis and it will work for wide range of Audience.
"""

def classifier(food):
    search_result = of.products.advanced_search({
        "search_terms": food,
    })
    i = 0
    v = 0
    f = 0
    try:
        while i < 12:
            check = search_result['products'][i]['ingredients_hierarchy']
            fruitcount = 0
            vegetablecount = 0
            for ch in check:
                if 'en:fruit' == ch:
                    fruitcount = fruitcount + 1
                elif 'en:vegetable' == ch:
                    vegetablecount = vegetablecount + 1
            if vegetablecount or fruitcount > 0:
                if fruitcount > vegetablecount:
                    #print('Fruit')
                    f += 1
                if vegetablecount > fruitcount:
                    #print('Vegetable')
                    v += 1
            i += 1
        #print(f)
        #print(v)
    except Exception:
        pass
    finally:
        if f > v:
            classification = 'fruit'
            return classification
        if v > f:
            classification = 'vegetable'
            return classification
        if f == v:
            print('Not classified')
            classification = 'None'
            return classification

def companyemployees(request, companyname):
    print("......")
    companydict = {}
    companydetails = Company.objects.filter(company=companyname)
    for companydetail in companydetails:
        print(companydetail.company)
        companyindex = companydetail.index
    print("got company name")
    employees = User.objects.filter(company__index=companyindex)
    print(employees)
    companydict.update({"Company Name": companyname})
    employeeslist = []
    for employeedetail in employees:
        print(employeedetail.name)
        employeeslist.append(employeedetail.name)

    print("count of employees")
    print(len(employeeslist))
    if len(employeeslist) >= 1:
        companydict.update({"Employees": employeeslist})
        data = json.dumps(companydict, indent=4)
        return HttpResponse(data)
    else:
        context = {'message': 'No Employees listed with the Company'}
        response = render(request, "message.html", context)
        return response



def persons(request, persononename, persontwoname):
    personsdict = {}
    personone = User.objects.filter(username=persononename)
    personone = person(personone)
    personsdict.update({"personone": personone})
    persontwo = User.objects.filter(username=persontwoname)
    persontwo = person(persontwo)
    personsdict.update({"persontwo": persontwo})
    friends = mutualfriends(personone, persontwo)
    personsdict["personone"].pop("friends")
    personsdict["persontwo"].pop("friends")
    personsdict.update({"friends": friends})
    #print(personsdict)
    data = json.dumps(personsdict, indent = 4)
    return HttpResponse(data)

def person(persondetail):
    person = {}
    for item in persondetail:
        person.update({"id": item.id})
        person.update({"name": item.name})
        person.update({"age": item.age})
        person.update({"address": item.address})
        person.update({"phone": item.phone})
        friends = item.friends.all()
        friendsd = {}
        for friend in friends:
            friendl = {}
            friendl.update({"id": friend.id})
            friendl.update({"name": friend.name})
            friendl.update({"eyeColor": friend.eyeColor})
            friendl.update({"has_died": friend.has_died})
            if friend.eyeColor == 'brown' and friend.has_died is False:
                friendsd.update({friend.id: friendl})

        person.update({"friends": friendsd})
    return person

def mutualfriends(personone, persontwo):
    friends = {}
    for key in personone["friends"].keys():
        if key in persontwo["friends"].keys():
            friends.update({persontwo["friends"][key]["id"]: persontwo["friends"][key]})
    return friends

def foodfor(request, personname):
    persondetail = User.objects.filter(username=personname)
    print(persondetail)
    details = {}
    for detail in persondetail:
        print(detail.username)
        print(detail.age)
        details.update({"username": detail.username})
        details.update({"age": detail.age})
        print(detail.fruit)
        fruits = detail.fruit.all()
        print(fruits)
        fruitlist = []
        for fru in fruits:
            print(fru.name)
            fruitlist.append(fru.name)
        vegetables = detail.vegetables.all()
        print(vegetables)
        vegetableslist = []
        for vegies in vegetables:
            vegetableslist.append(vegies.name)
        details["fruits"] = fruitlist
        details["vegetables"] = vegetableslist
        print(details)
        data = json.dumps(details, indent = 4)
    return HttpResponse(data)

def uploadpeople(request, env):
    if env == 'test':
        uploadcompanies()
        file = os.getcwd() + '/api/data/test/peopletest.json'
    else:
        #Flushing previous data
        call_command('flush', verbosity=3, interactive=False)
        # uploading companies data first
        uploadcompanies()
        file = os.getcwd() + '/api/data/people.json'
    print(file)
    password = make_password("pandora")
    peoplecount = 0
    with open(file) as fi:
        print("Creating People data in ...")
        data = json.load(fi)
        peoplecount = len(data)
        print("People count is ...")
        print(peoplecount)
        i = 0
        print("Creating People...")
        for item in data:
            username = item["name"].split(' ')[0] + str(item["index"])
            User.objects.create(username=username, name=item["name"], password=password, index=item["index"], age=item["age"], eyeColor=item["eyeColor"], has_died=item["has_died"], address=item["address"], phone=item["phone"])
            user = User.objects.filter(index=item["index"])
            # Adding Related Company
            companyid = item["company_id"]
            relatedcompanys = Company.objects.filter(index=companyid)
            for relatedcompany in relatedcompanys:
                for detail in user:
                    #print(detail.company)
                    detail.company.add(relatedcompany)
            print("Added related Company")
            # Adding Related Tags
            usertags = item["tags"]
            tagslist = []
            print("Creating tags...")
            for tag in usertags:
                tagstr = tag.lower()
                tagstr.strip(" ")
                Tag.objects.get_or_create(tag=tagstr)
                tagslist.append(tag)
            print("Adding tags to relevant users..")
            relatedusertags = Tag.objects.filter(tag__in=tagslist)
            #print(user)
            #print(relatedusertags)
            for relatedusertag in relatedusertags:
                for detail in user:
                    #print(detail.tags)
                    detail.tags.add(relatedusertag)
            print("Related Tags added..")
            # Adding related Food
            favouritefoods = item["favouriteFood"]
            favouritefoodslist = []
            fruitlist = []
            vegetablelist = []
            print("Creating foods...")
            for food in favouritefoods:
                foodstr = food.lower()
                foodstr.strip(" ")
                # Classify and if non existent in model then only then call classifier and create food.
                if not (Fruit.objects.filter(name=foodstr).exists() or Vegetable.objects.filter(name=foodstr).exists()):
                    classification = classifier(foodstr)
                    if classification == 'fruit':
                        Fruit.objects.get_or_create(name=foodstr)
                        fruitlist.append(foodstr)
                    if classification == 'vegetable':
                        Vegetable.objects.get_or_create(name=foodstr)
                        vegetablelist.append(foodstr)
                elif Fruit.objects.filter(name=foodstr).exists():
                    fruitlist.append(foodstr)
                elif Vegetable.objects.filter(name=foodstr).exists():
                    vegetablelist.append(foodstr)
                favouriteFood.objects.get_or_create(name=foodstr)
                favouritefoodslist.append(food)
            print("Adding foods to relevant users..")
            relatedfavouritefoods = favouriteFood.objects.filter(name__in=favouritefoodslist)
            relatedfruits = Fruit.objects.filter(name__in=fruitlist)
            relatevegetables = Vegetable.objects.filter(name__in=vegetablelist)
            #print(user)
            #print(relatedfavouritefoods)
            #print(relatedfruits)
            #print(relatevegetables)
            for relatedfavouritefood in relatedfavouritefoods:
                for detail in user:
                    #print(detail.favouriteFood)
                    detail.favouriteFood.add(relatedfavouritefood)
            # Adding related Fruits
            if relatedfruits.exists():
                for relatedfruit in relatedfruits:
                    for detail in user:
                        #print(detail.fruit)
                        detail.fruit.add(relatedfruit)
            # Adding related Vegetables
            if relatevegetables.exists():
                for relatedvegetable in relatevegetables:
                    for detail in user:
                        #print(detail.vegetables)
                        detail.vegetables.add(relatedvegetable)
            print("Related Favourite Foods added..")
            i += 1
            print("Creating People Completed")

        if i == peoplecount:
            fi.close()
            # Once all users are created then and only then Relations are added since they have many to many relation with user self
            uploadrelateddate(env)

    del(data)
    del(item)
    del(username)
    del(fi)
    gc.collect()
    return HttpResponse('Data Uploaded')

def uploadcompanies():
    companyfile = os.getcwd() + '/api/data/companies.json'
    print(companyfile)
    companycount = 0
    with open(companyfile) as cfi:
        print("Creating Companies data in ...")
        data = json.load(cfi)
        companycount = len(data)
        print("Company count is ...")
        print(companycount)
        for item in data:
            #print(item["index"])
            Company.objects.create(index=item["index"], company=item["company"])

    del (data)
    del (item)
    del (cfi)
    gc.collect()
    return HttpResponse('Company Data is uploading...')

def uploadrelateddate(env):
    if env == 'test':
        input = os.getcwd() + '/api/data/test/peopletest.json'
    else:
        input = os.getcwd() + '/api/data/people.json'
    print(input)
    print("Adding related Friends Data....")
    with open(input) as fi:
        data = json.load(fi)
        for item in data:
            friendlist = []
            friends = item["friends"]
            u = User.objects.filter(index=item["index"])
            for friendid in friends:
                friendlist.append(friendid["index"])
            relatedfriends = User.objects.filter(index__in=friendlist)
            for relatedfriend in relatedfriends:
                for detail in u:
                    detail.friends.add(relatedfriend)
            del (friendlist)
            del(relatedfriends)
            del (friends)
            del (friendid)
            gc.collect()
    print("Related Friends added..")


def handler500(request, *args, **argv):
    url_name = resolve(request.path).url_name
    print(url_name)
    if url_name == "companyemployees":
        context = {'message': 'No Company listed with the name'}
        response = render(request, "message.html", context)
        response.status_code = 500
        return response


from django.shortcuts import render
import mysql.connector
from  django.contrib import messages

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="shree7",
    database="photography",
    autocommit=True
)

cursor = mydb.cursor()

# Create your views here.
def index(requests):
    return render(requests,'index.html')

def photo_detail_clock(requests):
    return render(requests,'photo_detail_clock.html')    

def photo_detail_plant(requests):
    return render(requests,'photo_detail_plant.html') 

def photo_detail_morning(requests):
    return render(requests,'photo_detail_morning.html')  

def photo_detail_perfume(requests):
    return render(requests,'photo_detail_perfume.html')

def photo_detail_headphone(requests):
    return render(requests,'photo_detail_headphone.html')

def photo_detail_moon(requests):
    return render(requests,'photo_detail_moon.html')

def photo_detail_bus(requests):
    return render(requests,'photo_detail_bus.html')   

def photo_detail_abstract(requests):
    return render(requests,'photo_detail_abstract.html')

def photo_detail_flower(requests):
    return render(requests,'photo_detail_flower.html')     

def photo_detail_rosy(requests):
    return render(requests,'photo_detail_rosy.html')

def photo_detail_rock(requests):
    return render(requests,'photo_detail_rock.html')  

def photo_detail_purple(requests):
    return render(requests,'photo_detail_purple.html')

def photo_detail_sea(requests):
    return render(requests,'photo_detail_sea.html')

def photo_detail_turtle(requests):
    return render(requests,'photo_detail_turtle.html')

def photo_detail_peace(requests):
    return render(requests,'photo_detail_peace.html')    

def photo_detail_newyork(requests):
    return render(requests,'photo_detail_newyork.html')                                   


def about(requests):
    return render(requests,'about.html')    

def contact(requests):  
    if requests.method == 'POST':
        name = requests.POST['name']
        email = requests.POST['email']
        inquiry = requests.POST['inquiry']
        message = requests.POST['message']
        cursor.execute("INSERT INTO contact (name,email,inquiry,message) VALUES (%s,%s,%s,%s)",(name,email,inquiry,message))
        messages.success(requests, 'Your message has been sent!')
        return render(requests,'contact.html')

    return render(requests,'contact.html')
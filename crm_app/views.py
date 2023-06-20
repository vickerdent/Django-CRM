from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .forms import SignUpForm, EditRecordForm
from utils import collection, Customer

# Create your views here.
def home(request):
    plainers = []
    try:
        records = list(collection.find())
        for record in records:
            plainer = Customer(record["First Name"], record["Last Name"], record["Email"],
                            record["Phone Number"], record["Address"], record["City"], record["State"],
                            record["Zipcode"], record["Created At"])
            plainers.append(plainer)
    except:
        plainers = ["No Connection to Database Server", "Check your internet access"]
    
    return render(request, "home.html", {"records": plainers})

def login_user(request):
    # check if login attempt or normal request
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have logged in successfully.")
            return redirect("home")
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect("login")
        
    return render(request, "login.html", {})

def logout_user(request):
    logout(request)
    messages.success(request, "You've been logged out successfully.")
    return redirect("home")

def register(request):
    # check if registration attempt or normal request
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email") # get email from form
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists! Email must be unique!")
                return redirect("register")
            form.save()
            # Authenticate and login user
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have signed up and logged in successfully.")
            return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})

    return render(request, "register.html", {"form": form})

def customer_record(request, pk):
    if request.user.is_authenticated:
        # Look up record for user
        customer = collection.find_one({"Email": pk})
        if customer is not None:
            plainer = Customer(customer["First Name"], customer["Last Name"], customer["Email"],
                                customer["Phone Number"], customer["Address"], customer["City"], customer["State"],
                                customer["Zipcode"], customer["Created At"])
            return render(request, "record.html", {"customer": plainer})
        else:
            messages.error(request, "User does not exist!")
            return render(request, "record.html", {"customer": "Not existing"})
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect("login")
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        # Look up record for user
        collection.delete_one({"Email": pk})
        messages.success(request, "You have successfully deleted the record.")
        return redirect("home")
    else:
        messages.error(request, "You must be logged in to do that!")
        return redirect("login")
    
def add_record(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]
            zipcode = request.POST["zipcode"]

            if collection.find_one({"Email": email}) != None:
                messages.error(request, "Email already exists! Email must be unique")
                return redirect("add_record")

            new_customer = Customer(first_name, last_name, email, phone, address, city, state, zipcode)
            collection.insert_one(new_customer.to_dict())
        
            messages.success(request, "You have successfully added a new record.")
            return redirect("home")
        return render(request, "add_record.html", {})
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect("login")
    
def edit_record(request, pk):
    if request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]
            zipcode = request.POST["zipcode"]
            
            old_customer = Customer(first_name, last_name, email, phone, address, city, state, zipcode)
            collection.update_one({"Email": email},{
                "$set": old_customer.to_update()
            })

            messages.success(request, "You have successfully updated the record.")
            return redirect("home")
        else:
            customer = collection.find_one({"Email": pk})
            initial = {"first_name": customer["First Name"], "last_name": customer["Last Name"], 
                       "email": customer["Email"], "phone": customer["Phone Number"], "address": customer["Address"], 
                       "city": customer["City"], "state": customer["State"], "zipcode": customer["Zipcode"]}
            form = EditRecordForm(initial=initial)
            return render(request, "edit_record.html", {"form": form})
    else:
        messages.error(request, "You must be logged in to view that page...")
        return redirect("login")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Booking
from .forms import RegisterForm

# ------------------------------
# --- AUTHENTICATION VIEWS ---
# ------------------------------

def register(request):
    """
    Handle user registration:
    - POST: validate form, set password, save user, login, redirect to login page
    - GET: render empty registration form
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.username = form.cleaned_data['email']  # email as username
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    """
    Handle user login:
    - POST: authenticate and login, redirect to dashboard
    - GET / failed login: render login page with error
    """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')


def logout_view(request):
    """Logout user and redirect to login page"""
    logout(request)
    return redirect('login')

def home(request):
    return redirect('login')

# ------------------------------
# --- DASHBOARD & BOOKINGS ---
# ------------------------------

@login_required
def dashboard(request):
    """Show user's bookings on dashboard"""
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'bookings': bookings})


@login_required
def add_booking(request):
    """Add a new booking for the logged-in user"""
    if request.method == 'POST':
        Booking.objects.create(
            user=request.user,
            name=request.user.first_name,
            table_number=request.POST['table_number'],
            date=request.POST['date'],
            time=request.POST['time']
        )
    return redirect('dashboard')


@login_required
def delete_booking(request, booking_id):
    """Delete user's booking by ID"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.delete()
    return redirect('dashboard')


@login_required
def edit_booking(request, booking_id):
    """Edit booking via POST (AJAX)"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    if request.method == 'POST':
        booking.name = request.POST['name']
        booking.table_number = request.POST['table_number']
        booking.date = request.POST['date']
        booking.time = request.POST['time']
        booking.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'failed'})

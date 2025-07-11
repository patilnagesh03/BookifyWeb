from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistrationForm,UserIdentityForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
# from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Book, HindiVersion # Importing the Book and HindiVersion models

from django.utils.encoding import force_str, force_bytes # Importing necessary functions for encoding and decoding
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode # Importing necessary functions for encoding and decoding

# Create your views here.

# This view handles user registration
def ResisterView(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Registration successful!You can now log in.')
            email = form.cleaned_data.get('email')
            subject = 'Registration Successful'
            message = 'Thank you for registering with us. Your account has been successfully created and is now ready for use.'
            from_email = 'nageshpatil7311@gmail.com'
            recipient_list = [email]  # Add the user's email to the recipient list
            fail_silently = False  # Set to True to suppress errors
            send_mail(subject, message, from_email, recipient_list, fail_silently=fail_silently)

            return redirect('login')
    
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

# This view handles user login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_authenticated:
                    login(request, user)
                    # messages.info(request, 'Login successful!')
                return redirect('dashboard')  # Redirect to a home page or dashboard
        messages.error(request, 'Invalid username or password.')
        return redirect('login')  # Redirect to the login page if authentication fails
    
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# This view handles user logout
def logout_view(request):
    logout(request)
    messages.error(request, 'You have been logged out successfully.')
    return redirect('dashboard')  # Redirect to the login page after logout


# This view handles password change functionality
login_required(login_url='login')
def ChangePasswordView(request):
    user = User.objects.get(username=request.user.username)
    if request.method == 'POST':
        form = PasswordChangeForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!' )
            return redirect('book-list')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'change_password.html', {'form': form})

# This view displays a summary of books
def BookSummaryView(request):
    book_summary = Book.objects.all()
    return render(request, 'book_summary.html',{'book_summary': book_summary})

# This view displays the details of a specific book
@login_required(login_url='login')
def BookDetailView(request, book_id):
    try:
        book_summary = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        messages.error(request, 'Book not found.')
        return redirect('book-list')  # Redirect to the book summary page if the book does not exist
    
    return render(request, 'book_detail.html', {'book_summary': book_summary})

# This view handles user identity verification for password reset
def UserIdentityView(request):
    if request.method == 'POST':
        form = UserIdentityForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            if User.objects.filter(username = username).exists():
                en_uname = urlsafe_base64_encode(force_bytes(username))
                url = 'http://127.0.1:8000/reset-password/' + en_uname + '/'
                subject = 'Password Reset Request'
                message = f'Click the link below to reset your password:\n{url}'
                from_email = 'nageshpatil7311@gmail.com'
                recipient_list = [User.objects.get(username=username).email]
                fail_silently = True
                send_mail(subject, message, from_email, recipient_list, fail_silently=fail_silently)
                # return redirect(url)
                messages.success(request, 'Password reset link has been sent to your email.')
                return redirect('login')
            else:
                messages.error(request,'User not found')
        
    form = UserIdentityForm()
    return render(request, 'UserIdentity.html',{'form':form})

# This view handles the password reset functionality
def ResetPasswordView(request, en_uname):
    dc_name = force_str(urlsafe_base64_decode(en_uname))
    if request.method == 'POST':
        form = SetPasswordForm(user=User.objects.get(username=dc_name), data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password has been reset successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SetPasswordForm(user=User.objects.get(username=dc_name))
    return render(request, 'reset_password.html', {'form': form, 'username': dc_name})

# This view displays a summary of Hindi books
def HindiBookSummaryView(request):
    hindi_book_summary = HindiVersion.objects.all()
    return render(request, 'hindi_book_summary.html', {'hindi_book_summary': hindi_book_summary})

# This view displays the details of a specific Hindi book
@login_required(login_url='login')
def HindiBookDetailView(request, book_id):
    try:
        hindi_book_summary = HindiVersion.objects.get(id=book_id)
    except HindiVersion.DoesNotExist:
        messages.error(request, 'Hindi book not found.')
        return redirect('hindi-book-list')  # Redirect to the Hindi book summary page if the book does not exist
    
    return render(request, 'hindi_book_detail.html', {'hindi_book': hindi_book_summary})

# This views handles the search part
    
def search_books(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Book.objects.filter(title__icontains=query) | Book.objects.filter(author__icontains=query)
    return render(request, 'search_results.html', {'books': results, 'query': query})

def Dashboard_View(request):
    return render(request,'dashboard.html')
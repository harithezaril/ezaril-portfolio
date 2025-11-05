from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    print(f"🔥 Request method: {request.method}")  # Debug line
    print(f"🔥 POST data: {request.POST}")  # Debug line
    
    if request.method == 'POST':
        print("✅ Inside POST block!")  # Debug line
        
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        print(f"📧 Data: {name}, {email}, {subject}")  # Debug line
        
        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        
        print("💾 Message saved to database!")  # Debug line
        
        messages.success(request, 'Thank you! Your message has been sent successfully.')
        return redirect('contact')
    
    print("❌ Not POST, rendering form")  # Debug line
    return render(request, 'home/contact.html')
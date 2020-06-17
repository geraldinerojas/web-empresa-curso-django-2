from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    template = "contact/contact.html"
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}> \n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["geraldine.rojas@unillanos.edu.co"],
                reply_to=[email]
            )
            try:
                email.send()
                #Toodo ha ido bien
                return redirect(reverse('contact') + '?ok')
            except:
                # Algo no ha ido bien
                return redirect(reverse('contact')+'?fail')
    return render(request, template, {'contact_form': contact_form})
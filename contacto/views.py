from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    form_contacto = FormularioContacto()

    if request.method=='POST':
        form_contacto=FormularioContacto(data=request.POST)
        if form_contacto.is_valid():
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            envmail=EmailMessage("mensaje desde mavrd","El usuario: {} con el email: {} escribe:\n {}".format(nombre,email,contenido),"",["ramndiazgzmn@gmail.com"],reply_to=[email])
            #send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email', ''), ['ramndiazgzmn@gmail.com'],)
            try:
                envmail.send()

                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")

    return render(request,"contacto/contacto.html", {'miFormulario':form_contacto})

from django.shortcuts import render
from django.core.mail import send_mail

def index(request):
    return render(request, 'paginas/index.html')

def sobre(request):
    return render(request, 'paginas/sobre.html')

def contato(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        data = {
                'name':name,
                'subject':subject,
                'phone':phone,
                'email':email,
                'message':message
                
            
        }
        message = '''
        Nova mensagem: {}
        
        De: {}
        Nome: {}
        Telefone: {}
        '''.format(data['message'],data['email'],data['name'],data['phone'])
        send_mail(data['subject'],message, '' ,['xxxxxx@gmail.com'])
        
    return render(request, 'paginas/contato.html', {})

def projetos(request):
    return render(request, 'paginas/projetos.html')

# Create your views here.

""" 
    path('create',views.create),
    
    path('search/',views.search),
    path('apartments/',views.apartments),
    path('contact/',views.contact),
    path('images/',views.images),"""










 """   
  
def index(request):
    m = abc.objects.all()
    context ={}
    context['data'] = m
    return render(request,'index.html',context)

   

   
def search(request):
    m = abc.objects.all()
    context ={}
    context['data'] = m
    return render(request,'search.html',context)

def apartments(request):
    m = abc.objects.all()
    context ={}
    context['data'] = m
    return render(request,'apartments.html',context)

def images(request):
    m = abc.objects.all()
    context ={}
    context['data'] = m
    return render(request,'images.html',context)

def contact(request):
    m = abc.objects.all()
    context ={}
    context['data'] = m
    return render(request,'contact.html',context)


"""
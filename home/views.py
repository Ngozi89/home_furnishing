from django.shortcuts import render

# Create your views here.
# Home page
def index(request):
    '''
    A view to render the home page
    '''
    return render(request, 'home/index.html')

def about_page(request):
    ''' Renders About us page '''
    return render(request, 'home/about.html')

def support_page(request):
    ''' Renders Customer support page '''
    return render(request, 'home/support.html')

def privacy_page(request):
    ''' Renders Privacy Policy page '''
    return render(request, 'home/privacy_policy.html')
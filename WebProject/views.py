from django.shortcuts import render

# Create your views here.
def home(request):
    context = { 'message': "Success" }
    return render(request,'index.html', context)

    def contacts(request):
        string={'key':'Success'}
        return render(request, 'index.html',context)
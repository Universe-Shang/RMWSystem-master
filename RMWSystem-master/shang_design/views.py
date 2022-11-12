from django.shortcuts import render,redirect

# Create your views here.
def main_page(request):

    test = request.POST.get('fangjia')
    print(type(test))
    print("test = ", test)
    return render(request,'main_page.html')
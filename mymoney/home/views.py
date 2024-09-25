from django.shortcuts import render

money_soccer_value = 400.58
def homepage(request):
    return render(request, 'home/index.html', {'money_soccer': money_soccer_value})

def addmoney(request):
    return render(request, 'home/addmoney.html', {'money_soccer': money_soccer_value})

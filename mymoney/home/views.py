from django.shortcuts import render, redirect

# Set initial value of money_soccer
money_soccer_value = 400.58


def homepage(request):
    return render(request, 'home/index.html', {'money_soccer': money_soccer_value})

def addmoney(request):
    global money_soccer_value  # Use global variable to modify it

    if request.method == 'POST':
        # Get the amount from the form
        amount = request.POST.get('amount')
        try:
            # Convert to float, round to 2 decimal places, and add to existing value
            money_soccer_value += round(float(amount), 2)
        except ValueError:
            # Handle the case where conversion fails
            pass

        # Redirect to avoid re-submission on refresh
        return redirect('addmoney')

    return render(request, 'home/addmoney.html', {'money_soccer': money_soccer_value})
def makeshop(request):
    global money_soccer_value  # Use global variable to modify it
    if money_soccer_value <= 0:
        money_soccer_value = 0
    if request.method == 'POST':
        # Get the amount from the form
        amount = request.POST.get('amount')
        try:
            # Convert to float, round to 2 decimal places, and add to existing value
            money_soccer_value -= round(float(amount), 2)
        except ValueError:
            # Handle the case where conversion fails
            pass

        # Redirect to avoid re-submission on refresh
        return redirect('makeshop')

    return render(request, 'home/makeshop.html', {'money_soccer': money_soccer_value})

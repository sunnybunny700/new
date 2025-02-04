from django.shortcuts import render

# Home page view
def home(request):
    context={}
    return render(request, "myapp/home.html", context)

# MaterialBank page view
def bank(request):
    return render(request, "myapp/bank.html")

# Properties page view
def prop(request):
    return render(request, "myapp/prop.html")

# Diagnostic page view
def diagnostic(request):
    return render(request, "myapp/diagnostic.html")

# Wizard page view
def wizard(request):
    return render(request, "myapp/wizard.html")
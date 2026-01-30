from django.shortcuts import render
from . models import ShippingAddress

def checkout(request):
    
    #Users with account  Prefill the data in the form
    if request.user.is_authenticated:  
        try:
            shipping_address = ShippingAddress.objects.get( user = request.user.id )
            context = { 'shipping': shipping_address }
            return render(request, 'payment/checkout.html', context)
        
        except:
            #Autenticated Users with no shipping information 
            return render(request, 'payment/checkout.html')
    
    else : #Guess user 
        return render(request, 'payment/checkout.html')
    

def complete_order(request):
    pass

def payment_success(request):
    return render(request, 'payment/payment-success.html')

def payment_failed(request):
    return render(request, 'payment/payment-failed.html')

 
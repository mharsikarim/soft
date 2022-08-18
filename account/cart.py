from django.http import JsonResponse
from django.shortcuts import render, redirect
from societe.models import Services, Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def addtocart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
           prod_id = int(request.POST.get('service_id'))
           product_chek = Services.objects.get(id=prod_id)
           if(product_chek):
               if(Cart.objects.filter(user=request.user.id,service_id=prod_id)):
                   return JsonResponse({'status': "cette service est déja ajouter"})
               else:
                   prod_qty = int(request.POST.get('product_qty'))

                   Cart.objects.create(user=request.user,service_id=prod_id,product_qty=prod_qty)
                   return JsonResponse({'status': "cette service est ajouter avec success"})
           else:
            return JsonResponse({'status':"cette service est introuvable"})
        else:
            return JsonResponse({'status':"Login to continue"})

    return redirect('index')
@login_required(login_url="acces")
def viewcart(request):
    cart=Cart.objects.filter(user=request.user)
    context={'cart':cart}
    return render(request,'societe/service/cart.html',context)
def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('service_id'))
        if (Cart.objects.filter(user=request.user, service_id=prod_id)):
            prod_qty= int(request.POST.get('product_qty'))
            cart=Cart.objects.get(service_id=prod_id,user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status':"Updated successfully"})
    return redirect('index')
def deletecartitem (request):
     if request.method == 'POST':
        prod_id = int(request.POST.get('service_id'))
        if (Cart.objects.filter(user=request.user, service_id=prod_id)):
            cartitem=Cart.objects.get(service_id=prod_id,user=request.user)
            cartitem.delete()
            return JsonResponse({'status':"Deleted successfully"})
     return redirect('index')
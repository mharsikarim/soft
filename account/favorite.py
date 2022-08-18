from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from societe.models import Services, Wishlist


@login_required(login_url="acces")
def index(request):
  wishlist=Wishlist.objects.filter(user=request.user)
  context = {'wishlist':wishlist}
  return render(request,'societe/service/wishlist.html',context)

def addtowishlist(request):
  if request.method=="POST":
    if request.user.is_authenticated:
      prod_id=int(request.POST.get('service_id'))
      product_check= Services.objects.get(id=prod_id)
      if(product_check):
        if (Wishlist.objects.filter(user=request.user,service_id=prod_id)):
          return JsonResponse({'status':"cette service est déja dans favorite list"})
        else:
          Wishlist.objects.create(user=request.user,service_id=prod_id)
          return JsonResponse({'status':"cette service est ajouté avec success"})
      else:
        return JsonResponse({'status':"cette service est introuvable"})
    else:
      return JsonResponse({'status':"login to continue"})

  return redirect('service')
def deletewishlistitem(request):
  if request.method=='POST':
    prod_id=int(request.POST.get('service_id'))
    if request.user.is_authenticated:
       if (Wishlist.objects.filter(user=request.user,service_id=prod_id)):
          wishlistitem=Wishlist.objects.get(service_id=prod_id,user=request.user)
          wishlistitem.delete()
          return JsonResponse({'status':"cette service est supprimé "})
       else:
          return JsonResponse({'status':"cette service est introuvable dans favorite liste"})

    else:
      return JsonResponse({'status':"login to continue"})

  return redirect('index')
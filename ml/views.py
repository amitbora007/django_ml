from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
import pickle

# Create your views here.
def index(request):
	if request.method == 'POST':
		bathroom = int(request.POST['bathrooms'])
		gr = int(request.POST['guestroom'])
		hwh = int(request.POST['hotwaterheating'])
		mr = int(request.POST['mainroad'])
		ac = int(request.POST['airconditioning'])
		pa = int(request.POST['prefarea'])
		
		data = [bathroom,mr,gr,hwh,ac,pa]
		pickle_in=open('D:\scripts\web\python\django_ml\ml\lm.pkl','rb')
		
		model=pickle.load(pickle_in)
		res = model.predict([data])
		return HttpResponse(f"Price will be approx: {res}")
	return render(request, 'index.html')


from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import *
from .forms import *
from django.contrib import messages

from .models import *
from django.core.paginator import Paginator


def home(request):
	return render(request,'core/home.html')

def details(request,show_id):
	show = Show.objects.get(id=show_id)
	reviews=Review.objects.filter(show=show)
	context = {
	'show': show,
	'reviews': reviews,
	}
	return render(request,'core/details.html',context)

def profile(request, comedian_id, page_no):
	comedian = Comedian.objects.get(id=comedian_id)
	shows = comedian.show_set.all()
	pag = Paginator(shows,10)
	if page_no is None:
		page_no = 1;
	page_no = int(page_no)
	if page_no <= 0 or page_no > pag.num_pages:
		return redirect('profile', comedian_id=comedian_id) 
	lim_shows = pag.page(page_no)
	context = {
	 'shows' : lim_shows,
	 'comedian' : comedian,
	 'totPages': range(1,pag.num_pages+1),
	 'pno': page_no,
	 'cid': comedian_id,
	 'nextPage': page_no+1,
	 'prevPage': page_no-1,
	 'lastPage': pag.num_pages,
	}  


	return render(request, 'core/comedian.html', context)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()

            user=authenticate(username=username,password=password)
            if user is not None:
                if user.is_active:
                    login(request,user)

                    messages.success(request, f'Your account has been created!')
                    return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'core/register.html', {'form': form})


def shows(request, page_no):
	
	if request.method == 'GET':
		comedianName = request.GET.get('comedian')
		date = request.GET.get('date')
		city = request.GET.get('city')
		print(comedianName)
		print(date)
		print(city)

		c=0
		d=0
		ci=0

		if comedianName != '' and comedianName is not None:
			c=1
		if date != ''and date is not None:
			d=1
		if city != ''and city is not None:
			ci=1

		if c==1 and ci==1 and d==1:
			comedian = Comedian.objects.filter(name__icontains=comedianName)
			shows = Show.objects.none();
			for co in comedian:
				shows |= Show.objects.filter(comedian=co, city=city, date=date)

		if c==1 and ci==1 and d!=1:
			comedian = Comedian.objects.filter(name__icontains=comedianName)
			shows = Show.objects.none();
			for co in comedian:
				shows |= Show.objects.filter(comedian=co, city=city)

		if c==1 and ci!=1 and d==1:
			comedian = Comedian.objects.filter(name__icontains=comedianName)
			shows = Show.objects.none();
			for co in comedian:
				shows |= Show.objects.filter(comedian=co, date=date)

		if c==1 and ci!=1 and d!=1:
			comedian = Comedian.objects.filter(name__icontains=comedianName)
			shows = Show.objects.none();
			for co in comedian:
				shows |= Show.objects.filter(comedian=co)
			print(comedian)

		if c!=1 and ci==1 and d==1:
			shows = Show.objects.filter(city=city, date=date)

		if c!=1 and ci==1 and d!=1:
			shows = Show.objects.filter(city=city)

		if c!=1 and ci!=1 and d==1:
			shows = Show.objects.filter(date=date)

		if c!=1 and ci!=1 and d!=1:
			shows = Show.objects.all()


	if not shows:
		messages.warning(request,f'No Show found')


	pag = Paginator(shows,10)
	if page_no is None:
		page_no = 1;
	page_no = int(page_no)
	if page_no <= 0 or page_no > pag.num_pages:
		return redirect('shows') 
	lim_shows = pag.page(page_no)
	context = {
	 'shows' : lim_shows,
	 'totPages': range(1,pag.num_pages+1),
	 'pno': page_no,
	 'nextPage': page_no+1,
	 'prevPage': page_no-1,
	 'lastPage': pag.num_pages,
	}  

	return render(request, 'core/showlist.html', context)

def submitreview(request):
	if request.method=='POST':
		comment=request.POST['comment']
		show_id=request.POST['show']

		Review.objects.create(user=request.user.person,show=Show.objects.get(id=show_id),comment=comment)

		return render(request,'core/details.html')
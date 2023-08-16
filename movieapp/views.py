from django.shortcuts import render
from .models import movie
from.forms import movieform
from django.shortcuts import redirect
# Create your views here.
def mp3(request):
    Movie=movie.objects.all()
    info={
        "movie_list":Movie   }
    return render(request,"index.html",info)
def details(request,movie_id):
    mov=movie.objects.get(id=movie_id)
    
    return render(request,"details.html",{'movie':mov})
def add_movie(request):
    if request.method=="POST":
        name=request.POST.get("name",)
        desc=request.POST.get("desc",)
        year=request.POST.get("year",)
        image=request.FILES["image"]
        Movie=movie(name=name,desc=desc,year=year,image=image)
        Movie.save()

    return render(request,"add.html")
def update(request,id):
    Mov=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=Mov)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request,"edit.html",{'form':form,'movie':Mov})
def delete(request,id):
    if request.method=="POST":
        Movie=movie.objects.get(id=id)
        Movie.delete()
        return redirect('/')
    return render(request,"delete.html")


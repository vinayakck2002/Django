from django.shortcuts import render,redirect
from . models import Gallery

# Create your views here.
def viewsmain(request):
    if request.method == "POST":
        imgdef = request.FILES['files']  # Get the uploaded file from the request
        # print(imgdef)  # You can remove this print statement after testing
        
        # Create and save a new ImgForm object with the uploaded image
        obj = Gallery(classimages=imgdef)
        obj.save()
        return redirect(viewsmain)  # Redirect to the index view to refresh the page

    # Fetch all ImgForm objects to display the images
    imagefeeds = Gallery.objects.all()
    return render(request, "index.html", {"feeds": imagefeeds})

def delete(request,pk):
    imagefeeds=Gallery.objects.get(pk=pk)
    imagefeeds.delete()
    return redirect(viewsmain)

def add(request):
    return render(request,'imgadd.html')

def picture(request,id):
    imagefeeds=Gallery.objects.get(pk=id)
    feeds = imagefeeds.classimages.url
    return render(request,'images.html',{"feeds":feeds})




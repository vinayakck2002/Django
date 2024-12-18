from django.shortcuts import render, redirect
from .models import ImgForm

def index(request):
    if request.method == "POST" and request.FILES.get('files'):
        mainimage = request.FILES['files']  # Get the uploaded file from the request
        print(mainimage)  # You can remove this print statement after testing
        
        # Create and save a new ImgForm object with the uploaded image
        obj = ImgForm(main_image=mainimage)
        obj.save()
        
        return redirect(index)  # Redirect to the index view to refresh the page

    # Fetch all ImgForm objects to display the images
    feeds = ImgForm.objects.all()

    return render(request, "index.html", {"feeds": feeds})

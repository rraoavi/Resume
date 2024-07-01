from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404,HttpResponse
from .models import Resume
from .forms import ResumeForm
import io
from django.http import FileResponse
from django.template.loader import get_template
from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from pathlib import Path


# Create your views here.
def home(request):
    return render(request,"app/home.html")

def resume_form(request):
    if request.method=='POST':
        form= ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_detail', pk=form.instance.pk)
    else:
        form = ResumeForm()
    return render(request, 'app/resume_form.html', {'form': form})
def resume_detail(request,pk):
    resume= Resume.objects.get(pk=pk)
    context = {'resume': resume}
    return render(request,'app/resume_detail.html' ,context)

def download_jpg(request, pk):
    resume= Resume.objects.get(pk=pk)

    # Assuming you have a function to generate a JPG representation of the resume
    # Replace 'generate_jpg_resume' with the actual function name that generates JPG.
    jpg_content = generate_jpg_resume(resume)

    response = HttpResponse(content_type='image/jpeg')
    response['Content-Disposition'] = 'attachment; filename="resume.jpg"'

    response.write(jpg_content)
    return response

def generate_jpg_resume(resume):
    image_width = 800
    padding = 20
    line_height = 30

    resume_text = f"Name: {resume.name}\nEmail: {resume.email}\nExperience: {resume.experience}"
    num_lines = resume_text.count('\n') + 1
    image_height = padding * 2 + line_height * num_lines

    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    try:
        font_size = 20
        font_directory = Path(__file__).resolve().parent / 'fonts'
        font_path = str(font_directory / 'your_font_file.ttf')  # Adjust this according to your setup
        font = ImageFont.truetype(font_path, font_size)

        y = padding
        draw.text((padding, y), resume_text, font=font, fill='black')

        img_byte_arr = io.BytesIO()
        image.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)

        return img_byte_arr.getvalue()

    except OSError as e:
        print(f"Error loading font: {e}")
        return None  # Handle the error gracefully in your application


# def print_resume(request, pk):
#     resume= Resume.objects.get(pk=pk)

#     # Generate the printable HTML for the resume
#     template = get_template('app/printable_resume.html')
#     html_content = template.render({'resume': resume})

#     # Create PDF or send to printer, depending on your setup
#     # Here we assume direct printing to a printer, adjust as per your requirement

#     # For demonstration purpose, let's assume we send the HTML content directly to the browser
#     return HttpResponse(html_content, content_type='text/html')





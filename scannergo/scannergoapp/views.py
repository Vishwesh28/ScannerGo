from django.db.models.base import Model
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView
from django.http import Http404
from django.conf import settings
from scannergoapp.models import PicSubmission
from .forms import *
from .models import *
import os
#from settings import PROJECT_ROOT
from pathlib import Path
from scannergo.settings import MEDIA_ROOT
from django.templatetags.static import static
import subprocess, sys
from subprocess import Popen, PIPE
from subprocess import check_output
from platform import system


def get_open_command(filepath):
    """
    Get the console-like command to open the file
    for the current platform:
    - Windows: "start {{ filepath }}"
    - OS X: "open {{ filepath }}"
    - Linux based (wdg): "wdg-open {{ filepath }}"
    :param filepath:    Path to the file to be opened
    :type filepath:     string
    :return:            Command to run from a shell
    :rtype:             string
    """
#    if 'windows' in OSNAME:
    opener = 'start'
#    elif 'osx' in OSNAME or 'darwin' in OSNAME:
#        opener = 'open'
#    else:
#        opener = 'xdg-open'
    return '{opener} {filepath}'.format(opener=opener, filepath=filepath)

def subprocess_opener(filepath):
    """
    Method to open the file with the default program in a subprocess.
    As being called in a subprocess, it will not block the current one.
    This method runs the command on a subprocess using the default system shell.
    Check the docs of subprocess module for more info:
    https://docs.python.org/2/library/subprocess.html#subprocess.Popen
    The subprocess will run in background so you won't be able to bring back
    the result code, but the current log can be obtained via the Popen's PIPE:
    Usage:
    ```
    # Run as subprocess
    subproc = subprocess_opener(filepath)
    # Get the stdout for the subprocess
    print(subproc.stdout)
    # Get the stderr for the subprocess
    print(subproc.stderr)
    ```
    :type filepath:     string
    :param filepath:    Path to the file to open
    :rtype:             subprocess
    :return:            The pointer the subprocess returned by the Popen call
    """
    subproc = Popen(
        get_open_command(filepath),
        stdout=PIPE, stderr=PIPE, shell=True
    )
    subproc.wait()
    return subproc

class PicSubmissionView(CreateView):
    template_name = 'home.html'
    form_class = PicSubmissionForm
    success_url='connect'
#    def get_success_url(self):
#        return self.request.path
#    def get_success_url(self):
#        return reverse('display', kwargs={'home': self.kwargs['home']})

#    def form_valid(self, form):
#        form.instance.user = self.request.user
#        return super(AssignmentSubmissionView, self).form_valid(form)

#    def post(self, request, *args, **kwargs):
#        self.object = None
#        form = self.get_form()
#        if form.is_valid():
#            return self.form_valid(form)
#        else:
#            return self.form_invalid(form)

#class DisplayView(CreateView):
#    template_name = 'display.html'
#    form_class = PicSubmissionForm
#    model = PicSubmission

#    PicSubmission.delete()

def delete(self):
    P = os.path.join(MEDIA_ROOT, 'input_image.jpg')
    P2 = os.path.join(MEDIA_ROOT, 'Magic.jpeg')
    P3 = os.path.join(MEDIA_ROOT, 'input_code.exe')
    P4 = os.path.join(MEDIA_ROOT, 'Gaussian.jpeg')
    P5 = os.path.join(MEDIA_ROOT, 'Triangle.jpeg')
    try:
        subprocess.call(['rm', P])
        subprocess.call(['rm', P2])
        subprocess.call(['rm', P3])
        subprocess.call(['rm', P4])
        subprocess.call(['rm', P5])
    except:
        print('NULL')   
    return redirect('first')     
#    try:
#        shutil.rmtree(P)
#    except
#    os.rmdir(P)
#    documents = PicSubmission.objects.all()
#    for document in documents:
#        document.delete()
#    success_url='display'

#def delete_pics(request, pk):
#    if request.method == 'POST':
#        pic = PicSubmission.objects.get(pk=pk)
#        pic.delete()
#    return redirect('first') 

class midView(CreateView):
    form_class = PicSubmissionForm
    template_name = 'mid.html'

def getoutput(self):
    P = os.path.join(MEDIA_ROOT, 'input_code.exe')
    print(P)
#    subprocess.call(['chmod', '777', P])
#    subprocess.call(['chmod', '777', P])
    os.system('chmod 777 '+ P)
    os.system(P)
#    subprocess.call([P])
#    get_open_command(P)
#    subprocess_opener(P)
#    c = subprocess.Popen([P])
#    returncode = c.wait()
#    os.startfile(P)
#    opener = "open" if sys.platform == "darwin" else "xdg-open"
#    subprocess.call([opener, P])
    return redirect('pic-submission')
    
def index(request):
    path = settings.MEDIA_ROOT
    img_list = os.listdir(path)
    context = {'images' : img_list}
    return render(request, "display.html", context)    
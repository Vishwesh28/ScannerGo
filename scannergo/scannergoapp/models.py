from django.db import models
from django.utils import timezone

# Create your models here.
#from django.contrib.auth.models import AbstractUser

#from .managers import UserManager


# CUSTOM USER MODEL
    
import os

from scannergo.settings import BASE_DIR
from scannergo.settings import MEDIA_ROOT

def content_file_name(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % ('input', 'image', 'jpg')
#        P = os.path.join(MEDIA_ROOT, 'submissions')
        return (filename)
    
def content_file_name2(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s_%s.%s" % ('input', 'code', ext)
#        P = os.path.join(MEDIA_ROOT, 'code')
        return (filename)    
    

class PicSubmission(models.Model):
#    file = models.FileField(upload_to='submissions/',null=True, blank=True)
    Pic = models.ImageField(upload_to=content_file_name)
    Code = models.FileField(upload_to=content_file_name2)
#    def delete(self, *args, **kwargs):
#        P = os.path.join(MEDIA_ROOT, 'submissions')
#        os.rmdir(P)
#        super(PicSubmission,self).delete(*args,**kwargs)
    
    
    
#def delete(self, *args, **kwargs):
#    ext = self.file.name.split('.')[-1]
#    filename = "%s_%s.%s" % ('input', 'image', ext)
#    P = os.path.join(MEDIA_ROOT, 'submissions')
#    os.remove(os.path.join(P, filename))
#    super(PicSubmission,self).delete(*args,**kwargs)    

#    def __str__(self):
#        return '{}:{}'.format(str(self.Assignment),str(self.user))
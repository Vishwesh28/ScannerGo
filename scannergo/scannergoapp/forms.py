from django import forms

from .models import *


class PicSubmissionForm(forms.ModelForm):
    class Meta:
        model= PicSubmission
        fields = ['Pic','Code']
        
#class FileFieldForm(forms.ModelForm):       
#    class Meta: 
#        model= PicSubmission
#    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs=
#        {'multiple': True, 'webkitdirectory': True, 'directory': True}))    

#    def is_valid(self):
#        valid = super(AssignmentSubmissionForm, self).is_valid()

        # if already valid, then return True
#        if valid:
#            return valid
#        return valid

#    def save(commit=True):
#        course = super(AssignmentSubmissionForm).save(commit=False)
#        if commit:
#            course.save()
#        return course
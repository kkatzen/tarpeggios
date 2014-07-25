from django import forms
  
 
#class UploadFileForm(forms.ModelForm):
#     
 #   class Meta:
  #      model = UploadFile

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
    name = forms.CharField(
        label='Give it a name'
    )

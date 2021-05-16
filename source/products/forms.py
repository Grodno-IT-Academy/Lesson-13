from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label="Product Name", max_length=255)
    price = forms.DecimalField(max_digits=10000,decimal_places=2)
    description = forms.CharField(max_length=10000,label="Long Description",widget=forms.Textarea)
    short = forms.CharField(label="Short Description",max_length=400)
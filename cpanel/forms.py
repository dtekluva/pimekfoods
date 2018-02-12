from django import forms
from django.contrib.auth.models import User
from store.models import Customers, Product


class CustomersForm(forms.ModelForm):


    email    = forms.EmailField(max_length=128,
                           help_text="Please enter the your email.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model   = Customers
        fields  = ('email',)


class ProductForm(forms.ModelForm):
  
    name         = forms.CharField(max_length=30, required=False,
                            help_text="Name     ::")
    price        = forms.IntegerField(initial=0, required=False)
    image        = forms.FileField(required=False)
    prod_id      = forms.IntegerField(required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model   = Product
        fields  = ('name' ,'price', 'image','prod_id')

class EditproductForm(forms.ModelForm):
  
    new_name         = forms.CharField(max_length=30, required=False,
                            help_text="Name     ::")
    price        = forms.IntegerField(initial=0, required=False)
    image        = forms.FileField(required=False)
    prod_id      = forms.IntegerField(required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model   = Product
        fields  = ('new_name' ,'price', 'image','prod_id')

# class CommentForm(forms.ModelForm):

#     title       = forms.CharField(max_length=128, help_text="Enter Title :: ")

#     body        = forms.CharField(max_length=300, help_text="Comment ::")

#     image       = forms.FileField(required=False)

    
#     class Meta:
#         # Provide an association between the ModelForm and a model

#         model = Comment

#         fields  = ('title','body','image')
      

# class SearchForm(forms.ModelForm):
#     name   = forms.CharField(max_length=128,
#                             help_text="Please enter product name.")

#     class Meta:
#         # Provide an association between the ModelForm and a model
#         model   = Product
#         fields  = ('name',)
    

# # class UserAccountForm(forms.ModelForm):
# #     phone = forms.CharField(max_length=246)
# #     occupation = forms.CharField(max_length=13)
# #     class Meta:
# #         model = UserAccount
# #         fields = ('phone', 'occupation')

# class UserRegistrationForm(forms.ModelForm):
#     username    = forms.CharField(max_length=256, widget=forms.TextInput(), help_text="UserName     ::")
#     first_name  = forms.CharField(max_length=256, help_text="First name     ::")
#     last_name   = forms.CharField(max_length=256, help_text="Last name     ::")
#     email       = forms.CharField(max_length=256, widget=forms.EmailInput(), help_text="Email addr    ::")
#     password    = forms.CharField(max_length=256, widget=forms.PasswordInput(), help_text="Password    ::")
#     image       = forms.FileField(required=False)

#     class Meta:
#         model = UserAccount
#         fields = ('username', 'first_name', 'last_name', 'email', 'password', 'image')

class Signinform(forms.ModelForm):
    username   =   forms.CharField(max_length=256, widget=forms.EmailInput())
    password=   forms.CharField(max_length=256, widget=forms.PasswordInput())

    class Meta:
        model = User
        fields= ('username','password' )
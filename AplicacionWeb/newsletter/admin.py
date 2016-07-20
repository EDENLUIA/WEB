from django.contrib import admin
from .forms import SignUpForm

from  .models import SignUp

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp","updated"]
	#class Meta:
		#model=SignUp
	form = SignUpForm


admin.site.register(SignUp,SignUpAdmin)


# Register your models here.

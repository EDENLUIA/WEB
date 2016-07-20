from django.shortcuts import render,render_to_response,RequestContext

def about(request):
	context = {
		

		}
	return render(request,"about.html",context)
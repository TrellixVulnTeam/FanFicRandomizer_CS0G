from django.shortcuts import render, render_to_response

# Create your views here.
def index(response):
	return render_to_response('index.html')
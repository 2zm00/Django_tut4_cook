from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
# Create your views here.

def review_index(request):
	reviews = Review.objects.all().order_by('-created_at')
	context = {
		'reviews': reviews
	}
	return render(request, 'review/index.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'review/review_detail.html', {'review': review})

def review_create_page(request):
	return render(request, 'review/review_create.html')

def review_create(request):
    if request.method == 'POST':
        title = request.POST.get('review_title')
        content = request.POST.get('review_content')
        
        if title and content:
            Review.objects.create(title=title, content=content)
            return redirect('review:review_index')
    return render(request, 'review/review_create.html')
from django.shortcuts import render
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    # print(request)

    q = request.GET.get('q','')
    if q:
        
        #FTS ignores articles and single words

        '''
        simple full text search on a single field

        1. for searching on only and only 1 field
        2. blues, blueing ..
        '''
        # products = products.filter(description__search=q)
    

        '''
        full text search using postgres module (Using SearchVector only)
        '''
        # vector = SearchVector('name','description')
        # query = q
    
        # products = products.annotate(search = vector).filter(search=query)

        '''
        full text search using postgres module (Using SearchVector and SearchQuery only)
        '''
        # vector = SearchVector('name','description')
        # query = SearchQuery(q)

        # products = products.annotate(search = vector).filter(search=query)

        '''
        full text search using postgres module (Using SearchVector and SearchQuery and SearchRank)
        '''
        # vector = SearchVector('name','description')
        # query = SearchQuery(q)
        # rank = SearchRank(vector,query)

        # products = products.annotate(rank = rank).filter(rank__gte=0.001).order_by('-rank')

        '''
        full text search using postgres module (Using SearchVector and SearchQuery and SearchRank)
        with ranking
        '''
        vector = (
            SearchVector('name', weight='B') +
            SearchVector('description', weight='A')
            SearchVector('color', weight='C') +
            SearchVector('gender', weight='D')
            )
        query = SearchQuery(q)
        rank = SearchRank(vector,query)

        products = products.annotate(rank = rank).filter(rank__gte=0.001).order_by('-rank')

        print(vector)
        print(query)
        print(rank)
    
    context = {
        'products': products,
        'q':q,
    }
    return render(request,'index.html',context)
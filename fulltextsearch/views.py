from django.shortcuts import render
from django.contrib.postgres.search import (SearchQuery, SearchVector, SearchRank, 
                                            SearchHeadline, TrigramSimilarity)
from .models import *
from django.db.models import Q
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
        # vector = (
        #     SearchVector('name', weight='B') +
        #     SearchVector('description', weight='A') +
        #     SearchVector('color', weight='C') +
        #     SearchVector('gender', weight='D')
        #     )
        # # query = SearchQuery(q, search_type="phrase")
        
        # # Dynamically query generator

        # search_terms = q.split()
        # query = SearchQuery(search_terms[0])
        # # Loop through remaining terms and combine with OR operator
        # if len(search_terms) > 1:
        #     for term in search_terms[1:]:
        #         query &= SearchQuery(term)

        # # # query =  SearchQuery("bag") | SearchQuery("women")


        # rank = SearchRank(vector,query)

        # products = products.annotate(rank = rank).filter(rank__gte=0.001).order_by('-rank')

        '''
        full text search using postgres module (Using SearchVector and SearchQuery and SearchRank)
        with ranking and searchheadline
        '''
        vector = (
            SearchVector('name', weight='B') +
            SearchVector('description', weight='A') +
            SearchVector('color', weight='C') +
            SearchVector('gender', weight='D')
            )
        query = SearchQuery(q)
        search_headline = SearchHeadline('description',query)

        rank = SearchRank(vector,query)

        products = products.annotate(
            rank = rank,
            search_headline = search_headline
            ).filter(rank__gte=0.001).order_by('-rank')

        print(vector)
        print(query)
        print(rank)
        print(search_headline)
    
    context = {
        'products': products,
        'q':q,
    }
    return render(request,'index.html',context)



def trigramsearch(request):

    products = Product.objects.all()

    q = request.GET.get('q','')
    if q:
        vector = (
            SearchVector('name', weight='B') +
            SearchVector('description', weight='A') +
            SearchVector('color', weight='C') +
            SearchVector('gender', weight='D')
            )
        query = SearchQuery(q)
        rank = SearchRank(vector,query)

        Q_expression = Q(similarity__gte=0.1) & Q(rank__gte=0.1)
        
        products = products.annotate(
            rank = rank,
            similarity = TrigramSimilarity('name',q) + 
                        TrigramSimilarity('description',q) +
                        TrigramSimilarity('brand',q) +
                        TrigramSimilarity('color',q)
        ).filter(Q_expression).order_by('-rank','-similarity',)

    context = {
        'products': products,
        'q':q,
    }
    return render(request, 'trigram_search.html', context)
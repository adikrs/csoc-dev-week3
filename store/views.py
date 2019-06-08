from django.shortcuts import render
import datetime
from django.shortcuts import get_object_or_404
from store.models import *
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.



def index(request):
    return render(request, 'store/index.html')

def bookDetailView(request, bid):
    template_name='store/book_detail.html'
    context={
        #'book':book[bid-1], # set this to an instance of the required book #trying dummy books
       # 'num_available':1, # set this 1 if any copy of this book is available, otherwise 0
           'book':None,
           'num_available':None,

    }
    # START YOUR CODE HERE
    qp=Book.objects.get(id=bid)
    context['book']= qp

    try:
        present = BookCopy.objects.get(book = qp)
        context['num_available']=0
    except:
        context['num_available']=1   
    
    return render(request,template_name, context=context)


def bookListView(request):
    template_name='store/book_list.html'
    get_data=request.GET
    # START YOUR CODE HERE

    ons = Book.objects.all().order_by('rating')
    context={
    'books':ons,
    }

    return render(request,template_name, context=context)

@login_required
def viewLoanedBooks(request):
    template_name='store/loaned_books.html'
    takex = BookCopy.objects.filter(borrower=request.user).filter(status='False')
    context={
        'books':takex,
    }

    '''
    The above key books in dictionary context should contain a list of instances of the 
    bookcopy model. Only those books should be included which have been loaned by the user.
    '''
    # START YOUR CODE HERE

    return render(request,template_name,context=context)

@csrf_exempt
@login_required
def rating_bookView(request):
    rating = request.POST['rating']
    template_name='store/book_detail.html'
    response_data={
             'message':1,                        #sum=float()+
         }

    book_id = request.POST.get("bid")
    co = Book.objects.get(id=book_id);
    co.num_rating = co.num_rating + float(rating);
    co.total_user = co.total_user + int(1);
    co.rating = float(co.num_rating / co.total_user);
    co.save();

    return JsonResponse(response_data)




@csrf_exempt
@login_required
def loanBookView(request):
    response_data={
     

        'message' : None,

    }
    '''
    Check if an instance of the asked book is available.
    If yes, then set message to 'success', otherwise 'failure'
    '''
    # START YOUR CODE HERE
   # my  book_id = response_data # get the book id from post data
    
    #if Book.objects.filter(id='request.POST.get("bid")').filter(status='1')
    book_id = request.POST.get("bid")
    response_data['message'] = 'failure'
    ad = Book.objects.get(id = book_id)
    try:
        temp = BookCopy.objects.get(book = Book.objects.get(id = book_id))
    except:
        response_data['message'] = 1
        BookCopy.objects.create(borrower = request.user,book = ad, borrow_date = datetime.datetime.now().date() )

    return JsonResponse(response_data)

'''
FILL IN THE BELOW VIEW BY YOURSELF.
This view will return the issued book.
You need to accept the book id as argument from a post request.
You additionally need to complete the returnBook function in the loaned_books.html file
to make this feature complete
''' 
@csrf_exempt
@login_required
def returnBookView(request):

    response_data = {

         'message': None,
    }
    book_id = request.POST.get("bid")  # get the book id from post data
  
    lks = Book.objects.get(id = book_id)
    BookCopy.objects.filter(book = lks).update(
        status=True, borrow_date=None, borrower=None)
    BookCopy.objects.filter(book =lks).delete()
    response_data['message'] = 1
    return JsonResponse(response_data)



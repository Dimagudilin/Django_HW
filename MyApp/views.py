from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

mylist = {
    'pages': [
        {'title': 'Товары', 'id': 1},
        {'title': 'Гарантии', 'id': 2},
        {'title': 'FAQ', 'id': 3},
    ],
    'items': [
        {'title': 'Хлебушек', 'Price': '40',' discount': '15', 'address': ' FakeAdress229','type': '0','url' :'https://static10.tgstat.ru/channels/_0/f8/f810bd4bc3f89583bb6943cdadbce3e5.jpg'},
        {'title': 'Водичка', 'Price': '34', ' discount': '0', 'address': ' FakeAdress229', 'type': '1','url':'https://s00.yaplakal.com/pics/pics_original/2/2/1/11053122.jpg'},
        {'title': 'Бананы', 'Price': '56', ' discount': '15', 'address': ' FakeAdress229','type': '2', 'url':'https://images.lady.mail.ru/454593/'},
        {'title': 'Пирожки', 'Price': '32', ' discount': '15', 'address': ' FakeAdress229','type': '0', 'url':'data:image/jpeg;base64,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'},
        {'title': 'Сок', 'Price': '33', ' discount': '15', 'address': ' FakeAdress229', 'type': '1','url':'http://www.dobry.ru/assets-new/images/products/multifruit/image-2.png'}
    ]
}
##def (request):
##    return HttpResponse('this is function view')
def NavViews(request, nav_id):
    print('goodbye')
    return render(request, nav_id+'.html', mylist)

##class NavViews(View):
##    def get(self, request, title):
 ##       return render(request, 'Товары.html')

#class ExampleClass(View):
#    def get(self, request):
#        return HttpResponse('this is class')
class ExampleClass(View):
    def get(self, request):
        print('hello')
        return render(request, 'main.html', mylist)
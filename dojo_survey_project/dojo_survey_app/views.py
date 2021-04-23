from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print('index view method', request.method)
    return render(request, 'index.html')


def results(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        age = request.POST['age']
        location = request.POST['location']
        language = request.POST['language']
        # print('comment', request.POST['comment'])
        comment = request.POST['comment']
        context = {
            'firstname': firstname,
            'lastname': lastname,
            'age': age,
            'location': location,
            'language': language,
            'comment': comment

        }
        return render(request, 'results.html', context)
        # print('request.POST:', request.POST)
        # print(request.POST['firstname'], request.POST['lastname'])
        # print('method', request.method)
    return HttpResponse(request)

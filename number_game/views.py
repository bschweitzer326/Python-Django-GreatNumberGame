from django.shortcuts import render, redirect

import random

def root(request):
    if 'color' not in request.session: request.session['color'] = ''

    if 'count' not in request.session: request.session['count'] = 0

    if 'results' not in request.session: request.session['results'] = ''

    if 'rand' not in request.session:
        request.session['rand'] = random.randint(1, 100)
    print(request.session['rand'])

    context = {
        'results' : request.session['results'],
        'count' : request.session['count'],
        'color' : request.session['color'],
    }

    return render(request,'number_game.html', context)

def guess(request):
    print(request.POST)

    request.session['count'] += 1

    if int(request.POST['number']) < request.session['rand']:
        print('Too Low!')
        request.session['results'] = 'Too Low! \n'
        request.session['color'] = '#cf2a27'
    
    elif int(request.POST['number']) > request.session['rand']:
        print('Too High!')
        request.session['results'] = 'Too High! \n'
        request.session['color'] = '#cf2a27'
    
    else:
        print('was the number!')
        request.session['results'] = 'You got it! \n'
        request.session['color'] = '#009e0f'

    return redirect('/')

def reset(request):
    del request.session['results']
    del request.session['rand']
    del request.session['count']
    del request.session['color']
    return redirect("/")

# def leader(request):

#     return
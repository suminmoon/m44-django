from django.shortcuts import render
import random
from datetime import datetime
import requests
# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def dinner(request):
    menu = ['순대국밥', '쌀국수', '햄버거', '곱창']
    choice = random.choice(menu)

    return render(request, 'pages/dinner.html', {'dinner': choice})


def greeting(request, name):
    return render(request, 'pages/greeting.html', {'name': name})


def introduce(request, name, age):
    return render(request, 'pages/introduce.html', {'name': name, 'age':age})


def template_language(request):
    menus = ['자장면', '짬뽕', '볶음밥', '탕수육', '칠리새우']
    messages = ['apple', 'banana', 'mango', 'cucumber']
    my_sentence = 'Life is short, you need python'
    datetimenow = datetime.now()
    empty_list = []

    context = {

        'menus': menus,
        'messages': messages,
        'my_sentence': my_sentence,
        'datetimenow': datetimenow,
        'empty_list': empty_list,

    }

    return render(request, 'pages/template_language.html', context)


def throw(request):
    return render(request, 'pages/throw.html')


def catch(request):
    message = request.GET.get('message')
    message2 = request.GET.get('message2')
    context = {'message': message, 'message2': message2}
    return render(request, 'pages/catch.html', context)


def artii(request):
    return render(request, 'pages/artii.html')


def result(request):

    # 1. form 태그로 날린 데이터르 받는다.
    word = request.GET.get('word')

    # 2. ARTII  api 로 요청을 보내 응답결과를 text 로 fonts 에 저장한다.
    #     (fonts 를 받는다.)
    api_url = 'http://artii.herokuapp.com'
    fonts = requests.get(f'{api_url}/fonts_list').text

    # 3. fonts(str) 를 font_list(list) 으로 바꾼다.
    font_list = fonts.split('\n')

    # 4.  random 으로 font 1개를 선택해서 font 라는 변수에 저장한다.
    font = random.choice(font_list)

    # 5. 1번에서 받은 word 와 font 로 다시 요청을 보내서 응답 결과를
    #    result 라는 변수에 저장한다.
    ascii_result = requests.get(f'{api_url}/make?text={word} &font={font}').text

    # 6. result 에 담긴 문자열을 result.html 로 넘겨준다.
    context = {'result':ascii_result, 'font': font}
    return render(request, 'pages/result.html', context)


def static_example(request):
    return render(request, 'pages/static_example.html')




from django.shortcuts import render

def calculator(request):
    result = None

    if request.method == 'POST':
        a = float(request.POST.get('a'))
        b = float(request.POST.get('b'))
        operation = request.POST.get('operation')

        if operation == 'add':
            result = a + b
        elif operation == 'sub':
            result = a - b
        elif operation == 'mul':
            result = a * b
        elif operation == 'div':
            if b != 0:
                result = a / b
            else:
                result = 'Помилка: ділення на нуль'

    return render(request, 'calculator/index.html', {'result': result})
from flask import Blueprint, render_template, request, redirect, url_for

lab2 = Blueprint('lab2', __name__)

@lab2.route('/lab2/a')
def a():
    return 'без слеша'

@lab2.route('/lab2/a/')
def a2():
    return 'со слешем'

flowers = [
    {"name": "Роза", "price": 100},
    {"name": "Тюльпан", "price": 70},
    {"name": "Подсолнух", "price": 50},
    {"name": "Лилия", "price": 80}
]

@lab2.route('/lab2/add_flower/', methods=['GET', 'POST'])
def add_flower():
    if request.method == 'POST':
        name = request.form['name']
        price = int(request.form['price'])
        flowers.append({"name": name, "price": price})
        return redirect(url_for('lab2.list_flowers'))
    return render_template('lab2/add_flower.html')

@lab2.route('/lab2/flowers')
def list_flowers():
    return render_template('lab2/list_flowers.html', flowers=flowers)

@lab2.route('/lab2/flowers/<int:flower_id>')
def flower(flower_id):
    if 0 <= flower_id < len(flowers):
        return render_template('lab2/flower.html', flower=flowers[flower_id], flowers=flowers)
    return 'Нет такого цветка', 404

@lab2.route('/lab2/clear_flowers')
def clear_flowers():
    global flowers
    flowers = []
    return redirect(url_for('lab2.list_flowers'))

@lab2.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    if 0 <= flower_id < len(flowers):
        del flowers[flower_id]
        return redirect(url_for('lab2.list_flowers'))
    return 'Нет такого цветка', 404

@lab2.route('/lab2/')
def lab2_main():
    name = 'Мартынов Александр'
    lab_num = '2'
    curs_num = '3'
    group = 'ФБИ-24'
    fruits = [
        {'name': 'Яблоко', 'price': 100},
        {'name': 'Банан', 'price': 70},
        {'name': 'Апельсин', 'price': 120},
        {'name': 'Манго', 'price': 200}
    ]
    return render_template('lab2/lab2.html', name=name, lab_num=lab_num, curs_num=curs_num, group=group, fruits=fruits)

@lab2.route('/lab2/filter')
def filter_example():
    phrase = "сколько нам открытий чудных готовит просвещенья дух"
    return render_template('lab2/filter.html', phrase=phrase)

@lab2.route('/lab2/calc/')
def calc_default():
    return redirect(url_for('lab2.calc', a=1, b=1))

@lab2.route('/lab2/calc/<int:a>')
def calc_single(a):
    return redirect(url_for('lab2.calc', a=a, b=1))

@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum_result = a + b
    diff_result = a - b
    prod_result = a * b
    div_result = a / b if b != 0 else 'Ошибка: деление на ноль'
    pow_result = a ** b
    return render_template('lab2/calc.html', a=a, b=b, sum_result=sum_result, diff_result=diff_result, prod_result=prod_result, div_result=div_result, pow_result=pow_result)

@lab2.route('/lab2/books')
def list_books():
    books = [
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Научная фантастика", "pages": 328},
    {"author": "Рэй Брэдбери", "title": "451 градус по Фаренгейту", "genre": "Научная фантастика", "pages": 158},
    {"author": "Федор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 671},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432},
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Фантастика", "pages": 448},
    {"author": "Эрих Мария Ремарк", "title": "Три товарища", "genre": "Роман", "pages": 480},
    {"author": "Габриэль Гарсиа Маркес", "title": "Сто лет одиночества", "genre": "Магический реализм", "pages": 448},
    {"author": "Роберт Грин", "title": "48 законов власти", "genre": "Саморазвитие", "pages": 496},
    {"author": "Стивен Кинг", "title": "Оно", "genre": "Ужасы", "pages": 1138},
    {"author": "Агата Кристи", "title": "Убийство в Восточном экспрессе", "genre": "Детектив", "pages": 256}
    ]
    return render_template('lab2/books.html', books=books)

@lab2.route('/lab2/berries')
def list_berries():
    berries = [
    {"name": "Клубника", "description": "Сладкая и сочная ягода, популярная в десертах.", "image": "strawberry.jpg"},
    {"name": "Черника", "description": "Меньше по размеру, чем Голубика, но с более интенсивным вкусом.", "image": "blueberry.jpg"},
    {"name": "Ежевика", "description": "Спелая ежевика имеет сладкий вкус и используется в варенье и компотах.", "image": "blackberry.png"},
    {"name": "Голубика", "description": "Богатая антиоксидантами ягода, используемая в салатах и десертах.", "image": "cranberry.jpg"},
    {"name": "Малина", "description": "Сладкая и кислая ягода, популярная в десертах и напитках.", "image": "raspberry.jpg"}
    ]
    return render_template('lab2/berries.html', berries=berries)
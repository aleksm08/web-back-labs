from flask import Blueprint, render_template, request, make_response, redirect, url_for

lab3 = Blueprint('lab3', __name__)

# Список товаров (смартфоны)
products = [
    {"name": "iPhone 13", "price": 999, "brand": "Apple", "memory": "128GB"},
    {"name": "Samsung Galaxy S21", "price": 899, "brand": "Samsung", "memory": "128GB"},
    {"name": "Google Pixel 6", "price": 699, "brand": "Google", "memory": "128GB"},
    {"name": "OnePlus 9", "price": 799, "brand": "OnePlus", "memory": "128GB"},
    {"name": "Xiaomi Mi 11", "price": 699, "brand": "Xiaomi", "memory": "128GB"},
    {"name": "Sony Xperia 1 III", "price": 1199, "brand": "Sony", "memory": "256GB"},
    {"name": "Huawei P40 Pro", "price": 899, "brand": "Huawei", "memory": "256GB"},
    {"name": "LG Velvet", "price": 599, "brand": "LG", "memory": "128GB"},
    {"name": "Motorola Edge", "price": 699, "brand": "Motorola", "memory": "256GB"},
    {"name": "Nokia 8.3", "price": 499, "brand": "Nokia", "memory": "128GB"},
    {"name": "Oppo Find X3 Pro", "price": 1099, "brand": "Oppo", "memory": "256GB"},
    {"name": "Realme GT", "price": 599, "brand": "Realme", "memory": "128GB"},
    {"name": "Vivo X60 Pro", "price": 799, "brand": "Vivo", "memory": "256GB"},
    {"name": "ZTE Axon 30", "price": 499, "brand": "ZTE", "memory": "128GB"},
    {"name": "Asus ROG Phone 5", "price": 999, "brand": "Asus", "memory": "256GB"},
    {"name": "BlackBerry Key2", "price": 699, "brand": "BlackBerry", "memory": "128GB"},
    {"name": "HTC U12+", "price": 599, "brand": "HTC", "memory": "128GB"},
    {"name": "Lenovo Legion Phone Duel", "price": 899, "brand": "Lenovo", "memory": "256GB"},
    {"name": "Meizu 18", "price": 699, "brand": "Meizu", "memory": "128GB"},
    {"name": "TCL 20 Pro 5G", "price": 499, "brand": "TCL", "memory": "256GB"}
]

@lab3.route('/lab3/')
def lab3_main():
    name = request.cookies.get('name') or 'аноним'
    age = request.cookies.get('age') or 'неизвестный'
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, age=age, name_color=name_color)

@lab3.route('/lab3/cookie/', methods=['GET', 'POST'])
def set_cookie():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        name_color = request.form.get('name_color')

        response = make_response(redirect(url_for('lab3.lab3_main')))
        response.set_cookie('name', name, max_age=5)  # Куки будут жить 5 секунд
        response.set_cookie('age', age)
        response.set_cookie('name_color', name_color)
        return response

    return '''
        <form method="post">
            <label for="name">Имя:</label>
            <input type="text" id="name" name="name" required>
            <br>
            <label for="age">Возраст:</label>
            <input type="text" id="age" name="age" required>
            <br>
            <label for="name_color">Цвет текста:</label>
            <input type="text" id="name_color" name="name_color" required>
            <br>
            <button type="submit">Установить куки</button>
        </form>
    '''

@lab3.route('/lab3/clear_cookies/')
def clear_cookies():
    response = make_response(redirect(url_for('lab3.lab3_main')))
    response.delete_cookie('name')
    response.delete_cookie('age')
    response.delete_cookie('name_color')
    return response

@lab3.route('/lab3/form1', methods=['GET'])
def form1():
    user = request.args.get('user') or ''
    age = request.args.get('age') or ''
    sex = request.args.get('sex') or ''

    errors = {}
    if not user:
        errors['user'] = 'Заполните поле!'

    sex_ru = 'Не указан'
    if sex == 'male':
        sex_ru = 'Мужской'
    elif sex == 'female':
        sex_ru = 'Женский'

    return render_template('lab3/form1.html', user=user, age=age, sex=sex, sex_ru=sex_ru, errors=errors)

@lab3.route('/lab3/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        drink = request.form.get('drink')
        milk = 'milk' in request.form
        sugar = 'sugar' in request.form

        price = 0
        if drink == 'coffee':
            price = 120
        elif drink == 'black-tea':
            price = 80
        elif drink == 'green-tea':
            price = 70

        if milk:
            price += 30
        if sugar:
            price += 10

        return render_template('lab3/pay.html', price=price)

    return render_template('lab3/order.html')

@lab3.route('/lab3/pay', methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        card_number = request.form.get('card')
        card_name = request.form.get('name')
        card_cvv = request.form.get('cvv')

        # Здесь можно добавить логику проверки данных карты

        return render_template('lab3/success.html', price=request.form.get('price'))

    price = request.args.get('price')
    return render_template('lab3/pay.html', price=price)

@lab3.route('/lab3/settings', methods=['GET', 'POST'])
def settings():
    color = request.cookies.get('color')
    background_color = request.cookies.get('background_color')
    font_size = request.cookies.get('font_size')

    if request.method == 'POST':
        new_color = request.form.get('color')
        new_background_color = request.form.get('background_color')
        new_font_size = request.form.get('font_size')

        response = make_response(redirect(url_for('lab3.settings')))
        if new_color:
            response.set_cookie('color', new_color)
        if new_background_color:
            response.set_cookie('background_color', new_background_color)
        if new_font_size:
            response.set_cookie('font_size', new_font_size + 'px')  # Добавляем 'px' к значению размера шрифта

        return response

    return render_template('lab3/settings.html', color=color, background_color=background_color, font_size=font_size)

@lab3.route('/lab3/clear_all_cookies/')
def clear_all_cookies():
    response = make_response(redirect(url_for('lab3.lab3_main')))
    response.delete_cookie('name')
    response.delete_cookie('age')
    response.delete_cookie('name_color')
    response.delete_cookie('color')
    response.delete_cookie('background_color')
    response.delete_cookie('font_size')
    return response

@lab3.route('/lab3/ticket', methods=['GET', 'POST'])
def ticket():
    if request.method == 'POST':
        fio = request.form.get('fio')
        age = int(request.form.get('age'))
        bunk = request.form.get('bunk')
        bedding = 'bedding' in request.form
        baggage = 'baggage' in request.form
        departure = request.form.get('departure')
        destination = request.form.get('destination')
        date = request.form.get('date')
        insurance = 'insurance' in request.form

        errors = {}
        if not fio:
            errors['fio'] = 'Заполните поле!'
        if age < 1 or age > 120:
            errors['age'] = 'Возраст должен быть от 1 до 120 лет!'
        if not departure:
            errors['departure'] = 'Заполните поле!'
        if not destination:
            errors['destination'] = 'Заполните поле!'
        if not date:
            errors['date'] = 'Заполните поле!'

        if errors:
            return render_template('lab3/ticket_form.html', errors=errors)

        base_price = 700 if age < 18 else 1000
        if bunk in ['lower', 'lower_side']:
            base_price += 100
        if bedding:
            base_price += 75
        if baggage:
            base_price += 250
        if insurance:
            base_price += 150

        return render_template('lab3/ticket.html', fio=fio, age=age, bunk=bunk, bedding=bedding, baggage=baggage, departure=departure, destination=destination, date=date, insurance=insurance, price=base_price)

    return render_template('lab3/ticket_form.html', errors={})

@lab3.route('/lab3/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        min_price = float(request.form.get('min_price', 0))
        max_price = float(request.form.get('max_price', float('inf')))

        filtered_products = [product for product in products if min_price <= product['price'] <= max_price]
        return render_template('lab3/search_results.html', products=filtered_products)

    return render_template('lab3/search_form.html')
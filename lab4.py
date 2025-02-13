from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from PIL import Image, ImageDraw, ImageFont
import os

# Создание Blueprint
lab4 = Blueprint('lab4', __name__)

tree_count = 0

# Массив для хранения пользователей
users = []

@lab4.route('/lab4/')
def lab4_main():
    return render_template('lab4/lab4_main.html')

@lab4.route('/sum', methods=['GET', 'POST'])
def sum_page():
    if request.method == 'POST':
        num1 = request.form.get('num1', default=0, type=float)
        num2 = request.form.get('num2', default=0, type=float)
        result = num1 + num2
        return render_template('lab4/sum.html', result=result)
    return render_template('lab4/sum.html', result=None)

@lab4.route('/subtract', methods=['GET', 'POST'])
def subtract_page():
    error = None
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        if num1 == '' or num2 == '':
            error = "Оба поля должны быть заполнены."
        else:
            result = float(num1) - float(num2)
    return render_template('lab4/subtract.html', error=error, result=result)

@lab4.route('/multiply', methods=['GET', 'POST'])
def multiply_page():
    if request.method == 'POST':
        num1 = request.form.get('num1', default=1, type=float)
        num2 = request.form.get('num2', default=1, type=float)
        result = num1 * num2
        return render_template('lab4/multiply.html', result=result)
    return render_template('lab4/multiply.html', result=None)

@lab4.route('/power', methods=['GET', 'POST'])
def power_page():
    error = None
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        if num1 == '' or num2 == '':
            error = "Оба поля должны быть заполнены."
        elif float(num1) == 0 and float(num2) == 0:
            error = "Нельзя возводить 0 в 0."
        else:
            result = float(num1) ** float(num2)
    return render_template('lab4/power.html', error=error, result=result)

@lab4.route('/div', methods=['GET', 'POST'])
def div_page():
    error = None
    result = None
    if request.method == 'POST':
        num1 = request.form.get('num1')
        num2 = request.form.get('num2')
        if num1 == '' or num2 == '':
            error = "Оба поля должны быть заполнены."
        elif float(num2) == 0:
            error = "Деление на ноль невозможно."
        else:
            result = float(num1) / float(num2)
    return render_template('lab4/div.html', error=error, result=result)

@lab4.route('/lab4/tree', methods=['GET', 'POST'])
def tree():
    global tree_count

    if request.method == 'POST':
        operation = request.form.get('operation')
        if operation == 'plant':
            tree_count += 1
        elif operation == 'cut':
            if tree_count > 0:
                tree_count -= 1
        return redirect(url_for('lab4.tree'))

    return render_template('lab4/tree.html', tree_count=tree_count)

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        for user in users:
            if user['username'] == username and user['password'] == password:
                session['username'] = username
                return redirect(url_for('lab4.user_list'))

        flash('Неправильный логин или пароль')
    
    return render_template('lab4/login.html')

@lab4.route('/lab4/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        username = request.form['username']
        password = request.form['password']
        
        users.append({'name': name, 'username': username, 'password': password})
        flash('Пользователь успешно зарегистрирован!')
        return redirect(url_for('lab4.login'))
    
    return render_template('lab4/register.html')

@lab4.route('/lab4/users')
def user_list():
    if 'username' not in session:
        return redirect(url_for('lab4.login'))

    return render_template('lab4/user_list.html', users=users)

@lab4.route('/lab4/edit/<username>', methods=['GET', 'POST'])
def edit_user(username):
    if 'username' not in session:
        return redirect(url_for('lab4.login'))

    user = next((u for u in users if u['username'] == username), None)

    if request.method == 'POST':
        user['name'] = request.form['name']
        user['password'] = request.form['password']
        flash('Данные пользователя обновлены!')
        return redirect(url_for('lab4.user_list'))

    return render_template('lab4/edit_user.html', user=user)

@lab4.route('/lab4/delete/<username>', methods=['POST'])
def delete_user(username):
    if 'username' not in session:
        return redirect(url_for('lab4.login'))

    global users
    users = [u for u in users if u['username'] != username]
    flash('Пользователь удалён!')
    return redirect(url_for('lab4.user_list'))

@lab4.route('/lab4/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('lab4.login'))

@lab4.route('/lab4/clear_cookies')
def clear_cookies():
    response = redirect(url_for('lab4.login'))
    response.delete_cookie('username')  # Удалите нужные cookies
    response.delete_cookie('authorized')
    return response

@lab4.route('/fridge', methods=['GET', 'POST'])
def fridge():
    temperature = request.form.get('temperature')
    message, snowflakes = "", ""

    if temperature is None:
        message = "Ошибка: не задана температура."
    else:
        try:
            temperature = float(temperature)
            if temperature < -12:
                message = "Не удалось установить температуру — слишком низкое значение."
            elif temperature > -1:
                message = "Не удалось установить температуру — слишком высокое значение."
            elif -12 <= temperature <= -9:
                message = f"Установлена температура: {temperature}°С"
                snowflakes = "❄️❄️❄️"
            elif -8 <= temperature <= -5:
                message = f"Установлена температура: {temperature}°С"
                snowflakes = "❄️❄️"
            elif -4 <= temperature <= -1:
                message = f"Установлена температура: {temperature}°С"
                snowflakes = "❄️"
        except ValueError:
            message = "Ошибка: введите корректное значение температуры."

    return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes) 

@lab4.route('/order_grain', methods=['GET', 'POST'])
def order_grain():
    if request.method == 'POST':
        grain_type = request.form.get('grain_type')
        weight = request.form.get('weight', type=float)

        if weight is None:
            flash('Ошибка: вес не был указан.', 'error')
            return redirect(url_for('lab4.order_grain'))
        
        if weight <= 0:
            flash('Ошибка: вес должен быть больше нуля.', 'error')
            return redirect(url_for('lab4.order_grain'))

        prices = {
            'ячмень': 12345,
            'овёс': 8522,
            'пшеница': 8722,
            'рожь': 14111
        }

        if weight >= 500:
            flash('Ошибка: такого объёма сейчас нет в наличии.', 'error')
            return redirect(url_for('lab4.order_grain'))

        total_price = prices[grain_type] * weight

        # Применяем скидку
        discount = 0
        if weight > 50:
            discount = total_price * 0.10
            total_price -= discount
            message = f'Применена скидка за большой объём: {discount:.2f} руб.'
        
        else:
            message = 'Заказ успешно сформирован.'

        return render_template('lab4/order_grain.html', grain_type=grain_type, weight=weight, total_price=total_price, message=message)

    return render_template('lab4/order_grain.html')


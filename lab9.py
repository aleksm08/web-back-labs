from flask import Blueprint, render_template, request, redirect, url_for, session
import random

lab9 = Blueprint('lab9', __name__, template_folder='templates')

def get_random_background():
    backgrounds = ['christmas1.jpg', 'christmas2.jpg', 'christmas3.jpg']
    return f"/static/lab9/{random.choice(backgrounds)}"

@lab9.route('/lab9/')
def lab():
    if all(session.get(key) for key in ['name', 'age', 'gender', 'preference1', 'preference2']):
        return redirect(url_for('lab9.final'))
    return render_template('lab9/index.html', background=get_random_background())

@lab9.route('/lab9/step1_name', methods=['GET', 'POST'])
def step1_name():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('lab9.step2_age'))
    return render_template('lab9/step1_name.html', background=get_random_background())

@lab9.route('/lab9/step2_age', methods=['GET', 'POST'])
def step2_age():
    if request.method == 'POST':
        session['age'] = request.form.get('age')
        return redirect(url_for('lab9.step3_gender'))
    return render_template('lab9/step2_age.html', background=get_random_background())

@lab9.route('/lab9/step3_gender', methods=['GET', 'POST'])
def step3_gender():
    if request.method == 'POST':
        session['gender'] = request.form.get('gender')
        return redirect(url_for('lab9.step4_preference1'))
    return render_template('lab9/step3_gender.html', background=get_random_background())

@lab9.route('/lab9/step4_preference1', methods=['GET', 'POST'])
def step4_preference1():
    if request.method == 'POST':
        session['preference1'] = request.form.get('preference1')
        return redirect(url_for('lab9.step5_preference2'))
    return render_template('lab9/step4_preference1.html', background=get_random_background())

@lab9.route('/lab9/step5_preference2', methods=['GET', 'POST'])
def step5_preference2():
    if request.method == 'POST':
        session['preference2'] = request.form.get('preference2')
        return redirect(url_for('lab9.final'))
    return render_template('lab9/step5_preference2.html', background=get_random_background())

@lab9.route('/lab9/final')
def final():
    name = session.get('name', 'гость')
    age = int(session.get('age', 0))
    gender = session.get('gender')
    preference1 = session.get('preference1')
    preference2 = session.get('preference2')

    if age < 15:
        if gender == 'male':
            grown = f'''Дорогой {name}, желаем тебе быстро вырасти, быть умным, сильным и здоровым! 
            Пусть в новом году у тебя будет много игрушек и сладостей!'''
        else:
            grown = f'''Дорогая {name}, желаем тебе быстро вырасти, быть умной, красивой и здоровой! 
            Пусть в новом году у тебя будет много радости и подарков!'''
    else:
        if gender == 'male':
            grown = f'''Уважаемый {name}, желаем вам в новом году успехов в работе, крепкого здоровья и счастья! 
            Пусть все ваши мечты сбываются!'''
        else:
            grown = f'''Уважаемая {name}, желаем вам в новом году счастья, любви и благополучия! 
            Пусть каждый день приносит радость и вдохновение!'''

    if preference1 == 'вкусное' and preference2 == 'сладкое':
        gift = 'коробку конфет'
        img = 'candy.jpg'
    elif preference1 == 'вкусное' and preference2 == 'сытное':
        gift = 'пиццу'
        img = 'pizza.jpg'
    elif preference1 == 'красивое' and preference2 == 'украшения':
        gift = 'новогодние украшения'
        img = 'decorations.jpg'
    else:
        gift = 'книгу'
        img = 'book.png'

    return render_template('lab9/final.html', name=name, grown=grown, gift=gift, img=img, background=get_random_background())

@lab9.route('/lab9/restart')
def restart():
    session.clear()
    return redirect(url_for('lab9.step1_name'))
import os

from flask import Flask, render_template, request, flash, redirect, url_for

from exceptions import BaseChemException
from mendeleev_table import MendeleevTable

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'

if os.path.exists('/SERVER/is_server'):
    prefix = '/chemistry'
else:
    prefix = ''


@app.route(f'{prefix}/')
def page_index():
    return render_template('index.html', el_list=MendeleevTable.lst)


@app.route(f'{prefix}/element-by/<type_>', methods=['POST'])
def page_find_element(type_):
    func, param, err = {
        'number': (
            MendeleevTable.from_number,
            int(request.form.get('number', 0)),
            'Некорректный номер элемента'
        ),
        'label': (
            MendeleevTable.from_label,
            request.form.get('label'),
            f'Элемент с символом "{request.form.get("label")}" не найден'
        ),
        'name': (
            MendeleevTable.from_name,
            request.form.get('name'),
            f'Элемент с именем "{request.form.get("name")}" не найден'
        ),
        'position': (
            MendeleevTable.from_position,
            (
                int(request.form.get('position_period', 0)),
                int(request.form.get('position_group', 0)),
                int(request.form.get('position_subgroup') == 'A')
            ),
            'Элемент с такой позицией не найден'
        )
    }[type_]

    try:
        elem = func(param)
    except BaseChemException:
        flash(err, 'error')
        return redirect(url_for('page_index'))

    return redirect(url_for('page_element', el=elem.label))#f'/element/{elem.label}')


@app.route(f'{prefix}/element/<el>')
def page_element(el):
    return render_template('element.html', element=MendeleevTable.from_label(el), map=map, str=str)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8005)

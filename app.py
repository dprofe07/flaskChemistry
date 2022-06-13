from flask import Flask, render_template, request, flash, redirect

from exceptions import IncorrectElementNumberException, ElementNotFoundException, BaseChemException
from mendeleev_table import MendeleevTable

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fdgdfgdfggf786hfg6hfg6h7f'


@app.route('/')
def index():
    return render_template('index.html', el_list=MendeleevTable.lst)


@app.route('/element-by/<type_>', methods=['POST'])
def element_number(type_):
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
        return redirect('/', 302)

    return redirect(f'/element/{elem.label}', 302)


@app.route('/element/<el>')
def element(el):
    return render_template('element.html', element=MendeleevTable.from_label(el), map=map, str=str)






if __name__ == '__main__':
    app.run(debug=True)

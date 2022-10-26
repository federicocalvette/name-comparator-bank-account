from flask import Flask, render_template, request, url_for, flash, redirect, send_from_directory
import prometeo_request
import settings
import comparator

app = Flask(__name__)
app.config['SECRET_KEY'] = settings.SECRET_KEY


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        numero_cuenta = request.form['numero_cuenta']
        codigo_banco = request.form['codigo_banco']
        codigo_pais = request.form['codigo_pais']

        if not nombre_completo:
            flash('Name is required!')
        elif not numero_cuenta:
            flash('Account number is required!')
        elif not codigo_banco and codigo_pais == 'UY':
            flash('Bank code is required!')
        elif not codigo_pais:
            flash('Country code is required!')
        else:
            response_request = prometeo_request.make_request(numero_cuenta, codigo_banco, codigo_pais)

            if response_request == "Cuenta credito invalida":
                return render_template('index.html', msg="Cuenta credito invalida")

            elif response_request == "Error de comunicacion con el banco":
                return render_template('index.html', msg="Error de comunicacion con el banco")

            elif response_request == "Parametros invalidos":
                return render_template('index.html', msg="Parametros invalidos")

            else:
                name_response = response_request

                if "*" in name_response:
                    porcentage = comparator.name_comparator_mask(nombre_completo, name_response)
                    message_front = f'El titular de la cuenta bancaria {numero_cuenta} se llama: {name_response}. El porcentaje de coincidencia entre {nombre_completo} y {name_response} es de un {porcentage}%. Ignorando los *.'
                else:
                    porcentage = comparator.name_comparator(nombre_completo, name_response)
                    message_front = f'El titular de la cuenta bancaria {numero_cuenta} se llama: {name_response}. El porcentaje de coincidencia entre {nombre_completo} y {name_response} es de un {porcentage}%.'
                return render_template('index.html', msg=message_front)

        return render_template('index.html')

    return render_template('index.html')

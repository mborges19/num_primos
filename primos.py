# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

def num_primo(n):
    """Função para verificar se um número é primo."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

@app.route('/')
def imprime_num_primo():
    """Função para exibir os 100 primeiros números primos."""
    primos = []
    num = 2
    while len(primos) < 100:
        if num_primo(num):
            primos.append(num)
        num += 1
    return render_template('index.html', primos=primos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
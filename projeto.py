from flask import Flask, render_template, request, redirect, url_for, send_file
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAUjnJX5IetZFKMss7J6PuXfQQapKZuKB0")

app = Flask(__name__)

def generate_recommendation(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form1', methods=['GET', 'POST'])
def form1():
    if request.method == 'POST':
        genero = request.form['genero']
        peso = request.form['peso']
        altura = request.form['altura']
        idade = request.form['idade']
        
        return redirect(url_for('form2', genero=genero, peso=peso, altura=altura, idade=idade))
    return render_template('formpag1.html')

@app.route('/form2', methods=['GET', 'POST'])
def form2():
    if request.method == 'POST':
        genero = request.args.get('genero')
        peso = request.args.get('peso')
        altura = request.args.get('altura')
        idade = request.args.get('idade')
        objetivo = request.form['objetivo']
        atividades = request.form['atividades']
        musculacao = request.form['musculacao']
        tempo_meta = request.form['tempo_meta']
        restricao = request.form['restricao']
        restricao_tipo = request.form['restricao_tipo']

        return redirect(url_for('loading', genero=genero, peso=peso, altura=altura, idade=idade,
                                objetivo=objetivo, atividades=atividades, musculacao=musculacao,
                                tempo_meta=tempo_meta, restricao=restricao, restricao_tipo=restricao_tipo))
    return render_template('formpag2.html', 
                                genero=request.args.get('genero'), 
                                peso=request.args.get('peso'), 
                                altura=request.args.get('altura'), 
                                idade=request.args.get('idade'))

@app.route('/loading')
def loading():
    genero = request.args.get('genero')
    peso = request.args.get('peso')
    altura = request.args.get('altura')
    idade = request.args.get('idade')
    objetivo = request.args.get('objetivo')
    atividades = request.args.get('atividades')
    musculacao = request.args.get('musculacao')
    tempo_meta = request.args.get('tempo_meta')
    restricao = request.args.get('restricao')
    restricao_tipo = request.args.get('restricao_tipo')

    nome_cadastro = f"recomendacao_{genero}_{peso}_{altura}_{idade}".replace(" ", "_").lower()
    diretorio = r"C:\Users\62129532024.1\Documents\GitHub\pfinal-python\resultadoIA"
    arquivo = os.path.join(diretorio, f"{nome_cadastro}.txt")

    os.makedirs(diretorio, exist_ok=True)

    with open(arquivo, "w") as file:
        file.write(f"Gênero: {genero}\n")
        file.write(f"Peso: {peso} kg\n")
        file.write(f"Altura: {altura} cm\n")
        file.write(f"Idade: {idade} anos\n")
        file.write(f"Objetivo: {objetivo}\n")
        file.write(f"Atividades físicas: {atividades}\n")
        file.write(f"Musculação: {musculacao}\n")
        file.write(f"Tempo para a meta: {tempo_meta}\n")
        file.write(f"Restrição alimentar: {restricao}\n")
        file.write(f"Tipo de restrição: {restricao_tipo}\n")

    respostagptrest = (
        f"Faça uma dieta e uma lista de treinos cardio, inferiores e superiores, separados em dias da semana, de acordo "
        f"com os seguintes objetivos e dados de uma pessoa do sexo biológico {genero} de {peso}kg, {altura}cm de altura "
        f"e {idade} anos. O objetivo dessa pessoa é {objetivo}. A pergunta 'faz atividades físicas?', a resposta do usuário "
        f"foi '{atividades}'. A pergunta 'faz treino de musculação', a resposta foi '{musculacao}'. Essa pessoa pretende "
        f"alcançar sua meta em {tempo_meta}. A pergunta 'tem restrição alimentar?', a resposta foi '{restricao}'. A "
        f"restrição informada pela pessoa é {restricao_tipo}."
    )

    recommendation = generate_recommendation(respostagptrest)

    with open(arquivo, "a") as file:
        file.write("\n\nRecomendação de Treino e Dieta:\n")
        file.write(recommendation)
    
    return redirect(url_for('resultado', txt_file=nome_cadastro))

@app.route('/resultado')
def resultado():
    txt_file = request.args.get('txt_file')
    return render_template('resultado.html', txt_file=txt_file)

@app.route('/download/<filename>')
def download_file(filename):
    diretorio = r"C:\Users\62129532024.1\Documents\GitHub\pfinal-python\resultadoIA"
    return send_file(os.path.join(diretorio, f"{filename}.txt"), as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)

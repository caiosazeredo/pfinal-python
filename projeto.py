import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBJi4xHOMKw1DYvt8r0q4ZD7NuVaP0uL6k")

def generate_recommendation(prompt):
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    response = model.generate_content([prompt])
    return response.text

# Solicitação das informações ao usuário
nome_cadastro = input("Qual o nome do arquivo que será salvo? ").strip().replace(" ", "_").lower()
diretorio = r"C:\Users\62129532024.1\Documents\GitHub\Projeto-final"
arquivo = f"{diretorio}\\{nome_cadastro}.txt"

# Criar o diretório se não existir
os.makedirs(diretorio, exist_ok=True)

gender = input("Gênero: ")
weight = input("Peso: ")
height = input("Altura: ")
age = input("Idade: ")
principal = input("Objetivo: ")
atividades = input("Atividades físicas: ")
musculacao = input("Musculação: ")
tempo_meta = input("Tempo para a meta: ")
restricao = input("Restrição alimentar: ")
restricaotipo = input("Tipo de restrição: ")

# Escrevendo as informações no arquivo
with open(arquivo, "w") as file:
    file.write(f"Gênero: {gender}\n")
    file.write(f"Peso: {weight} kg\n")
    file.write(f"Altura: {height} cm\n")
    file.write(f"Idade: {age} anos\n")
    file.write(f"Objetivo: {principal}\n")
    file.write(f"Atividades físicas: {atividades}\n")
    file.write(f"Musculação: {musculacao}\n")
    file.write(f"Tempo para a meta: {tempo_meta}\n")
    file.write(f"Restrição alimentar: {restricao}\n")
    file.write(f"Tipo de restrição: {restricaotipo}\n")

print(f"O arquivo foi salvo em {arquivo}")

# Criando os prompts para o modelo
respostagpt = (
    f"Faça uma dieta e uma lista de treinos cardio, inferiores e superiores, separados em dias da semana, de acordo "
    f"com os seguintes objetivos e dados de uma pessoa do sexo biológico {gender} de {weight}kg, {height}cm de altura "
    f"e {age} anos. O objetivo dessa pessoa é {principal}. A pergunta 'faz atividades físicas?', a resposta do usuário "
    f"foi '{atividades}'. A pergunta 'faz treino de musculação', a resposta foi '{musculacao}'. Essa pessoa pretende "
    f"alcançar sua meta em {tempo_meta}. A pergunta 'tem restrição alimentar?', a resposta foi '{restricao}'."
)

respostagptrest = (
    f"Faça uma dieta e uma lista de treinos cardio, inferiores e superiores, separados em dias da semana, de acordo "
    f"com os seguintes objetivos e dados de uma pessoa do sexo biológico {gender} de {weight}kg, {height}cm de altura "
    f"e {age} anos. O objetivo dessa pessoa é {principal}. A pergunta 'faz atividades físicas?', a resposta do usuário "
    f"foi '{atividades}'. A pergunta 'faz treino de musculação', a resposta foi '{musculacao}'. Essa pessoa pretende "
    f"alcançar sua meta em {tempo_meta}. A pergunta 'tem restrição alimentar?', a resposta foi '{restricao}'. A "
    f"restrição informada pela pessoa é {restricaotipo}."
)

# Gerando recomendação de treino e dieta
recommendation = generate_recommendation(respostagptrest)

# Salvando a recomendação no arquivo
with open(arquivo, "a") as file:
    file.write("\n\nRecomendação de Treino e Dieta:\n")
    file.write(recommendation)

print("Recomendação gerada e salva no arquivo.")

# Lendo e exibindo o conteúdo do arquivo
with open(arquivo, 'r') as file:
    for linha in file:
        print(linha.strip())
import tkinter as tk
from tkinter import messagebox
import Urna  # Importando o módulo Urna

# Variável para controlar se a votação está ativa
votacao_ativa = False

# Função que exibe os candidatos na interface gráfica
def exibir_candidatos():
    candidatos_texto.delete(1.0, tk.END)  # Limpa a caixa de texto antes de mostrar os candidatos
    candidatos = Urna.listar_candidatos()
    for numero, nome, partido in candidatos:
        candidatos_texto.insert(tk.END, f"Número: {numero} | Nome: {nome} | Partido: {partido}\n")

# Função que registra o voto
def registrar_voto():
    if not votacao_ativa:
        messagebox.showwarning("Erro", "A votação ainda não foi iniciada!")
        return

    try:
        numero_voto = int(entry_numero.get())  # Pega o número do candidato inserido
        sucesso, mensagem = Urna.registrar_voto(numero_voto)  # Chama a função registrar_voto do Urna.py

        # Exibe a mensagem correspondente
        if sucesso:
            messagebox.showinfo("Sucesso", mensagem)
        else:
            messagebox.showwarning("Aviso", mensagem)

    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números válidos.")

# Função que exibe o resultado
def exibir_resultados():
    if not votacao_ativa:
        messagebox.showwarning("Erro", "A votação ainda não foi iniciada!")
        return

    resultado = Urna.obter_resultado()  # Chama a função obter_resultado do Urna.py
    messagebox.showinfo("Resultado Final", resultado)

# Função que salva o resultado em um arquivo
def salvar_resultado():
    Urna.salvar_resultado_txt()  # Chama a função salvar_resultado_txt do Urna.py
    messagebox.showinfo("Sucesso", "Resultados salvos com sucesso!")

# Função para iniciar a votação
def iniciar_votacao():
    global votacao_ativa  # Garantir que estamos acessando a variável global
    if votacao_ativa:
        messagebox.showwarning("Aviso", "A votação já foi iniciada.")
    else:
        votacao_ativa = True
        messagebox.showinfo("Votação Iniciada", "A votação foi iniciada! Agora, você pode votar.")

# Função para finalizar a votação
def finalizar_votacao():
    global votacao_ativa  # Garantir que estamos acessando a variável global
    if not votacao_ativa:
        messagebox.showwarning("Erro", "A votação ainda não foi iniciada!")
    else:
        votacao_ativa = False
        exibir_resultados()  # Exibe o resultado quando a votação for finalizada

# Criando a interface gráfica
janela = tk.Tk()
janela.title("Urna Eletrônica")
janela.geometry("600x500")

# Caixa de texto para exibir os candidatos
candidatos_texto = tk.Text(janela, height=10, width=70)
candidatos_texto.pack(pady=20)

# Botão para exibir os candidatos
botao_exibir = tk.Button(janela, text="Exibir Candidatos", command=exibir_candidatos)
botao_exibir.pack(pady=10)

# Campo para digitar o número do candidato
entry_numero = tk.Entry(janela)
entry_numero.pack(pady=10)
entry_numero.insert(0, "Digite o número do candidato")

# Botão para registrar o voto
botao_voto = tk.Button(janela, text="Votar", command=registrar_voto)
botao_voto.pack(pady=10)

# Botão para iniciar a votação
botao_iniciar_votacao = tk.Button(janela, text="Iniciar Votação", command=iniciar_votacao)
botao_iniciar_votacao.pack(pady=10)

# Botão para finalizar a votação
botao_finalizar_votacao = tk.Button(janela, text="Finalizar Votação", command=finalizar_votacao)
botao_finalizar_votacao.pack(pady=10)

# Botão para exibir os resultados
botao_resultados = tk.Button(janela, text="Imprimir Resultados", command=exibir_resultados)
botao_resultados.pack(pady=10)

# Botão para salvar os resultados em um arquivo
botao_salvar = tk.Button(janela, text="Salvar Resultados", command=salvar_resultado)
botao_salvar.pack(pady=10)

# Inicia a interface gráfica
janela.mainloop()

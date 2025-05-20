# Urna.py

# Lista de candidatos fixos com seus números, nomes e partidos
candidatos = {
    10: {"nome": "Ana Futuro", "partido": "Partido do Futuro", "votos": 0},
    20: {"nome": "Bruno Joven", "partido": "Movimento Jovem", "votos": 0},
    30: {"nome": "Carlos Educa", "partido": "Educação em 1º Lugar", "votos": 0}
}

votos_nulos = 0

def listar_candidatos():
    """Retorna uma lista de tuplas com número, nome e partido."""
    return [(numero, dados["nome"], dados["partido"]) for numero, dados in candidatos.items()]

def registrar_voto(numero):
    """Registra um voto em um candidato, ou considera nulo."""
    global votos_nulos
    if numero in candidatos:
        candidatos[numero]["votos"] += 1
        return True, f"Voto computado para {candidatos[numero]['nome']}"
    else:
        votos_nulos += 1
        return False, "Voto nulo registrado."

def obter_resultado():
    """Gera o texto do relatório final da votação."""
    resultado = "\n=== RESULTADOS DA VOTAÇÃO ===\n\n"
    vencedor = None
    maior_votacao = -1

    for numero, info in candidatos.items():
        resultado += f"{info['nome']} ({info['partido']}) - {info['votos']} voto(s)\n"
        if info["votos"] > maior_votacao:
            maior_votacao = info["votos"]
            vencedor = info

    resultado += f"\nVotos nulos: {votos_nulos}\n"

    if vencedor and vencedor["votos"] > 0:
        resultado += f"\n🎉 CANDIDATO VENCEDOR 🎉\n{vencedor['nome']} ({vencedor['partido']}) com {vencedor['votos']} voto(s)\n"
    else:
        resultado += "\nNenhum candidato recebeu votos válidos."

    return resultado

def salvar_resultado_txt():
    """Salva o resultado final em um arquivo de texto."""
    texto = obter_resultado()
    with open("resultado_votacao.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(texto)

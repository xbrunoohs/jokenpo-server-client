JOKENPO_DICTIONARY = {0:"Pedra", 1:"Papel", 2:"Tesoura"}

mensagem_vitoria = 'Vitória!'
mensagem_derrota = 'Você perdeu!'
mensagem_empate = 'Empate!'
mensagem_invalida = 'Jogada inválida!'

def jokenpo_logica(jogada_cliente, jogada_servidor):
    if jogada_cliente == 0:
        if jogada_servidor == 0:
            return mensagem_empate
        elif jogada_servidor == 1:
            return mensagem_derrota
        elif jogada_servidor == 2:
            return mensagem_vitoria
        else: 
            return mensagem_invalida

    elif jogada_cliente == 1:
        if jogada_servidor == 0:
            return mensagem_vitoria
        elif jogada_servidor == 1:
            return mensagem_empate
        elif jogada_servidor == 2:
            return mensagem_derrota
        else: 
            return mensagem_invalida
        
    elif jogada_cliente == 2:
        if jogada_servidor == 0:
            return mensagem_derrota
        elif jogada_servidor == 1:
            return mensagem_vitoria
        elif jogada_servidor == 2:
            return mensagem_empate
        else: 
            return mensagem_invalida
    
    else:
        return mensagem_invalida
    
    
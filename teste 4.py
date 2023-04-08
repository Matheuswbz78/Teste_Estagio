distancia = 100

v_carro = 110
v_caminhao = 80
tempo_pedagio = 5/60

tempo_encontro = distancia / (v_carro + v_caminhao)

distancia_carro = v_carro * tempo_encontro
distancia_caminhao = v_caminhao * tempo_encontro

distancia_falta_carro = distancia - distancia_carro
distancia_falta_caminhao = distancia - distancia_caminhao

tempo_falta_carro = distancia_falta_carro / v_carro
tempo_falta_caminhao = distancia_falta_caminhao / v_caminhao + tempo_pedagio * 2

distancia_ribeirao_preto_carro = distancia_carro - distancia_falta_carro
distancia_ribeirao_preto_caminhao = distancia_falta_caminhao

if distancia_ribeirao_preto_carro < distancia_ribeirao_preto_caminhao:
    print("O carro está mais proximo de RP quando houver o encontro entre os dois")

elif distancia_ribeirao_preto_caminhao < distancia_ribeirao_preto_carro:
    print("O caminhão está mais próximo de RP quando houver o encontro entre os dois.")

else:
    print("Os dois estão iguais quando houver o encontro para a RP")




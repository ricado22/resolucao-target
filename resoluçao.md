#Exercício 3:

Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);

Para determinar o valor final da variável SOMA, vamos seguir o loop passo a passo:

Resposta:

Inicialmente, K = 1 e SOMA = 0.
O loop continua enquanto K < 12.
Vamos calcular as iterações:

Iteração 1: K = 2, SOMA = 0 + 2 = 2
Iteração 2: K = 3, SOMA = 2 + 3 = 5
Iteração 3: K = 4, SOMA = 5 + 4 = 9
Iteração 4: K = 5, SOMA = 9 + 5 = 14
Iteração 5: K = 6, SOMA = 14 + 6 = 20
Iteração 6: K = 7, SOMA = 20 + 7 = 27
Iteração 7: K = 8, SOMA = 27 + 8 = 35
Iteração 8: K = 9, SOMA = 35 + 9 = 44
Iteração 9: K = 10, SOMA = 44 + 10 = 54
Iteração 10: K = 11, SOMA = 54 + 11 = 65
Iteração 11: K = 12, SOMA = 65 + 12 = 77

O loop termina quando K atinge 12, então a última iteração não é executada.

Portanto, ao final do processamento, o valor da variável SOMA será 77

#Exercício 4:

Descubra a lógica e complete o próximo elemento:
a) 1, 3, 5, 7, ___
b) 2, 4, 8, 16, 32, 64, ____
c) 0, 1, 4, 9, 16, 25, 36, ____
d) 4, 16, 36, 64, ____
e) 1, 1, 2, 3, 5, 8, ____
f) 2,10, 12, 16, 17, 18, 19, ____

Resposta:
a) 9
b) 128
c) 49
d) 100
e) 13
f) 200

#Exercício 5:

Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada? 

Resposta:

Passo 1: Primeiro, ligue o primeiro interruptor.

Passo 2: Deixe o primeiro interruptor ligado por aproximadamente 10 minutos.

Passo 3: Após 10 minutos, desligue o primeiro interruptor.

Passo 4: Agora, ligue o segundo interruptor.

Passo 5: Deixe o terceiro interruptor desligado durante todo o tempo.

Passo 6: Vá até as salas onde estão as lâmpadas.

Passo 7: Observe as lâmpadas. A lâmpada que está acesa corresponde ao segundo interruptor.

Passo 8: Toque nas lâmpadas que estão desligadas.

Passo 9: A lâmpada que estiver quente corresponde ao primeiro interruptor, que você deixou ligado por 10 minutos e depois desligou.

ou

verifique se há algum sinal de atividade, como piscadas ou luminescência residual se as lâmpadas forem de LED

Passo 10: A lâmpada que estiver fria corresponde ao terceiro interruptor, que permaneceu desligado o tempo todo.
# Projeto que de mini piano 

Projeto arduino que tem um botão que toca musica  além de todas as notas e um led que se acende toda vez que uma tecla é precionada.

* Sobre o código a musica foi feita nota por nota de maneira bem amadora e esdruxula mas funciona rs. *

## Materiais:
1 Arduino Uno (ou compatível)
7 botões (um para cada nota)
1 buzzer piezoelétrico (ativo ou passivo)
7 resistores de 10kΩ (para os botões)
Jumpers e protoboard


## Funcionamento do Circuito
-Cada botão está conectado a uma porta digital do Arduino (por exemplo, pinos 2, 3, 4, 5...).
-O buzzer está ligado a outro pino digital (exemplo: pino 8), com o outro terminal conectado ao GND.
-Cada botão, ao ser pressionado, envia um sinal HIGH (5V) para o Arduino.
-O Arduino identifica esse sinal e envia um comando para reproduzir uma frequência sonora no buzzer.
Nota: Cada botão utiliza um resistor ligado ao GND (pull-down) para manter o pino em estado LOW quando o botão não estiver pressionado, evitando leituras 
Incorretas.

## Funcionalidade do Projeto
-Ao apertar um botão, o Arduino detecta qual botão foi pressionado.
-Com base nessa leitura, ele utiliza a função tone(pino, frequência, duração) para reproduzir uma nota musical específica.
-Isso simula o funcionamento de um teclado musical simples, emitindo sons diferentes conforme o botão pressionado.
- Além disso  dos 7 botões que corresponde as notas musicais a um 8 botão que possui a função tocar musica 
- E por fim toda vez que uma nota é tocada o led também se acende
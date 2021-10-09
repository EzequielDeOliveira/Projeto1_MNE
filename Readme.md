Projeto 1 - MNE

# Softwares para modelagem e acompanhamento de doenças

## Execução
Para executar o programa é necessário:
- Python >= 3.6
- Numpy


Com os requisitos instalados bastar executar o comando:
```
python3 main.py
```
## Experimento de software aplicado ao acompanhamento de doenças

Para esse experimento, os dados do mês de setembro sobre os novos casos de COVID-19 foram coletados e salvos no *y.txt* e os dias respectivos no *x.txt* os dados de entrada foram fornecidos os casos do dia 01/09/2021 até 20/09/2021, a partir dai usando python e a biblioteca numpy, os números foram tratados, e foi aplicado um ajuste de curva linear e um quadrático a fins de comparação, foi gerada a estimativa dos dias 21/09/2021 até 30/09/2021 a partir dessa estimativa temos como resultado o erro comparado aos dados reais.

![image](https://user-images.githubusercontent.com/37127457/136646673-97864668-1f42-47fd-994d-68b2a4bb337e.png)

Neste experimento foram feitas predições para datas conhecidas para obter parâmetros de comparação, mas esse mesmo código pode ser expandido para predições futuras.

## Referências
- [Ajuste de curva](https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/adc-ajuste_de_uma_reta.html)
- [Dados covid](https://github.com/wcota/covid19br)

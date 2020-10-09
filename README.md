# Star wars social network analysis

![Badge](https://img.shields.io/static/v1?label=Python&message=v3.8.2&color=FFE135&style=for-the-badge)
![Badge](https://img.shields.io/static/v1?label=Networkx&message=v2.5&color=CD5C5C&style=for-the-badge)

> Atividade proposta pela disciplina de Redes complexas da Universidade Federal de São João del Rei, para prática na utilização de ferramentas de estudo de redes. Nesse trabalho foi utilizado Networkx para análise das redes sociais dos 6 primeiros episódios de star wars.

![Storm-troopers](./assets/storm-troopers.jpg)

> A rede social foi obtida em: https://www.kaggle.com/ruchi798/star-wars

## Redes

Na base de dados das redes encontramos 4 tipos de arquivos:

- starwars-episode-N-interactions.json: Rede extraída do episódio N, a qual as interações entre os personagens são definidas pelo número de vezes que os personagens falam dentro de uma mesma cena.

- starwars-episode-N-mentions.json: Rede extraída do episódio N, a qual as interações entre os personagens são definidas pelo número de vezes que os personagens são mencionados em uma mesma cena.

- starwars-episode-N-interactions-allCharacters.json: Rede de interações entre R2-D2 e Chewbacca com dados adicionados da rede de menções.

- starwars-full-...: Contém as redes sociais extraídas dos 6 episódios.

## Estudo

Nas redes citadas a cima foram estudas as seguintes características:

- Número de personagens e ligações
- Densidade e diâmetro de rede
- Grau e coeficiente de clusterização médio
- Plotagem da rede
- Plotagem da distribuição de graus
- Ranking dos 20 vértices(personagens) mais centrais, utilizando como medidas de centralidade: closeness, betweeness, grau e autovetor.

## Demo

```sh
git clone https://github.com/LucasVidigal98/star-wars-network.git
```

```sh
cd star-wars-network/src
```

```sh
python3 main.py
```

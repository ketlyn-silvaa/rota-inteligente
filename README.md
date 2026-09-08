# 🚚 Rota Inteligente: Otimização de Entregas com Algoritmos de IA

## 📌 Sobre o Projeto

O projeto **Rota Inteligente** foi desenvolvido para ajudar uma empresa fictícia de delivery de alimentos chamada **Sabor Express**.

A empresa enfrenta dificuldades para organizar suas entregas, principalmente nos horários de maior movimento, como almoço e jantar. Atualmente, os entregadores escolhem as rotas de forma manual, utilizando apenas a experiência e o conhecimento sobre a região.

Isso pode fazer com que sejam escolhidos caminhos mais longos, aumentando o tempo das entregas, o consumo de combustível e os custos da empresa.

Pensando nisso, este projeto propõe uma solução utilizando conceitos de **Inteligência Artificial** para ajudar a encontrar rotas mais eficientes e organizar melhor os pedidos.

---

# 🎯 Objetivo

O objetivo principal do projeto é desenvolver uma solução baseada em Inteligência Artificial capaz de ajudar a empresa Sabor Express a encontrar rotas de entrega mais rápidas e eficientes.

Com isso, busca-se:

* 🚗 Reduzir a distância percorrida pelos entregadores;
* ⏱️ Diminuir o tempo das entregas;
* ⛽ Reduzir o consumo de combustível;
* 📦 Organizar melhor os pedidos;
* 📍 Agrupar entregas próximas;
* 😊 Melhorar a satisfação dos clientes.

---

# 🧠 Problema

A empresa Sabor Express realiza diversas entregas durante o dia.

Nos horários de maior movimento, vários pedidos podem ser realizados ao mesmo tempo.

Como as rotas são escolhidas manualmente, os entregadores podem percorrer caminhos mais longos ou demorados.

Isso pode causar:

* Atrasos nas entregas;
* Maior consumo de combustível;
* Aumento dos custos operacionais;
* Dificuldade para organizar vários pedidos;
* Insatisfação dos clientes.

A solução proposta é utilizar algoritmos de Inteligência Artificial para analisar os locais de entrega e sugerir rotas mais eficientes.

---

# 🗺️ Representação do Problema com Grafos

Para representar a região onde as entregas acontecem, será utilizado o conceito de **grafo**.

Um grafo é formado por pontos e conexões.

No projeto:

* 📍 Os **nós ou vértices** representam os locais, bairros ou pontos de entrega;
* 🛣️ As **arestas** representam as ruas ou caminhos entre os locais;
* 📏 Os **pesos** representam a distância, o tempo ou o custo do caminho.

### Exemplo:

```text
Restaurante
     |
     | 2 km
     |
   Centro
   /    \
  /      \
3 km      4 km
/          \
Moema      Vila Mariana
```

Dessa forma, o sistema consegue analisar diferentes caminhos e encontrar a rota mais eficiente.

---

# 🔎 Algoritmos de Busca

Os algoritmos de busca são utilizados para encontrar soluções para determinados problemas.

Neste projeto, eles podem ser utilizados para encontrar caminhos entre o restaurante e os locais de entrega.

Os principais algoritmos estudados são:

* BFS — Busca em Largura;
* DFS — Busca em Profundidade;
* A* — Algoritmo A Estrela.

---

## 🔵 BFS — Busca em Largura

A **Busca em Largura**, também conhecida como BFS (*Breadth-First Search*), explora primeiro os pontos mais próximos do local inicial.

Depois, o algoritmo continua explorando os próximos pontos.

Podemos imaginar o funcionamento do BFS como uma busca por camadas.

Primeiro, ele analisa os locais mais próximos.

Depois, analisa os locais um pouco mais distantes.

E assim continua até encontrar o destino.

### Vantagens

* Simples de entender;
* Pode encontrar caminhos com menos etapas em grafos simples;
* Pode ser utilizado para comparar diferentes algoritmos.

### Limitações

O BFS não é a melhor opção quando os caminhos possuem diferentes distâncias ou custos.

---

## 🟠 DFS — Busca em Profundidade

A **Busca em Profundidade**, também conhecida como DFS (*Depth-First Search*), funciona explorando um caminho até o máximo possível.

Se encontrar um caminho sem saída, o algoritmo volta e tenta outro caminho.

### Vantagens

* Simples de implementar;
* Pode explorar diferentes caminhos;
* Ajuda a entender a estrutura de um grafo.

### Limitações

O DFS não garante encontrar o caminho mais curto ou mais eficiente.

---

# ⭐ Algoritmo A*

O algoritmo **A***, também conhecido como **A Estrela**, é o principal algoritmo proposto para encontrar rotas mais eficientes.

Ele é bastante utilizado em problemas que envolvem:

* Mapas;
* Navegação;
* Jogos;
* Sistemas de localização;
* Otimização de rotas.

O algoritmo A* utiliza duas informações principais:

* O custo do caminho que já foi percorrido;
* Uma estimativa da distância que ainda falta para chegar ao destino.

A fórmula utilizada é:

```text
f(n) = g(n) + h(n)
```

Onde:

* `g(n)` = custo real do caminho já percorrido;
* `h(n)` = estimativa do custo até o destino;
* `f(n)` = custo total estimado.

A parte `h(n)` é chamada de **heurística**.

A heurística ajuda o algoritmo a escolher caminhos que parecem mais promissores.

### Vantagens do A*

* ⭐ Pode encontrar caminhos eficientes;
* 📍 Considera a distância ou custo;
* 🧠 Utiliza uma heurística;
* ⚡ Pode reduzir a quantidade de caminhos explorados;
* 🚚 É adequado para problemas de rotas.

Por esses motivos, o algoritmo A* é uma boa opção para o problema de entregas da Sabor Express.

---

# 📦 Agrupamento das Entregas com K-Means

Durante os horários de maior movimento, a empresa pode receber vários pedidos ao mesmo tempo.

Para facilitar a organização das entregas, será utilizado o algoritmo **K-Means**.

O K-Means é um algoritmo de aprendizado de máquina não supervisionado utilizado para dividir dados em grupos chamados de **clusters**.

No projeto, ele poderá analisar a localização das entregas e identificar quais pedidos estão próximos uns dos outros.

### Exemplo:

### 🔵 Cluster 1

* Entrega A;
* Entrega B;
* Entrega C.

### 🔴 Cluster 2

* Entrega D;
* Entrega E;
* Entrega F.

Dessa forma, as entregas próximas podem ficar no mesmo grupo.

Cada entregador pode ser responsável por uma determinada região.

---

## ⚙️ Como funciona o K-Means

De forma simples, o K-Means funciona seguindo estas etapas:

1. Define-se a quantidade de grupos;
2. O algoritmo cria pontos centrais para os grupos;
3. Cada entrega é colocada no grupo mais próximo;
4. Os pontos centrais são recalculados;
5. O processo continua até que os grupos estejam organizados.

O objetivo é fazer com que entregas próximas fiquem dentro do mesmo grupo.

---

# 🔄 Funcionamento da Solução

A solução proposta funciona em algumas etapas:

```text
PEDIDOS DE ENTREGA
        ↓
COLETA DOS DADOS
        ↓
AGRUPAMENTO COM K-MEANS
        ↓
ORGANIZAÇÃO DAS ENTREGAS
        ↓
CRIAÇÃO DO GRAFO
        ↓
BUSCA COM ALGORITMO A*
        ↓
DEFINIÇÃO DA MELHOR ROTA
        ↓
REDUÇÃO DE TEMPO E DISTÂNCIA
```

---

## 1️⃣ Recebimento dos Pedidos

Primeiramente, o sistema recebe as informações sobre os pedidos.

Essas informações podem incluir:

* Local da entrega;
* Bairro;
* Coordenadas;
* Distância aproximada.

Os dados podem ser armazenados em arquivos CSV.

---

## 2️⃣ Agrupamento das Entregas

O algoritmo K-Means analisa os locais das entregas.

As entregas próximas são agrupadas.

Cada grupo pode representar uma região de atendimento.

---

## 3️⃣ Criação do Grafo

A cidade é representada como um grafo.

Os locais são os nós.

As ruas são as conexões.

Cada conexão possui um peso relacionado à distância ou ao tempo.

---

## 4️⃣ Busca pela Melhor Rota

O algoritmo A* analisa os caminhos disponíveis.

Ele utiliza o custo dos caminhos e uma estimativa para encontrar rotas mais eficientes.

Assim, o sistema pode sugerir caminhos melhores para os entregadores.

---

## 5️⃣ Análise dos Resultados

Depois que as rotas são calculadas, os resultados podem ser analisados.

Algumas informações importantes são:

* Distância percorrida;
* Tempo estimado;
* Número de caminhos explorados;
* Quantidade de entregas por grupo;
* Comparação entre os algoritmos.

---

# 📊 Comparação entre os Algoritmos

| Algoritmo | Como funciona                              | Encontra o melhor caminho?      | Utiliza heurística? |
| --------- | ------------------------------------------ | ------------------------------- | ------------------- |
| BFS       | Explora os caminhos mais próximos primeiro | Em grafos simples               | ❌ Não               |
| DFS       | Explora um caminho até o máximo possível   | ❌ Não garante                   | ❌ Não               |
| A*        | Considera custo e estimativa               | ✅ Sim, dependendo da heurística | ✅ Sim               |
| K-Means   | Agrupa entregas próximas                   | Não se aplica                   | ❌ Não               |

O BFS e o DFS podem ser utilizados para comparar diferentes formas de busca.

O A* é mais adequado para encontrar rotas porque considera os custos dos caminhos.

O K-Means possui uma função diferente, sendo utilizado para organizar as entregas em grupos.

---

# 📈 Métricas para Avaliação

Para analisar se a solução está funcionando bem, podem ser utilizadas algumas métricas.

## 📏 Distância Total Percorrida

Essa métrica mostra a distância total percorrida pelos entregadores.

O objetivo é verificar se a solução consegue reduzir os quilômetros percorridos.

Quanto menor for a distância, menor pode ser o gasto com combustível.

---

## ⏱️ Tempo Estimado das Entregas

Essa métrica permite analisar quanto tempo é necessário para realizar as entregas.

A solução busca reduzir o tempo necessário para chegar aos destinos.

---

## 🔍 Número de Nós Explorados

Essa métrica mostra quantos pontos do grafo foram analisados pelos algoritmos.

Ela pode ser utilizada para comparar a eficiência dos algoritmos.

---

## 📦 Organização das Entregas

Também será possível analisar como as entregas foram divididas entre os clusters.

O objetivo é verificar se os pedidos próximos ficaram no mesmo grupo.

---

# ✅ Benefícios Esperados

A utilização da solução Rota Inteligente pode trazer vários benefícios para a empresa Sabor Express.

Entre eles:

* 🚚 Redução da distância percorrida;
* ⏱️ Entregas mais rápidas;
* ⛽ Redução do consumo de combustível;
* 📦 Melhor organização dos pedidos;
* 👥 Melhor divisão das entregas;
* ⏳ Redução de atrasos;
* 😊 Maior satisfação dos clientes;
* 💰 Redução dos custos operacionais.

---

# ⚠️ Limitações da Solução

Mesmo sendo uma solução útil, existem algumas limitações.

Uma delas está relacionada à qualidade dos dados.

Se os dados sobre ruas, distâncias ou locais estiverem incorretos, as rotas calculadas também podem apresentar problemas.

Além disso, uma versão inicial do projeto pode não considerar informações em tempo real.

Na realidade, vários fatores podem mudar o tempo de uma entrega, como:

* 🚗 Trânsito;
* 🚧 Obras;
* ⚠️ Acidentes;
* 🌧️ Chuvas;
* ⏰ Horários de pico.

Outro ponto é que o K-Means precisa que seja definida previamente a quantidade de grupos.

Em algumas situações, pode ser difícil saber qual é a quantidade ideal de clusters.

---

# 🚀 Melhorias Futuras

O projeto poderá ser melhorado futuramente com novas tecnologias e funcionalidades.

Algumas possibilidades são:

* 🛰️ Utilização de GPS;
* 🚦 Informações de trânsito em tempo real;
* 🗺️ Integração com APIs de mapas;
* 🔄 Atualização automática das rotas;
* 📊 Utilização de dados históricos;
* 🤖 Aprendizado por reforço;
* 🧬 Algoritmos genéticos;
* 📍 Utilização do DBSCAN para agrupamento;
* 👥 Consideração da quantidade de entregadores;
* 📦 Consideração da quantidade de pedidos.

Essas melhorias poderiam tornar a solução ainda mais próxima de sistemas utilizados por empresas reais de delivery.

---

# 🧠 Inteligência Artificial no Projeto

A Inteligência Artificial é utilizada em diferentes partes do projeto.

Os algoritmos de busca ajudam a encontrar caminhos entre os locais.

O algoritmo A* utiliza custos e uma heurística para encontrar rotas mais eficientes.

O K-Means utiliza aprendizado não supervisionado para identificar grupos de entregas próximas.

A combinação dessas técnicas permite organizar melhor os pedidos e encontrar rotas mais adequadas.

Dessa forma, o projeto demonstra como conceitos de Inteligência Artificial podem ser aplicados para resolver problemas reais.

---

# 🏁 Conclusão

O projeto **Rota Inteligente: Otimização de Entregas com Algoritmos de IA** apresenta uma proposta para melhorar a organização das entregas da empresa fictícia Sabor Express.

A utilização de grafos permite representar os locais e as ruas da região.

O algoritmo A* pode ser utilizado para encontrar caminhos mais eficientes entre os pontos de entrega.

O K-Means ajuda a organizar os pedidos em grupos de acordo com a proximidade entre eles.

Com a combinação dessas técnicas, é possível criar uma solução capaz de reduzir a distância percorrida e melhorar a organização das entregas.

Mesmo sendo uma versão inicial, o projeto demonstra como algoritmos de Inteligência Artificial podem ser utilizados para resolver problemas do dia a dia.

No futuro, a solução poderá ser melhorada com informações de trânsito em tempo real, GPS e algoritmos mais avançados.

Assim, este projeto mostra como a Inteligência Artificial pode ajudar empresas a reduzir custos, melhorar seus processos e oferecer um serviço melhor aos clientes.

---

# 📚 Referências

* Estudo de caso UPS — ORION (On-Road Integrated Optimization and Navigation);
* Materiais sobre otimização logística e clustering;
* Estudos sobre Inteligência Artificial aplicada à otimização de rotas;
* Conteúdos da disciplina Artificial Intelligence Fundamentals.

# Template Repositório IA do Processo Seletivo Intensivo Laboratório Maker

## Objetivo

O objetivo desta etapa do processo seletivo é avaliar as competências técnicas dos candidatos à etapa de Intensivo em Laboratório Maker. Neste teste prático, você será apresentado a um conjunto de dados relacionado à classificação de dígitos manuscritos (MNIST).

Seu objetivo é realizar a classificação utilizando um modelo de Visão Computacional, exibindo a acurácia do modelo, salvando-o no formato Keras (.h5) e, em seguida, exportando-o para o formato otimizado LiteRT (TensorFlow Lite - TFLite).

## Sobre os dados

O conjunto de dados definidos para este teste é o MNIST, que contém imagens de dígitos manuscritos (0-9). Este dataset faz parte da biblioteca do TensorFlow e será utilizado para treinar e avaliar seu modelo de classificação.

<img width="392" height="230" alt="image" src="https://github.com/user-attachments/assets/2e510ab2-22c4-4910-80bd-c84e975189f1" />

Figura – Dataset MNIST

## Requisitos

### Etapa 1: 

<img width="196" height="53" alt="image" src="https://github.com/user-attachments/assets/187e22a2-0a05-4f45-8db3-cd32eadb0ec4" />

1. Carregar o dataset MNIST utilizando a biblioteca TensorFlow.
2. Treinar um modelo de classificação de dígitos.
3. Exibir a acurácia do modelo após o treinamento.
4. Salvar o modelo treinado no formato Keras (.h5).

### Etapa 2: 

1. Exportar o modelo treinado para o formato TFLite, utilizando uma otimização como o 'dynamic range'.

## Estrutura de Pastas

A estrutura de pastas que você utilizará será semelhante a esta:

C:.
│ model.h5
│ requirements.txt
│ train_model.py
│ optimize_model.py
│ model.tflite
│
├───.github
│ └───workflows
│ ci.yml

- **model.h5**: Modelo treinado no formato Keras.
- **requirements.txt**: Lista de bibliotecas necessárias para o projeto.
- **train_model.py**: Script para treinar o modelo.
- **optimize_model.py**: Script para otimizar o modelo.
- **model.tflite**: Modelo otimizado no formato TensorFlow Lite.
- **.github**: Diretório para configurações do GitHub Actions, se necessário.

## Instruções para Início

### 1. Criar uma conta no GitHub

- Acesse <a data-v-2acd734d="" href="https://github.com/" class="reference-btn" target="_blank">https://github.com/</a>e clique em "Sign up".
- Siga as instruções para criar sua conta.

### 2. Clonar este repositório

Após criar sua conta, siga estes passos para clonar o repositório:

1. No seu terminal ou prompt de comando, navegue até o diretório onde você deseja clonar o repositório.
2. Execute o seguinte comando (substitua `<URL do repositório>` pela URL do repositório que você deseja clonar):
   ```bash
   git clone <URL do repositório>

3. Navegue até a pasta do repositório clonado:
   cd nome-do-repositorio

### 3. Critérios de Avaliação
- Escolha da biblioteca adequada para o treinamento do modelo.
- Realização das etapas de treinamento e teste de forma correta.
- Uso de métricas adequadas para avaliar o desempenho do modelo.
- Otimização do modelo para melhorar a acurácia e eficiência.
- Implementação de boas práticas de codificação e organização do projeto.
**Observações Adicionais**
Os candidatos poderão utilizar como referência os exemplos e materiais dos cursos de Fundamentos de IA para Sistemas Embarcados, Sistemas de Visão Computacional e Otimização de Modelos em Sistemas Embarcados. Esses recursos podem fornecer insights valiosos e orientações para a realização desta etapa prática.

### 4. Instruções de Entrega
- Crie um fork do repositório no seu GitHub.
- Faça o push do código desenvolvido no seu GitHub.
- Inclua um arquivo chamado README.md do projeto, explicando:
   - Decisão da arquitetura utilizada.
   - Lista de bibliotecas de terceiros utilizadas.
   - Quais requisitos obrigatórios que não foram entregues.
   - Após finalizar, submeta o link do repositório do GitHub (ex. https://github.com/seuusuariogithub/nomedorepositorio).

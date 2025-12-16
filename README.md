# 🚀 Desafio Técnico  
## Processo Seletivo – Laboratório Maker | Edge AI

Bem-vindo(a) à **etapa prática do processo seletivo para o Laboratório Intensivo Maker**.

Esta atividade tem como objetivo avaliar competências técnicas relacionadas a **Visão Computacional**, **Machine Learning** e **implantação de modelos em dispositivos embarcados (Edge AI)**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

---

## 📌 Navegação Rápida

- 🏁 [Passo 0 – Antes de Tudo](#-passo-0-antes-de-tudo)
- 🛠️ [Passo 1 – Preparação do Ambiente](#-passo-1-preparação-do-ambiente)
- 💻 [Passo 2 – O Desafio Técnico](#-passo-2-o-desafio-técnico)
- 📂 [Estrutura do Projeto](#-estrutura-do-projeto)
- 📚 [Material de Apoio](#-material-de-apoio)
- ⚖️ [Critérios de Avaliação](#️-critérios-de-avaliação)
- 📤 [Passo 4 – Instruções de Entrega](#-passo-4-instruções-de-entrega)
- 📝 [Relatório do Candidato](#-relatório-do-candidato)

---

## 🏁 Passo 0: Antes de Tudo

Caso ainda não possua familiaridade com o GitHub, siga **obrigatoriamente** as etapas abaixo.

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**
3. Siga as instruções para criação de uma conta gratuita

### 2️⃣ Instalação do Git

- **Windows**:  
  Baixe e instale o Git Bash em:  
  https://git-scm.com/downloads

- **Linux / macOS**:  
  Verifique se o Git já está instalado executando no terminal:
  ```bash


## 🛠️ Passo 1 Preparação do Ambiente

Para desenvolver o desafio, é necessário criar uma cópia deste repositório em sua conta pessoal e baixá-lo para o seu computador.

1️⃣ Fork do Repositório

No canto superior direito desta página, clique em Fork

Uma cópia deste repositório será criada no seu perfil do GitHub

2️⃣ Clone do Repositório

No repositório recém-criado (Fork), clique em <> Code

Copie a URL no formato HTTPS

No terminal (ou Git Bash), execute:

git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
  git --version

3️⃣ Instalação das Dependências

Instale todas as bibliotecas necessárias para execução do projeto:

pip install -r requirements.txt


## 💻 Passo 2: O Desafio Técnico

O desafio consiste na classificação de dígitos manuscritos utilizando técnicas de Visão Computacional, com posterior otimização do modelo para execução em dispositivos Edge (IoT e sistemas embarcados).

🎯 Conjunto de Dados

Será utilizado o dataset MNIST, composto por imagens de dígitos manuscritos de 0 a 9.

✔️ O dataset está disponível diretamente via TensorFlow/Keras, não sendo necessário download manual.

✅ Requisitos Obrigatórios
🧠 Etapa 1: Treinamento do Modelo (train_model.py)

Implemente no arquivo train_model.py um código que realize:

Carregamento do dataset MNIST via TensorFlow

Construção e treinamento de um modelo de classificação (Rede Neural)

Exibição da acurácia final no terminal

Salvamento do modelo treinado no formato Keras (.h5 ou .keras)

⚡ Etapa 2: Otimização do Modelo (optimize_model.py)

No arquivo optimize_model.py, implemente:

Carregamento do modelo treinado

Conversão do modelo para TensorFlow Lite (LiteRT – .tflite)

Aplicação de técnica de otimização, como:

Dynamic Range Quantization

O objetivo é reduzir o tamanho do modelo, mantendo eficiência para execução em Edge AI.

📂 Estrutura do Projeto

⚠️ Atenção:
A estrutura e os nomes dos arquivos não devem ser alterados, pois o processo de correção automática depende disso.

seu-repositorio/
├── .github/workflows/   # 🚫 Não alterar (automação da correção)
├── train_model.py       # ✏️ Implementação do treinamento
├── optimize_model.py    # ✏️ Implementação da otimização/conversão
├── requirements.txt     # 📄 Dependências do projeto
├── model.h5             # 🤖 Modelo treinado (gerado)
├── model.tflite         # ⚡ Modelo otimizado (gerado)
└── README.md            # 📝 Relatório final do candidato

📚 Material de Apoio

Os candidatos podem utilizar como referência os conteúdos abordados nos cursos da etapa anterior, incluindo:

Fundamentos de IA para Sistemas Embarcados

Sistemas de Visão Computacional

Otimização de Modelos em Sistemas Embarcados

Esses materiais fornecem conceitos, exemplos práticos e trechos de código relevantes para o desafio.

## ⚖️ Critérios de Avaliação

A avaliação considerará os seguintes aspectos:

- Funcionalidade

- Execução correta dos scripts

- Geração dos arquivos .h5 e .tflite

- Machine Learning

   - Arquitetura do modelo

   - Métricas e abordagem adotadas

   - Conversão correta para TensorFlow Lite

   - Preenchimento do relatório



## 📤 Passo 4: Instruções de Entrega
✔️ Validação Local

Antes do envio, execute os scripts e confirme que os arquivos abaixo foram gerados:

- model.h5

- model.tflite

## 📝 Relatório

Preencha a seção Relatório do Candidato ao final deste arquivo README.md.

⬆️ Envio do Código
git add .
git commit -m "Entrega do desafio técnico - Seu Nome"
git push origin main

🔍 Verificação Automática

- Acesse a aba Actions no GitHub

- Verifique se o workflow foi executado com sucesso (✅)

- Em caso de erro (❌), consulte os logs, corrija e envie novamente

📎 Submissão Final

- Copie o link do seu repositório e envie conforme orientações do processo seletivo.

## 📝 Relatório do Candidato

Nome Completo:
[Preencha aqui]

1️⃣ Resumo da Arquitetura

Descreva a arquitetura do modelo desenvolvido (camadas, tipo de rede, funções de ativação, etc.).

2️⃣ Bibliotecas Utilizadas

Liste as principais bibliotecas e versões utilizadas.

3️⃣ Técnica de Otimização

Explique a estratégia adotada para conversão e otimização do modelo.

4️⃣ Resultados Obtidos

Informe a acurácia final no conjunto de testes.

5️⃣ Comentários Adicionais (Opcional)

Relate eventuais dificuldades, limitações ou observações relevantes.


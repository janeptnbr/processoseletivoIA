# 🚀 Desafio Técnico  
## Processo Seletivo – Laboratório Maker | AI

Bem-vindo(a) à **etapa prática do processo seletivo para o Laboratório Intensivo Maker**.

Esta atividade tem como objetivo avaliar competências técnicas relacionadas a **Visão Computacional**, **Machine Learning** e **Otimização de modelos para sistemas embarcados (Edge AI)**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

---

## 📌 Navegação Rápida

- 🏁 [Passo 0 – Antes de Tudo](#-passo-0-antes-de-tudo)
- 🛠️ [Passo 1 – Preparação do Ambiente](#-ambiente)
- 💻 [Passo 2 – O Desafio Técnico](#-passo-2-o-desafio-técnico)
- 🎯 [Conjunto de Dados](#-conjunto-de-dados)
- 📂 [Estrutura do Projeto](#-estrutura-do-projeto)
- 📚 [Material de Apoio](#-material-de-apoio)
- ⚖️ [Critérios de Avaliação](#️-critérios-de-avaliação)
- 📤 [Passo 4 – Instruções de Entrega](#-passo-4-instruções-de-entrega)
- 📝 [Relatório do Candidato](#-relatório-do-candidato)

---

## 🏁 Passo 0: Antes de Tudo

Caso você **nunca tenha utilizado Git ou GitHub**, não se preocupe.  
Siga atentamente as etapas abaixo.

### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

📌 *O GitHub será utilizado para envio, versionamento e correção automática do seu projeto.*

---

### 2️⃣ Instalação do Git

O **Git** é a ferramenta que permite versionar e enviar seu código para o GitHub.

- **Windows**  
  Baixe e instale o **Git Bash**:  
  https://git-scm.com/downloads

- **Linux / macOS**  
  Verifique se o Git já está instalado:
  ```bash
  git --version
  ```

---

## 🛠️ Passo 1: Preparação do Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório e baixá-la para seu computador.

### 1️⃣ Fork do Repositório

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

1. No canto superior direito desta página, clique em **Fork**
2. Uma cópia deste repositório será criada no **seu perfil do GitHub**

📌 *O Fork permite que você trabalhe de forma independente sem alterar o repositório original.*

---

### 2️⃣ Clone do Repositório

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

Agora vamos baixar o projeto para o seu computador.

1. No repositório do **seu Fork**, clique em **<> Code**
2. Copie a URL no formato **HTTPS**
3. No terminal (ou Git Bash), execute:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```

📌 *O comando `git clone` cria uma cópia local do repositório.*

---

### 3️⃣ Instalação das Dependências

Instale as bibliotecas necessárias para execução do projeto:

```bash
pip install -r requirements.txt
```

📌 *Esse comando instala automaticamente todas as dependências listadas no arquivo `requirements.txt`.*

---

## 💻 Passo 2: O Desafio Técnico

O desafio consiste em desenvolver um **modelo de Visão Computacional** capaz de **classificar dígitos manuscritos**, e posteriormente **otimizá-lo para execução em dispositivos Edge**, como sistemas embarcados e IoT.

O foco não é apenas obter alta acurácia, mas também **compreender o fluxo completo**:
treinamento → salvamento → conversão → otimização.

---

## 🎯 Conjunto de Dados

Será utilizado o dataset **MNIST**, composto por imagens de dígitos manuscritos de **0 a 9**.
<img width="500" height="294" alt="image" src="https://github.com/user-attachments/assets/f323b4cc-d759-4e05-bb58-13e4d6dc7e5b" />


✔️ O dataset já está disponível na biblioteca **TensorFlow/Keras**, não sendo necessário download manual.

📌 *O MNIST é amplamente utilizado para introdução à Visão Computacional e Redes Neurais.*

---

## ✅ Requisitos Obrigatórios

### 🧠 Etapa 1: Treinamento do Modelo (`train_model.py`)

Implemente no arquivo `train_model.py` um código que realize:

- Carregamento do dataset MNIST via TensorFlow
- Construção e treinamento de um modelo de classificação baseado em Redes Neurais Convolucionais (CNN), utilizando camadas Conv2D e MaxPooling.
- Treinamento do modelo
- Exibição da **acurácia final** no terminal
- Salvamento do modelo treinado no formato **Keras** (`.h5` ou `.keras`)

📌 *O modelo salvo será utilizado na etapa de otimização.*

---

### ⚡ Etapa 2: Otimização do Modelo (`optimize_model.py`)

No arquivo `optimize_model.py`, implemente:

- Carregamento do modelo treinado
- Conversão para **TensorFlow Lite (LiteRT – `.tflite`)**
- Aplicação de técnica de otimização, como:
  - **Dynamic Range Quantization**

🎯 **Objetivo:** reduzir o tamanho do modelo, mantendo desempenho adequado para Edge AI.

---

## 📂 Estrutura do Projeto

⚠️ **Atenção:**  
A estrutura e os nomes dos arquivos **não devem ser alterados**.

```plaintext
seu-repositorio/
├── .github/
│   └── workflows/
│       └── ci.yml            # 🤖 Pipeline de correção automática (NÃO ALTERAR)
├── train_model.py            # ✏️ Treinamento do modelo
├── optimize_model.py         # ✏️ Conversão e otimização
├── requirements.txt          # 📄 Dependências do projeto
├── model.h5                  # 🤖 Modelo treinado (gerado)
├── model.tflite              # ⚡ Modelo otimizado (gerado)
└── README.md                 # 📝 Relatório final do candidato
```

---
## ⚠️ Restrições e Considerações de Engenharia

Este desafio é avaliado automaticamente por meio de um pipeline de
integração contínua (CI), executado em um ambiente controlado e
limitado de recursos computacionais.

Você **não precisa conhecer GitHub Actions** para realizar o desafio.
No entanto, é importante respeitar algumas diretrizes para garantir
que seu código execute corretamente nesse ambiente.

### Diretrizes para o Modelo

- O modelo deve ser uma **CNN simples**, adequada para aplicações de **Edge AI**.
- Evite arquiteturas muito profundas ou complexas.
- Recomenda-se utilizar **até 3 camadas convolucionais**.
- Não utilize modelos pré-treinados.
- O número de épocas deve ser **limitado** (exemplo: até 5 épocas).

### Diretrizes de Execução

- O tempo total de treinamento deve ser reduzido, para não exceder o tempo máximo de execução do pipeline automático.
- O modelo deve ser treinado utilizando apenas CPU.
- O código deve ser executável do início ao fim sem intervenção manual.

> 💡 **Importante:**  
> O objetivo do desafio não é obter a maior acurácia possível, mas sim
> demonstrar a capacidade de projetar um modelo eficiente, compatível
> com ambientes automatizados e com restrições de recursos, como é
> comum em aplicações reais de Edge AI.


---

## 📚 Material de Apoio

Os cursos realizados na etapa anterior **devem ser utilizados como referência**.

### 📘 Fundamentos de Inteligência Artificial para Sistemas Embarcados

### 👁️ Sistemas de Visão Computacional Embarcada 

### ⚙️ Otimização de Modelos em Sistemas Embarcados
Nome do cursoOtimização de Modelos em Sistemas Embarcados

📌 *Os exemplos apresentados nesses cursos podem ser adaptados e reutilizados neste desafio.*

---

## ⚖️ Critérios de Avaliação

A avaliação considerará:

- **Funcionalidade**  
  Execução correta dos scripts e geração dos arquivos `.h5` e `.tflite`.

- **Machine Learning**  
  Arquitetura do modelo, métricas e abordagem adotadas.

- **Edge AI**  
  Conversão correta para TensorFlow Lite e aplicação de otimização.

- **Documentação**  
  Preenchimento adequado do relatório.

---

## 📤 Passo 4: Instruções de Entrega

### ✔️ Validação Local

Antes do envio, execute os scripts e confirme a geração dos arquivos:
- `model.h5`
- `model.tflite`

---

### ⬆️ Envio do Código

```bash
git add .
git commit -m "Entrega do desafio técnico - Seu Nome"
git push origin main
```

---

### 🔍 Verificação Automática

1. Acesse a aba **Actions** no GitHub
2. Verifique se o workflow foi executado com sucesso (✅)
3. Em caso de erro (❌), consulte os logs, corrija e envie novamente

---

### 📎 Submissão Final

Copie o link do seu repositório e envie conforme orientações do processo seletivo no Moodle.

---

## 📝 Relatório do Candidato

**Nome Completo:**  
[Preencha aqui]

### 1️⃣ Resumo da Arquitetura
[Descreva a arquitetura do modelo]

### 2️⃣ Bibliotecas Utilizadas
[Liste bibliotecas e versões]

### 3️⃣ Técnica de Otimização
[Explique a estratégia adotada]

### 4️⃣ Resultados Obtidos
[Informe a acurácia final]

### 5️⃣ Comentários Adicionais (Opcional)
[Observações relevantes]

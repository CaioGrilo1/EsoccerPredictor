# ⚽ EsoccerPredictor Online v3.0  
Sistema inteligente de previsão de gols em partidas **eSoccer (FIFA 12 minutos)**

---

## 🧠 Sobre o projeto
O **EsoccerPredictor** é um programa desenvolvido para estimar a quantidade provável de gols — por partida e por jogador — com base em **dados reais coletados automaticamente** dos sites:

- [GTLeagues.com](https://www.gtleagues.com/past-results)  
- [eSoccerBet.com.br](https://esoccerbet.com.br/fifa-12-minutos/)

O sistema utiliza aprendizado contínuo (machine learning leve) e observa fatores comportamentais e de contexto:

- Últimos **20 jogos** de cada jogador  
- Desempenho **head-to-head** entre jogadores  
- Efeito do **time utilizado** (maiores clubes da Europa elevam médias de gols)  
- Fator comportamental: após marcar **2+ gols no primeiro confronto**,  
  a chance de repetir o feito no **segundo confronto da rodada** diminui.

---

## ⚙️ Funcionalidades principais
✅ Coleta automática e invisível de dados online  
✅ Armazena histórico local para aprendizado contínuo  
✅ Estima gols prováveis e placar agregado  
✅ Ajusta probabilidades com base em comportamento observado  
✅ Interface simples (basta 1 clique para rodar)

---

## 🖥️ Como instalar e rodar
### 1️⃣ Pré-requisitos
- Windows 10 ou superior  
- Google Chrome instalado  
- Python 3.9 ou superior ([Baixar aqui](https://www.python.org/downloads/))  
  > Durante a instalação do Python, **marque a opção "Add Python to PATH"**

---

### 2️⃣ Estrutura de pastas esperada

Baixe o **ChromeDriver** compatível com sua versão do navegador:  
👉 https://chromedriver.chromium.org/downloads  
Coloque o arquivo `chromedriver.exe` dentro da pasta `drivers`.

---

### 3️⃣ Como executar
1. Dê **duplo clique** no arquivo `run_esoccer.bat`  
2. Aguarde o programa:
   - Instalar as dependências (primeira vez apenas)
   - Coletar os dados automaticamente
   - Gerar o arquivo de previsões  
3. Ao final, você verá algo como:


---

## 📊 Exemplo de saída

---

## 🔄 Atualizações automáticas
Sempre que você executar o programa:
- Ele coleta os dados mais recentes;
- Treina o modelo novamente;
- Atualiza o arquivo `data/match_predictions.csv`.

---

## 🧩 Aprendizado contínuo
O sistema aprende a partir dos últimos **20 jogos** de cada jogador,  
ajustando automaticamente os pesos de:
- Média de gols do jogador  
- Força do time utilizado  
- Histórico direto entre jogadores  
- Comportamento após sequência de vitórias ou goleadas

---

## 🧑‍💻 Desenvolvido por
**Caio César Grilo Oliveira** — idealização e análise comportamental  
**Assistência técnica:** ChatGPT (GPT-5)  

---

## 📬 Contato
Caso queira expandir o projeto (por exemplo, incluir interface visual, app web, ou predições em tempo real), basta abrir uma *Issue* no GitHub ou adicionar novos módulos Python.

---

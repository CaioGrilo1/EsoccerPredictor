# ===============================================================
# EsoccerPredictor v3.0 (Online Learning Version)
# Autor: Caio César Grilo Oliveira (conceito)
# Desenvolvido com apoio GPT-5
# ===============================================================

import os
import time
import random
import pandas as pd
import numpy as np
from datetime import datetime
from sklearn.linear_model import LinearRegression
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# ===============================================================
# CONFIGURAÇÕES
# ===============================================================

DATA_DIR = "data"
HISTORY_FILE = os.path.join(DATA_DIR, "match_history.csv")
PRED_FILE = os.path.join(DATA_DIR, "match_predictions.csv")

GTLEAGUES_URL = "https://www.gtleagues.com/past-results"
ESOCCERBET_URL = "https://esoccerbet.com.br/fifa-12-minutos/"

# ===============================================================
# COLETA DE DADOS
# ===============================================================

def get_driver():
    """Inicializa o Chrome em modo invisível"""
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    service = Service("drivers/chromedriver.exe")
    return webdriver.Chrome(service=service, options=chrome_options)

def coletar_dados():
    """Extrai resultados de GTLeagues e eSoccerBet"""
    driver = get_driver()
    dados = []

    for site in [GTLEAGUES_URL, ESOCCERBET_URL]:
        try:
            driver.get(site)
            time.sleep(3)
            html = driver.page_source
            soup = BeautifulSoup(html, "html.parser")

            linhas = soup.find_all("tr")
            for linha in linhas:
                cols = [c.get_text(strip=True) for c in linha.find_all("td")]
                if len(cols) >= 3:
                    # Exemplo: PlayerA (PSG) 2–1 PlayerB (Real Madrid)
                    dados.append(cols)
        except Exception as e:
            print(f"[ERRO] Falha ao coletar {site}: {e}")

    driver.quit()
    return dados

# ===============================================================
# TRATAMENTO E ANÁLISE
# ===============================================================

def processar_dados(dados):
    """Formata os dados em DataFrame e salva histórico"""
    if not dados:
        return None

    df = pd.DataFrame(dados, columns=["Col1", "Col2", "Col3"])
    df["timestamp"] = datetime.now()

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if os.path.exists(HISTORY_FILE):
        old = pd.read_csv(HISTORY_FILE)
        df = pd.concat([old, df]).drop_duplicates().tail(200)

    df.to_csv(HISTORY_FILE, index=False)
    return df

# ===============================================================
# MODELO DE PREVISÃO DE GOLS
# ===============================================================

def calcular_probabilidades(df):
    """Treina modelo simples e estima gols esperados"""

    # Simula estrutura de dataset (substituir por parsing real)
    players = ["JogadorA", "JogadorB", "JogadorC", "JogadorD"]
    teams = ["PSG", "Real Madrid", "Barcelona", "Liverpool"]

    # Base sintética (para exemplo)
    registros = []
    for p in players:
        for t in teams:
            media = random.uniform(0.8, 2.5)
            registros.append([p, t, media])

    base = pd.DataFrame(registros, columns=["jogador", "time", "media_gols"])

    # Ajusta comportamento especial no 2º confronto
    base["ajuste_comportamental"] = np.where(
        base["media_gols"] >= 2,
        base["media_gols"] * 0.7,
        base["media_gols"]
    )

    # Aprendizado simples (mock)
    X = np.arange(len(base)).reshape(-1, 1)
    y = base["ajuste_comportamental"]
    model = LinearRegression().fit(X, y)

    base["gols_estimados"] = model.predict(X)

    base.to_csv(PRED_FILE, index=False)
    return base

# ===============================================================
# INTERFACE SIMPLES
# ===============================================================

def main():
    print("\n⚽ Coletando dados mais recentes de eSoccer ...")
    dados = coletar_dados()

    print("📊 Processando histórico ...")
    df = processar_dados(dados)

    print("🤖 Calculando probabilidades de gols ...")
    pred = calcular_probabilidades(df)

    print("\n✅ Previsões concluídas! Confira em:")
    print(f"   {os.path.abspath(PRED_FILE)}")

if __name__ == "__main__":
    main()

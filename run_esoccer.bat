@echo off
title Esoccer Predictor v3
echo Iniciando o EsoccerPredictor Online...
echo.

if not exist venv (
    python -m venv venv
)

call venv\Scripts\activate
echo Instalando dependências...
pip install -r requirements.txt >nul

echo.
echo Executando o sistema...
python esoccer_predictor_v3.py

echo.
echo ======================================
echo Previsões geradas com sucesso!
echo Pressione qualquer tecla para sair...
pause >nul

#!/bin/bash

# Запускаем бота в фоне
python bot.py &

# Запускаем FastAPI
uvicorn main:app --host 0.0.0.0 --port $PORT

#!/bin/bash
docker run -it -v $(pwd):/app rasa/rasa:2.0.3-full run 
  --model models --enable-api --cors "*" --debug -p $PORT
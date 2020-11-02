#!/bin/bash
docker run -v $(pwd):/app rasa/rasa:2.0.3-full train --fixed-model-name model

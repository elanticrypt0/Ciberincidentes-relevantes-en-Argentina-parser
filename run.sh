#!/bin/bash

echo 'Ejecutando...'

python3 ./convert_timeline.ipynb && python3 ./convert_datosenfuga.ipynb && python3 ./merge_data.ipynb
# Studienarbeit Visual Analytics mit Fitnessdaten
Diese Repository enthält die Ausarbeitung und den Quellcode der Studienarbeit Visual Analytics mit Fitnessdaten von David Schönberger.

## Visualisierungen
Um die implementierten Visualisierungen zu nutzen müssen zuerst die Verzeichnisse src/data/v1/ und src/data/v2/ angelegt werden. In diesen Verzeichnissen werden die zu visualisierenden FIT-Dateien abgelegt.
Die Visualisierungen sind in Jupyter-Notebooks implementiert. Die notwendigen Abhängigkeiten sind in src/requirements.txt dokumentiert und können mit pip installiert werden.
```
pip install -r src/requirements.txt
```

Wenn alle Abhängigkeiten installiert sind kann ein Jupyter Server gestartet und die Visualisierungen können genutzt werden.
```
jupyter notebook
```
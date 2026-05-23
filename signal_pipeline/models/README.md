# Models

Trained classifier models are saved here.

## File format

Models are saved using joblib:

```python
classifier.save('signal_pipeline/models/classifier.pkl')
```

## Naming convention

```
classifier_<participant_id>_<date>.pkl
```

Example:
```
classifier_p001_2026-05-23.pkl
```

## What is not committed here

Raw participant data and personally identifiable information are never committed to this repository. See datasets/ and .gitignore.

## Loading a saved model

```python
from classifier import SatiClassifier
clf = SatiClassifier.load('signal_pipeline/models/classifier_p001_2026-05-23.pkl')
```

# canvas_kaboom

A minimal demo app showcasing broken canvas interactions under near-default
configuration in celery 3.1.x

## chord_chain

A chord with a chain as its callback fails spectacularly.

Expected use:
* Run ```chord_chain worker --config=canvas_kaboom.config```
* Run ```chord_chain shell --config=canvas_kaboom.config```
```python
from canvas_kaboom.chord_chain import works, fails
works()
fails()
```
* Observe output in worker

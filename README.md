## Логирование кода python

```python
from visual_logging import VisualLogger
from time import sleep

logger = VisualLogger(online=True, file='tracing.log')


@logger.logit
def g(x):
    if x > 0:
        g(x - 1)
    else:
        return x


@logger.logit
def f(a):
    sleep(1)
    return g(a)


f(3)

```
Содержание файла `tracing.log`
```log
  *  *  *  g [0.0] -> 0
  *  *  g [0.0 : 0.0]
  *  g [0.0 : 0.0]
  g [0.001 : 0.0]
f [1.002 : 1.001]
```
Каждый вызов логируемой функции замеряется по времени и записывается в файл

Если параметр file не задан, вывод пишется в stdout

Декоратор `@logger.logit` можно применять к функциям и к классам, тогда будут 
проиндексированы все его методы

Пример файла example
```
python3 example.py
```
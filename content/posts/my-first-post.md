+++
date = '2026-01-28T14:09:09+08:00'
draft = false
title = 'Notes for *Neural Network From Zero to Hero*'
+++

大模型课程

auto grad
makemore
## MLP

```py
def class Value:
    def __init__(self, data, _op='', _backward=None, _children=[], _prevs=None, _label=''):
        self.data = data
        self._op = _op
        self._backward = _backward
        self._children = _chidren
        self._prevs = set(self._children)
        self._label = _label
```
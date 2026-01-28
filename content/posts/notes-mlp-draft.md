+++
title = '神经网络笔记：MLP（草稿）'
date = '2026-01-28T17:00:00+08:00'
draft = true
description = '记录 MLP 的基础概念与公式，后续补充。'
tags = ['机器学习','MLP','笔记']
categories = ['学习']
author = 'zanyyan123'
math = true
+++

本草稿用于测试目录、代码块与数学公式渲染。

## 公式示例

$$
\hat{y} = \sigma(Wx + b)
$$

## 代码块示例

```python
import torch
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, x):
        return self.net(x)
```

## TODO

- 补充网络结构图
- 解释反向传播
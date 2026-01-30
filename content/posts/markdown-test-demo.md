+++
title = 'Markdown 格式测试 Demo'
date = '2026-01-28T18:00:00+08:00'
draft = true
description = '完整的 Markdown 格式演示：标题、列表、代码、公式、图片、表格等。'
tags = ['测试','Markdown','Demo']
categories = ['文档']
author = 'zanyyan123'
math = true
+++

本文展示所有常用 Markdown 格式，用于验证博客渲染效果。

## 标题结构

### 小标题演示

#### 更小的标题

##### 五级标题

###### 六级标题

## 文本格式

这是**粗体文本**，这是*斜体文本*，这是***加粗斜体***，这是~~删除线~~。

这是`行内代码块`示例。

## 列表

### 无序列表

- 第一项
- 第二项
  - 嵌套项 1
  - 嵌套项 2
- 第三项

### 有序列表

1. 首先完成这个
2. 然后做这个
   1. 子步骤 1
   2. 子步骤 2
3. 最后完成这个

## 代码块

### Python 代码

```python
def fibonacci(n):
    """计算斐波那契数列"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# 调用
result = fibonacci(10)
print(f"第10项: {result}")
```

### JavaScript 代码

```javascript
const greet = (name) => {
    return `Hello, ${name}!`;
};

console.log(greet("Hugo"));
```

### Bash 脚本

```bash
#!/bin/bash
echo "Hugo 博客构建"
hugo -s ./quickstart
echo "完成！"
```

## 数学公式

### 行内公式

这是一个行内公式：$E = mc^2$，用于表示质量能量转换关系。

### 块级公式

#### 线性回归模型

$$
\hat{y} = \beta_0 + \beta_1 x
$$

#### 神经网络激活函数

$$
\sigma(z) = \frac{1}{1 + e^{-z}}
$$

#### 多元高斯分布

$$
P(x) = \frac{1}{(2\pi)^{n/2}|\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu)\right)
$$

## 引用

> 这是一个引用块。
> 可以包含多行文本。

> 这是嵌套引用
> > 更深层的引用
> > > 甚至更深

## 链接和图片

[链接到 Hugo 官方文档](https://gohugo.io)

[链接到 GitHub](https://github.com)

### 图片示例

![示例图片](data:image/jpeg;base64,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)

## 表格

| 特性 | 说明 | 状态 |
|------|------|------|
| 本地搜索 | JSON 索引搜索 | ✅ 已启用 |
| 数学公式 | KaTeX 渲染 | ✅ 已启用 |
| 文章目录 | 自动生成 TOC | ✅ 已启用 |
| 评论系统 | Disqus/Giscus | ⏳ 计划中 |

## 分割线

---

## 任务列表

- [x] 完成基础配置
- [x] 创建示例文章
- [x] 启用本地搜索
- [x] 启用公式渲染
- [ ] 添加更多主题选项
- [ ] 优化移动端体验

## 总结

这篇文章包含了 Hugo 技术博客常用的 Markdown 格式，包括：

1. **多层级标题** - 便于组织内容
2. **代码块** - 支持语法高亮
3. **数学公式** - 使用 KaTeX 渲染
4. **列表和表格** - 清晰展示数据
5. **引用和链接** - 增强文章互动性
6. **任务列表** - 跟踪进度

现在，你的博客已经具备完整的内容渲染能力。
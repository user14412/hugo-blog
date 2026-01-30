# Hugo 技术博客 - 功能接口速查表

> 网站已完成核心功能搭建并提交到 GitHub。本表列出所有常用操作及配置修改方法。

---

## 📝 博客文章操作

### 1. 创建新文章

```bash
hugo new posts/文章-标题.md
```

自动生成的 Frontmatter 模板（见 `archetypes/default.md`）：
```toml
+++
date = '2026-01-29T12:00:00+08:00'
draft = true
title = '文章标题'
description = ''
tags = []
categories = []
author = ''
math = true
+++
```

**重要**：
- `title` 就是文章标题，正文**不要**重复写 H1
- 正文从 `## 二级标题` 开始
- `draft = false` 时文章发布可见
- `draft = true` 时文章仅本地可见（用 `hugo -D` 构建时显示）
- `math = true` 启用该文章的数学公式渲染

### 2. 删除文章

直接删除 `content/posts/` 中对应的 `.md` 文件，重新构建即可。

### 3. 编辑文章

修改 `content/posts/` 中的 `.md` 文件，保存后 `hugo server` 会自动热刷新。

---

## 🎨 网站外观和主题配置

### 4. 切换深浅主题

**当前配置**：固定浅色主题

修改位置：`hugo.toml`
```toml
[params]
    defaultTheme = "light"  # 浅色
    # defaultTheme = "dark"   # 深色（需完善）
    # defaultTheme = "auto"   # 跟随系统
```

### 5. 修改字体和间距

**主要配置文件**：`assets/css/extended/custom.css`

常用修改项：
```css
:root {
  --line-height: 1.8;      /* 行高，改为 2.0 会更宽松 */
  --font-size-base: 16px;  /* 基础字号，改为 18px 会更大 */
}

body {
  font-family: "字体名称";  /* 修改正文字体 */
}

h1, h2, h3, h4 {
  margin-top: 1.5em;       /* 标题上方间距 */
  margin-bottom: 0.8em;    /* 标题下方间距 */
}

p {
  margin-bottom: 1.2em;    /* 段落间距 */
}
```

### 6. 修改代码块样式

```css
pre {
  border-radius: 8px;      /* 圆角大小 */
  padding: 1.2rem;         /* 内边距 */
}

code {
  font-family: "Consolas"; /* 代码字体 */
  font-size: 0.95em;       /* 代码字号 */
}
```

### 7. 修改链接样式

```css
a {
  text-decoration: underline;      /* 链接样式 */
  text-decoration-thickness: 1px;  /* 下划线粗细 */
  text-underline-offset: 4px;      /* 下划线偏移 */
}

a:hover {
  text-decoration-thickness: 2px;  /* 悬停时下划线变粗 */
}
```

### 8. 修改 Favicon

**方法**：替换 `static/images/logo.svg` 文件或放置其他格式的图标

配置位置：`hugo.toml`
```toml
[params.assets]
    favicon = "./images/logo.svg"
```

---

## 🔍 搜索功能

### 9. 启用/禁用本地搜索

**当前状态**：已启用

验证方法：
1. 构建站点：`hugo`
2. 查看 `public/index.json` 是否存在
3. 访问 `/search` 页面输入关键词搜索

配置位置：`hugo.toml`
```toml
[outputs]
    home = ["HTML", "RSS", "JSON"]  # JSON 用于搜索索引
```

---

## 📐 数学公式支持

### 10. 在文章中使用数学公式

**行内公式**：
```markdown
这是一个行内公式：$E = mc^2$
```

**块级公式**：
```markdown
$$
\hat{y} = \beta_0 + \beta_1 x
$$
```

**启用/禁用全局数学支持**：`hugo.toml`
```toml
[params]
    math = true  # 全局启用
```

**单篇文章启用/禁用**：Frontmatter 中
```toml
math = true   # 启用该文章的公式
# math = false  # 禁用该文章的公式
```

---

## ⬆️ 回到顶部按钮

### 11. 自定义回到顶部按钮

**当前行为**：
- 滚动超过 300px 后出现在右下角
- 圆形按钮，点击平滑滚回顶部

**修改位置**：`assets/css/extended/custom.css`

```css
#scroll-to-top {
  bottom: 2rem;        /* 距底部距离 */
  right: 2rem;         /* 距右边距离 */
  width: 48px;         /* 按钮宽度 */
  height: 48px;        /* 按钮高度 */
  border-radius: 50%;  /* 圆形 */
  background: var(--primary);  /* 按钮背景色 */
}
```

**修改触发阈值**：`layouts/partials/extend_footer.html`
```javascript
if (window.pageYOffset > 300) {  // 改为其他数值，如 500、100
  btn.classList.add('show');
}
```

---

## 🏠 首页和菜单配置

### 12. 修改首页个人简介

**配置位置**：`hugo.toml`

```toml
[params.profileMode]
    enabled = true
    title = "你好，我是..."
    subtitle = "zanyyan123"
    imageUrl = "https://avatars.githubusercontent.com/u/你的ID?s=400..."  # 头像URL
    imageTitle = "我的头像"
    imageWidth = 120
    imageHeight = 120
```

### 13. 修改顶部菜单

```toml
[[menu.main]]
    name = "文章"
    url = "/posts"
    weight = 1

[[menu.main]]
    name = "搜索"
    url = "/search"
    weight = 2
```

**增加新菜单项**：在上述配置后添加
```toml
[[menu.main]]
    name = "关于"
    url = "/about"
    weight = 3
```

### 14. 修改社交链接

```toml
[[params.socialIcons]]
    name = "github"
    url = "https://github.com/用户名"

# 增加其他社交平台
[[params.socialIcons]]
    name = "twitter"
    url = "https://twitter.com/用户名"
```

---

## 📋 其他常用配置

### 15. 修改网站基本信息

```toml
baseURL = 'https://zanyan.xyz/'  # 网站 URL
languageCode = 'zh-cn'           # 语言
title = '我的技术博客'            # 网站标题
```

### 16. 启用/禁用功能

```toml
[params]
    ShowReadingTime = true       # 显示阅读时间
    ShowShareButtons = false     # 禁用分享按钮
    ShowToc = true              # 显示文章目录
    hideCreditText = true       # 隐藏页脚版权链接
```

### 17. 修改 Markdown 渲染设置

```toml
[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true  # 允许 HTML 原始渲染
  [markup.highlight]
    noClasses = false  # 使用 CSS class 而非 inline style
```

---

## 🔄 本地开发和发布

### 18. 本地预览网站

```bash
# 显示所有文章（包含草稿）
hugo server -D

# 仅显示发布文章
hugo server
```

访问：`http://localhost:1313`

### 19. 生成静态网站

```bash
hugo
```

生成文件保存在 `public/` 目录，可部署到 Netlify / GitHub Pages 等平台。

### 20. 提交到 GitHub

```bash
cd c:\Code\Hugo\quickstart
git add .
git commit -m "提交信息"
git push origin master
```

---

## 📦 项目结构速览

```
quickstart/
├── hugo.toml                    # 网站配置文件
├── archetypes/default.md        # 新文章模板
├── content/
│   ├── posts/                   # 博客文章目录
│   └── search.md                # 搜索页面
├── assets/
│   └── css/extended/custom.css  # 自定义样式
├── layouts/
│   └── partials/                # 页面扩展
├── static/                      # 静态文件（图片等）
├── public/                      # 生成的网站（部署用）
└── themes/PaperMod/             # 主题
```

---

## 💡 常见问题

**Q: 如何隐藏/显示某篇文章？**  
A: 修改 Frontmatter 的 `draft` 字段：`draft = true` 隐藏，`draft = false` 显示。

**Q: 如何修改阅读时间的显示？**  
A: 在 `hugo.toml` 中修改 `ShowReadingTime = false` 即可隐藏。

**Q: 如何在文章中插入图片？**  
A: 将图片放在 `static/images/` 中，在 Markdown 中引用：`![描述](../images/文件名.jpg)`

**Q: 深色模式显示不正常，怎么办？**  
A: 当前已固定浅色模式。深色模式优化在下一阶段进行。

---

**最后更新**：2026-01-29  
**版本**：Phase 1 - 核心功能稳定版

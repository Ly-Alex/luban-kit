<p align="center">
    <img alt="logo" height="15%" width="15%" src="docs/_media/logo.png">
</p>

<h1 align="center" style="margin: 30px 0 30px; font-weight: bold;">鲁班工具箱 (Luban Kit)</h1>
<h5 align="center">一个免费、开源、好用的在线工具箱</h5>

<p align="center">
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/Ly-Alex/luban-kit?style=social">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Ly-Alex/luban-kit?style=social">
    <img alt="GitHub followers" src="https://img.shields.io/github/followers/Ly-Alex?style=social">
    <img alt="GitHub issues" src="https://img.shields.io/github/issues/Ly-Alex/luban-kit">
    <img alt="GitHub" src="https://img.shields.io/github/license/Ly-Alex/luban-kit">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Ly-Alex/luban-kit">
    <img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/Ly-Alex/luban-kit/Deploy%20to%20Deta">
</p>

## 背景故事

**鲁班 [lǔ bān]**
（公元前507年—公元前444年），姬姓，公输氏，名班，人称公输盘、公输般、班输，尊称公输子，又称鲁盘或者鲁般，惯称“鲁班”。字依智，春秋时期鲁国人。《事物绀珠》、《物原》、《古史考》等不少古籍记载，木工使用的不少工具器械都是他创造的，如**曲尺**（也叫矩或鲁班尺），又如**墨斗**、**刨子**、**钻子**、**锯子**等工具传说也都是鲁班发明的。这些木工工具的发明使当时工匠们从原始繁重的劳动中解放出来，**劳动效率成倍提高**。

## 特性

- 永远不会有广告
- 源代码自由开放、随意复制
- 所有资源免费提供

## 文档

> [在线文档 : https://ly-alex.github.io/luban-kit](https://ly-alex.github.io/luban-kit/)

## 工具清单

| 名称          | 接口地址                             |
| :------------ | :----------------------------------- |
| 必应壁纸      | https://luban-kit.deta.dev/bing      |
| 必应壁纸 Json | https://luban-kit.deta.dev/bing/json |

## 目录结构

~~~
luban-kit
├── common                                                  // 公共类
├── docs                                                    // 文档目录
├── resource                                                // 蓝图
├── spider                                                  // 爬虫
├── static                                                  // 静态资源
├── templates                                               // 模板
├── init.py                                                 // 初始化封装
├── main.py                                                 // 入口
~~~

## 项目

1.本地运行（debug方式）

```shell
flask --app main --debug run
```

2.运行文档

```shell
docsify serve dosc
```

3.部署到 Deta Micros（微型服务器）

[![Deploy](https://button.deta.dev/1/svg)](https://go.deta.dev/deploy?repo=https://github.com/Ly-Alex/luban-kit)

## 关于开源协议

> 该项目为开源项目，使用请遵守 **Apache License 2.0** 协议，并务必保留作者和 Copyright 信息。

## 其他说明

> 本项目所有资源均来自于互联网，如有侵权请及时联系删除。

> 欢迎提交 [issues](https://github.com/Ly-Alex/luban-kit/issues) ，并填写清楚遇到的问题及原因、环境、复显步骤等。

## 联系作者

- QQ：776676504
- 邮箱：alexvitalik8@gmail.com

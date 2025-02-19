# GitHub Pages and Jekyll

## Introduction

GitHub Pages is a static website hosting service provided by GitHub. It allows you to publish web pages directly from a GitHub repository without the need for additional servers. Additionally, it allows you to create all the content of the page using Markdown files that are editable and viewable from VS Code.

In this project, very few of the functionalities of GitHub Pages with Jekyll will be used. For complete documentation, you can visit the tutorial [Setting up a GitHub Pages site with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll).

## Setup

It is not necessary to install anything locally or on the VM to work with GitHub Pages. Everything runs in the GitHub repository in the cloud. To enable it, simply:

- Go to Settings → Pages within your repository on GitHub.
- In the "Source" section, select the main branch and the docs/ folder, then click "Save".
- GitHub will automatically generate your site at https://your-username.github.io/your-repository/.

## Set up Jekyll

Create and modify the \_config.yml file in the docs/ folder to customize the website.
Example of basic configuration:

```yaml
title: "My Blog with Jekyll"
description: "Documentation generated with Jekyll and hosted on GitHub Pages"
theme: jekyll-theme-minimal
```

To change the design, you can use themes compatible with GitHub Pages:
[List of supported themes](https://pages.github.com/themes/)

## Create documentation

Once activated, all .md files in the `docs/` folder will be transformed into HTMLs viewable at the URL https://your-username.github.io/your-repository/ completely transparently to the user.

It is recommended to create an [index.md](index.md) with the structure of the documentation and links to the rest of the pages.

The documentation files are written in Markdown. This [beginner's tutorial](https://hackernoon.com/a-beginners-guide-to-markdown-everything-you-need-to-know-to-get-started) is good for learning the basics. It is also useful to read [how to create code blocks](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks) as it is something we will use a lot in a development project documentation.

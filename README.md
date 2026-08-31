# Butterfly Blog

基于 [Hexo](https://hexo.io/) 与 [hexo-theme-butterfly](https://github.com/jerryc127/hexo-theme-butterfly) 的中文个人博客。已开启本地搜索，评论使用 Waline（需单独部署服务端）。

## 环境

- Node.js 18+（本机开发使用 Node 24）
- pnpm

```bash
pnpm install
```

## 本地预览

```bash
pnpm exec hexo clean
pnpm exec hexo generate
pnpm exec hexo server
```

浏览器打开 [http://localhost:4000](http://localhost:4000)。

## 写文章

```bash
pnpm exec hexo new "文章标题"
```

草稿会生成在 `source/_posts/`。改完后重新 `hexo generate` 或保持 `hexo server` 即可预览。

常用页面：

- 标签：`source/tags/index.md`
- 分类：`source/categories/index.md`
- 关于：`source/about/index.md`

站点信息在 `_config.yml`，主题覆盖在 `_config.butterfly.yml`。

## 部署到 GitHub Pages

推送到 `main` 后，GitHub Actions 会执行 `hexo generate` 并发布站点。

- 仓库若叫 `butterfly-blog`，地址一般是 `https://<用户名>.github.io/butterfly-blog/`
- 仓库若叫 `<用户名>.github.io`，地址是 `https://<用户名>.github.io/`
- 本地 `_config.yml` 仍用 `http://localhost:4000`，构建时由 Actions 改成 GitHub Pages 的 `url` / `root`

仓库 Settings → Pages → Source 选 **GitHub Actions**。

## 部署 Waline 评论服务

评论后端是**另一个** Vercel 项目，需要你登录后自己完成：

1. 打开 [Waline Vercel 部署文档](https://waline.js.org/en/guide/deploy/vercel.html)，用官方模板一键部署。
2. 在 Vercel 项目的 Storage 中创建 Neon 数据库。
3. 到 Neon 的 SQL Editor 执行 [waline.pgsql](https://github.com/walinejs/waline/blob/main/assets/waline.pgsql) 建表。
4. 回到 Vercel 对最新 Deployment 执行 Redeploy。
5. 访问服务地址，打开 `/ui` 注册第一个账号（即为管理员）。
6. 把服务地址填进 `_config.butterfly.yml`：

```yaml
waline:
  serverURL: https://你的-waline.vercel.app
```

未填写真实 `serverURL` 时，文章页评论区无法加载，这是预期行为。

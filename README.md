# TV//Box v3 — musebox / TVBoxQ 版订阅

自动用 [Supprise0901/TVBox_live](https://github.com/Supprise0901/TVBox_live) 的直播分组**替换** TVmuse.json 基础配置里的直播部分，直播源失效时自动兜底。

- `base.json` — 固定模板（10 个点播站），lives 部分被上游分组完全替换，不会回流到产物里
- `build.py` — 抓上游 live.txt，过滤 `.php` 接口/广告等非直播条目，按 `#genre#` 分组合并，给每条线路加 `$线路N` 别名
- `TVBoxv3xg.json` — 每天自动生成的最终配置（电视端填这个）
- GitHub Actions 每 6 小时跑一次，上游有更新自动提交

## 订阅地址（电视端填这个）

**国内不翻墙推荐（任选一，打不开就换下一条）：**

```
https://gh-proxy.com/https://raw.githubusercontent.com/jwqsir2-lang/tvbox-live-sub/main/TVBoxv3xg.json
```

```
https://ghfast.top/https://raw.githubusercontent.com/jwqsir2-lang/tvbox-live-sub/main/TVBoxv3xg.json
```

```
https://cdn.jsdelivr.net/gh/jwqsir2-lang/tvbox-live-sub@main/TVBoxv3xg.json
```

**原始地址（需翻墙）：**

```
https://raw.githubusercontent.com/jwqsir2-lang/tvbox-live-sub/main/TVBoxv3xg.json
```

> 镜像可能有缓存延迟（jsdelivr 约 12 小时），gh-proxy / ghfast 较实时。
> 优先级建议：gh-proxy → ghfast → jsdelivr → raw。

## 手动触发更新

Actions 页面 → "Build TVBox Config" → Run workflow，立即重建一次直播源。

## 数据对照

- 2026-11-24：lives 改为**完全替换**为上游 live.txt 自带分组（🇨🇳河南地方 / 🇨🇳IPV4线路 / 🇨🇳组播线路，共 229 频道 / 595 线路），不再保留底板里的央视/卫视/新闻/体育/其他；base.json 同步更新为 TVmuse.json 版（10 个点播站）
- 2026-11-06：首次构建，5 个点播站

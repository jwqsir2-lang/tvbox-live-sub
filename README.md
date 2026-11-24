# TV//Box v3 — musebox / TVBoxQ 版订阅

自动合并 [Supprise0901/TVBox_live](https://github.com/Supprise0901/TVBox_live) 的直播源到 `TVmuse.json` 基础配置，直播源失效时自动兜底。

- `base.json` — 固定模板（10 个点播站 + 原有央视/卫视/新闻/体育/其他直播组），不会变
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

- 2026-11-24：base.json 更新为 TVmuse.json 版（10 个点播站，补齐光速/豪华/极速/金鹰/母鸡）；上游过滤后新增 3 个直播分组共 229 个频道 / 595 条线路（🇨🇳河南地方 13、🇨🇳IPV4线路 94、🇨🇳组播线路 122）
- 2026-11-06：首次构建，5 个点播站

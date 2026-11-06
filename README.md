# TVBox v3 自动订阅

老电视专用：**每次打开都能拿到最新有效直播源**。

- 点播（sites/解析）固定不变 —— 保持你桌面向我提供的原配置
- 直播源每 **6 小时**自动从 [Supprise0901/TVBox_live](https://github.com/Supprise0901/TVBox_live) 的 `live.txt` 合并一次
- 原有直播分组（央视/卫视/新闻/体育/其他）全部保留，新增上游 5 个分组
- GitHub Actions 自动构建并提交，无需手动维护

## 订阅地址（电视端填这个）

**国内不翻墙推荐（任选一）：**

```
https://gh-proxy.com/https://raw.githubusercontent.com/jwqsir2-lang/tvbox-live-sub/main/TVBoxv3xg.json
```

```
https://cdn.jsdelivr.net/gh/jwqsir2-lang/tvbox-live-sub@main/TVBoxv3xg.json
```

**原始地址（需翻墙）：**

```
https://raw.githubusercontent.com/jwqsir2-lang/tvbox-live-sub/main/TVBoxv3xg.json
```

> 镜像可能有缓存延迟（jsdelivr 约 12 小时），gh-proxy 较实时。电视上哪个能打开用哪个。
> 优先级建议：第一条 gh-proxy 打不开就换 jsdelivr，都不行才用 raw。

## 手动触发更新

Actions 页面 → "Build TVBox Config" → Run workflow，立即重建一次直播源。

## 数据对照（2026-11-06 首次构建）

- 点播站点：5 个（原样保留）
- 直播分组：5 原有 + 5 新增（河南地方/IPV4/组播/电影在线/影音剧场）
- 频道总数：347

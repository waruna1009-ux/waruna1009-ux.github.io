# 叮叮喵官网公开声明台账

更新时间：2026-06-02

用途：记录官网和 GEO 内容中的关键公开 claim，防止智能体把未验证内容写成事实。发布规则见 `/Users/ron/.hermes/agent-workspace/knowledge-base/trade/website-geo-publishing-governance.md`。

## 当前可公开基础事实

| Claim | 等级 | 状态 | 公开口径 |
|---|---|---|---|
| 公司/品牌名：烟台叮叮喵水产 / Yantai Dingdingmiao Seafood | C0 | 可用 | 可直接使用 |
| 地点：Yantai, Shandong, China / 中国山东烟台 | C0 | 可用 | 可直接使用 |
| 联系邮箱：waruan825@agentmail.to | C0 | 可用 | 可直接使用 |
| WhatsApp：+86 13954508112 | C0 | 可用 | 可直接使用 |
| 产品大类：salmon, squid, cod, shrimp, mackerel, sardine, tuna, tilapia, basa, surimi | C0/C1 | 可用 | 作为采购/出口支持范围，不保证库存 |
| 服务：产品匹配、规格沟通、单证核查、装前检验可安排、冷链协调 | C1 | 可用 | 必须使用“support/can arrange/confirmed per order” |

## 已软化或删除的高风险声明

| 原声明 | 风险 | 当前处理 |
|---|---|---|
| 10+ years / foundingDate 2011 | 缺可追踪证据 | 从首页、关于页 meta/schema/正文移除 |
| HACCP/BAP certified | 容易被理解为本公司持证 | 改为按产品、合作工厂和订单确认证书 |
| EU Approved / FDA Registered / MSC / Halal Certified | 主体、适用品类和有效期未核实 | 改为按产品、工厂和市场逐单核查 |
| Export to 15+ countries / serving Japan, Korea, USA... | 缺出货或客户记录 | 改为 multi-market buyer support |
| Every shipment undergoes pre-loading inspection | 绝对承诺 | 改为可按要求安排 |
| quotes within 24 hours / 12-24 hours | 固定服务承诺 | 改为工作日通常回复/尽快回复 |
| factory-direct / no middleman markup | 价格和供应链结构绝对化 | 改为 practical sourcing comparison / transparent trade terms |
| China's frozen mackerel exports exceeded 350,000 MT in 2025 | 缺来源 | 从首页移除，未来需来源后作为博客数据 |
| LinkedIn/Facebook sameAs | 账号归属未完全核实 | 从 schema 删除，待 Ron 确认后恢复 |

## 待 Ron 补证后可升级的内容

| 主题 | 需要证据 | 可升级公开口径 |
|---|---|---|
| 出口年限 | 营业执照、历史合同、报关/出货记录、可核验里程碑 | “X years of seafood export/sourcing experience” |
| 证书 | 证书 PDF、持证主体、有效期、适用品类、工厂授权 | “products can be supplied from [certificate] plants where applicable” |
| 出口市场 | 已出货国家、客户类型、时间范围、可公开程度 | “served buyers in...” 或市场案例 |
| 客户案例 | 客户授权、行业类别、产品、结果 | 可写匿名 case study |
| 官方数据 | 来源 URL、发布日期、适用范围 | 可进入博客/FAQ，并标注来源 |

## 发布状态

- 首页：首页、FAQ 和 schema 已按谨慎口径调整。
- 关于页：证书、市场、年限和客户案例已按谨慎口径调整。
- 联系页：固定 24 小时承诺已软化。
- robots/llms/sitemap：已调整为支持图片/CSS 抓取和谨慎事实描述。

## 智能体执行要求

- 文曲星新增页面或博客前必须先读本台账。
- 金札改写软文/开发信时不得重新加入已经软化或删除的高风险声明。
- 判官和钟馗审查公开内容时，以本台账作为最低检查清单。
- 鲁班只发布 `publish_gate=approved_for_publish` 的内容，并核对台账是否更新。

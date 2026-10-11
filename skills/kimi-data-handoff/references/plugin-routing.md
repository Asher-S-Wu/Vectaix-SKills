# Kimi 插件选择表

能力与安装状态来自 2026-10-04 用户浏览器的插件页快照，共 61 项。当时 59 项已安装，Stripe、企业微信显示安装入口。安装状态与外部应用连接状态分别核实；Kimi 执行请求时记录实际状态。

先按需求定位相关插件，再将当前任务的对象、字段和口径写入取数请求。具体技能与应用说明见 [完整详情快照](kimi-plugins.md)，按插件名称查找相应条目。

## 按需求定位

| 需求 | 相关插件 | 请求中写清 |
| --- | --- | --- |
| 证券、基金、债券与公司财务 | 用户指定的机构数据源；万得、东方财富、同花顺、恒生聚源、标普、财新、全球金融数据库 | 市场与代码、日期、币种、单位、报价时点、财报及复权口径 |
| 公司公告、机构研报与路演 | SEC、进门投研、Alpha派投研；按需使用相关金融数据插件 | 文档类型、公司标识、期间、题名、文档编号与原文获取范围 |
| 财经新闻与政策 | 财联社资讯、新华财经资讯及相关金融资讯源 | 时间范围、栏目、关键词、发布时间与来源 |
| 企业工商、风险与关系 | 天眼查 | 企业名称与标识、所需类别、关联关系范围和查询时点 |
| 宏观、公共与国际统计 | 中国政府开放数据、世界银行、IMF、国际组织官方数据 | 地区和指标代码、频率、版本、单位、发布日期及预测／历史类型 |
| 法律、案例和标准 | 华宇元典法律数据库、法律助手、国家及行业标准查询 | 文号、案号、标准号、地域、效力状态、日期和引用条款 |
| 学术与生物医学文献 | 学术数据库、PubMed & PMC | 检索式、日期、筛选条件、标识、元数据及全文范围 |
| 分子、蛋白、序列和材料 | PubChem、ChEMBL、UniProt、PDB、NCBI BLAST、MP、OQMD | 对应数据库的对象编号、所需属性、结构或比对条件 |
| 用户已连接的办公或业务数据 | 飞书、钉钉、WPS、百度网盘、Notion、邮件、Moka、TikTok for Business；按当次状态使用企业微信与 Stripe | 项目或工作区、时间范围、筛选条件、导出字段 |
| 代码、数据库、流量与开发文档 | GitHub、Supabase、Neon、Cloudflare、Context7 | 仓库或项目标识、查询范围、版本、数据字段和时间 |
| 报告、模型、看板与素材 | 以下表中对应的资料处理、工作流或设计插件 | 最终交付物、输入数据与来源、计算或生成类型 |

## 全部插件

表中“数据与资料查询”概括可用于本流程的读取能力。部分插件同时有修改能力；本技能给 Kimi 的请求限定为本任务的查询、导出和打包。

### 金融

| 插件 | 用途 | 类型 | 当时状态 |
| --- | --- | --- | --- |
| [机构金融百宝箱](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a0ac0e2-c832-8731-8000-00008e20217b) | 完成机构投研中的财务建模、深度报告、汇报材料、早报、组合复盘和授信调查等复杂任务。 | 查询与分析工作流 | 已安装 |
| [金融投资分析](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f4f5e7-d1f2-825b-8000-000064691980) | 进行个股、行业、宏观和量化研究，并分析投资组合、风险及估值。 | 查询与分析工作流 | 已安装 |
| [金融市场终端](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a081818-8132-8802-8000-00000a3cd948) | 在 Kimi Work 中搭建全球金融市场看板，配置定时刷新和晨报推送。 | 看板与报告交付 | 已安装 |
| [企业财务会计](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f4f5e7-4222-837c-8000-0000eeb77517) | 协助企业关账、对账、编制报表、预测现金流、准备审计底稿及处理税务和基金会计。 | 查询与分析工作流 | 已安装 |
| [投资银行私募股权](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f4f5e7-86a2-8cd9-8000-00000c2ec468) | 协助投行和私募完成尽调、估值、交易建模、投委会材料及交易流程文档。 | 查询与分析工作流 | 已安装 |
| [标普全球市场财智](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ec0b5f-9722-84ce-8000-00000c767e72) | 查询标普的全球上市公司财务、盈利预测、股东、资本结构和并购数据。 | 数据与资料查询 | 已安装 |
| [万得金融数据服务](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f13845-ed02-8982-8000-00006e26b02c) | 查询万得的证券行情、公司资料、财务、股东、基金和债券等专业金融数据。 | 数据与资料查询 | 已安装 |
| [东方财富妙想金融数据](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19fa7815-97d2-859e-8000-0000de127ce1) | 查询东方财富金融数据，筛选证券、诊断股票和基金，并生成多种投研报告。 | 数据与资料查询 | 已安装 |
| [财联社资讯](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a08017c-0622-8f8e-8000-0000623abde2) | 查询财联社实时财经快讯、深度报道和指定栏目或时间段的新闻。 | 数据与资料查询 | 已安装 |
| [财新数据](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19fc62e5-1292-865a-8000-0000c7668ce0) | 查询财新覆盖的股票、债券、基金、宏观、企业、产业链及其他专业数据。 | 数据与资料查询 | 已安装 |
| [新华财经资讯](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f89ab5-4592-8191-8000-000056c7bd26) | 查询新华财经的市场新闻、政策和公告，用于投研及经济产业分析。 | 数据与资料查询 | 已安装 |
| [同花顺iFinD金融数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb03e2-a3f2-80a5-8000-00009111a8a7) | 查询同花顺的证券行情、公司财务、公告、持仓和分析预测等金融数据。 | 数据与资料查询 | 已安装 |
| [恒生聚源金融数据](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ebbac4-0bc2-8b67-8000-000013d2d1b6) | 查询聚源金融数据，并完成选股、基金分析、估值、市场复盘和研究报告等工作。 | 数据与资料查询 | 已安装 |
| [天眼查](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eaf954-fa42-8439-8000-000058d6536e) | 查询企业工商、股东、投资、融资、风险及关联关系，辅助背景调查和商业尽调。 | 数据与资料查询 | 已安装 |
| [进门投研](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ff537d-b602-8e9a-8000-0000750e6b8e) | 查询机构路演、研报、券商观点、市场行情、财务数据和量化因子。 | 数据与资料查询 | 已安装 |
| [恒生PTrade](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f4a369-3072-8538-8000-00002e47588b) | 把交易策略描述转成恒生 PTrade 代码，并解答或修复策略开发问题。 | 资料处理与交付 | 已安装 |
| [Stripe](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ecb31b-68b2-8bdb-8000-0000f43af5cf) | 连接 Stripe 账户，查询客户、余额和交易，并处理支付、账单、发票及退款。 | 数据与资料查询 | 安装入口 |
| [Alpha派投研](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a0f15fd-ae52-8d35-8000-0000a74417c1) | 查询公告、研报、会议纪要、机构观点和金融数据，并处理录音转记等投研事项。 | 数据与资料查询 | 已安装 |
| [国际组织官方数据](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eeed8d-07f2-8536-8000-0000a5129eda) | 查询国际组织的健康、农业、经济和社会统计，以及 FRED 宏观时间序列。 | 数据与资料查询 | 已安装 |
| [SEC](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb4d48-4082-8e8e-8000-00000cce61cc) | 查询美国上市公司的年报、季报、招股文件和其他监管披露材料。 | 数据与资料查询 | 已安装 |
| [全球金融数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb03e6-82b2-89c5-8000-0000113d89b0) | 查询全球主要市场的股票行情、财经资讯、公司财务和历史数据。 | 数据与资料查询 | 已安装 |
| [世界银行公开数据](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb03e5-5942-8bdb-8000-0000b5e69bb9) | 查询各国 GDP、人口、贸易、教育和健康等发展指标，进行国家和趋势对比。 | 数据与资料查询 | 已安装 |
| [IMF 国际货币基金组织数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb03e4-2282-82e7-8000-0000e64b42a4) | 查询全球增长、通胀、债务、就业和贸易等宏观数据及预测。 | 数据与资料查询 | 已安装 |

### 效率与办公

| 插件 | 用途 | 类型 | 当时状态 |
| --- | --- | --- | --- |
| [Word](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a00fc97-f192-8f5d-8000-0000a553b6f1) | 创建、编辑和审阅 Word 文档，处理批注、修订和格式校验。 | 资料处理与交付 | 已安装 |
| [PDF](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a00fc98-6cc2-8dd2-8000-0000372b3fab) | 创建和处理 PDF 报告，支持公式、图表、引用、文本提取及文件合并拆分。 | 资料处理与交付 | 已安装 |
| [Excel](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a00fc98-3872-8ee7-8000-0000025fb722) | 制作和检查电子表格，并处理预算、图表和财务估值模型。 | 资料处理与交付 | 已安装 |
| [邮件](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ebbba6-4cd2-81f1-8000-000043e0e272) | 连接邮箱，搜索、读取、发送、移动和标记邮件。 | 数据与资料查询 | 已安装 |
| [Notion](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ec5827-5b32-8976-8000-000032a21f63) | 搜索和整理 Notion 文档，管理页面、数据库记录和协作评论。 | 数据与资料查询 | 已安装 |
| [WPS云文档](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ec0235-7582-8efd-8000-0000149e8964) | 检索、读取、汇总和编辑 WPS 金山文档中的文档、表格与团队资料。 | 数据与资料查询 | 已安装 |
| [百度网盘](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eafeb2-c2a2-876a-8000-000064f43f01) | 查找和整理网盘文件，查看目录，并处理文件上传下载。 | 数据与资料查询 | 已安装 |
| [钉钉](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb5514-0fa2-880f-8000-0000871d1459) | 处理钉钉群聊、通讯录、待办、审批和文档等日常协作事项。 | 数据与资料查询 | 已安装 |
| [飞书](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb543c-4cf2-842c-8000-00002d6c45b7) | 处理飞书消息、文档、表格、审批、会议、日历和任务等办公协作事项。 | 数据与资料查询 | 已安装 |
| [企业微信](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a00e511-e8d2-8881-8000-000054c519a4) | 通过企业微信处理消息、通讯录、待办、审批、日程、会议和在线文档。 | 数据与资料查询 | 安装入口 |
| [Moka](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a00fb86-9f12-8efe-8000-000034fc03b0) | 查询和整理职位、候选人、简历、面试、员工与招聘进度等人事信息。 | 数据与资料查询 | 已安装 |
| [TikTok for Business](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a0a4fb5-dda2-83ae-8000-000083cfa657) | 查看 TikTok 广告数据，创建和管理投放，并分析广告效果。 | 已连接系统查询 | 已安装 |

### 创意与设计

| 插件 | 用途 | 类型 | 当时状态 |
| --- | --- | --- | --- |
| [Canva可画](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19ebc7dd-2c72-861a-8000-0000cb9eb002) | 通过文字描述生成和修改海报、演示文稿、封面等 Canva 设计。 | 设计与素材 | 已安装 |
| [灵感池](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f21f9f-db62-873d-8000-00003d31ef09) | 在设计网站前寻找视觉灵感，帮助生成更有变化的设计方案。 | 设计与素材 | 已安装 |
| [灵动报告](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f6b451-0412-8a82-8000-00000f5e8189) | 把静态报告制作成可交互网页，让报告中的数据和内容更直观。 | 看板与报告交付 | 已安装 |
| [视频生成](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f1c7f9-d312-8bcf-8000-0000b9411fbe) | 根据文字描述生成视频，并使用图片、视频或音频作为参考素材。 | 设计与素材 | 已安装 |
| [图像生成](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f1c7f9-7c12-8e41-8000-00000bf3d3c7) | 根据文字描述生成图像，并使用尺寸、透明背景和参考图等设置。 | 设计与素材 | 已安装 |
| [音频生成](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f1c7f9-45c2-8940-8000-00007892fab8) | 把文字转成语音，或按描述和时长生成音效。 | 设计与素材 | 已安装 |

### 3D

| 插件 | 用途 | 类型 | 当时状态 |
| --- | --- | --- | --- |
| [Tripo 3D](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a07f32e-a352-8920-8000-0000bf54ee67) | 把文字或参考图片变成 3D 模型，并处理贴图、骨骼、模型简化和格式转换。 | 设计与素材 | 已安装 |

### 开发与工程

| 插件 | 用途 | 类型 | 当时状态 |
| --- | --- | --- | --- |
| [GitHub](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eafe2e-9a42-8b4e-8000-0000d72c114d) | 查询代码仓库、提交、问题、合并请求和工作流，整理项目开发信息。 | 数据与资料查询 | 已安装 |
| [Cloudflare](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eafd72-0f52-8f23-8000-00007d858bf8) | 查询 Cloudflare 账户配置、流量与日志，并处理网站运维、性能和安全相关事项。 | 数据与资料查询 | 已安装 |
| [Supabase](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eafe2e-8552-8d5c-8000-000007bc9580) | 查看和管理数据库表，执行查询、迁移，查询日志及安全和性能建议。 | 数据与资料查询 | 已安装 |
| [Neon](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eafe2e-70e2-8925-8000-00005fb61302) | 管理云端 PostgreSQL 数据库项目，执行查询、迁移和表结构调整。 | 数据与资料查询 | 已安装 |
| [Context7](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a032fcc-8982-81bd-8000-0000be2198c3) | 按所用版本查询软件库的官方开发文档和示例代码。 | 数据与资料查询 | 已安装 |
| [可交互架构图](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a099933-8022-8167-8000-0000a051cad7) | 把代码库或系统描述画成可交互的架构、流程、时序和数据流图。 | 资料处理与交付 | 已安装 |

### 学习与研究

| 插件 | 用途 | 类型 | 当时状态 |
| --- | --- | --- | --- |
| [学术数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb4d46-ee12-8068-8000-000079a151b9) | 检索论文、作者、引用信息及其他学术资料，并查看作者学术指标。 | 数据与资料查询 | 已安装 |
| [华宇元典法律数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eb4d49-7a12-8bce-8000-0000422b607f) | 检索中国大陆法律法规、司法解释和案例，按效力、法院、地区及日期等条件筛选。 | 数据与资料查询 | 已安装 |
| [PubMed & PMC](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f89feb-f722-8b29-8000-0000ad37831b) | 检索生物医学论文、文献信息及允许访问的 PMC 全文。 | 数据与资料查询 | 已安装 |
| [PubChem 化合物数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a013c74-8e62-83fa-8000-00006fbc3b12) | 查询化合物标识、分子性质和同义词，并搜索结构相似的化合物。 | 数据与资料查询 | 已安装 |
| [MP 材料数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a013c75-cc22-8886-8000-00008d2e8d07) | 从 Materials Project 查询无机材料的带隙、稳定性、密度及晶体性质。 | 数据与资料查询 | 已安装 |
| [NCBI BLAST](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a00f541-5692-848c-8000-0000ed3e8b6b) | 把核酸或蛋白质序列提交到 NCBI，寻找相似序列并获取比对结果。 | 数据与资料查询 | 已安装 |
| [ChEMBL 数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a013c74-e252-8e87-8000-00000b1f1a0c) | 检索活性分子、药物靶点、实验效价和药物作用机制，辅助药物研究。 | 数据与资料查询 | 已安装 |
| [PDB 蛋白结构数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a013c75-2e92-8b99-8000-0000a7c22602) | 查询蛋白质、核酸及复合物的实验三维结构、序列、配体和测定信息。 | 数据与资料查询 | 已安装 |
| [UniProt](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a013c74-3e92-836e-8000-0000f57ec750) | 查询蛋白质序列、功能注释和跨数据库引用，并转换不同数据库的蛋白标识。 | 数据与资料查询 | 已安装 |
| [OQMD 开放量子材料数据库](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a013c75-8502-8777-8000-0000214bd933) | 查询无机晶体材料的计算性质，并获取候选材料的晶体结构。 | 数据与资料查询 | 已安装 |

### 补充插件

| 插件 | 用途 | 类型 | 当时状态 |
| --- | --- | --- | --- |
| [法律助手](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=1a038a4b-e7b2-846e-8000-00007e3a3482) | 协助国内律师和法务检索法律与案例、审查合同、整理尽调底稿及诉讼材料。 | 资料处理与交付 | 已安装 |
| [中国政府开放数据](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19eeed8b-8c62-8bd9-8000-0000659ba6c4) | 查询国家统计局指标及国家、省级政府开放数据目录。 | 数据与资料查询 | 已安装 |
| [国家及行业标准查询](https://www.kimi.com/plugins?pluginEnterMethod=plugin_button&pluginId=19f1ec3f-9bf2-8375-8000-00009c1329bb) | 检索中国国家、行业、地方和团体标准的编号、名称、状态及相关信息。 | 数据与资料查询 | 已安装 |

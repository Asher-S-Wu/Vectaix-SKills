# Kimi 数据交付包约定

用于用户把 Kimi 的结果一次交给 Agent。包名为任务编号加 .zip；内部使用相对路径和清楚的文件名。文件按实际需要建立，下面的示例表示结构。

~~~text
task-id.zip
├── manifest.json
├── request.md
├── sources.csv
├── delivery.md
├── field_dictionary.csv    有表格时
├── gaps.csv                有缺项时
├── data/                   CSV、JSON 等查询结果
├── documents/              本次需要的原始报告、公告、论文或纪要
├── media/                  本次需要的图片、音频或视频
└── generated/              本次需要的计算结果、整理报告或生成素材
~~~

## manifest.json

必需字段如下：

| 字段 | 内容 |
| --- | --- |
| schema_version | 本约定为字符串 1.0 |
| task_id | Agent 在提示词中确定的任务编号，补交时沿用 |
| created_at | 实际打包时间，ISO 8601 格式，带时区 |
| status | 全部请求完成为 complete，有未完成项为 partial |
| requests | 每项请求的实际查询条件、使用插件、状态、结果数量及覆盖说明 |
| files | 除 manifest.json 自身之外的全部包内文件及其用途、内容类型、关联请求和来源 |

每项 requests 记录包括：

| 字段 | 内容 |
| --- | --- |
| request_id | 与请求一致的编号，例如 R01 |
| description | 本项需要的数据或资料 |
| plugins_used | 实际调用的插件名称；未调用时为空数组 |
| parameters | 对象标识、日期、截止时间、筛选条件、分页和查询上限等实际参数 |
| requested_fields | 提示词要求的字段；纯文档项可为空数组 |
| status | complete、partial 或 unavailable |
| returned_rows | 本项交付的表格数据总行数，整数；纯文档项为 null |
| coverage_note | 实际时间与对象范围、是否取全、分页情况、被截断部分或缺项 |

每项 files 记录包括：

| 字段 | 内容 |
| --- | --- |
| path | 包内相对路径，使用 / 分隔目录 |
| role | 文件在当前任务中的用途 |
| content_type | observed_data 查询实得；calculated_data 计算结果；original_document 原文；generated_material 生成或整理材料；metadata 交接记录 |
| request_ids | 与本文件有关的请求编号数组，通用交接文件可为空数组 |
| source_ids | 与本文件有关的来源编号数组，通用交接文件可为空数组 |
| rows | CSV 的数据行数，表头另计；其他文件为 null |

表格行数填实际整数。查询结果只有一部分时写明覆盖情况和缺少范围；空结果写明查询条件及返回 0 条这一实际情况。来源结构本身缺字段、接口限额、权限或连接等原因分别记录，便于后续处理。

## request.md 与 delivery.md

request.md 保存本次转交 Kimi 的请求全文。delivery.md 简要列出每项请求交付的文件、覆盖范围、数据口径、处理步骤和重要缺项，供 Agent 开始读取时定位。

## sources.csv

UTF-8 编码，表头：

~~~csv
source_id,request_ids,plugin,provider,title,url,document_id,published_at,retrieved_at,query,note
~~~

source_id 在包内唯一，例如 S001。request_ids 使用 | 连接多个编号，例如 R01|R02。query 保存查询语句、检索式或关键参数；必要时引用同时交付的查询响应文件。

provider 填数据机构或原文发布者。title 填报告题名、数据表名、指标名或资料名称。url 与 document_id 至少一项能再次定位来源；需要账号访问的来源保留机构、文档或数据集标识和访问说明。published_at 记录可取得的发布日期，retrieved_at 记录实际检索时间。字段缺失原因写入 note。链接中的访问凭证留在原系统中。

## 表格与字段说明

查询表格使用 UTF-8 CSV。每行用 request_id、source_id 关联请求及其主要来源；需要多个来源共同支撑的行在数据列或说明文件中列明各输入来源。原始文件各自保留，合并过程写明连接键和处理方法。

field_dictionary.csv 覆盖每个表格的每一列，表头：

~~~csv
file,field,description,data_type,unit,currency,frequency,time_basis,note
~~~

file 对应包内相对路径；field 与实际表头一致；description 解释列的含义。单位、币种和时间口径在适用时填写，其他格留空。保留原始标识中的前导零，例如证券代码、文献标识和企业编号。缺失值与数值 0 分别表达。

按需求补充有关口径：

- 金融：证券代码和市场、交易或报价时间、报告期、币种、单位、复权方式、财报合并口径；估值、比率或预测数据的计算依据。
- 宏观：国家或地区代码、指标代码、频率、单位、价格基期、季调状态、发布日期及数据版本。
- 法律与标准：题名、文号或标准号、发布机关、效力或状态、施行日期、引用条款、来源定位。
- 科研：检索式、筛选条件、数据库标识、作者、年份、DOI／PMID／PMCID 或相应材料、化合物、结构及蛋白编号；全文的实际可取得范围。
- 办公与工程：查询的工作区、项目、文件或记录标识，明确日期范围、筛选字段和导出范围。

## 原文与生成材料

原文放入 documents/，在 manifest.json 关联其请求与来源。文件名反映对象及日期，保留题名和文档标识。只有摘要或检索结果时记录实际取得的类型。

计算结果、研究判断、整理报告和生成素材放入 generated/ 或在 manifest.json 标明类型。计算结果附公式、输入和处理步骤；引用的数据另有来源记录。素材的生成条件、参考来源和格式按任务需要说明。

## gaps.csv

实际存在缺项时建立，表头：

~~~csv
request_id,missing_item,reason,impact,requires_user_action
~~~

逐项记录未取得的字段、对象、期间或附件，以及原因、对任务的影响和需要用户处理的具体事项。查询结果完整且核对通过时，manifest.json 记录 complete。

## Agent 收包检查

先对照本次真实请求，再核对 manifest.json：

1. 任务编号和逐项请求对应，补交文件能追溯同一任务。
2. 清单与实际文件一致，文件可读取；CSV 行数和字段说明对应。
3. 请求及来源编号能相互定位，来源含检索时间和查询条件。
4. 数据范围、截止时点、频率、单位和计算口径满足后续工作。
5. 文件类型和完成状态符合实际，缺项说明足以写出有针对性的补数请求。

核查结果用来决定可继续的工作范围。保留收到的数据原文，按缺项记录生成补数请求。

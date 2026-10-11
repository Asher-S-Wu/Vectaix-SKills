# 给 Kimi 的数据请求提示词

Agent 按当前任务改写下列模板。花括号表示需要填入的信息，成稿直接交给用户复制；只有任务所需的要求进入成稿。

~~~text
我正在让另一个 Agent 完成【{任务}】。请使用我在 Kimi 中可用的相关插件，取得下面列出的数据和资料，并把本阶段需要的内容整合为一个可下载的 ZIP 包。Agent 会读取这个包继续完成任务。

任务编号：{task_id}
数据用途：{具体用途}
时间口径：{用户时区、明确日期范围和截止时点}
操作范围：查询、读取、导出和打包；保留原系统内容与配置。

一、逐项请求

{每项均列出以下内容，按 R01、R02 等编号}

R01：{需要的数据或资料}
- 插件：{插件页中的准确名称；如用户指定数据源，保留该要求}
- 对象：{公司、证券、国家、论文、材料、文档、项目等对象的名称及标识}
- 范围：{市场、日期、报告期、地域、目录或检索条件}
- 字段：{具体列名；保留对象标识、日期和后续计算需要的原始值}
- 口径：{单位、币种、频率、复权方式、合并报表口径或其他必要条件}
- 附件：{所需原始报告、公告、论文全文、纪要、查询响应或其他资料}
- 交付文件：{data/ 下的文件名，或 documents/、media/、generated/ 中的文件名}
- 完整性要求：{完整日期序列、所有匹配记录、指定页数或明确的数量上限}

二、查询与来源

请核实当前插件可用性、连接状态、数据覆盖和账号权限。记录实际调用的插件、提供数据的机构、查询条件、检索时间、数据发布日期或报告期，并给出来源链接或可再次定位的文档／数据集标识。

按每项请求的范围取得结果；涉及分页时记录页数、返回条数和是否已经取全。市场数据记录报价时间与时区；文献记录检索式、筛选条件和结果数量；原文附件按当前账号可导出的范围收集。

表格保留原始数值和标识，单独列出单位与币种。计算值写明公式和输入来源；报告判断与生成内容注明类型。未取得的数据在缺项记录中说明原因和受影响的请求，数据表使用明确的缺失值。

三、交付包

文件名：{task_id}.zip

包内包括：
1. manifest.json：任务编号、生成时间、逐项查询条件、完成情况、文件路径和记录数。
2. request.md：这份请求全文，供 Agent 对照。
3. sources.csv：来源编号及其对应的请求、插件、机构、链接或文档标识、发布日期、检索时间和查询条件。
4. delivery.md：取得的内容、各项覆盖范围、重要口径，以及需要 Agent 留意的缺项。
5. 实际数据与附件：按以下清单保存全部已取得的文件。
{在这里列出本任务每项所需的文件和字段}
6. field_dictionary.csv：有表格时，逐列说明含义、类型、单位、币种和时间口径。
7. gaps.csv：有缺项时，列出请求编号、缺少的内容、原因、影响和需要用户处理的事项。

sources.csv 表头：source_id,request_ids,plugin,provider,title,url,document_id,published_at,retrieved_at,query,note
来源编号在包内唯一；多个 request_ids 使用 | 分隔。url 与 document_id 至少一项能再次定位来源，字段缺失原因写入 note。
field_dictionary.csv 表头：file,field,description,data_type,unit,currency,frequency,time_basis,note
gaps.csv 表头：request_id,missing_item,reason,impact,requires_user_action

表格使用 UTF-8 CSV，JSON 保留完整字段结构。表格中的 request_id 和 source_id 对应请求清单与 sources.csv；原文附件在 manifest.json 中关联其请求编号和来源编号。returned_rows 与 rows 填写实际整数；纯文档请求和非 CSV 文件填 null。账号密钥、授权码和令牌保留在原系统中。

manifest.json 按以下结构填写，所有值使用本次实际结果。示例中的 0 表示整数行数：
{
  "schema_version": "1.0",
  "task_id": "{task_id}",
  "created_at": "{实际生成时间，含时区}",
  "status": "{complete 或 partial}",
  "requests": [
    {
      "request_id": "R01",
      "description": "{本项内容}",
      "plugins_used": ["{实际调用的插件}"],
      "parameters": {"{筛选条件}": "{实际取值}"},
      "requested_fields": ["{请求字段}"],
      "status": "{complete、partial 或 unavailable}",
      "returned_rows": 0,
      "coverage_note": "{范围、日期、分页、上限及完成情况}"
    }
  ],
  "files": [
    {
      "path": "{包内相对路径}",
      "role": "{文件用途}",
      "content_type": "{observed_data、calculated_data、original_document、generated_material 或 metadata}",
      "request_ids": ["R01"],
      "source_ids": ["S001"],
      "rows": 0
    }
  ]
}

请先核对每项请求、文件清单和来源，再交付这一个 ZIP 包。manifest.json 的 files 列出包内除 manifest.json 本身以外的全部文件。最终回复给出下载附件，并简要说明逐项完成情况、总文件数和重要缺项；查询结果以包内文件交付。
~~~

## 填写时注意

- 明确数据是“交易日收盘价”“财报期末值”还是“查询时快照”，按原任务确定截止时点。
- 每项请求保留固定编号；一项可以对应多个文件，一个来源可以用于多项请求。
- 字段使用能够支撑后续工作的实际列名。只有“帮我分析一下”这类概括要求时，先拆出分析需要的数据。
- JSON 示例中的 returned_rows、rows 表示整数或 null；提示词说明使用实得行数。
- 选择相关插件并收集所需资料。目录中的加工、看板和生成类插件在任务需要相应交付物时使用。
- 请求规模较大时，在同一提示词中写清分组、完整性要求和可接受的查询上限；由 Kimi 将所有已取得文件合并为一个包。

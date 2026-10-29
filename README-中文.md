# 我的学术 CV 模板

面向计算机研究生的欧洲 PhD 申请。保留 Xovee 的简洁单栏外观，加入 CurVe 启发的论文管理方式。默认 A4、11 pt、黑白、可点击链接；个人信息、经历和论文分别维护。

**交付 PDF 中的姓名、学校、经历、论文均为示例，不代表你的真实履历。** 所有论文标题均以 Example 开头。填完后再关闭模板提示。

## 第一次使用

1. 打开 `profile.tex`，替换姓名、身份、单位、邮箱、链接及更新日期。
2. 修改 `sections/` 下的教育、研究经历、奖励、技能等内容；无关栏目可在 `main.tex` 中停用。
3. 清空 `publications.bib` 的示例，加入自己已核实的论文记录。每篇只保留一个状态标签；挑选申请版论文时加 `selected`。
4. 核对作者加粗和论文状态。完成全部替换后，将 `cv-settings.tex` 的 `\CVTemplatetrue` 改为 `\CVTemplatefalse`。
5. 编译并检查 PDF 页数、链接、分页和论文状态。项目规定了上限时严格遵守；默认两页是目标，不是截断规则。

## 在 Overleaf 编辑

本地交付可直接上传 `personal-academic-cv-overleaf.zip`；从 GitHub 获取时，选择 **Code → Download ZIP**，然后在 Overleaf 选择 **Upload Project**。主文件选 `main.tex`，编译器选 pdfLaTeX；Overleaf 会按 BibLaTeX 设置调用 Biber。

- **申请精选版：**主文件 `main.tex`。只显示带 `selected` 标签的论文，默认隐藏在审论文；经历中 `\cvfullonly{...}` 的内容也隐藏。
- **完整维护版：**主文件改为 `cv-full.tex`。读取同一组文件，包含额外研究经历、全部论文和附加栏目。
- 两版只是内容筛选不同，不强制页数，也不会自动删字或缩小字体。当前示例两版都可排入两页；填入实际信息后页数可能改变。
- 本次使用本地 TeX Live + Biber 验证；未登录 Overleaf 上传验证。

## 平时改哪里

| 文件 | 用途 |
| --- | --- |
| `profile.tex` | 姓名、联系方式、个人链接、作者姓名别名 |
| `cv-settings.tex` | 模板提示、在审论文显示等开关 |
| `main.tex` | 申请版入口与栏目顺序 |
| `cv-full.tex` | 完整版入口，无须复制另一份内容 |
| `sections/*.tex` | 教育、研究、奖励、技能、教学/服务等 |
| `publications.bib` | 唯一论文库 |
| `personal-cv.sty` | 本次定制的排版及论文管理规则，通常不用改 |
| `xovee-cv.sty` | 保留的上游样式，通常不用改 |

非论文经历默认进入两版。若某项只适合完整维护版，使用 `\cvfullonly{完整的一项内容}` 包住；只在申请版显示的文字可用 `\cvselectedonly{...}`。不需要为每所学校复制整套论文库。

## 论文只录入一次

每条 `keywords` 必须包含下列状态中的**一个且仅一个**：

| 状态标签 | 输出栏目 | 如何使用 |
| --- | --- | --- |
| `published` | Published Papers | 已正式发表的论文 |
| `accepted` | Accepted Papers | 有正式录用通知，尚未正式发表 |
| `preprint` | Preprints | 公开的预印本，例如 arXiv |
| `underreview` | Under Review | 尚未接收、需要明确标注在审的稿件 |

再加 `selected` 才进入精选申请版。**在审稿件还需要显式启用 `\CVShowUnderReviewtrue`**；默认精选版隐藏这一组，完整维护版显示它。

同一篇稿件若既有预印本又在审，保留一个记录，选一个主要输出状态，并在 `note` 中说明另一事实；不要为同一篇稿件建两条记录。论文接收或发表后更新原记录的状态与出版信息。

可用这个结构录入一篇已接收会议论文：

```bibtex
@inproceedings{unique-key,
  author    = {Family, Given and Other, Coauthor},
  author+an = {1=me},
  title     = {Your Verified Paper Title},
  booktitle = {Conference Name},
  date      = {2026},
  pubstate  = {accepted},
  keywords  = {accepted, selected}
}
```

会议论文用 `@inproceedings`，期刊论文用 `@article`，预印本可用 `@online`，未接收稿件可用 `@unpublished`。没有正式刊名时不要给 `@article` 编造刊名。已有 DOI/arXiv 编号时填实际值；示例故意没有伪造真实编号。

每组内部按年份从新到旧排序。编号按组顺序连续输出；如果文献管理器导出了 `sortkey` 或 `sortyear`，它们可能覆盖常规排序，需核对。

## 作者姓名、共同一作与通讯作者

在 `profile.tex` 用 `\cvownernames{姓/名,姓/缩写}` 设置实际出现的姓名形式。它按姓与名同时精确匹配，示例的 Alex / A. 已测试。

复杂、多词姓名或同名作者优先用 `.bib` 作者注释，避免自动匹配的不确定性：

```bibtex
author    = {YourFamily, YourGiven and SameFamily, SameInitial and Other, Person},
author+an = {1=me,cofirst; 2=notme; 3=corresponding},
```

- 作者从 1 开始编号；`me` 强制本人加粗，`notme` 强制普通字体，且 `notme` 优先。
- `cofirst` 显示共同一作符号 `*`；`corresponding` 显示通讯作者符号 `†`。
- 一个作者有多个标记时，用逗号连接在同一项内。
- **修改作者顺序后同步修改位置编号。** 自动识别不能凭缩写判断现实身份。

## 本地编译与数据检查

安装 TeX Live 或其他包含 pdfLaTeX、latexmk、Biber 的发行版后，在项目目录运行 `./build.ps1`，结果保存在 `output/pdf/`。脚本仅改当前项目；不安装依赖或修改系统配置。

若有 Python，可先运行 `python tools/check_data.py`。它检查状态缺失、多状态冲突和重复键；`--self-test` 可验证这些护栏。这个小检查器支持花括号记录及花括号/引号关键词字段；复杂 BibTeX 宏仍以 Biber 诊断为准。

`tools/verify_preview.py` 是交付示例的检查与图片生成工具，依赖 pdfplumber 和 pypdfium2，且包含示例标题断言；**替换成个人内容后不应把它当作通用 CV 验收器。** 普通使用只需编译并检查 PDF。

## 提交前

- 替换全部示例和方括号提示，关闭模板提示。
- 对照招生公告和申请系统确认页数、附件、文件大小与格式要求。
- 核实研究贡献、作者顺序、论文状态、指标及链接；在审稿件不作为已发表成果。
- 单独提交的推荐人信息、研究计划等按项目要求处理；不用在 CV 中机械重复。
- 检查页边距、可读字号、断页、空白和姓名/页码。删减低相关内容优先于压缩字号。

## 来源

保留 Xovee 原样式及 MIT 许可证。CurVe 的贡献是管理方式上的启发，本项目没有混用 CurVe 文档类。详见 `SOURCES-AND-LICENSES.md` 与 `LICENSE-Xovee.txt`。
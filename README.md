# Personal Academic CV Template

面向计算机研究生与欧洲 PhD 申请的个人学术 CV 模板：保留 Xovee 的简洁单栏版式，加入 CurVe 启发的论文管理方式。

**全部姓名、学校、经历和论文均为示例。填写真实信息并核实后，再用于申请。**

## 特点

- A4、11 pt、黑白、单栏；联系方式与作品链接可点击。
- 同一份 `.bib` 论文库管理全部成果，分别输出已发表、已接收、预印本和在审稿件。
- 申请精选版和完整维护版共享同一组内容；不自动缩字或截断页数。
- 支持本人作者加粗、共同一作及通讯作者标记，提供同名作者的手动覆盖方式。
- 个人信息、经历栏目和论文分开维护；附数据检查工具。

## 快速使用

1. 选择 **Code → Download ZIP**，在 Overleaf 中通过 **Upload Project** 导入；或克隆后本地编译。
2. 在 `profile.tex` 中修改姓名、联系方式、个人链接和作者姓名别名。
3. 替换 `sections/` 与 `publications.bib` 中的示例内容。
4. 申请精选版主文件为 `main.tex`；完整维护版主文件为 `cv-full.tex`。使用 pdfLaTeX + Biber。
5. 完成替换后，在 `cv-settings.tex` 中设置 `\CVTemplatefalse`，关闭示例提示。

详细操作、状态标签与姓名消歧规则见 [中文使用说明](README-中文.md)。本地可运行 `./build.ps1` 同时生成两版 PDF。

## 预览

[申请精选版 PDF](output/pdf/cv-selected.pdf) · [完整维护版 PDF](output/pdf/cv-full.pdf)

当前示例两版均为两页。实际页数由填写内容决定，提交时以目标项目的规定为准。

![申请精选版第一页预览](output/preview/selected-1.png)

## 文件结构

| 文件 | 用途 |
| --- | --- |
| `profile.tex` | 个人信息与作者姓名别名 |
| `cv-settings.tex` | 内容显示与模板提示开关 |
| `main.tex` / `cv-full.tex` | 精选版 / 完整版入口 |
| `sections/` | 教育、研究、奖励、技能等栏目 |
| `publications.bib` | 唯一论文库 |
| `personal-cv.sty` | 定制版式与论文管理规则 |
| `tools/check_data.py` | 状态缺失、状态冲突和重复键检查 |

## 验证与来源

示例已使用本地 TeX Live + Biber 编译，并检查论文筛选、作者字体及 PDF 排版；未向 Overleaf 上传验证。源码中不包含申请人的真实履历。

视觉基础来自 [Xovee's CV Template](https://github.com/Xovee/latex-cv)，保留其原样式与 [MIT 许可证](LICENSE-Xovee.txt)。论文管理方式参考 [A Customised CurVe CV](https://www.overleaf.com/latex/templates/a-customised-curve-cv/mvmbhkwsnmwv)，没有混用其文档类。详见 [来源与许可说明](SOURCES-AND-LICENSES.md)。
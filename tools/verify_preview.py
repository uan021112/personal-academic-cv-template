"""Delivery QA for the illustrative previews; requires pdfplumber/pypdfium2."""
from pathlib import Path
import json
import re
import pdfplumber
import pypdfium2
from check_data import check

ROOT = Path(__file__).resolve().parents[1]
(ROOT / "output" / "preview").mkdir(parents=True, exist_ok=True)
ENTRIES = check((ROOT / "publications.bib").read_text(encoding="utf-8"))
TOKENS = {
    "example-published": "Hierarchical Representations",
    "example-accepted": "Geometry-Aware Learning",
    "example-preprint": "Evaluating Spatial Generalization",
    "example-older": "Reproducible Baselines",
    "example-underreview": "Physics-Grounded Evaluation",
    "example-same-initial": "Long-Horizon Research Software",
}


def compact(text):
    return re.sub(r"[^a-z0-9]", "", text.lower())


report = {"note": "Illustrative content only; not an applicant CV", "versions": {}}
for mode in ("selected", "full"):
    path = ROOT / "output" / "pdf" / f"cv-{mode}.pdf"
    expected = [e for e in ENTRIES if mode == "full" or (e["selected"] and e["status"] != "underreview")]
    with pdfplumber.open(path) as doc:
        text = "\n".join(page.extract_text() or "" for page in doc.pages)
        assert "\ufffd" not in text, "Broken replacement character"
        for entry in ENTRIES:
            present = compact(TOKENS[entry["key"]]) in compact(text)
            assert present == (entry in expected), f"Wrong selection: {mode}/{entry['key']}"
        labels = [int(n) for n in re.findall(r"(?m)^\[(\d+)\]", text)]
        assert labels == list(range(1, len(expected) + 1)), f"Non-contiguous labels: {labels}"
        assert ("underreview" in compact(text)) == (mode == "full")
        name_fonts = []
        for page in doc.pages:
            assert abs(page.width - 595.276) < 1 and abs(page.height - 841.89) < 1, "Not A4"
            for word in page.extract_words(extra_attrs=["fontname"]):
                if "Researcher" in word["text"]:
                    name_fonts.append(word["fontname"])
            for char in page.chars:
                assert -1 <= char["x0"] <= char["x1"] <= page.width + 1, "Horizontal clipping"
                assert -1 <= char["top"] <= char["bottom"] <= page.height + 1, "Vertical clipping"
        assert any("Bold" in f for f in name_fonts) and any("Regular" in f for f in name_fonts)
        log = (ROOT / "build" / mode / f"cv-{mode}.log").read_text(encoding="utf-8", errors="replace")
        assert not re.search(r"Overfull \\[hv]box|LaTeX Warning:|Package \S+ Warning:", log), "Unresolved TeX warning"
        report["versions"][mode] = {"pages": len(doc.pages), "papers": len(expected), "labels": labels, "a4": True,
            "mixed_author_fonts": True, "clipping_checks": "pass", "latex_warnings": 0}
    pdf = pypdfium2.PdfDocument(str(path))
    for i in range(len(pdf)):
        page = pdf[i]
        bitmap = page.render(scale=1.45)
        image = bitmap.to_pil()
        image.save(ROOT / "output" / "preview" / f"{mode}-{i + 1}.png")
        bitmap.close()
        page.close()
    pdf.close()
(ROOT / "output" / "verification.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
print(json.dumps(report, indent=2))
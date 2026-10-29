$ErrorActionPreference = 'Stop'
$cvRoot = $PSScriptRoot
$cvOldLocale = $env:LC_ALL
$cvOldLang = $env:LANG
$env:LC_ALL = 'C'
$env:LANG = 'C'
Push-Location -LiteralPath $cvRoot
try {
    foreach ($cvMode in @('selected','full')) {
        $cvEntry = if ($cvMode -eq 'selected') { 'main.tex' } else { 'cv-full.tex' }
        $cvBuildDir = "build/$cvMode"
        New-Item -ItemType Directory -Path $cvBuildDir -Force | Out-Null
        & latexmk -pdf -interaction=nonstopmode -halt-on-error "-outdir=$cvBuildDir" "-jobname=cv-$cvMode" $cvEntry
        if ($LASTEXITCODE -ne 0) { throw "LaTeX build failed: $cvMode" }
        New-Item -ItemType Directory -Path 'output/pdf' -Force | Out-Null
        Copy-Item -LiteralPath "$cvBuildDir/cv-$cvMode.pdf" -Destination "output/pdf/cv-$cvMode.pdf" -Force
    }
} finally { Pop-Location; $env:LC_ALL = $cvOldLocale; $env:LANG = $cvOldLang }
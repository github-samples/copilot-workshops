$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $false
$exitCode = 1
$linkRoot = $null
$link = $null
$locationPushed = $false

try {
    $repo = (Resolve-Path (Join-Path $PSScriptRoot '../../../..')).Path
    $website = Join-Path $repo 'website'
    Push-Location -LiteralPath $website
    $locationPushed = $true
    $npm = if ($env:OS -eq 'Windows_NT') { 'npm.cmd' } else { 'npm' }
    Get-Command $npm, lychee -ErrorAction Stop | Out-Null
    if (!(Test-Path -LiteralPath 'astro.config.mjs' -PathType Leaf) -or
        !(Test-Path -LiteralPath 'package.json' -PathType Leaf)) {
        throw 'Expected the workshop website configuration and package.json.'
    }

    & $npm run check:all
    if ($LASTEXITCODE -ne 0) { $exitCode = $LASTEXITCODE; throw 'Type checks failed.' }
    $dist = Join-Path $website 'dist'
    if (Test-Path -LiteralPath $dist) {
        $existing = Get-Item -LiteralPath $dist -Force
        if (!$existing.PSIsContainer -or ($existing.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
            throw 'Refusing to remove dist: expected a directory, not a link or file.'
        }
        Remove-Item -LiteralPath $dist -Recurse -Force
    }
    & $npm run build
    if ($LASTEXITCODE -ne 0) { $exitCode = $LASTEXITCODE; throw 'Site build failed.' }
    $built = Get-Item -LiteralPath $dist -Force
    if (!$built.PSIsContainer -or ($built.Attributes -band [IO.FileAttributes]::ReparsePoint)) {
        throw 'Build did not produce a regular dist directory.'
    }

    $linkRoot = Join-Path ([IO.Path]::GetTempPath()) ('workshop-links-' + [guid]::NewGuid())
    New-Item -ItemType Directory -Path $linkRoot | Out-Null
    # Match the current base in website/astro.config.mjs, as the Pages workflow does.
    $link = Join-Path $linkRoot 'copilot-workshops'
    $linkType = if ($env:OS -eq 'Windows_NT') { 'Junction' } else { 'SymbolicLink' }
    New-Item -ItemType $linkType -Path $link -Target $dist | Out-Null
    & lychee --offline --no-progress --root-dir $linkRoot (Join-Path $dist '**/*.html')
    $exitCode = $LASTEXITCODE
} catch {
    Write-Error $_ -ErrorAction Continue
} finally {
    # Delete the link itself, never recurse into the built site through it.
    if ($link -and (Test-Path -LiteralPath $link)) { [IO.Directory]::Delete($link) }
    if ($linkRoot -and (Test-Path -LiteralPath $linkRoot)) { [IO.Directory]::Delete($linkRoot) }
    if ($locationPushed) { Pop-Location }
}
exit $exitCode

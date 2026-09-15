#!/usr/bin/env bash
set -euo pipefail

repo=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../../../.." && pwd -P)
cd -- "$repo/website"
for tool in npm lychee; do
  command -v "$tool" >/dev/null || { echo "Required tool not found: $tool" >&2; exit 1; }
done
if [[ ! -f astro.config.mjs || ! -f package.json ]]; then
  echo "Expected the workshop website configuration and package.json." >&2
  exit 1
fi

npm run check:all
if [[ -L dist || ( -e dist && ! -d dist ) ]]; then
  echo "Refusing to remove dist: expected a directory, not a symlink or file." >&2
  exit 1
fi
rm -rf -- "$PWD/dist"
npm run build
if [[ ! -d dist || -L dist ]]; then
  echo "Build did not produce a regular dist directory." >&2
  exit 1
fi

link_root=$(mktemp -d)
trap 'status=$?; rm -f -- "$link_root/copilot-workshops"; rmdir -- "$link_root"; exit "$status"' EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
# Match the current base in website/astro.config.mjs, as the Pages workflow does.
ln -s -- "$PWD/dist" "$link_root/copilot-workshops"
lychee --offline --no-progress --root-dir "$link_root" "$PWD/dist/**/*.html"

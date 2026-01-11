#!/bin/bash

uv sync
pnpm install

# add husky hooks
npx husky init
echo "task format && task lint && git add -A ." > .husky/pre-commit
echo "task test" > .husky/pre-push
echo "npx --no-install commitlint --edit \$1" > .husky/commit-msg
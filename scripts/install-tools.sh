#!/bin/bash

uv sync
pnpm install

# add husky hooks
npx husky init
cat > .husky/pre-commit << 'HOOK'
STAGED=$(git diff --cached --name-only --diff-filter=ACM -- '*.py')
[ -z "$STAGED" ] && exit 0
uv run ruff check --select I,F401 --fix $STAGED && uv run ruff format $STAGED && uv run pyrefly check $STAGED && git add $STAGED
HOOK
cat > .husky/pre-push << 'HOOK'
CHANGED=$(git diff --name-only origin/main...HEAD -- '*.py')
[ -z "$CHANGED" ] && exit 0

TEST_FILES=""
for f in $CHANGED; do
  if echo "$f" | grep -q "^tests/"; then
    TEST_FILES="$TEST_FILES $f"
  else
    dir=$(echo "$f" | sed -n 's|^src/\([^/]*\)/.*|\1|p')
    [ -n "$dir" ] && TEST_FILES="$TEST_FILES $(find tests -name "test_${dir}*" -type f 2>/dev/null)"
  fi
done

TEST_FILES=$(echo "$TEST_FILES" | tr ' ' '\n' | sort -u | tr '\n' ' ' | xargs)
[ -z "$TEST_FILES" ] && exit 0
uv run pytest $TEST_FILES
HOOK
echo "npx --no-install commitlint --edit \$1" > .husky/commit-msg

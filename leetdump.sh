#!/bin/zsh
get_all_submissions () {
  OUTPUT_DIR="$LEETCODE_OUTPUT"
  HEADER_COOKIE="csrftoken=$CSRF_TOKEN; LEETCODE_SESSION=$LEETCODE_SESSION;"
  HEADER_CONTENT_TYPE='content-type: application/json'
  HEADER_ORIGIN='origin: https://leetcode.com'
  HEADER_USER_AGENT="user-agent: $USER_AGENT"

  if [[ $# -ne 3 ]]; then
    echo -n "ERROR: Missing arguments - OFFSET LIMIT FILENAME"
    return 1
  fi

  OFFSET=$1
  LIMIT=$2
  FILENAME=$3

  if [[ $LIMIT -lt 240 ]]; then
    LAST=$LIMIT
  else
    LAST=240
  fi

  for OFFSET in {$OFFSET..$LAST..$LIMIT}; do
    echo -n "FETCHING $OFFSET/$LAST\r"
    curl -s "https://leetcode.com/api/submissions/?offset=$OFFSET&limit=$LIMIT" \
      -b $HEADER_COOKIE \
      -H $HEADER_CONTENT_TYPE \
      -H $HEADER_ORIGIN \
      -H 'referer: https://leetcode.com/submissions/' \
      -H $HEADER_USER_AGENT | jq .submissions_dump >> "$OUTPUT_DIR/$FILENAME" && echo -n "---\n" >> "$OUTPUT_DIR/$FILENAME"
  done
  return 0
}

# Ensure that LEETCODE_OUTPUT, CSRF_TOKEN, LEETCODE_SESSION, USER_AGENT are defined in your shell environment.
echo ""
get_all_submissions 0 1 submissions_dump_latest.json
echo -n "\n\nDone.\n\n"
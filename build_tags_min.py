#!/usr/bin/env python3
"""Convert the full Danbooru Korean dataset into the compact runtime format.
Output rows: [english_name, korean_name, keyword, major_categories, count]
"""
import gzip, json, sys
from pathlib import Path
src = Path(sys.argv[1] if len(sys.argv) > 1 else 'tags.json')
out = Path(sys.argv[2] if len(sys.argv) > 2 else 'data/tags.min.json')
data = json.loads(src.read_text(encoding='utf-8'))
rows = [[x.get('english_name',''), x.get('korean_name',''), x.get('keyword',''), x.get('major_categories',''), x.get('count',0)] for x in data]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(rows, ensure_ascii=False, separators=(',',':')), encoding='utf-8')
gz = out.with_suffix(out.suffix + '.gz')
with gzip.open(gz, 'wb', compresslevel=9) as f: f.write(out.read_bytes())
print('source rows:', len(data))
print('output rows:', len(rows))
print('json bytes:', out.stat().st_size)
print('gzip bytes:', gz.stat().st_size)

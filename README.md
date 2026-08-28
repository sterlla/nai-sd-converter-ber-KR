# 프롬프트 도구함 — NAI ↔ SD 변환 · 자연어 태그

NovelAI와 Stable Diffusion 프롬프트를 양방향으로 변환하고,
한국어 문장을 Danbooru 태그로 바꿔주는 도구입니다.

**HTML 파일 하나가 전부입니다.** 설치도, 빌드도, 인터넷 연결도 필요 없습니다.

## 세 가지 탭

### 1. NAI → SD
NAI의 `가중치::…::` 블록을 `(태그:1.4)` 형식으로 변환합니다.
- 음수 가중치는 네거티브 채널로 자동 분리 (`-6::` → `1.6`)
- 문법 오류를 **원문에 색으로 표시**하고 버튼으로 바로 수정
- 안 닫힌 블록, `artist:` 오타, 콜론 충돌, 중복 태그, 이상 가중치 감지
- Danbooru 태그 1,100+ 내장 사전으로 오타 교정 제안
  (사전에 없는 태그는 경고 없이 그대로 통과 — 자작 태그 안전)
- txt/csv 태그 목록을 불러와 사전 확장 가능

### 2. SD → NAI
로컬 SD 프롬프트를 NAI 문법으로 되돌립니다.
- 같은 가중치가 이어지면 하나의 블록으로 묶음: `(a:1.4), (b:1.4)` → `1.4::a, b::`
- `((태그))` = 1.21, `[태그]` = 0.91 로 괄호 강조를 숫자로 환산
- 네거티브는 NAI의 UC(Undesired Content) 칸용으로 따로 출력

### 3. 자연어 → 태그
한국어 문장을 쓰면 태그와 가중치가 자동으로 나옵니다.

> 입력: `키가 크고 가슴이 큰 톰보이. 선글라스를 낮게 걸쳐쓰고 흰 배경 앞에`
> 출력: `1girl, tall, large breasts, tomboy, sunglasses, (lowered eyewear:1.2), (white background:1.2), ...`

- **"매우/아주"** → 가중치 올림, **"살짝/약간"** → 내림
- **"없이/빼고/말고"** 가 붙은 표현은 네거티브로 이동
- SD 형식과 NAI 형식 둘 다 출력
- 인식 못한 표현은 아래에 회색 칩으로 표시

### 태그 사전 확장 (중요)
내장 사전은 기본 어휘만 담고 있습니다. **단보루 태그 데이터셋을 불러오면
한국어 인식 범위가 크게 넓어집니다.**

3번 탭 하단 `데이터셋 불러오기` 버튼으로 다음 형식을 지원합니다.

| 형식 | 내용 |
|---|---|
| `tags.json` | `english_name` / `korean_name` / `keyword` / `major_categories` / `count` |
| `autocomplete.csv` | `태그,분류,횟수,"설명 / 키워드: ..."` |
| `.txt` | 한 줄에 태그 하나, 또는 쉼표 구분 |

- 한 번 불러오면 **브라우저에 저장**되어 다음에 열어도 유지됩니다
- 작가 태그는 `아티스트`·`작가` 같은 키워드를 수만 개가 공유해 한국어 매칭을
  망치므로, 기본값은 영어 오타 검사에만 사용합니다
- 참고 데이터셋: [단보루 태그툴](https://danbooru-tag.mephistopheles.moe/) 제작자가
  공개한 CSV / JSON (약 37,000개 태그, 한국어명 포함)


## 사용법

`index.html`을 브라우저로 열면 끝. 각 탭의 **[예시]** 버튼으로 바로 체험할 수 있습니다.

단축키: `Ctrl+Enter` Positive 복사 · `Ctrl+Shift+Enter` Negative 복사

## 개인정보

네트워크 요청이 **아예 없습니다.** 입력 내용은 브라우저 밖으로 나가지 않습니다.

## 배포

정적 파일 하나라 GitHub Pages, Netlify, Cloudflare Pages 어디든 올라갑니다.
저장소 루트에 `index.html`을 두고 Pages를 켜면 됩니다.

## 라이선스

MIT

## Bundled dataset
`data/tags.min.json` is generated from the full `tags.json` dataset by `scripts/build_tags_min.py`.
Runtime row format: `[english_name, korean_name, keyword, major_categories, count]`.
The `description` field is intentionally omitted from the production payload.

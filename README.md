# 가짜 공격 생성기

테스트용 가짜 공격을 생성하는 간단한 프로그램입니다. 양식에 맞춰 공격용 함수를 작성하면 텍스트 기반 UI가 제공됩니다.

## 시작 방법

먼저 아래 명령을 통해 관련된 패키지들을 설치합니다.
```bash
pip install -r requirements.txt
```

`config.py` 파일을 열어 `Target_IP`를 대상 ip로 수정합니다.
```py
TARGET_IP = "YOUR_TARGET_IP"
```

`main.py`를 실행합니다.
```bash
python main.py
```


## config.py

Config에서 import하는 변수들은 다음과 같은 내용으로 사용하시면 됩니다.

| **변수명** | **자료형** | **설명** |
| --- | --- | --- |
| TARGET_IP | str | 공격 대상의 IP주소 |
| DEFAULT_TARGET_PORT | int | 기본 공격 포트번호 (80) |
| DEFAULT_COUNT | int | 기본으로 패킷을 보낼 횟수 (100회) |
| DEFAULT_INTERVAL | float | 패킷을 보내는 간격 (0.01초) |

이 변수들은 각 **공격 파일 내에서는 절대** 수정하지 마시고 **고정된 값**으로만 사용하세요.

수정할 필요가 있다면 다른 변수에 할당해서 사용하시기 바랍니다.

## 코드 추가

아래는 공격의 예시입니다. 해당 템플릿에 맞춰서 코드를 작성하세요.

```python
from config import TARGET_IP, DEFAULT_TARGET_PORT, DEFAULT_COUNT, DEFAULT_INTERVAL
from scapy.all import IP, UDP, Raw, send
import time
from tqdm import tqdm

NAME = "EXAMPLE Attack"

def run():
    # print("EXAMPLE Attack 실행")
    payload = b"A" * 1400   # 큰 응답을 흉내

    # Count만큼 패킷을 보내고, Interval만큼 대기
    for _ in tqdm(range(DEFAULT_COUNT)):
        packet = (
            IP(src="8.8.8.8", dst=TARGET_IP) /
            UDP(sport=53, dport=DEFAULT_TARGET_PORT) /
            Raw(payload)
        )

        # 실제로 패킷을 보내면 안돼서 주석 처리
        # send(packet, verbose=False)
        time.sleep(DEFAULT_INTERVAL)

if __name__ == "__main__":
    run()

```

**import**는 모두 동일하게 하시고, **NAME** 값은 공격 이름으로 바꾸어 저장합니다.

**run()** 함수 내부에 **공격 코드의 구현 내용**을 집어넣습니다.

```python
if __name__ == "__main__":
    run()
```

이 부분은 그대로 둡니다. 이 파일을 실행했을 때에도 실행이 되도록 써둔 코드입니다.



## 레퍼런스
**원본 레포지토리**
https://github.com/RyunK/FakeAttackMaker

**Fork 안내 블로그**
https://qkrrmsdud.tistory.com/43

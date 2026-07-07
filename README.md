# 가짜 공격 생성기


**내부망**으로 가짜 공격을 수행할 수 있는 프로그램입니다.

반드시 이 템플릿에 맞추어야 하는 건 아니고, 개별로 테스트하셔도 무관합니다만

최종적으로 모든 공격 코드들을 이 프로그램에 추가할 예정이고, **좀 더 결과를 확인하기 편한 템플릿**도 제공하고 있기 때문에 활용하시는 걸 추천드립니다.

## 코드 다운로드

### Fork

**Fork**는 앞서서도 해보셨죠? 제 github 주소에서 Fork 레포지토리를 다시 만듭니다.

```bash
cd [프로젝트를 다운받으실 경로]
git clone [Fork하신 개인 프로젝트 주소]
git remote add upstream https://github.com/RyunK/FakeAttackMaker.git
```

위 명령어를 순서대로 실행합니다.

FakeAttackMaker 폴더를 VSCode에서 연 뒤 (Open Folder),

 `ctrl+shift+p` > Python: Select Interpreter > Create Virtual Invironment

를 통해 가상환경도 구성합니다.

이 상태에서 터미널에 다음 명령어들을 실행하여 필요한 라이브러리들을 설치합니다.

```bash
pip install scapy tqdm
```

`main.py` 와 `config.py` 는 건드리지 않는 것을 전제로 합니다.

## 코드 추가

`attacks` 폴더 안에 `example.py` 파일이 있습니다. 제가 작성해둔 공격의 예시입니다. 해당 템플릿에 맞춰서 코드를 작성하세요.

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

**import**는 모두 동일하게 하시고, **NAME** 값은 각자 구현하시는 내용으로 바꾸어 저장합니다.

**run()** 함수 내부에 **공격 코드의 구현 내용**을 집어넣습니다.

```python
if __name__ == "__main__":
    run()
```

이 부분은 그대로 둡니다. 이 파일을 실행했을 때에도 실행이 되도록 써둔 코드입니다.

## 코드 실행

두 가지 방법이 있습니다. main을 실행할 수도, 개발한 각 파일만 실행할 수도 있습니다.

### Main

동일하게 `main.py` 파일 우측 상단의 삼각형 버튼을 누르거나, 터미널에 아래와 같은 명령어를 입력하여 실행할 수도 있습니다.

```bash
python main.py
```

터미널에 명령어를 입력할 때에는 경로 명의 마지막에 **FakeAttackMaker** (프로젝트 폴더)가 써있는지 꼭 확인해야 합니다. 


A를 입력하면 attacks 내부에 있는 모든 파일을 실행합니다.

### 파일 하나만 실행하기

마찬가지로 **FakeAttackMaker** 경로에서 다음 명령어를 실행합니다.

```bash
# python -m attacks.[.py 제외한 파일명]
```

예시 코드라면 다음과 같이 씁니다.

```bash
python -m attacks.example
```

파일에서 우측 상단의 실행 버튼을 누르면 config를 import 할 수 없다고 오류가 뜰 것입니다. 

config에서 받아오는 변수들을 사용하지 않으면 우측 상단의 실행 버튼으로도 실행이 가능하겠지만 어차피 **최종적으로 수정을 통해 IP 번호 등은 받아와야 할 필요가 있으므로**, 처음부터 이렇게 작업하며 손에 익혀두는 것을 추천드립니다.

## Config 변수들 설명

Config에서 import하는 변수들은 다음과 같은 내용으로 사용하시면 됩니다.

| **변수명** | **자료형** | **설명** |
| --- | --- | --- |
| TARGET_IP | str | 공격 대상의 IP주소 |
| DEFAULT_TARGET_PORT | int | 기본 공격 포트번호 (80) |
| DEFAULT_COUNT | int | 기본으로 패킷을 보낼 횟수 (100회) |
| DEFAULT_INTERVAL | float | 패킷을 보내는 간격 (0.01초) |

이 변수들은 **절대** 수정하지 마시고 **고정된 값으**로만 사용하세요.

수정할 필요가 있다면 다른 변수에 할당해서 사용하시기 바랍니다.

## 레퍼런스
**원본 레포지토리**
https://github.com/RyunK/FakeAttackMaker

**Fork 안내 블로그**
https://qkrrmsdud.tistory.com/43

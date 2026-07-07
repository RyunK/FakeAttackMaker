import importlib
import pkgutil
import time

import attacks

attack_modules = []

# attacks 폴더 안의 모든 py 파일 읽기
for _, module_name, _ in pkgutil.iter_modules(attacks.__path__):

    module = importlib.import_module(f"attacks.{module_name}")

    attack_modules.append(module)

attack_modules.sort(key=lambda m: m.NAME)

while True:

    print("\n===== Attack Simulator =====")

    for i, attack in enumerate(attack_modules, start=1):
        print(f"{i}. {attack.NAME}")

    print("A. Run All")
    print("Q. Exit")

    cmd = input("> ").strip().upper()

    if cmd == "Q":
        break

    elif cmd == "A":

        for attack in attack_modules:

            print(f"\n[{attack.NAME}]")
            attack.run()
            print(f"[{attack.NAME}] 완료")
            time.sleep(2)  # 각 공격 사이에 2초 대기

    elif cmd.isdigit():

        idx = int(cmd) - 1

        if 0 <= idx < len(attack_modules):

            print(f"\n[{attack_modules[idx].NAME}]")

            attack_modules[idx].run()
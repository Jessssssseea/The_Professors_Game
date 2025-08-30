def draw(heaps):
    for i, cnt in enumerate(heaps):
        print(f"堆 {i}: " + "🪨 " * cnt)

def main():
    n = int(input("堆数："))
    heaps = list(map(int, input(f"请依次输入 {n} 堆的石子数（空格分隔）：").split()))
    if len(heaps) != n:
        print("输入数量不符！")
        return

    names = ["A", "B", "C"]
    turn = 0

    while sum(heaps) > 0:
        print("\n" * 30)
        draw(heaps)
        print(f"\n{names[turn]} 的回合")
        try:
            idx, k = map(int, input("输入 “堆号 拿几颗”：").split())
            if not (0 <= idx < n and 1 <= k <= heaps[idx]):
                raise ValueError
        except ValueError:
            print("输入非法，请重试！")
            input("按回车继续...")
            continue
        heaps[idx] -= k
        turn = (turn + 1) % 3

    # 公布名次
    winner = (turn - 1) % 3
    first, second, third = names[winner], names[(winner + 1) % 3], names[(winner - 1) % 3]
    print("\n游戏结束！")
    print(f"\n第一名：{first}")
    print(f"第二名：{second}")
    print(f"第三名：{third}")

if __name__ == "__main__":
    main()
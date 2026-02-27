import random
import datetime

FORTUNES = [
    ("大吉", "今日は最高の流れ。小さく始めたことが大きく育ちます。"),
    ("中吉", "良い兆し。無理せず淡々と進めるほど成果が出ます。"),
    ("小吉", "安定の日。整理整頓や準備がツキを呼びます。"),
    ("吉",   "まずまず。丁寧なコミュニケーションが鍵です。"),
    ("末吉", "後半に良いことがありそう。焦らないでOK。"),
    ("凶",   "慎重に。大事な判断は一晩おいてから。"),
]

def main() -> None:
    today = datetime.date.today().isoformat()
    fortune, message = random.choice(FORTUNES)
    print(f"📅 {today}")
    print(f"🔮 今日の運勢: {fortune}")
    print(f"💬 {message}")

if __name__ == "__main__":
    main()

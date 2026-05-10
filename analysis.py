import sys
sys.stdout.reconfigure(encoding="utf-8")

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 200

age = rng.integers(20, 60, size=n)
experience = (age - 20) + rng.integers(0, 5, size=n)
salary = 250_000 + experience * 15_000 + rng.normal(0, 30_000, size=n)
department = rng.choice(["Engineering", "Sales", "Marketing", "HR"], size=n, p=[0.4, 0.3, 0.2, 0.1])
score = np.clip(rng.normal(70, 15, size=n), 0, 100)

df = pd.DataFrame({
    "age": age,
    "experience": experience,
    "salary": salary.astype(int),
    "department": department,
    "performance_score": score.round(1),
})

print("=" * 50)
print("【データ概要】")
print(f"行数: {len(df)}, 列数: {df.shape[1]}")
print(df.head())

print("\n" + "=" * 50)
print("【基本統計量】")
print(df.describe().round(1))

print("\n" + "=" * 50)
print("【部署別 平均給与・平均スコア】")
summary = df.groupby("department").agg(
    人数=("salary", "count"),
    平均給与=("salary", "mean"),
    平均スコア=("performance_score", "mean"),
).round(1)
print(summary.sort_values("平均給与", ascending=False))

print("\n" + "=" * 50)
print("【相関係数 (数値列)】")
print(df[["age", "experience", "salary", "performance_score"]].corr().round(3))

print("\n" + "=" * 50)
print("【高パフォーマー (スコア85以上) の割合】")
high = df[df["performance_score"] >= 85]
print(f"全体: {len(high)}/{len(df)} ({len(high)/len(df)*100:.1f}%)")
print(high.groupby("department").size().rename("人数"))

# CLAUDE.md — プロジェクト作業ガイド

## プロジェクト概要

Python データ分析・機械学習プロジェクト。従業員データの探索的分析スクリプトと、Kaggle Playground Series (S6E4) の灌漑需要予測コンペノートブックが含まれる。

## 技術スタック

- **Python**: 3.12
- **パッケージ管理**: `uv`（`pyproject.toml` / `uv.lock`）
- **仮想環境**: `.venv/`
- **主要ライブラリ**: numpy, pandas, matplotlib, scikit-learn, jupyter
- **OS**: Windows 11 / PowerShell

## ファイル構成

```
claude-code-analysis/
├── analysis.py                          # 従業員データ分析スクリプト（pandas/numpy）
├── main.py                              # ユーティリティ関数（greet, add）
├── pg-s6e4-xgb-cv-0-97723-lb-0-97644.ipynb  # Kaggle XGBoost コンペノートブック
├── train.csv / test.csv                 # データ（大容量 ~80MB / ~33MB）
├── eda_01_target.png ～ eda_07_scatter.png  # EDA 可視化出力
├── pyproject.toml                       # 依存関係定義
└── uv.lock                              # ロックファイル
```

## コマンド早見表

```powershell
# 仮想環境の有効化
.\.venv\Scripts\activate.ps1

# スクリプト実行
.\.venv\Scripts\python.exe analysis.py
.\.venv\Scripts\python.exe main.py

# JupyterLab 起動
.\.venv\Scripts\jupyter-lab.exe

# パッケージ追加（uv）
uv add <package>

# 依存関係の同期
uv sync
```

## Kaggle ノートブック (pg-s6e4) 概要

- **コンペ**: Playground Series S6E4 — 灌漑需要 (Low/Medium/High) 分類
- **モデル**: XGBoost (`multi:softprob`)
- **CV スコア**: 0.97723 / LB: 0.97644
- **評価指標**: `balanced_accuracy_score`
- **手法**: StratifiedKFold (5-fold), TargetEncoder, ペアワイズ特徴量生成, クラス重み付け

## 作業上の注意点

- `ls` は PowerShell で `Get-ChildItem` を使う（bash の `ls` 不可）
- `train.csv` / `test.csv` は大容量なので直接 `Read` しない
- `.venv` 内のファイルは編集しない
- git リポジトリは未初期化（コミット不要）
- EDA 画像は `analysis.py` を実行して再生成するもの（手動編集不要）

# FastAPI × Next.js 学習プロジェクト

---

## プロジェクト概要

- **バックエンド**：FastAPI  
- **フロントエンド**：Next.js（React + Tailwind CSS）  
- **通信方法**：Fetch API（HTTPリクエスト）
- **目的**：
  - FastAPIでREST APIを構築する方法を理解する
  - Next.jsからバックエンドAPIを呼び出す方法を学ぶ
  - JSONデータの送受信を実装する
  - CORS設定の重要性を理解する

---

## ディレクトリ構成

```

project/
├── backend/
│   ├── app.py              # FastAPIのメインアプリ
│   └── requirements.txt
│
└── frontend/
└── app/page.jsx        # Next.jsのトップページ

````

---

## バックエンド（FastAPI）

### 起動方法

```
cd backend
uvicorn app:app --reload
```

### エンドポイント一覧

| メソッド   | パス                   | 説明             | 例                                                     |
| ------ | -------------------- | -------------- | ----------------------------------------------------- |
| `GET`  | `/`                  | テスト用（固定メッセージ）  | —                                                     |
| `GET`  | `/api/hello`         | 固定メッセージを返す     | `{"message": "Hello kenta"}`                          |
| `GET`  | `/api/multiply/{id}` | 数値を2倍にして返す     | `/api/multiply/10` → `{"doubled_value": 20}`          |
| `POST` | `/api/echo`          | 送信メッセージをそのまま返す | `{"message": "hello"}` → `{"message": "echo: hello"}` |
| `GET`  | `/api/divide/{id}`   | 数値を2で割る        | `/api/divide/8` → `{"half_value": 4}`                 |
| `GET`  | `/api/count/{text}`  | 文字列の長さを返す      | `/api/count/abc` → `{"count": 3}`                     |

### ポイント学習

* `pydantic.BaseModel` で受信JSONデータを型安全に扱う
* `CORSMiddleware` でNext.jsとの通信を許可
* Pythonのprintでサーバー側ログを確認できる
* FastAPIは自動でAPIドキュメント（Swagger UI）を生成（`/docs`で確認可）

---

## フロントエンド（Next.js）

### 起動方法

```
cd frontend
npm run dev
```

### 主な機能

| 機能        | 説明                              |
| --------- | ------------------------------- |
| GETリクエスト  | `/api/hello` から固定メッセージ取得        |
| 数値2倍      | `/api/multiply/{id}` を呼び出して結果表示 |
| POSTリクエスト | `/api/echo` に文字を送り、サーバーの応答を表示   |
| 数値割り算     | `/api/divide/{id}` で2で割った値を表示   |
| 文字カウント    | `/api/count/{text}` で文字数を返す     |

### ポイント学習

* `useState()` で入力値とAPI応答を状態管理
* `fetch()` 関数で非同期通信を実装
* `async/await` 構文でレスポンスを待機
* CORS設定がないとブラウザでエラーになる点を理解
* Tailwind CSSで簡潔にスタイリング

---

## 学んだことまとめ

### バックエンド側

* FastAPIは軽量で開発が高速
* Pythonの型ヒントが自動でバリデーションに利用される
* 自動ドキュメント生成（Swagger UI / Redoc）が便利
* CORSを理解しないとフロントから通信できない

### フロントエンド側

* fetchでAPI通信を行う基本的な書き方を理解
* JSONの送受信（`Content-Type: application/json`）の仕組みを学習
* React Hooks（useState）で動的なUI更新を実装
* APIレスポンスをリアルタイムで画面に反映

---

## 参考資料

* [FastAPI公式ドキュメント](https://fastapi.tiangolo.com/)
* [Next.js公式ドキュメント](https://nextjs.org/docs)
* [MDN Fetch API](https://developer.mozilla.org/ja/docs/Web/API/Fetch_API)
* [Tailwind CSS Docs](https://tailwindcss.com/docs)

---



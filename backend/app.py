from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# FastAPIアプリケーションを作成
app = FastAPI()

# ===== CORS設定 =====
# フロントエンド（Next.js）とバックエンド（FastAPI）が異なるポートで動作しているため、
# ブラウザのセキュリティ制約（同一オリジンポリシー）を回避する設定を行う。
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.jsの実行URLを許可
    allow_credentials=True, #オリジン間リクエストでCookieをサポートする必要があることを示している。デフォルトは False
    allow_methods=["*"], # GET, POST, PUT, DELETE
    allow_headers=["*"] # Accept, Accept-Language, Content-Language, Content-Type
)

# ===== データスキーマ定義 =====
# POSTリクエストで送信されるJSONデータをPythonオブジェクトとして受け取るためのモデル。
class EchoMessage(BaseModel):
    message: str | None = None  # messageキーの値を保持（Noneを許可）

# ====== APIエンドポイント定義 ======

# シンプルなルートパス "/" にアクセスしたときの応答
@app.get("/")
def hello():
    return {"message": "FastAPI hello!"}

# Must課題①: 固定メッセージを返すAPI
@app.get("/api/hello")
def hello_world():
    # Next.js側のGETボタンから呼ばれる
    return {"message": "Hello kenta"}

# 数値を2倍にして返すAPI
@app.get("/api/multiply/{id}") #パス内に{id: int}とは書けない
def multiply(id: int):
    print("multiply")
    doubled_value = id * 2
    return {"doubled_value": doubled_value}

# 受け取ったメッセージをそのまま返す（エコー）API
@app.post("/api/echo")
def echo(message: EchoMessage):
    print("echo")
    if not message:
        raise HTTPException(status_code=400, detail="Invalid JSON") #エラーハンドリング，今回BaseModelを使っているから不要？追加で調べる！！

    # 受け取ったメッセージがあればそのまま返す。なければデフォルトメッセージ。
    echo_message = message.message if message.message else "No message provided"
    return {"message": f"echo: {echo_message}"}

# Must課題②: 数値を2で割るAPI
@app.get("/api/divide/{id}")
def divide(id: int):
    print("divide")
    half_value = id / 2  # 割り算して半分にする
    return {"half_value": half_value}

# Want課題①: 文字列の長さを数えるAPI
@app.get("/api/count/{text}")
def count(text: str):
    print("count")
    text_length = len(text)  # len関数で文字数をカウント
    return {"count": text_length}

# ====== アプリ起動設定 ======
if __name__ == "__main__":
    import uvicorn
    # すべてのIPからアクセスできるようにし、ポート8000で起動
    uvicorn.run(app, host="0.0.0.0", port=8000)

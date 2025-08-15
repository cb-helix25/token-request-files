# exchange_asana_code_fixed.py
import requests
import urllib.parse

# ── CONFIG ──────────────────────────────────────────────────────
CLIENT_ID     = "1210963272515110"
CLIENT_SECRET = "74777e377bcc0fea7a2913c25b363148"
REDIRECT_URI  = "https://helix-law.co.uk/"   # must exactly match your Asana app settings
TOKEN_URL     = "https://app.asana.com/-/oauth_token"
# ────────────────────────────────────────────────────────────────

def exchange_code_for_tokens(raw_code: str) -> dict:
    code = urllib.parse.unquote(raw_code)    # <-- decode here
    resp = requests.post(
        TOKEN_URL,
        data={
            "grant_type":    "authorization_code",
            "client_id":     CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "redirect_uri":  REDIRECT_URI,
            "code":          code,
        },
    )
    resp.raise_for_status()
    return resp.json()

if __name__ == "__main__":
    # your URL-encoded code
    raw_code = "2%2F1210936861491525%2F1210963272515110%3A32abd214fa7f8e4e934ccfeb9c4f5bb7"
    tokens = exchange_code_for_tokens(raw_code)
    print("Access Token: ", tokens["access_token"])
    print("Refresh Token:", tokens["refresh_token"])

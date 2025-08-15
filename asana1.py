# asana_auth_url.py
from requests_oauthlib import OAuth2Session

# ── CONFIG ──────────────────────────────────────────────────────
CLIENT_ID    = "1210963272515110"
REDIRECT_URI = "https://helix-law.co.uk/"  # must match your Asana app settings
AUTH_BASE_URL = "https://app.asana.com/-/oauth_authorize"
# ────────────────────────────────────────────────────────────────

def main():
    oauth = OAuth2Session(CLIENT_ID, redirect_uri=REDIRECT_URI)
    auth_url, state = oauth.authorization_url(
        AUTH_BASE_URL,
        state="random_state_string"
    )
    print("1) Go here and authorize:\n", auth_url)

if __name__ == "__main__":
    main()
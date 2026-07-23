from flask import Flask

app = Flask(__name__)

APP_VERSION = "v8"

FONTS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Space+Grotesk:wght@400;500;600;700"
    "&family=JetBrains+Mono:wght@400;500;600"
    "&display=swap"
)

PAGE = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>flask-app · GitOps on EKS</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{FONTS_URL}" rel="stylesheet">
<style>
  :root {{
    --bg: #0F141B;
    --panel: #161D27;
    --panel-border: #232C3A;
    --text: #E7ECF3;
    --muted: #8592A3;
    --blue: #4C8DFF;
    --amber: #FFB454;
    --green: #34D399;
  }}

  * {{ box-sizing: border-box; }}

  body {{
    margin: 0;
    background: var(--bg);
    background-image:
      radial-gradient(circle at 15% 0%, rgba(76,141,255,0.08), transparent 45%),
      radial-gradient(circle at 85% 15%, rgba(255,180,84,0.06), transparent 40%);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    -webkit-font-smoothing: antialiased;
  }}

  .wrap {{
    max-width: 880px;
    margin: 0 auto;
    padding: 72px 24px 48px;
  }}

  .eyebrow {{
    color: var(--muted);
    font-size: 13px;
    letter-spacing: 0.06em;
    display: flex;
    align-items: center;
    gap: 8px;
  }}

  .eyebrow .sep {{ color: var(--panel-border); }}

  h1 {{
    font-family: 'Space Grotesk', sans-serif;
    font-weight: 700;
    font-size: clamp(36px, 6vw, 56px);
    line-height: 1.05;
    margin: 18px 0 12px;
    letter-spacing: -0.01em;
  }}

  .lede {{
    color: var(--muted);
    font-size: 15px;
    max-width: 480px;
    line-height: 1.6;
    margin: 0 0 28px;
  }}

  .status-row {{
    display: flex;
    align-items: center;
    gap: 18px;
    flex-wrap: wrap;
    margin-bottom: 56px;
  }}

  .pill {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: var(--panel);
    border: 1px solid var(--panel-border);
    border-radius: 999px;
    padding: 7px 14px;
    font-size: 12.5px;
    color: var(--text);
  }}

  .dot {{
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--green);
    box-shadow: 0 0 0 0 rgba(52,211,153,0.6);
    animation: pulse 2s infinite;
  }}

  @keyframes pulse {{
    0%   {{ box-shadow: 0 0 0 0 rgba(52,211,153,0.55); }}
    70%  {{ box-shadow: 0 0 0 7px rgba(52,211,153,0); }}
    100% {{ box-shadow: 0 0 0 0 rgba(52,211,153,0); }}
  }}

  .pill.muted {{ color: var(--muted); }}
  .pill b {{ color: var(--amber); font-weight: 600; }}

  /* pipeline */
  .section-label {{
    font-size: 11.5px;
    letter-spacing: 0.12em;
    color: var(--muted);
    text-transform: uppercase;
    margin-bottom: 18px;
  }}

  .pipeline {{
    position: relative;
    background: var(--panel);
    border: 1px solid var(--panel-border);
    border-radius: 14px;
    padding: 36px 24px 28px;
    margin-bottom: 48px;
    overflow: hidden;
  }}

  .track {{
    position: relative;
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }}

  .track::before {{
    content: "";
    position: absolute;
    top: 17px;
    left: 17px;
    right: 17px;
    height: 2px;
    background: linear-gradient(90deg, var(--blue), var(--amber));
    opacity: 0.35;
  }}

  .track::after {{
    content: "";
    position: absolute;
    top: 14px;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: var(--blue);
    box-shadow: 0 0 12px 2px rgba(76,141,255,0.8);
    animation: travel 5s linear infinite;
  }}

  @keyframes travel {{
    0%   {{ left: 0%; background: var(--blue); }}
    50%  {{ background: var(--amber); }}
    100% {{ left: calc(100% - 8px); background: var(--blue); }}
  }}

  .node {{
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 20%;
  }}

  .node .ring {{
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: var(--bg);
    border: 2px solid var(--blue);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    margin-bottom: 12px;
    z-index: 1;
  }}

  .node .label {{
    font-size: 12px;
    font-weight: 600;
    color: var(--text);
    font-family: 'Space Grotesk', sans-serif;
    margin-bottom: 4px;
  }}

  .node .caption {{
    font-size: 10.5px;
    color: var(--muted);
    line-height: 1.4;
  }}

  @media (max-width: 640px) {{
    .track {{ flex-direction: column; gap: 20px; align-items: flex-start; }}
    .track::before, .track::after {{ display: none; }}
    .node {{ width: 100%; flex-direction: row; text-align: left; gap: 12px; }}
    .node .ring {{ margin-bottom: 0; flex-shrink: 0; }}
  }}

  /* stack grid */
  .stack {{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 56px;
  }}

  .badge {{
    border: 1px solid var(--panel-border);
    background: var(--panel);
    color: var(--muted);
    font-size: 12.5px;
    padding: 8px 14px;
    border-radius: 8px;
    transition: border-color 0.15s ease, color 0.15s ease, transform 0.15s ease;
  }}

  .badge:hover {{
    border-color: var(--blue);
    color: var(--text);
    transform: translateY(-1px);
  }}

  footer {{
    border-top: 1px solid var(--panel-border);
    padding-top: 22px;
    color: var(--muted);
    font-size: 12px;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 10px;
  }}

  footer .prompt {{ color: var(--blue); }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="eyebrow">
      <span>ap-south-1</span><span class="sep">·</span>
      <span>flux-system</span><span class="sep">·</span>
      <span>flask-app</span>
    </div>

    <h1>Hello from GitOps</h1>
    <p class="lede">
      Every push to main rebuilds, retags, and redeploys this service
      on its own. No manual kubectl apply.
    </p>

    <div class="status-row">
      <span class="pill"><span class="dot"></span>live</span>
      <span class="pill muted">build <b>{APP_VERSION}</b></span>
      <span class="pill muted" id="health-pill">health: checking /health…</span>
    </div>

    <div class="section-label">Deployment pipeline</div>
    <div class="pipeline">
      <div class="track">
        <div class="node">
          <div class="ring">①</div>
          <div class="label">git push</div>
          <div class="caption">main branch</div>
        </div>
        <div class="node">
          <div class="ring">②</div>
          <div class="label">CI</div>
          <div class="caption">lint · test · build</div>
        </div>
        <div class="node">
          <div class="ring">③</div>
          <div class="label">Docker Hub</div>
          <div class="caption">tagged image</div>
        </div>
        <div class="node">
          <div class="ring">④</div>
          <div class="label">Flux CD</div>
          <div class="caption">image policy sync</div>
        </div>
        <div class="node">
          <div class="ring">⑤</div>
          <div class="label">EKS</div>
          <div class="caption">rolling deploy</div>
        </div>
      </div>
    </div>

    <div class="section-label">Stack</div>
    <div class="stack">
      <span class="badge">Terraform</span>
      <span class="badge">Amazon EKS</span>
      <span class="badge">Flux CD</span>
      <span class="badge">Helm</span>
      <span class="badge">GitHub Actions</span>
      <span class="badge">Docker</span>
      <span class="badge">AWS ALB</span>
      <span class="badge">Flask</span>
    </div>

    <footer>
      <span class="prompt">$ kubectl get deployment flask-app -n flask-app</span>
      <span>infrastructure as code · GitOps continuous deployment</span>
    </footer>
  </div>

  <script>
    fetch('/health').then(r => r.json()).then(d => {{
      document.getElementById('health-pill').textContent = 'health: ' + d.status;
    }}).catch(() => {{
      document.getElementById('health-pill').textContent = 'health: unreachable';
    }});
  </script>
</body>
</html>"""


@app.route("/")
def home():
    return PAGE


@app.route("/health")
def health():
    return {"status": "UP"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

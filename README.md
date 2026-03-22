<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Resume Project Snippets — Amruth Kumar M</title>
<link href="https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Mono:wght@400;500&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
  :root {
    --violet: #7C3AED;
    --violet-light: #A78BFA;
    --violet-glow: rgba(124, 58, 237, 0.18);
    --ink: #0D0A1A;
    --surface: #120E22;
    --card: #1C1630;
    --border: rgba(124, 58, 237, 0.22);
    --text-primary: #F0EBff;
    --text-secondary: #9D8FC4;
    --text-muted: #5E5480;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    background: var(--ink);
    color: var(--text-primary);
    font-family: 'Outfit', sans-serif;
    min-height: 100vh;
    padding: 48px 24px 80px;
    position: relative;
    overflow-x: hidden;
  }
  body::before {
    content: '';
    position: fixed;
    top: -200px; left: 50%;
    transform: translateX(-50%);
    width: 900px; height: 600px;
    background: radial-gradient(ellipse, rgba(124,58,237,0.12) 0%, transparent 70%);
    pointer-events: none;
    z-index: 0;
  }
  .wrapper { max-width: 860px; margin: 0 auto; position: relative; z-index: 1; }

  /* Header */
  .page-header { text-align: center; margin-bottom: 60px; animation: fadeDown 0.7s ease both; }
  .page-header .label {
    font-family: 'DM Mono', monospace;
    font-size: 11px; letter-spacing: 3px; text-transform: uppercase;
    color: var(--violet-light); margin-bottom: 14px; display: block;
  }
  .page-header h1 {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(28px, 5vw, 44px); color: var(--text-primary);
    line-height: 1.15; margin-bottom: 12px;
  }
  .page-header h1 em { font-style: italic; color: var(--violet-light); }
  .page-header p { color: var(--text-secondary); font-size: 15px; font-weight: 300; }

  /* Card */
  .project-card {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 36px 40px;
    margin-bottom: 28px;
    position: relative;
    overflow: hidden;
    animation: fadeUp 0.6s ease both;
    transition: border-color 0.3s, box-shadow 0.3s;
  }
  .project-card:nth-child(1) { animation-delay: 0.1s; }
  .project-card:nth-child(2) { animation-delay: 0.2s; }
  .project-card:nth-child(3) { animation-delay: 0.3s; }
  .project-card:hover { border-color: rgba(124,58,237,0.5); box-shadow: 0 0 40px rgba(124,58,237,0.1); }
  .project-card::before {
    content: '';
    position: absolute; top: 0; right: 0;
    width: 120px; height: 120px;
    background: radial-gradient(circle at top right, rgba(124,58,237,0.15), transparent 70%);
    pointer-events: none;
  }
  .card-num {
    position: absolute; top: 36px; right: 40px;
    font-family: 'DM Serif Display', serif; font-size: 72px;
    color: rgba(124,58,237,0.07); line-height: 1;
    user-select: none; pointer-events: none;
  }
  .card-top { display: flex; align-items: flex-start; gap: 16px; margin-bottom: 20px; }
  .card-icon {
    width: 46px; height: 46px; border-radius: 12px;
    background: var(--violet-glow); border: 1px solid rgba(124,58,237,0.3);
    display: flex; align-items: center; justify-content: center;
    font-size: 20px; flex-shrink: 0;
  }
  .card-meta { flex: 1; }
  .card-title {
    font-family: 'DM Serif Display', serif; font-size: 20px;
    color: var(--text-primary); line-height: 1.3; margin-bottom: 8px;
  }
  .tag-row { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 8px; }
  .tag {
    font-family: 'DM Mono', monospace; font-size: 10.5px;
    padding: 3px 9px; border-radius: 5px; font-weight: 500; letter-spacing: 0.5px;
  }
  .tag-violet { background: rgba(124,58,237,0.18); color: var(--violet-light); border: 1px solid rgba(124,58,237,0.25); }
  .tag-green  { background: rgba(16,185,129,0.12); color: #6EE7B7; border: 1px solid rgba(16,185,129,0.2); }
  .tag-amber  { background: rgba(245,158,11,0.12); color: #FCD34D; border: 1px solid rgba(245,158,11,0.2); }
  .tag-cyan   { background: rgba(6,182,212,0.12); color: #67E8F9; border: 1px solid rgba(6,182,212,0.2); }
  .link-row { display: flex; gap: 12px; }
  .proj-link {
    font-family: 'DM Mono', monospace; font-size: 11px; color: var(--violet-light);
    text-decoration: none; display: flex; align-items: center; gap: 5px;
    opacity: 0.85; transition: opacity 0.2s;
  }
  .proj-link:hover { opacity: 1; text-decoration: underline; }
  .card-divider {
    height: 1px;
    background: linear-gradient(to right, transparent, var(--border), transparent);
    margin: 20px 0;
  }

  /* Copy-all row */
  .copy-all-row {
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 12px;
  }
  .section-label {
    font-family: 'DM Mono', monospace; font-size: 10px;
    letter-spacing: 2px; text-transform: uppercase; color: var(--text-muted);
  }
  .btn-copy-all {
    display: flex; align-items: center; gap: 6px;
    background: rgba(124,58,237,0.12);
    border: 1px solid rgba(124,58,237,0.28);
    border-radius: 7px; padding: 5px 12px;
    font-family: 'DM Mono', monospace; font-size: 11px;
    color: var(--violet-light); cursor: pointer;
    transition: background 0.2s, border-color 0.2s, transform 0.15s;
    letter-spacing: 0.4px;
  }
  .btn-copy-all:hover {
    background: rgba(124,58,237,0.22);
    border-color: rgba(124,58,237,0.5);
    transform: translateY(-1px);
  }
  .btn-copy-all svg { width: 12px; height: 12px; }

  /* Bullets list */
  .bullets { list-style: none; display: flex; flex-direction: column; gap: 8px; }
  .bullets li {
    display: flex; align-items: flex-start;
    font-size: 14.5px; line-height: 1.65; color: var(--text-secondary);
    background: rgba(255,255,255,0.018);
    border: 1px solid transparent;
    border-radius: 10px;
    padding: 10px 12px 10px 14px;
    transition: background 0.2s, border-color 0.2s;
    position: relative;
  }
  .bullets li:hover {
    background: rgba(124,58,237,0.07);
    border-color: rgba(124,58,237,0.18);
  }
  .bullet-left {
    padding-top: 8px; margin-right: 12px; flex-shrink: 0;
  }
  .bullet-dot {
    width: 6px; height: 6px; border-radius: 50%; background: var(--violet);
  }
  .bullet-text { flex: 1; }
  .bullets li strong { color: var(--text-primary); font-weight: 600; }
  .bullets li .hl { color: var(--violet-light); font-weight: 500; }

  /* Per-bullet copy btn */
  .btn-copy-bullet {
    display: flex; align-items: center; gap: 4px;
    background: transparent;
    border: 1px solid transparent;
    border-radius: 6px; padding: 4px 8px;
    font-family: 'DM Mono', monospace; font-size: 10px;
    color: var(--text-muted); cursor: pointer;
    transition: all 0.2s; flex-shrink: 0;
    margin-left: 10px; margin-top: 3px;
    white-space: nowrap; opacity: 0;
  }
  .bullets li:hover .btn-copy-bullet { opacity: 1; }
  .btn-copy-bullet:hover {
    background: rgba(124,58,237,0.14);
    border-color: rgba(124,58,237,0.3);
    color: var(--violet-light);
  }
  .btn-copy-bullet.copied {
    color: #6EE7B7 !important;
    border-color: rgba(16,185,129,0.3) !important;
    background: rgba(16,185,129,0.08) !important;
    opacity: 1 !important;
  }
  .btn-copy-bullet svg { width: 11px; height: 11px; }

  /* Stat pills */
  .stat-row {
    display: flex; flex-wrap: wrap; gap: 10px;
    margin-top: 20px; padding-top: 18px;
    border-top: 1px solid var(--border);
  }
  .stat-pill {
    display: flex; align-items: center; gap: 7px;
    background: var(--surface); border: 1px solid var(--border);
    border-radius: 8px; padding: 7px 14px; font-size: 12.5px;
  }
  .stat-pill .val { font-family: 'DM Mono', monospace; font-weight: 500; color: var(--violet-light); }
  .stat-pill .lbl { color: var(--text-muted); }

  /* Toast */
  #toast {
    position: fixed; bottom: 32px; left: 50%;
    transform: translateX(-50%) translateY(20px);
    background: #1e1a30;
    border: 1px solid rgba(124,58,237,0.4);
    border-radius: 10px; padding: 11px 20px;
    font-family: 'DM Mono', monospace; font-size: 12px;
    color: var(--violet-light);
    display: flex; align-items: center; gap: 8px;
    opacity: 0; pointer-events: none;
    transition: opacity 0.25s, transform 0.25s;
    z-index: 999;
    box-shadow: 0 8px 30px rgba(0,0,0,0.4);
    white-space: nowrap;
  }
  #toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
  #toast .tick { color: #6EE7B7; font-size: 14px; }

  .copy-hint {
    text-align: center; margin-top: 40px;
    color: var(--text-muted); font-size: 12px;
    font-family: 'DM Mono', monospace; letter-spacing: 0.5px;
    animation: fadeUp 0.7s 0.5s ease both;
  }

  @keyframes fadeDown { from { opacity:0; transform:translateY(-20px); } to { opacity:1; transform:translateY(0); } }
  @keyframes fadeUp   { from { opacity:0; transform:translateY(24px);  } to { opacity:1; transform:translateY(0); } }

  @media (max-width: 600px) {
    .project-card { padding: 24px 18px; }
    .card-num { font-size: 52px; top: 24px; right: 18px; }
    .card-top { flex-direction: column; gap: 12px; }
    .btn-copy-bullet { opacity: 1; }
  }
</style>
</head>
<body>

<div id="toast"><span class="tick">✓</span><span id="toast-msg">Copied!</span></div>

<div class="wrapper">

  <header class="page-header">
    <span class="label">Portfolio · Resume Snippets</span>
    <h1>Amruth Kumar M<br><em>Project Highlights</em></h1>
    <p>B.Tech AI &amp; Data Science · REVA University · Data Science Intern @ iStudio</p>
  </header>

  <!-- ══════════ CARD 1 ══════════ -->
  <article class="project-card">
    <span class="card-num">01</span>
    <div class="card-top">
      <div class="card-icon">📉</div>
      <div class="card-meta">
        <h2 class="card-title">Customer Churn Prediction &amp; Retention ROI System</h2>
        <div class="tag-row">
          <span class="tag tag-violet">Python</span>
          <span class="tag tag-violet">XGBoost</span>
          <span class="tag tag-violet">SHAP</span>
          <span class="tag tag-green">Streamlit</span>
          <span class="tag tag-amber">Docker</span>
        </div>
        <div class="link-row">
          <a href="#" class="proj-link">⌥ GitHub</a>
          <a href="#" class="proj-link">↗ Live App</a>
        </div>
      </div>
    </div>
    <div class="card-divider"></div>
    <div class="copy-all-row">
      <span class="section-label">Bullet Points</span>
      <button class="btn-copy-all" onclick="copyAll(this,'card1')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
        Copy All 3 Bullets
      </button>
    </div>
    <ul class="bullets" id="card1">
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Engineered an <strong>end-to-end ML pipeline</strong> — raw Excel → EDA → feature engineering → model selection (4 algorithms benchmarked) → deployment; <span class="hl">XGBoost won with AUC 0.9989</span> and 98.76% accuracy on imbalanced data (16.84% churn rate).</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Surfaced <strong>937 high-risk customers</strong> representing <span class="hl">₹47,40,000 preventable annual loss</span>; discovered 0–3 month customers churn at 41.9% via cohort analysis — insight invisible in raw data, now the <strong>#1 retention recommendation</strong>.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Shipped an <strong>8-page live Streamlit dashboard</strong> with per-prediction SHAP explanations, 12-factor What-If Simulator, and Budget Optimizer proving <span class="hl">224% campaign ROI</span> — Dockerized and deployed on Streamlit Cloud.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
    </ul>
    <div class="stat-row">
      <div class="stat-pill"><span class="val">0.9989</span><span class="lbl">AUC-ROC</span></div>
      <div class="stat-pill"><span class="val">98.76%</span><span class="lbl">Accuracy</span></div>
      <div class="stat-pill"><span class="val">₹47.4L</span><span class="lbl">Revenue Saved</span></div>
      <div class="stat-pill"><span class="val">224%</span><span class="lbl">Campaign ROI</span></div>
      <div class="stat-pill"><span class="val">937</span><span class="lbl">At-risk Customers</span></div>
    </div>
  </article>

  <!-- ══════════ CARD 2 ══════════ -->
  <article class="project-card">
    <span class="card-num">02</span>
    <div class="card-top">
      <div class="card-icon">🌊</div>
      <div class="card-meta">
        <h2 class="card-title">Social Media Sentiment Analysis — Enterprise PySpark Engine</h2>
        <div class="tag-row">
          <span class="tag tag-violet">Python</span>
          <span class="tag tag-cyan">PySpark</span>
          <span class="tag tag-cyan">Delta Lake</span>
          <span class="tag tag-green">Streamlit</span>
          <span class="tag tag-amber">Docker</span>
          <span class="tag tag-amber">GitHub Actions</span>
        </div>
        <div class="link-row">
          <a href="https://github.com/Amruth011/Social_Media_Sentiment_Analysis" target="_blank" class="proj-link">⌥ GitHub</a>
          <a href="https://socialmediasentimentanalysis-9hj7cfkcjjsdky5xwbmzzr.streamlit.app/" target="_blank" class="proj-link">↗ Live Dashboard</a>
        </div>
      </div>
    </div>
    <div class="card-divider"></div>
    <div class="copy-all-row">
      <span class="section-label">Bullet Points</span>
      <button class="btn-copy-all" onclick="copyAll(this,'card2')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
        Copy All 3 Bullets
      </button>
    </div>
    <ul class="bullets" id="card2">
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Built a <strong>production-grade distributed PySpark pipeline</strong> that replaces fragile Jupyter-to-CSV workflows — raw CSV → data quality assertions → custom UDF feature engineering → <span class="hl">5 Delta Lake ACID sinks</span> with time-travel capability.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Implemented <strong>fail-fast data quality layer</strong> with schema validation, null checks, and pre-processing assertions; modularized into OOP Python packages with <span class="hl">PyTest unit tests and CI/CD via GitHub Actions</span> — automated on every push to main.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Delivered <strong>5 analytical insights</strong> (top sentiments, platform distribution, country engagement, hourly trends) via an interactive Streamlit executive dashboard; <span class="hl">Dockerized</span> for Databricks/Kubernetes cluster deployment.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
    </ul>
    <div class="stat-row">
      <div class="stat-pill"><span class="val">5</span><span class="lbl">Delta Tables</span></div>
      <div class="stat-pill"><span class="val">ACID</span><span class="lbl">Transactions</span></div>
      <div class="stat-pill"><span class="val">CI/CD</span><span class="lbl">GitHub Actions</span></div>
      <div class="stat-pill"><span class="val">Prod-Grade</span><span class="lbl">Architecture</span></div>
    </div>
  </article>

  <!-- ══════════ CARD 3 ══════════ -->
  <article class="project-card">
    <span class="card-num">03</span>
    <div class="card-top">
      <div class="card-icon">📚</div>
      <div class="card-meta">
        <h2 class="card-title">Kannada Book AI Agent — Multilingual RAG Chatbot</h2>
        <div class="tag-row">
          <span class="tag tag-violet">Python</span>
          <span class="tag tag-violet">RAG</span>
          <span class="tag tag-cyan">ChromaDB</span>
          <span class="tag tag-cyan">Surya OCR</span>
          <span class="tag tag-green">Sarvam AI</span>
          <span class="tag tag-amber">Streamlit</span>
        </div>
        <div class="link-row">
          <a href="https://github.com/Amruth011/kannada-rag-agent" target="_blank" class="proj-link">⌥ GitHub</a>
          <a href="https://kannada-rag-agent-hqvwhfejguymb9ijrvz4hd.streamlit.app/" target="_blank" class="proj-link">↗ Live Demo</a>
        </div>
      </div>
    </div>
    <div class="card-divider"></div>
    <div class="copy-all-row">
      <span class="section-label">Bullet Points</span>
      <button class="btn-copy-all" onclick="copyAll(this,'card3')">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>
        Copy All 3 Bullets
      </button>
    </div>
    <ul class="bullets" id="card3">
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Designed a <strong>7-stage scanned-PDF-to-RAG pipeline</strong> from scratch: pdf2image → OpenCV preprocessing → <span class="hl">Surya OCR (GPU-batched tensor processing)</span> → indic-nlp normalization → semantic chunking → ChromaDB vector store → Sarvam-M LLM.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Processed <strong>346 pages into 687 semantic chunks</strong> with multilingual bilingual Q&amp;A (Kannada + English), conversational memory, page-level citations, and <span class="hl">end-to-end TTS audio</span> via Sarvam AI's bulbul:v3 with custom API chunking &amp; byte stitching.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
      <li>
        <div class="bullet-left"><div class="bullet-dot"></div></div>
        <span class="bullet-text">Shipped a <strong>premium glassmorphism Streamlit UI</strong> with smart query routing (general vs RAG), toggle-able source chunk inspection, and bilingual switching — targeting <span class="hl">Indic-language AI accessibility</span> as a portfolio differentiator for AI Engineer roles.</span>
        <button class="btn-copy-bullet" onclick="copyBullet(this)">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 01-2-2V4a2 2 0 012-2h9a2 2 0 012 2v1"/></svg>copy
        </button>
      </li>
    </ul>
    <div class="stat-row">
      <div class="stat-pill"><span class="val">346</span><span class="lbl">Pages Processed</span></div>
      <div class="stat-pill"><span class="val">687</span><span class="lbl">Semantic Chunks</span></div>
      <div class="stat-pill"><span class="val">Bilingual</span><span class="lbl">KN + EN Q&A</span></div>
      <div class="stat-pill"><span class="val">TTS</span><span class="lbl">Audio Output</span></div>
    </div>
  </article>

  <p class="copy-hint">hover a bullet → copy · or use "Copy All" to grab all 3 at once</p>

</div>

<script>
  let toastTimer = null;

  function showToast(msg) {
    const toast = document.getElementById('toast');
    document.getElementById('toast-msg').textContent = msg;
    toast.classList.add('show');
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove('show'), 2200);
  }

  function copyBullet(btn) {
    const li = btn.closest('li');
    const text = '• ' + li.querySelector('.bullet-text').innerText.trim();
    navigator.clipboard.writeText(text).then(() => {
      const orig = btn.innerHTML;
      btn.classList.add('copied');
      btn.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>done`;
      showToast('Bullet copied to clipboard');
      setTimeout(() => { btn.classList.remove('copied'); btn.innerHTML = orig; }, 2000);
    }).catch(() => fallback(text));
  }

  function copyAll(btn, id) {
    const items = document.getElementById(id).querySelectorAll('.bullet-text');
    const text = Array.from(items).map(el => '• ' + el.innerText.trim()).join('\n\n');
    navigator.clipboard.writeText(text).then(() => {
      const orig = btn.innerHTML;
      btn.innerHTML = `<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>Copied!`;
      btn.style.cssText += 'color:#6EE7B7;border-color:rgba(16,185,129,0.4)';
      showToast('All 3 bullets copied to clipboard');
      setTimeout(() => { btn.innerHTML = orig; btn.style.color=''; btn.style.borderColor=''; }, 2200);
    }).catch(() => fallback(text));
  }

  function fallback(text) {
    const ta = Object.assign(document.createElement('textarea'),
      { value: text, style: 'position:fixed;opacity:0' });
    document.body.appendChild(ta);
    ta.select(); document.execCommand('copy');
    document.body.removeChild(ta);
    showToast('Copied!');
  }
</script>
</body>
</html>

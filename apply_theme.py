import re

new_style = """<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

  :root{
    /* ==========================================================================
       THEME: Premium White & Royal Sapphire Blue
       Primary Accent: The Definitive Electric Sapphire (#1d6bf3 / #2563eb)
       ========================================================================== */
    --blue-primary: #1d6bf3;
    --blue-hover: #1557cf;
    --blue-dark: #0f3d99;
    --blue-deep: #0a2558;
    --blue-electric: #2563eb;
    --blue-glow: rgba(29, 107, 243, 0.35);
    
    /* Secondary & Highlight Blues */
    --blue-sky: #38bdf8;
    --blue-cyan: #06b6d4;
    --blue-light: #60a5fa;
    --blue-soft: #93c5fd;
    --blue-ice: #dbeafe;
    --blue-ice-soft: #eff6ff;
    --blue-subtle: #f0f7ff;
    
    /* Backgrounds: Pure Crisp Whites & Frosted Alabaster */
    --bg-white: #ffffff;
    --bg-light: #f8faff;
    --bg-surface: #ffffff;
    --bg-subtle: #f0f5ff;
    --bg-card: #ffffff;
    
    /* Deep Oceanic / Midnight Navies (For Project, Terminal & Contact Sections) */
    --navy-darkest: #030712;
    --navy-950: #060e1e;
    --navy-900: #0a1932;
    --navy-850: #0d2246;
    --navy-800: #102d5e;
    
    /* Typography Colors */
    --text-navy: #091325;
    --text-primary: #0f172a;
    --text-secondary: #334155;
    --text-muted: #64748b;
    --text-light-muted: #94a3b8;
    --text-white: #ffffff;
    
    /* Borders & Subtle Lines */
    --border-subtle: rgba(29, 107, 243, 0.1);
    --border-blue: rgba(29, 107, 243, 0.2);
    --border-hover: rgba(29, 107, 243, 0.45);
    --line: rgba(255, 255, 255, 0.12);
    --line-dark: rgba(15, 23, 42, 0.08);
  }

  *{margin:0;padding:0;box-sizing:border-box;}
  html{scroll-behavior:smooth;}
  section, header, [id]{scroll-margin-top: 90px;}
  body{
    font-family:'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background:var(--bg-white);
    color:var(--text-primary);
    -webkit-font-smoothing:antialiased;
    -moz-osx-font-smoothing:grayscale;
    overflow-x:hidden;
  }
  
  /* Modern Custom Scrollbar */
  ::-webkit-scrollbar {
    width: 10px;
  }
  ::-webkit-scrollbar-track {
    background: #f1f5f9;
  }
  ::-webkit-scrollbar-thumb {
    background: #93c5fd;
    border-radius: 999px;
    border: 2px solid #f1f5f9;
  }
  ::-webkit-scrollbar-thumb:hover {
    background: var(--blue-primary);
  }

  ::selection{background:var(--blue-primary); color:#ffffff;}

  @media (prefers-reduced-motion: reduce){
    *{animation-duration:0.01ms !important; animation-iteration-count:1 !important; transition-duration:0.01ms !important; scroll-behavior:auto !important;}
  }
  a{color:inherit;text-decoration:none;}
  img{display:block;max-width:100%;}

  /* ---------- TOP BAR ---------- */
  .topbar{
    position:fixed; top:0; left:0; right:0; z-index:50;
    display:flex; justify-content:space-between; align-items:center;
    padding:18px 5vw;
    font-size:13.5px; letter-spacing:.015em;
    color:var(--text-primary);
    background:rgba(255, 255, 255, 0.88);
    backdrop-filter:blur(16px);
    -webkit-backdrop-filter:blur(16px);
    border-bottom:1px solid rgba(29, 107, 243, 0.08);
    box-shadow:0 4px 20px rgba(15, 23, 42, 0.03);
    transition:all .3s ease;
  }
  .topbar .brand{
    font-weight:700;
    color:var(--text-navy);
    display:flex;
    align-items:center;
    gap:8px;
    letter-spacing:-0.01em;
  }
  .topbar .brand::before{
    content:"";
    display:inline-block;
    width:8px; height:8px;
    border-radius:50%;
    background:var(--blue-primary);
    box-shadow:0 0 10px var(--blue-glow);
  }
  .topbar .tag{
    color:var(--text-muted);
    text-align:right;
    font-size:12.5px;
    line-height:1.45;
  }

  /* ---------- HERO ---------- */
  .hero{
    position:relative;
    min-height:100vh;
    background:
      radial-gradient(75% 60% at 50% 0%, rgba(29, 107, 243, 0.13) 0%, rgba(56, 189, 248, 0.07) 35%, rgba(240, 247, 255, 0.5) 65%, #ffffff 100%),
      linear-gradient(180deg, #ffffff 0%, #f6faff 100%);
    color:var(--text-primary);
    display:flex;
    flex-direction:column;
    padding:120px 5vw 0;
    overflow:hidden;
  }
  /* Subtle blueprint/tech grid */
  .hero::before{
    content:"";
    position:absolute;
    inset:0;
    background-image:
      linear-gradient(to right, rgba(29, 107, 243, 0.04) 1px, transparent 1px),
      linear-gradient(to bottom, rgba(29, 107, 243, 0.04) 1px, transparent 1px);
    background-size:44px 44px;
    mask-image:radial-gradient(ellipse 75% 55% at 50% 30%, #000 50%, transparent 100%);
    -webkit-mask-image:radial-gradient(ellipse 75% 55% at 50% 30%, #000 50%, transparent 100%);
    pointer-events:none;
    z-index:0;
  }
  .hero-top-row{
    display:flex; justify-content:space-between; align-items:flex-start; gap:24px; margin-bottom:10px;
    position:relative; z-index:2;
  }
  .hero-desc{
    max-width:360px; font-size:15px; line-height:1.65; color:var(--text-secondary);
    font-weight:450;
  }
  .icon-row{display:flex; gap:10px; margin-top:18px;}
  .icon-pill{
    width:36px;height:36px;border-radius:50%;
    background:rgba(255,255,255,0.92);
    border:1px solid rgba(29, 107, 243, 0.16);
    display:flex;align-items:center;justify-content:center;
    color:var(--blue-primary);
    box-shadow:0 4px 12px rgba(29, 107, 243, 0.08);
    transition:transform .25s cubic-bezier(.16,1,.3,1), background .25s ease, border-color .25s ease, box-shadow .25s ease;
  }
  .icon-pill:hover{
    transform:translateY(-3px);
    background:var(--blue-primary);
    border-color:var(--blue-primary);
    box-shadow:0 8px 20px rgba(29, 107, 243, 0.35);
  }
  .icon-pill:hover svg path{
    fill: #ffffff !important;
  }
  .icon-pill svg{display:block;}
  
  .hero-inner{
    flex:1;
    position:relative;
    display:flex;
    align-items:flex-end;
    justify-content:center;
    min-height:0;
  }
  .hero-photo-wrap{
    width:min(520px, 62vw);
    align-self:flex-end;
    position:relative;
    z-index:1;
    opacity:0.88;
    filter:drop-shadow(0 20px 45px rgba(29, 107, 243, 0.12));
  }
  .hero-photo-wrap img{
    width:100%; height:auto; display:block;
    filter:contrast(1.04) brightness(1.02);
    mask-image:linear-gradient(to bottom, black 75%, transparent 100%);
    -webkit-mask-image:linear-gradient(to bottom, black 75%, transparent 100%);
  }
  .hero-title{
    position:absolute;
    left:0; right:0; bottom:8px;
    text-align:center;
    font-size:clamp(48px, 9.5vw, 148px);
    line-height:0.9;
    font-weight:800;
    letter-spacing:-0.035em;
    color:var(--navy-darkest);
    z-index:2;
    pointer-events:none;
    text-shadow:0 12px 35px rgba(29, 107, 243, 0.12);
  }
  .hero-title .thin{
    font-weight:400;
    color:var(--blue-primary);
  }

  /* ---------- SECTION SHELL ---------- */
  section{padding:120px 5vw;}
  .eyebrow{
    text-transform:uppercase; font-size:12px; letter-spacing:.14em; font-weight:700;
    color:var(--blue-primary); margin-bottom:18px;
    display:inline-flex; align-items:center; gap:8px;
  }
  .eyebrow::before{
    content:""; width:6px; height:6px; border-radius:50%; background:var(--blue-primary);
  }
  .section-head{
    display:grid; grid-template-columns:1.2fr 0.8fr; gap:40px; align-items:end; margin-bottom:64px;
  }
  .section-title{
    font-size:clamp(30px,4vw,48px); font-weight:800; letter-spacing:-0.025em; line-height:1.08;
    color:var(--text-navy);
  }
  .section-sub{
    font-size:15px; line-height:1.75; color:var(--text-muted); max-width:380px;
  }

  /* ---------- ABOUT STRIP ---------- */
  .about{
    background:var(--bg-white);
    padding-top:85px; padding-bottom:85px;
    border-bottom:1px solid var(--border-subtle);
  }
  .about-grid{display:grid; grid-template-columns:1fr 1fr; gap:60px;}
  .about-grid p{font-size:16px; line-height:1.8; color:var(--text-secondary);}
  .about-grid .cta-link{
    display:inline-flex; align-items:center; gap:8px; margin-top:24px;
    font-size:14px; font-weight:600; color:var(--blue-primary);
    border-bottom:2px solid rgba(29, 107, 243, 0.25); padding-bottom:3px;
    transition:all .25s ease;
  }
  .about-grid .cta-link:hover{
    border-color:var(--blue-primary);
    gap:12px;
    color:var(--blue-hover);
  }

  /* ---------- WORK / PROJECT ---------- */
  .work{
    background:linear-gradient(180deg, #f8faff 0%, #f0f6ff 100%);
    position:relative;
  }
  .project-card{
    position:relative; border-radius:24px; overflow:hidden;
    background:linear-gradient(135deg, #071224 0%, #0c2044 55%, #0f2c66 100%);
    color:#fff;
    min-height:480px;
    display:flex; flex-direction:column; justify-content:space-between;
    padding:48px;
    isolation:isolate;
    border:1px solid rgba(56, 189, 248, 0.22);
    box-shadow:0 30px 70px -20px rgba(10, 25, 49, 0.35), 0 0 50px -10px rgba(37, 99, 235, 0.22);
  }
  .project-card::before{
    content:""; position:absolute; inset:0; z-index:-1;
    background-image:
      radial-gradient(circle at 18% 18%, rgba(56, 189, 248, 0.35), transparent 45%),
      radial-gradient(circle at 85% 80%, rgba(29, 107, 243, 0.35), transparent 50%),
      radial-gradient(circle at 50% 100%, rgba(14, 165, 233, 0.2), transparent 40%);
  }
  .project-tagline{
    font-size:12px; letter-spacing:.14em; text-transform:uppercase;
    color:var(--blue-sky); font-weight:600; margin-bottom:auto;
  }
  .project-body{max-width:580px;}
  .project-body h3{
    font-size:clamp(28px,3.5vw,42px); font-weight:800; letter-spacing:-0.02em; margin-bottom:16px;
    color:#ffffff;
  }
  .project-body p{
    font-size:15px; line-height:1.75; color:rgba(238, 244, 255, 0.88); margin-bottom:26px;
  }
  .stack-row{display:flex; flex-wrap:wrap; gap:8px; margin-bottom:28px;}
  .stack-chip{
    font-size:12px; padding:7px 14px; border-radius:999px;
    background:rgba(255,255,255,0.12); border:1px solid rgba(255,255,255,0.22);
    backdrop-filter:blur(8px);
    display:inline-flex; align-items:center; gap:7px;
    color:#ffffff; font-weight:500;
    transition:all .25s ease;
  }
  .stack-chip:hover{
    background:rgba(255,255,255,0.22);
    transform:translateY(-2px);
    border-color:rgba(56, 189, 248, 0.5);
  }
  .stack-chip img, .stack-chip svg{width:14px; height:14px;}
  .project-links{display:flex; gap:14px;}
  .project-links a{
    font-size:13.5px; font-weight:600; padding:12px 24px; border-radius:999px;
    background:var(--blue-primary); color:#ffffff;
    box-shadow:0 8px 24px rgba(29, 107, 243, 0.4);
    transition:all .25s ease;
  }
  .project-links a:hover{
    background:var(--blue-hover);
    transform:translateY(-2px);
    box-shadow:0 12px 30px rgba(29, 107, 243, 0.55);
  }
  .project-links a.secondary{
    background:rgba(255,255,255,0.1); color:#ffffff;
    border:1px solid rgba(255,255,255,0.3);
    box-shadow:none;
    backdrop-filter:blur(8px);
  }
  .project-links a.secondary:hover{
    background:rgba(255,255,255,0.2);
    border-color:#ffffff;
    transform:translateY(-2px);
  }

  /* ---------- TERMINAL SIGNATURE ---------- */
  .terminal-wrap{margin-top:34px;}
  .terminal-caption{
    font-size:13px; color:var(--text-muted); margin-bottom:14px;
    display:flex; align-items:center; gap:8px; font-weight:500;
  }
  .terminal-caption::before{
    content:""; width:6px; height:6px; border-radius:50%;
    background:var(--blue-primary); flex-shrink:0;
  }
  .terminal-card{
    background:#071224;
    border-radius:18px;
    overflow:hidden;
    border:1px solid rgba(59, 130, 246, 0.22);
    box-shadow:0 35px 80px -25px rgba(10, 25, 49, 0.35), 0 0 40px -10px rgba(37, 99, 235, 0.18);
  }
  .terminal-bar{
    display:flex; align-items:center; gap:8px;
    padding:14px 18px;
    background:#0b1933;
    border-bottom:1px solid rgba(59, 130, 246, 0.15);
  }
  .tdot{width:12px;height:12px;border-radius:50%; flex-shrink:0;}
  .terminal-title{
    margin-left:10px; font-size:12.5px; color:rgba(186, 215, 255, 0.6);
    font-family:'JetBrains Mono', 'SF Mono', Consolas, Menlo, monospace;
  }
  .terminal-body{
    padding:26px 28px 28px;
    font-family:'JetBrains Mono', 'SF Mono', Consolas, Menlo, monospace;
    font-size:14px; line-height:1.75;
  }
  .terminal-line{color:#e2e8f0;}
  .prompt{color:var(--blue-sky); margin-right:10px; font-weight:700;}
  .cmd{color:#f8fafc; font-weight:500;}
  .term-cursor{
    display:inline-block; color:var(--blue-sky); margin-left:3px;
    animation:blink 1s step-end infinite;
  }
  @keyframes blink{ 50%{ opacity:0; } }
  .resp{
    margin:16px 0 0; white-space:pre-wrap; word-break:break-word;
    color:rgba(238, 244, 255, 0.9);
  }
  .resp .k{color:var(--blue-sky); font-weight:600;}
  .resp .s{color:#93c5fd;}
  .resp .n{color:#fde047;}
  .resp .p{color:rgba(255,255,255,0.35);}
  .status-line{
    display:flex; align-items:center; gap:8px; margin-top:18px;
    font-size:12.5px; color:rgba(186, 215, 255, 0.65);
    opacity:0; transition:opacity .5s ease;
  }
  .status-line.visible{opacity:1;}
  .live-dot{
    width:8px; height:8px; border-radius:50%; background:#38bdf8;
    box-shadow:0 0 0 0 rgba(56, 189, 248, 0.6);
    animation:pulseDot 1.8s ease-out infinite;
  }
  @keyframes pulseDot{
    0%{box-shadow:0 0 0 0 rgba(56, 189, 248, 0.6);}
    70%{box-shadow:0 0 0 10px rgba(56, 189, 248, 0);}
    100%{box-shadow:0 0 0 0 rgba(56, 189, 248, 0);}
  }
  @media (prefers-reduced-motion: reduce){
    .term-cursor{animation:none;}
    .live-dot{animation:none;}
  }

  /* ---------- SKILLS (CRISP WHITE & BLUE) ---------- */
  .skills{
    background:var(--bg-white);
    color:var(--text-primary);
    position:relative;
  }
  .skills::before{
    content:""; position:absolute; inset:0;
    background:radial-gradient(ellipse 60% 40% at 50% 0%, rgba(29, 107, 243, 0.05) 0%, transparent 80%);
    pointer-events:none;
  }
  .skills .eyebrow{color:var(--blue-primary);}
  .skills .section-title{color:var(--text-navy);}
  .skills .section-sub{color:var(--text-muted);}

  .skills-grid{
    display:grid; grid-template-columns:repeat(3,1fr); gap:22px;
    background:transparent;
    border:none;
  }
  .skill-card{
    background:var(--bg-card);
    border:1px solid rgba(29, 107, 243, 0.12);
    border-radius:20px;
    padding:32px 28px;
    min-height:190px;
    display:flex; flex-direction:column; gap:12px;
    box-shadow:0 10px 30px -10px rgba(29, 107, 243, 0.07), 0 2px 6px rgba(15, 23, 42, 0.03);
    transition:all .35s cubic-bezier(.16,1,.3,1);
    position:relative;
    overflow:hidden;
  }
  .skill-card::after{
    content:""; position:absolute; top:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg, var(--blue-primary), var(--blue-sky));
    opacity:0;
    transition:opacity .3s ease;
  }
  .skill-card:hover{
    transform:translateY(-6px);
    background:#ffffff;
    border-color:rgba(29, 107, 243, 0.35);
    box-shadow:0 22px 45px -12px rgba(29, 107, 243, 0.18), 0 4px 12px rgba(29, 107, 243, 0.08);
  }
  .skill-card:hover::after{
    opacity:1;
  }
  .skill-card .num{
    font-size:12px; font-weight:700; color:var(--blue-primary);
    letter-spacing:.1em;
    background:var(--blue-ice-soft);
    padding:4px 10px; border-radius:999px;
    display:inline-block; width:fit-content;
  }
  .skill-card h4{
    font-size:18px; font-weight:700; letter-spacing:-0.015em; color:var(--text-navy);
  }
  .skill-card p{
    font-size:13.5px; line-height:1.65; color:var(--text-secondary);
  }
  .skill-card .logo-row{
    display:flex; gap:12px; margin-top:auto; padding-top:16px;
    border-top:1px solid rgba(29, 107, 243, 0.08);
  }
  .skill-card .logo-row img, .skill-card .logo-row svg{
    width:22px; height:22px; opacity:.95;
    color:var(--blue-primary) !important;
    transition:transform .25s ease, opacity .25s ease;
  }
  .skill-card:hover .logo-row img, .skill-card:hover .logo-row svg{opacity:1;}
  .skill-card .logo-row img:hover, .skill-card .logo-row svg:hover{transform:translateY(-3px) scale(1.12);}
  @media (max-width:820px){ .skills-grid{grid-template-columns:1fr 1fr;} }
  @media (max-width:560px){ .skills-grid{grid-template-columns:1fr;} }

  /* ---------- CS CONCEPTS STRIP ---------- */
  .strip{
    margin-top:36px;
    display:grid; grid-template-columns:1fr 1fr; gap:22px;
    background:transparent; border:none;
  }
  .strip-card{
    background:#ffffff;
    border:1px solid rgba(29, 107, 243, 0.12);
    border-radius:20px;
    padding:32px 28px;
    box-shadow:0 10px 30px -10px rgba(29, 107, 243, 0.07);
    transition:all .35s ease;
    position:relative;
    overflow:hidden;
  }
  .strip-card::before{
    content:""; position:absolute; top:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg, var(--blue-primary), var(--blue-sky));
  }
  .strip-card:hover{
    transform:translateY(-4px);
    box-shadow:0 20px 40px -12px rgba(29, 107, 243, 0.16);
    border-color:rgba(29, 107, 243, 0.3);
  }
  .strip-card h4{font-size:17px; font-weight:700; color:var(--text-navy); margin-bottom:10px;}
  .strip-card p{font-size:13.5px; line-height:1.65; color:var(--text-secondary); margin-bottom:18px;}
  .tag-row{display:flex; flex-wrap:wrap; gap:8px;}
  .tag-row span{
    font-size:11.5px; font-weight:600; padding:6px 13px; border-radius:999px;
    background:var(--blue-ice-soft); color:var(--blue-dark);
    border:1px solid rgba(29, 107, 243, 0.15);
    transition:all .2s ease;
  }
  .tag-row span:hover{
    background:var(--blue-primary); color:#ffffff; border-color:var(--blue-primary);
  }
  @media (max-width:820px){ .strip{grid-template-columns:1fr;} }

  /* ---------- CONTACT & FOOTER ---------- */
  .contact{
    background:linear-gradient(135deg, #050b17 0%, #091730 45%, #0d2757 100%);
    color:#ffffff; padding-top:85px; padding-bottom:0;
    position:relative;
    border-top:1px solid rgba(56, 189, 248, 0.2);
  }
  .contact::before{
    content:""; position:absolute; inset:0;
    background:radial-gradient(circle at 80% 20%, rgba(29, 107, 243, 0.28), transparent 45%),
               radial-gradient(circle at 20% 80%, rgba(56, 189, 248, 0.18), transparent 40%);
    pointer-events:none;
  }
  .contact-top{
    font-size:13px; color:var(--blue-sky); font-weight:600; letter-spacing:.08em;
    text-transform:uppercase; margin-bottom:10px;
  }
  .contact-headline{
    font-size:clamp(32px,5vw,58px); font-weight:800; letter-spacing:-0.025em; margin-bottom:56px;
    color:#ffffff;
  }
  .contact-row{
    display:flex; justify-content:space-between; align-items:center; gap:24px;
    border-top:1px solid rgba(255,255,255,0.12); padding-top:36px; padding-bottom:56px;
    flex-wrap:wrap;
  }
  .contact-details{display:flex; gap:48px; flex-wrap:wrap;}
  .contact-details div span{
    display:block; font-size:11px; color:var(--blue-sky); margin-bottom:6px;
    text-transform:uppercase; letter-spacing:.12em; font-weight:600;
  }
  .contact-details div a, .contact-details div p{
    font-size:15px; font-weight:600; color:#ffffff;
    transition:color .2s ease;
  }
  .contact-details div a:hover{color:var(--blue-sky);}
  .get-in-touch{
    width:130px;height:130px;border-radius:50%;
    background:linear-gradient(135deg, var(--blue-primary) 0%, #1557cf 100%);
    display:flex;align-items:center;justify-content:center;
    text-align:center; font-size:14px; font-weight:700;
    flex-shrink:0;
    transition:transform .35s ease, box-shadow .35s ease;
    cursor:pointer;
    border:none; color:#fff; font-family:inherit;
    box-shadow:0 10px 35px rgba(29, 107, 243, 0.45);
  }
  .get-in-touch:hover{
    transform:scale(1.08);
    box-shadow:0 15px 45px rgba(29, 107, 243, 0.65);
  }
  .get-in-touch:focus-visible{outline:2px solid var(--blue-sky); outline-offset:4px;}
  .social-row{
    display:flex; gap:14px; flex-wrap:wrap;
    padding-bottom:48px;
  }
  .social-row a{
    display:flex; align-items:center; gap:10px;
    padding:11px 20px; border-radius:999px;
    border:1px solid rgba(255,255,255,0.15);
    background:rgba(255,255,255,0.06);
    backdrop-filter:blur(8px);
    font-size:13.5px; font-weight:500; color:rgba(255,255,255,0.9);
    transition:all .25s ease;
  }
  .social-row a:hover{
    transform:translateY(-3px);
    background:rgba(29, 107, 243, 0.25);
    border-color:var(--blue-primary);
    color:#ffffff;
    box-shadow:0 8px 20px rgba(29, 107, 243, 0.3);
  }

  .footer-banner{
    background:#030712; color:#fff;
    padding:30px 5vw 36px;
    position:relative;
    border-top:1px solid rgba(56, 189, 248, 0.15);
  }
  .footer-row-top{display:flex; justify-content:space-between; align-items:center; margin-bottom:8px;}
  .footer-label{font-size:14px; color:rgba(186, 215, 255, 0.6); font-weight:500;}
  .footer-arrow{
    width:38px;height:38px;border-radius:50%;background:var(--blue-primary);color:#fff;
    display:flex;align-items:center;justify-content:center; font-size:15px;
    transition:transform .3s ease, background .3s ease;
  }
  .footer-banner:hover .footer-arrow{
    transform:rotate(45deg);
    background:var(--blue-sky);
  }
  .footer-name{
    font-size:clamp(52px,13vw,150px); font-weight:900; letter-spacing:-0.03em; line-height:1;
    word-break:break-word;
    background:linear-gradient(180deg, #ffffff 40%, rgba(147, 197, 253, 0.4) 100%);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
  }

  /* ---------- ANIMATIONS ---------- */
  @keyframes fadeUp{
    from{opacity:0; transform:translateY(24px);}
    to{opacity:1; transform:translateY(0);}
  }
  @keyframes fadeIn{
    from{opacity:0;}
    to{opacity:1;}
  }
  @keyframes fadeInPhoto{
    from{opacity:0;}
    to{opacity:0.88;}
  }
  .hero-top-row{animation:fadeUp .8s cubic-bezier(.16,1,.3,1) .1s both;}
  .hero-title{animation:fadeUp 1s cubic-bezier(.16,1,.3,1) .25s both;}
  .hero-photo-wrap{animation:fadeInPhoto 1.2s ease .4s both;}

  .reveal{
    opacity:0; transform:translateY(28px);
    transition:opacity .8s cubic-bezier(.16,1,.3,1), transform .8s cubic-bezier(.16,1,.3,1);
  }
  .reveal.visible{opacity:1; transform:translateY(0);}
  .reveal-stagger.visible .stagger-item{
    animation:fadeUp .7s cubic-bezier(.16,1,.3,1) both;
  }
  .stagger-item:nth-child(1){animation-delay:.05s;}
  .stagger-item:nth-child(2){animation-delay:.12s;}
  .stagger-item:nth-child(3){animation-delay:.19s;}
  .stagger-item:nth-child(4){animation-delay:.26s;}
  .stagger-item:nth-child(5){animation-delay:.33s;}
  .stagger-item:nth-child(6){animation-delay:.40s;}
</style>"""

def main():
    with open(r'c:\Users\LENOVO\OneDrive\Desktop\My-portfolio\index.html', 'r', encoding='utf-8', errors='ignore') as f:
        html = f.read()

    # Replace <style>...</style>
    style_pattern = re.compile(r'<style>.*?</style>', re.DOTALL)
    html = style_pattern.sub(new_style, html, count=1)

    # In skills section, replace style="color:#ffffff" on svg with style="color:#1d6bf3"
    skills_start = html.find('<section class="skills"')
    contact_start = html.find('<section class="contact"')
    if skills_start != -1 and contact_start != -1:
        skills_chunk = html[skills_start:contact_start]
        skills_chunk_updated = skills_chunk.replace('style="color:#ffffff"', 'style="color:#1d6bf3"')
        html = html[:skills_start] + skills_chunk_updated + html[contact_start:]

    # Fix character encodings for entities
    html = html.replace('© Code by Kunal', '&copy; Code by Kunal')
    html = html.replace('Ac Code by Kunal', '&copy; Code by Kunal')
    html = html.replace('More about me →', 'More about me &rarr;')
    html = html.replace('Kunal — Backend Developer', 'Kunal &mdash; Backend Developer')

    with open(r'c:\Users\LENOVO\OneDrive\Desktop\My-portfolio\index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    # Also update C:\Users\LENOVO\Downloads\index_2.html so user gets it immediately in their active editor
    try:
        with open(r'C:\Users\LENOVO\Downloads\index_2.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print(r"Updated C:\Users\LENOVO\Downloads\index_2.html")
    except Exception as e:
        print("Downloads update note:", e)

    # Also update C:\Users\LENOVO\Downloads\PortFolio\index.html if exists
    try:
        with open(r'C:\Users\LENOVO\Downloads\PortFolio\index.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print(r"Updated C:\Users\LENOVO\Downloads\PortFolio\index.html")
    except Exception as e:
        print("PortFolio update note:", e)

    print("Theme applied successfully to workspace index.html!")

if __name__ == '__main__':
    main()

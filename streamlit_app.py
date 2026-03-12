import streamlit as st
import time

st.set_page_config(
    page_title="Recursie Uitgelegd",
    page_icon="🔁",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] { font-family: 'Syne', sans-serif; }
.stApp { background: #0d0d0d; color: #f0ede6; }
h1, h2, h3 { font-family: 'Syne', sans-serif !important; font-weight: 800 !important; color: #f0ede6 !important; }

.hero-title { font-family: 'Syne', sans-serif; font-size: 4rem; font-weight: 800; line-height: 1.0; color: #f0ede6; letter-spacing: -2px; }
.hero-accent { color: #ff5e1a; }
.section-label { font-family: 'Space Mono', monospace; font-size: 0.72rem; letter-spacing: 0.2em; text-transform: uppercase; color: #ff5e1a; margin-bottom: 0.5rem; }

.concept-card { background: #1a1a1a; border: 1px solid #2a2a2a; border-left: 3px solid #ff5e1a; border-radius: 4px; padding: 1.4rem 1.6rem; margin-bottom: 1rem; }
.call-frame { font-family: 'Space Mono', monospace; font-size: 0.85rem; padding: 0.6rem 1rem; border-radius: 3px; margin: 4px 0; }
.frame-active { background: #ff5e1a22; border-left: 3px solid #ff5e1a; color: #ff8c55; }
.frame-waiting { background: #1e1e1e; border-left: 3px solid #444; color: #777; }
.frame-done { background: #1a2e1a; border-left: 3px solid #4caf50; color: #6fcf6f; }

.stButton>button { background: #ff5e1a !important; color: #0d0d0d !important; border: none !important; font-family: 'Syne', sans-serif !important; font-weight: 700 !important; font-size: 0.9rem !important; padding: 0.55rem 1.4rem !important; border-radius: 3px !important; }
.stButton>button:hover { background: #ff7a3d !important; }
div[data-baseweb="tab-list"] { background: #161616 !important; border-bottom: 1px solid #222; }
div[data-baseweb="tab"] { color: #888 !important; font-family: 'Space Mono', monospace !important; font-size: 0.78rem !important; }
div[aria-selected="true"][data-baseweb="tab"] { color: #ff5e1a !important; border-bottom: 2px solid #ff5e1a !important; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div style="padding:2.5rem 0 1.5rem 0">
  <div class="section-label">Informatica · Algoritmen · Python</div>
  <div class="hero-title">Re<span class="hero-accent">cursie</span><br>Uitgelegd</div>
  <p style="color:#888;font-size:1.05rem;margin-top:1rem;max-width:560px;line-height:1.6">
    Een functie die <em>zichzelf aanroept</em>. Klinkt gek?
    Na deze interactieve les snap je het volledig.
  </p>
</div>
<hr style="border:none;border-top:1px solid #222;margin:1rem 0 2rem 0">
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4 = st.tabs([
    "📖  Wat is recursie?",
    "🔢  Faculteit stap voor stap",
    "🌳  Fibonacci boom",
    "⚠️  Valkuilen & tips",
])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — Uitleg
# ══════════════════════════════════════════════════════════════════════════════
with tab1:
    col_a, col_b = st.columns([1, 1], gap="large")

    with col_a:
        st.markdown("### Wat is recursie?")
        st.markdown("""
<div class="concept-card">
  <div class="section-label">Definitie</div>
  <p style="color:#f0ede6;margin:0;line-height:1.7">
    <strong>Recursie</strong> is een techniek waarbij een functie
    <span style="color:#ff5e1a"><strong>zichzelf aanroept</strong></span>
    om een probleem op te lossen door het steeds kleiner te maken,
    totdat een basisgeval wordt bereikt.
  </p>
</div>
""", unsafe_allow_html=True)

        st.markdown("**De twee vereisten van elke recursieve functie:**")
        st.markdown("""
<div class="concept-card" style="border-left-color:#4caf50">
  <div class="section-label" style="color:#4caf50">1 · Basisgeval (Base Case)</div>
  <p style="color:#ccc;margin:0;line-height:1.6">
    De stopconditie. Zonder dit gaat de functie <em>eindeloos</em> door
    en krijg je een <code>RecursionError</code>.
  </p>
</div>
<div class="concept-card" style="border-left-color:#2196f3">
  <div class="section-label" style="color:#2196f3">2 · Recursief geval</div>
  <p style="color:#ccc;margin:0;line-height:1.6">
    De functie roept zichzelf aan met een <em>kleinere</em> of
    <em>eenvoudigere</em> versie van het probleem.
  </p>
</div>
""", unsafe_allow_html=True)

    with col_b:
        st.markdown("### Simpelste voorbeeld: aftellen")
        st.code("""def aftellen(n):
    # Basisgeval: stop bij 0
    if n == 0:
        print("Starten!")
        return

    print(f"  {n}...")

    # Recursief geval: roep jezelf aan
    aftellen(n - 1)


aftellen(5)""", language="python")

        st.markdown("**Uitvoer:**")
        st.markdown("""
<div style="font-family:'Space Mono',monospace;font-size:0.82rem;
     background:#111;border:1px solid #222;border-radius:4px;
     padding:1rem 1.2rem;color:#f0ede6;line-height:1.8">
  5...<br>  4...<br>  3...<br>  2...<br>  1...<br>Starten!
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### Recursie vs. Iteratie")

    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("**Recursief**")
        st.code("""def som_recursief(n):
    if n == 0:       # basisgeval
        return 0
    return n + som_recursief(n - 1)

print(som_recursief(5))  # 15""", language="python")

    with col2:
        st.markdown("**Iteratief**")
        st.code("""def som_iteratief(n):
    totaal = 0
    for i in range(n + 1):
        totaal += i
    return totaal

print(som_iteratief(5))  # 15""", language="python")

    st.info("💡 Beide geven hetzelfde resultaat. Recursie is vaak **eleganter** maar gebruikt meer geheugen.")


# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — Faculteit stap voor stap
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("### Faculteit: `n! = n × (n-1) × … × 1`")

    st.code("""def faculteit(n):
    if n == 0 or n == 1:   # basisgeval
        return 1
    return n * faculteit(n - 1)  # recursief geval""", language="python")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Kies een getal en zie de aanroepen live:**")

    n = st.slider("Waarde van n", min_value=1, max_value=8, value=4)

    if st.button("Animeer de aanroepen"):
        calls = list(range(n, 0, -1))
        placeholder = st.empty()

        # Phase 1: going down
        for i, k in enumerate(calls):
            frames_html = ""
            for j, c in enumerate(calls):
                indent = j * 20
                if j < i:
                    frames_html += f'<div class="call-frame frame-waiting" style="margin-left:{indent}px">faculteit({c}) — wacht op resultaat...</div>'
                elif j == i:
                    frames_html += f'<div class="call-frame frame-active" style="margin-left:{indent}px">▶ faculteit({c}) — huidige aanroep</div>'
                    if c == 1:
                        frames_html += f'<div class="call-frame frame-done" style="margin-left:{indent+20}px">✓ basisgeval bereikt! geeft 1 terug</div>'

            with placeholder.container():
                st.markdown("**Fase 1 — Afdalen (aanroepen stapelen)**")
                st.markdown(frames_html, unsafe_allow_html=True)
            time.sleep(0.55)

        # Phase 2: unwinding
        results = {}
        for k in range(1, n + 1):
            results[k] = 1 if k <= 1 else k * results[k - 1]

        for i, k in enumerate(range(1, n + 1)):
            frames_html = ""
            for j, c in enumerate(calls):
                indent = j * 20
                val = results.get(c, "?")
                if c < k:
                    frames_html += f'<div class="call-frame frame-done" style="margin-left:{indent}px">✓ faculteit({c}) = {val}</div>'
                elif c == k:
                    frames_html += f'<div class="call-frame frame-active" style="margin-left:{indent}px">▶ faculteit({c}) = {val} — lost op!</div>'
                else:
                    frames_html += f'<div class="call-frame frame-waiting" style="margin-left:{indent}px">faculteit({c}) — wacht...</div>'

            with placeholder.container():
                st.markdown("**Fase 2 — Opstijgen (resultaten terugkoppelen)**")
                st.markdown(frames_html, unsafe_allow_html=True)
            time.sleep(0.55)

        with placeholder.container():
            st.markdown("**Klaar!**")
            st.markdown(frames_html, unsafe_allow_html=True)

        import math
        result = math.factorial(n)
        st.success(f"🎉 faculteit({n}) = {result}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Wiskundige uitwerking:**")
    steps = " × ".join(str(i) for i in range(n, 0, -1))
    import math
    result = math.factorial(n)
    st.markdown(f"""
<div style="font-family:'Space Mono',monospace;font-size:1rem;
     background:#111;border:1px solid #222;border-radius:4px;
     padding:1.2rem 1.4rem;color:#f0ede6;text-align:center">
  {n}!  =  {steps}  =  <span style="color:#ff5e1a;font-size:1.3rem"><strong>{result}</strong></span>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — Fibonacci boom
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("### Fibonacci: overlappende deelproblemen")

    col_l, col_r = st.columns([1, 1], gap="large")

    with col_l:
        st.code("""def fibonacci(n):
    # Basisgevallen
    if n == 0:
        return 0
    if n == 1:
        return 1

    # Recursief geval: twee aanroepen!
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(6))  # 8""", language="python")

        st.markdown("""
<div class="concept-card" style="border-left-color:#9c27b0;margin-top:1rem">
  <div class="section-label" style="color:#9c27b0">Let op: dubbele recursie</div>
  <p style="color:#ccc;margin:0;line-height:1.6">
    Fibonacci roept zichzelf <strong>twee keer</strong> aan.
    Dit leidt tot een <em>boomstructuur</em> van aanroepen.
  </p>
</div>
""", unsafe_allow_html=True)

    with col_r:
        fib_n = st.selectbox("Bereken fibonacci(n):", [3, 4, 5, 6], index=1)

        call_log = []

        def fib_trace(n, depth=0):
            indent = "    " * depth
            branch = "└── " if depth > 0 else ""
            if n <= 1:
                call_log.append(f"{indent}{branch}fib({n}) = {n}  ← basis")
                return n
            call_log.append(f"{indent}{branch}fib({n})")
            left = fib_trace(n - 1, depth + 1)
            right = fib_trace(n - 2, depth + 1)
            val = left + right
            call_log.append(f"{indent}{branch}fib({n}) = {val}  ✓")
            return val

        fib_trace(fib_n)
        tree_text = "\n".join(call_log)
        st.markdown("**Aanroepboom:**")
        st.code(tree_text, language="text")

    # Count calls
    call_counter = [0]

    def fib_count(n):
        call_counter[0] += 1
        if n <= 1:
            return n
        return fib_count(n - 1) + fib_count(n - 2)

    def fib(n):
        return n if n <= 1 else fib(n - 1) + fib(n - 2)

    fib_count(fib_n)
    total_calls = call_counter[0]
    fib_val = fib(fib_n)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
<div style="background:#161616;border:1px solid #222;border-radius:4px;padding:1.2rem;text-align:center">
  <div style="font-family:'Syne',sans-serif;font-size:2.5rem;font-weight:800;color:#ff5e1a">{fib_n}</div>
  <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#666;text-transform:uppercase;letter-spacing:0.1em;margin-top:0.3rem">Invoer n</div>
</div>""", unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
<div style="background:#161616;border:1px solid #222;border-radius:4px;padding:1.2rem;text-align:center">
  <div style="font-family:'Syne',sans-serif;font-size:2.5rem;font-weight:800;color:#4caf50">{fib_val}</div>
  <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#666;text-transform:uppercase;letter-spacing:0.1em;margin-top:0.3rem">Uitkomst</div>
</div>""", unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
<div style="background:#161616;border:1px solid #222;border-radius:4px;padding:1.2rem;text-align:center">
  <div style="font-family:'Syne',sans-serif;font-size:2.5rem;font-weight:800;color:#9c27b0">{total_calls}</div>
  <div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#666;text-transform:uppercase;letter-spacing:0.1em;margin-top:0.3rem">Totaal aanroepen</div>
</div>""", unsafe_allow_html=True)

    st.warning(f"⚠️ fibonacci({fib_n}) veroorzaakte **{total_calls} functieaanroepen**. Voor fibonacci(30) zijn dat al meer dan 1 miljoen!")

    st.markdown("**Oplossing: Memoization (resultaten onthouden)**")
    st.code("""from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_snel(n):
    if n <= 1:
        return n
    return fibonacci_snel(n - 1) + fibonacci_snel(n - 2)

# Nu slechts lineair aantal aanroepen!
print(fibonacci_snel(50))  # razendsnel""", language="python")


# ══════════════════════════════════════════════════════════════════════════════
# TAB 4 — Valkuilen & tips
# ══════════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("### Veelgemaakte fouten & hoe je ze vermijdt")

    st.markdown("#### Fout 1: Vergeten basisgeval")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("**Fout (eindeloze lus):**")
        st.code("""def aftellen(n):
    # Geen basisgeval!
    print(n)
    aftellen(n - 1)

# Geeft RecursionError""", language="python")

    with col2:
        st.markdown("**Goed (met basisgeval):**")
        st.code("""def aftellen(n):
    if n == 0:       # basisgeval
        return
    print(n)
    aftellen(n - 1)  # recursief

aftellen(5)  # werkt""", language="python")

    st.markdown("<hr style='border:none;border-top:1px solid #1e1e1e;margin:1.5rem 0'>", unsafe_allow_html=True)

    st.markdown("#### Fout 2: Probleem wordt niet kleiner")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("**Fout:**")
        st.code("""def som(n):
    if n == 0:
        return 0
    return n + som(n)  # n verandert niet!
    # RecursionError""", language="python")

    with col2:
        st.markdown("**Goed:**")
        st.code("""def som(n):
    if n == 0:
        return 0
    return n + som(n - 1)  # n - 1
    # Wordt steeds kleiner""", language="python")

    st.markdown("<hr style='border:none;border-top:1px solid #1e1e1e;margin:1.5rem 0'>", unsafe_allow_html=True)

    st.markdown("#### Python's recursielimiet")
    st.code("""import sys

# Standaard limiet in Python:
print(sys.getrecursionlimit())  # 1000

# Aanpassen (voorzichtig!):
sys.setrecursionlimit(5000)""", language="python")

    st.markdown("<hr style='border:none;border-top:1px solid #1e1e1e;margin:1.5rem 0'>", unsafe_allow_html=True)

    st.markdown("#### Wanneer gebruik je recursie?")
    col1, col2 = st.columns(2, gap="medium")
    with col1:
        st.markdown("""
<div class="concept-card" style="border-left-color:#4caf50">
  <div class="section-label" style="color:#4caf50">Goed geschikt voor:</div>
  <ul style="color:#ccc;line-height:1.9;margin:0;padding-left:1.2rem">
    <li>Boomstructuren (BST, DOM, bestanden)</li>
    <li>Divide-and-conquer algoritmen</li>
    <li>Quicksort &amp; mergesort</li>
    <li>Doolhoven &amp; graaf-doorzoeken</li>
    <li>Wiskundige definities (n!, fib)</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div class="concept-card" style="border-left-color:#f44336">
  <div class="section-label" style="color:#f44336">Minder geschikt voor:</div>
  <ul style="color:#ccc;line-height:1.9;margin:0;padding-left:1.2rem">
    <li>Eenvoudige lussen (gebruik for)</li>
    <li>Grote invoer zonder memoization</li>
    <li>Prestatiekritieke systemen</li>
    <li>Als de iteratieve versie even leesbaar is</li>
  </ul>
</div>
""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("#### Interactieve oefening")
    st.markdown("Schrijf een recursieve functie die de macht berekent: `macht(2, 10) → 1024`")

    user_code = st.text_area("Jouw oplossing:", value="""def macht(basis, exponent):
    # Tip: basisgeval is exponent == 0
    pass
""", height=120)

    if st.button("Test jouw oplossing"):
        try:
            exec_globals = {}
            exec(user_code, exec_globals)
            fn = exec_globals.get("macht")
            if fn is None:
                st.error("Geen functie 'macht' gevonden.")
            else:
                tests = [(2, 0, 1), (2, 1, 2), (2, 10, 1024), (3, 4, 81), (5, 3, 125)]
                passed = 0
                for basis, exp, expected in tests:
                    result = fn(basis, exp)
                    if result == expected:
                        st.success(f"✅  macht({basis}, {exp}) = {result}")
                        passed += 1
                    else:
                        st.error(f"❌  macht({basis}, {exp}) → verwacht {expected}, kreeg {result}")
                if passed == len(tests):
                    st.balloons()
                    st.success("🎉 Alle tests geslaagd! Je hebt recursie onder de knie!")
        except Exception as e:
            st.error(f"Fout in jouw code: {e}")

    with st.expander("Toon de oplossing"):
        st.code("""def macht(basis, exponent):
    if exponent == 0:        # basisgeval: alles tot de 0e macht = 1
        return 1
    return basis * macht(basis, exponent - 1)  # recursief


print(macht(2, 10))  # 1024""", language="python")


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<hr style="border:none;border-top:1px solid #1a1a1a;margin:3rem 0 1rem 0">
<div style="font-family:'Space Mono',monospace;font-size:0.65rem;color:#444;text-align:center;padding-bottom:1.5rem">
  Recursie Uitgelegd · gebouwd met Python &amp; Streamlit
</div>
""", unsafe_allow_html=True)

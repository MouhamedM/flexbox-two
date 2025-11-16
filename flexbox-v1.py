import streamlit as st
import streamlit.components.v1 as components

# ============================================
# PAGE CONFIGURATION
# ============================================
st.set_page_config(
    page_title="Flexbox Visual Learner",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================
# CUSTOM CSS - MINIMALIST STYLE
# ============================================
st.markdown("""
<style>
    /* Clean minimalist design */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    
    h1 {
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        font-weight: 600;
        margin-top: 2rem;
        margin-bottom: 1rem;
        color: #2c3e50;
    }
    
    h3 {
        font-weight: 500;
        color: #34495e;
    }
    
    /* Clean separator */
    hr {
        margin: 3rem 0;
        border: none;
        height: 1px;
        background: #e0e0e0;
    }
    
    /* Minimize visual clutter */
    .stSelectbox label, .stSlider label {
        font-weight: 500;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# TRANSLATIONS
# ============================================
TRANSLATIONS = {
    "English": {
        # Header
        "title": "Flexbox Visual Learner (Parents)",
        "subtitle": "Interactive, visual, no confusion",
        
        # Steps
        "step1": "Flex Direction",
        "step2": "Justify Content",
        "step3": "Align Items",
        
        # Sections
        "live_demo": "Live Demo",
        "wrap_demo": "Flex Wrap",
        "examples": "Real Examples",
        "docs": "Documentation",
        "parent_width": "Container Width",
        
        # Examples
        "hero": "Hero",
        "cards": "Cards",
        "gallery": "Gallery",
        
        # Documentation
        "doc_parent_title": "Parent Controls",
        "doc_parent_desc": "The parent element controls the layout of all children",
        "doc_child_title": "Child Properties",
        "doc_child_desc": "Children can override their own behavior",
        
        "doc_direction": "Flex Direction",
        "doc_direction_desc": "Controls the main axis flow",
        "doc_direction_row": "Horizontal left to right",
        "doc_direction_row_reverse": "Horizontal right to left",
        "doc_direction_column": "Vertical top to bottom",
        "doc_direction_column_reverse": "Vertical bottom to top",
        
        "doc_justify": "Justify Content",
        "doc_justify_desc": "Distributes items along the main axis",
        "doc_justify_start": "Items at start",
        "doc_justify_center": "Items centered",
        "doc_justify_end": "Items at end",
        "doc_justify_between": "Space between items",
        "doc_justify_around": "Space around items",
        "doc_justify_evenly": "Equal space everywhere",
        
        "doc_align": "Align Items",
        "doc_align_desc": "Aligns items along the cross axis",
        "doc_align_start": "Align to start",
        "doc_align_center": "Align to center",
        "doc_align_end": "Align to end",
        "doc_align_stretch": "Stretch to fill",
        "doc_align_baseline": "Align text baseline",
        
        "doc_wrap": "Flex Wrap",
        "doc_wrap_desc": "Controls wrapping behavior",
        "doc_wrap_nowrap": "Single line (no wrap)",
        "doc_wrap_wrap": "Wrap to new lines",
        "doc_wrap_reverse": "Wrap in reverse",
        
        "doc_child_props": "Child Properties",
        "doc_flex_grow": "Ability to grow",
        "doc_flex_shrink": "Ability to shrink",
        "doc_flex_basis": "Initial size",
        "doc_align_self": "Individual alignment",
        
        "doc_when_use": "When to Use",
        "doc_when_not": "When NOT to Use",
        "doc_reverse_use": "RTL interfaces (Arabic, Hebrew), Chat apps, Timelines, Special layouts",
        "doc_reverse_avoid": "Normal sections, Hero layouts, Product cards, Standard grids, Most responsive layouts",
    },
    
    "العربية": {
        # Header
        "title": "تعلم Flexbox بصريًا",
        "subtitle": "تفاعلي، مرئي، بدون تعقيد",
        
        # Steps
        "step1": "الاتجاه",
        "step2": "التوزيع",
        "step3": "المحاذاة",
        
        # Sections
        "live_demo": "تجربة مباشرة",
        "wrap_demo": "التفاف العناصر",
        "examples": "أمثلة حقيقية",
        "docs": "التوثيق",
        "parent_width": "عرض الحاوية",
        
        # Examples
        "hero": "الهيرو",
        "cards": "البطاقات",
        "gallery": "المعرض",
        
        # Documentation
        "doc_parent_title": "تحكم العنصر الأب",
        "doc_parent_desc": "العنصر الأب يتحكم في تخطيط جميع الأبناء",
        "doc_child_title": "خصائص الأبناء",
        "doc_child_desc": "الأبناء يمكنهم تجاوز السلوك الخاص بهم",
        
        "doc_direction": "الاتجاه",
        "doc_direction_desc": "يتحكم في اتجاه المحور الرئيسي",
        "doc_direction_row": "أفقي من اليسار لليمين",
        "doc_direction_row_reverse": "أفقي من اليمين لليسار",
        "doc_direction_column": "عمودي من الأعلى للأسفل",
        "doc_direction_column_reverse": "عمودي من الأسفل للأعلى",
        
        "doc_justify": "التوزيع",
        "doc_justify_desc": "يوزع العناصر على المحور الرئيسي",
        "doc_justify_start": "العناصر في البداية",
        "doc_justify_center": "العناصر في الوسط",
        "doc_justify_end": "العناصر في النهاية",
        "doc_justify_between": "مسافة بين العناصر",
        "doc_justify_around": "مسافة حول العناصر",
        "doc_justify_evenly": "مسافة متساوية في كل مكان",
        
        "doc_align": "المحاذاة",
        "doc_align_desc": "يحاذي العناصر على المحور العرضي",
        "doc_align_start": "محاذاة للبداية",
        "doc_align_center": "محاذاة للوسط",
        "doc_align_end": "محاذاة للنهاية",
        "doc_align_stretch": "تمديد لملء المساحة",
        "doc_align_baseline": "محاذاة خط النص",
        
        "doc_wrap": "التفاف العناصر",
        "doc_wrap_desc": "يتحكم في سلوك الالتفاف",
        "doc_wrap_nowrap": "سطر واحد (بدون التفاف)",
        "doc_wrap_wrap": "التفاف لأسطر جديدة",
        "doc_wrap_reverse": "التفاف معكوس",
        
        "doc_child_props": "خصائص الأبناء",
        "doc_flex_grow": "القدرة على النمو",
        "doc_flex_shrink": "القدرة على الانكماش",
        "doc_flex_basis": "الحجم الأولي",
        "doc_align_self": "المحاذاة الفردية",
        
        "doc_when_use": "متى تستخدم",
        "doc_when_not": "متى لا تستخدم",
        "doc_reverse_use": "واجهات RTL (عربي، عبري)، تطبيقات الدردشة، الجداول الزمنية، تخطيطات خاصة",
        "doc_reverse_avoid": "الأقسام العادية، تخطيطات الهيرو، بطاقات المنتجات، الشبكات القياسية، معظم التخطيطات المتجاوبة",
    }
}

# ============================================
# HELPER FUNCTIONS
# ============================================
def render_flexbox_visual(direction, justify, align):
    """Minimalist flexbox visualization"""
    html = f"""
    <div style='
        display: flex;
        flex-direction: {direction};
        justify-content: {justify};
        align-items: {align};
        gap: 16px;
        border: 2px solid #ddd;
        padding: 24px;
        height: 200px;
        background: #fafafa;
        border-radius: 8px;
    '>
        <div style='background: #3b82f6; width: 80px; height: 80px; border-radius: 8px;'></div>
        <div style='background: #10b981; width: 80px; height: 80px; border-radius: 8px;'></div>
        <div style='background: #f59e0b; width: 80px; height: 80px; border-radius: 8px;'></div>
    </div>
    """
    components.html(html, height=240)


def render_wrap_demo(wrap_mode, parent_width):
    """Clean wrap demonstration"""
    html = f"""
    <style>
        .wrap-container {{
            display: flex;
            flex-wrap: {wrap_mode};
            gap: 12px;
            padding: 20px;
            border: 2px solid #ddd;
            background: #fafafa;
            width: {parent_width}px;
            border-radius: 8px;
        }}
        .wrap-box {{
            width: 100px;
            height: 100px;
            background: #8b5cf6;
            border-radius: 8px;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-weight: 600;
            font-size: 24px;
        }}
    </style>
    <div class="wrap-container">
        <div class="wrap-box">1</div>
        <div class="wrap-box">2</div>
        <div class="wrap-box">3</div>
        <div class="wrap-box">4</div>
        <div class="wrap-box">5</div>
        <div class="wrap-box">6</div>
    </div>
    """
    components.html(html, height=300)


def render_hero(direction, justify, align):
    """Minimalist hero section"""
    html = f"""
    <style>
        .hero {{
            display: flex;
            flex-direction: {direction};
            justify-content: {justify};
            align-items: {align};
            gap: 24px;
            padding: 32px;
            background: #f8fafc;
            border-radius: 8px;
            border: 1px solid #e2e8f0;
        }}
        .hero-img {{
            flex: 1;
            background: #cbd5e1;
            padding: 60px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #64748b;
            font-weight: 500;
        }}
        .hero-text {{
            flex: 1.5;
            background: white;
            padding: 32px;
            border-radius: 8px;
        }}
        .hero-text h2 {{
            margin: 0 0 12px 0;
            color: #1e293b;
            font-size: 24px;
        }}
        .hero-text p {{
            margin: 0;
            color: #64748b;
            line-height: 1.6;
        }}
    </style>
    <div class='hero'>
        <div class='hero-img'>Image</div>
        <div class='hero-text'>
            <h2>Clean Hero Section</h2>
            <p>Simple and elegant layout using Flexbox principles.</p>
        </div>
    </div>
    """
    components.html(html, height=240)


def render_cards(justify, align):
    """Minimalist cards"""
    html = f"""
    <style>
        .cards {{
            display: flex;
            justify-content: {justify};
            align-items: {align};
            gap: 16px;
            padding: 24px;
            background: #fafafa;
            border-radius: 8px;
        }}
        .card {{
            width: 160px;
            height: 120px;
            background: white;
            border: 1px solid #e5e7eb;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #6b7280;
            font-weight: 500;
        }}
    </style>
    <div class='cards'>
        <div class='card'>Card 1</div>
        <div class='card'>Card 2</div>
        <div class='card'>Card 3</div>
    </div>
    """
    components.html(html, height=200)


def render_gallery(justify):
    """Minimalist gallery"""
    html = f"""
    <style>
        .gallery {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
            justify-content: {justify};
            padding: 24px;
            background: #fafafa;
            border-radius: 8px;
        }}
        .gallery-item {{
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-weight: 600;
            font-size: 32px;
        }}
    </style>
    <div class='gallery'>
        <div class='gallery-item'>1</div>
        <div class='gallery-item'>2</div>
        <div class='gallery-item'>3</div>
        <div class='gallery-item'>4</div>
    </div>
    """
    components.html(html, height=280)


def render_documentation(ui):
    """Clean, organized documentation"""
    
    # Parent Controls
    st.markdown(f"### {ui['doc_parent_title']}")
    st.caption(ui['doc_parent_desc'])
    
    with st.container():
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
**{ui['doc_direction']}**  
{ui['doc_direction_desc']}
- `row` — {ui['doc_direction_row']}
- `row-reverse` — {ui['doc_direction_row_reverse']}
- `column` — {ui['doc_direction_column']}
- `column-reverse` — {ui['doc_direction_column_reverse']}
            """)
            
            st.markdown(f"""
**{ui['doc_justify']}**  
{ui['doc_justify_desc']}
- `flex-start` — {ui['doc_justify_start']}
- `center` — {ui['doc_justify_center']}
- `flex-end` — {ui['doc_justify_end']}
- `space-between` — {ui['doc_justify_between']}
- `space-around` — {ui['doc_justify_around']}
- `space-evenly` — {ui['doc_justify_evenly']}
            """)
        
        with col2:
            st.markdown(f"""
**{ui['doc_align']}**  
{ui['doc_align_desc']}
- `flex-start` — {ui['doc_align_start']}
- `center` — {ui['doc_align_center']}
- `flex-end` — {ui['doc_align_end']}
- `stretch` — {ui['doc_align_stretch']}
- `baseline` — {ui['doc_align_baseline']}
            """)
            
            st.markdown(f"""
**{ui['doc_wrap']}**  
{ui['doc_wrap_desc']}
- `nowrap` — {ui['doc_wrap_nowrap']}
- `wrap` — {ui['doc_wrap_wrap']}
- `wrap-reverse` — {ui['doc_wrap_reverse']}
            """)
    
    st.markdown("---")
    
    # Child Controls
    st.markdown(f"### {ui['doc_child_title']}")
    st.caption(ui['doc_child_desc'])
    
    st.markdown(f"""
- `flex-grow` — {ui['doc_flex_grow']}
- `flex-shrink` — {ui['doc_flex_shrink']}
- `flex-basis` — {ui['doc_flex_basis']}
- `align-self` — {ui['doc_align_self']}
    """)
    
    st.markdown("---")
    
    # Usage Guidelines
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"**✅ {ui['doc_when_use']} `*-reverse`**")
        st.caption(ui['doc_reverse_use'])
    
    with col2:
        st.markdown(f"**❌ {ui['doc_when_not']} `*-reverse`**")
        st.caption(ui['doc_reverse_avoid'])


# ============================================
# MAIN APPLICATION
# ============================================
def main():
    # Language selector (minimal)
    language = st.selectbox(
        "🌐",
        ["English", "العربية"],
        label_visibility="collapsed"
    )
    ui = TRANSLATIONS[language]

    # Header
    st.title(ui["title"])
    st.caption(ui["subtitle"])
    
    st.markdown("<br>", unsafe_allow_html=True)

    # ========================================
    # CONTROLS
    # ========================================
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader(ui["step1"])
        direction = st.segmented_control(
            "direction",
            ["row", "column"],
            default="row",
            label_visibility="collapsed"
        )
    
    with col2:
        st.subheader(ui["step2"])
        justify = st.segmented_control(
            "justify",
            ["flex-start", "center", "flex-end", "space-between", "space-around", "space-evenly"],
            default="center",
            label_visibility="collapsed"
        )
    
    with col3:
        st.subheader(ui["step3"])
        align = st.segmented_control(
            "align",
            ["flex-start", "center", "flex-end", "stretch"],
            default="center",
            label_visibility="collapsed"
        )

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Live Demo
    st.subheader(ui["live_demo"])
    render_flexbox_visual(direction, justify, align)

    st.markdown("<br><br>", unsafe_allow_html=True)

    # ========================================
    # WRAP DEMO
    # ========================================
    st.subheader(ui["wrap_demo"])
    
    col_w1, col_w2 = st.columns([1, 2])
    
    with col_w1:
        wrap_mode = st.segmented_control(
            "wrap",
            ["nowrap", "wrap", "wrap-reverse"],
            default="wrap",
            label_visibility="collapsed"
        )
    
    with col_w2:
        parent_width = st.slider(
            ui["parent_width"],
            200, 900, 500, 50,
            label_visibility="collapsed"
        )
    
    render_wrap_demo(wrap_mode, parent_width)

    st.markdown("---")

    # ========================================
    # REAL EXAMPLES
    # ========================================
    st.header(ui["examples"])
    
    tab1, tab2, tab3 = st.tabs([ui["hero"], ui["cards"], ui["gallery"]])
    
    with tab1:
        render_hero(direction, justify, align)
    
    with tab2:
        render_cards(justify, align)
    
    with tab3:
        render_gallery(justify)

    st.markdown("---")

    # ========================================
    # DOCUMENTATION
    # ========================================
    with st.expander(f"📖 {ui['docs']}", expanded=False):
        render_documentation(ui)


# ============================================
# RUN
# ============================================
if __name__ == "__main__":
    main()
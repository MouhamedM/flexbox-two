import streamlit as st
import streamlit.components.v1 as components

# Page configuration
st.set_page_config(
    page_title="Flexbox Made Simple(Parents)",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS for visual examples
st.markdown("""
<style>
    .visual-demo {
        border: 2px solid #333;
        padding: 20px;
        margin: 10px 0;
        border-radius: 10px;
    }
    .body-demo {
        background-color: #e3f2fd;
        min-height: 300px;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .container-demo {
        background-color: #c8e6c9;
        padding: 20px;
        display: flex;
        gap: 10px;
    }
    .box-demo {
        background-color: #ffcc80;
        padding: 20px;
        border: 2px solid #ff9800;
        border-radius: 5px;
    }
    .family-tree {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin: 20px 0;
    }
    .step-box {
        background-color: white;
        color: #333;
        padding: 15px;
        margin: 10px;
        border-radius: 10px;
        border-left: 5px solid #4CAF50;
    }
    .kid-explanation {
        background-color: #fff9c4;
        padding: 20px;
        border-radius: 15px;
        border: 3px solid #ffd54f;
        font-size: 18px;
    }
</style>
""", unsafe_allow_html=True)

# Language selection
language = st.sidebar.selectbox("🌍 Choose Language / اختر اللغة", ["English", "العربية"])

if language == "English":
    
    st.title("🎯 Flexbox Made Super Simple")
    
    # Family relationship visualization
    st.markdown("""
    <div class="family-tree">
        <h2>👨‍👩‍👧‍👦 The Family Control System</h2>
        <h3>Body → Parent → Child → Content</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Visual documentation of relationships
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 10px;">
            <h3>🏠 Body</h3>
            <p>The big house that holds everything</p>
            <p><strong>Controls:</strong> Where parent sits</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #c8e6c9; border-radius: 10px;">
            <h3>📦 Parent</h3>
            <p>The main container box</p>
            <p><strong>Controls:</strong> Where children sit</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #ffcc80; border-radius: 10px;">
            <h3>🎁 Child</h3>
            <p>Boxes inside parent</p>
            <p><strong>Controls:</strong> Its own content</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #f8bbd0; border-radius: 10px;">
            <h3>📝 Content</h3>
            <p>Text and items inside child</p>
            <p><strong>Just follows</strong> what child says</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Audience selection
    audience = st.radio("Choose how you want to learn:", ["Simple Explanation", "For Kids 🧒", "See Live Example"])
    
    if audience == "Simple Explanation":
        
        st.header("🤔 Problem 1: Why can't I see justify-content working?")
        
        st.markdown("""
        <div class="step-box">
            <h4>🔍 The Problem:</h4>
            When you use <code>inline-flex</code>, your container becomes exactly as wide as your boxes.
            So when you try to move boxes to the end, they're already at the end!
        </div>
        """, unsafe_allow_html=True)
        
        # Visual example
        st.subheader("👀 See the Difference:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Small Container (inline-flex):**")
            st.markdown("""
            <div class="visual-demo">
                <div style="display: inline-flex; background: #c8e6c9; padding: 10px;">
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">Box 1</div>
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">Box 2</div>
                </div>
                <p><small>Container is exactly box width - no space to move!</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Big Container (flex):**")
            st.markdown("""
            <div class="visual-demo">
                <div style="display: flex; background: #c8e6c9; padding: 10px; justify-content: flex-end;">
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">Box 1</div>
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">Box 2</div>
                </div>
                <p><small>Container is wide - boxes can move to end!</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        st.header("🎯 Problem 2: How to center container with background")
        
        st.markdown("""
        <div class="step-box">
            <h4>🏠 The Solution: Use the Family System</h4>
            Make Body control Parent, Parent control Children!
        </div>
        """, unsafe_allow_html=True)
        
        # Step by step solution
        st.subheader("📋 Step-by-Step Solution:")
        
        steps = [
            ("Step 1", "Make Body a flex container", "body { display: flex; justify-content: center; }"),
            ("Step 2", "Body centers the Parent container", "This happens automatically now!"),
            ("Step 3", "Parent controls its Children", ".container { display: flex; justify-content: center; }")
        ]
        
        for step, description, code in steps:
            with st.expander(f"{step}: {description}"):
                st.code(code, language="css")
        
        # Final visual result
        st.subheader("🎉 Final Result:")
        st.markdown("""
        <div class="visual-demo body-demo">
            <div class="container-demo" style="justify-content: center;">
                <div class="box-demo">Box 1</div>
                <div class="box-demo">Box 2</div>
                <div class="box-demo">Box 3</div>
            </div>
        </div>
        <p><strong>See how:</strong> Body (blue) centers Parent (green), Parent centers Children (orange)</p>
        """, unsafe_allow_html=True)
    
    elif audience == "For Kids 🧒":
        
        st.markdown('<div class="kid-explanation">', unsafe_allow_html=True)
        st.header("🎨 Flexbox for Kids!")
        
        st.subheader("🎁 The Toy Box Story")
        
        st.markdown("""
        ### Chapter 1: The Magic Moving Toys
        
        Once upon a time, you had a **small toy box** that was exactly the same size as your toys.
        
        When you said "toys, move to the right!", they couldn't move because the box was too small!
        
        **The Fix:** Get a **bigger toy box** so your toys have space to move around!
        """)
        
        # Visual for kids
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Small Box Problem:**")
            st.markdown("""
            <div style="background: #ffcc80; display: inline-block; padding: 10px;">
                🧸🧸🧸
            </div>
            <p>No space to move!</p>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**Big Box Solution:**")
            st.markdown("""
            <div style="background: #ffcc80; padding: 10px; width: 200px; text-align: right;">
                🧸🧸🧸
            </div>
            <p>Lots of space to move!</p>
            """, unsafe_allow_html=True)
        
        st.subheader("👨‍👩‍👧‍👦 The Family Rules")
        
        st.markdown("""
        ### Your Toy Family:
        
        - **Grandpa Body** = Your whole room 🏠
        - **Dad Container** = Your toy box 📦  
        - **You & Siblings** = The toys 🧸
        - **Your Clothes** = What's inside toys 👕
        
        **Family Rules:**
        1. Grandpa decides where Dad sits in the room
        2. Dad decides where you and siblings sit in the toy box
        3. You decide what clothes you wear
        """)
        
        st.markdown("""
        ### 🎯 Simple Code for Kids:
        ```
        /* Grandpa Room rules */
        body {
            display: flex;
            justify-content: center;    /* Put Dad in room center */
        }
        
        /* Dad Toy Box rules */
        .container {
            display: flex;
            background: green;
            justify-content: center;    /* Put toys in box center */
        }
        ```
        """)
        st.markdown('</div>', unsafe_allow_html=True)
    
    else:  # Live Example
        st.header("🎮 Live Flexbox Example")
        
        st.markdown("""
        <div class="step-box">
            <h4>🔧 Try It Yourself!</h4>
            See how the family system works by changing the code below.
        </div>
        """, unsafe_allow_html=True)
        
        # Interactive code example
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📝 Your Code")
            body_display = st.selectbox("Body display:", ["flex", "block"])
            body_justify = st.selectbox("Body justify-content:", ["center", "flex-start", "flex-end"])
            container_display = st.selectbox("Container display:", ["flex", "inline-flex"])
            container_justify = st.selectbox("Container justify-content:", ["center", "flex-start", "flex-end"])
        
        with col2:
            st.subheader("👀 Live Result")
            
            # Generate the live preview
            live_css = f"""
            <style>
                .live-preview-body {{
                    background-color: #e3f2fd;
                    min-height: 200px;
                    display: {body_display};
                    justify-content: {body_justify};
                    align-items: center;
                    padding: 20px;
                    border: 2px dashed #2196F3;
                }}
                .live-preview-container {{
                    background-color: #c8e6c9;
                    padding: 20px;
                    display: {container_display};
                    justify-content: {container_justify};
                    gap: 10px;
                    border: 2px solid #4CAF50;
                }}
            </style>
            """
            
            st.markdown(live_css, unsafe_allow_html=True)
            st.markdown("""
            <div class="live-preview-body">
                <div class="live-preview-container">
                    <div style="background: #ffcc80; padding: 15px;">Toy 1</div>
                    <div style="background: #ffcc80; padding: 15px;">Toy 2</div>
                    <div style="background: #ffcc80; padding: 15px;">Toy 3</div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.subheader("🧠 What You Learned:")
        
        learnings = {
            "Body controls Parent": "Change Body's justify-content to see Parent move",
            "Parent controls Children": "Change Container's justify-content to see Children move", 
            "Display type matters": "Switch between flex and inline-flex to see width changes"
        }
        
        for title, description in learnings.items():
            with st.expander(f"✅ {title}"):
                st.write(description)

else:  # Arabic Version
    st.title("🎯 Flexbox شرح مبسط جداً")
    
    # Family relationship visualization in Arabic
    st.markdown("""
    <div class="family-tree" style="text-align: center; direction: rtl;">
        <h2>👨‍👩‍👧‍👦 نظام التحكم العائلي</h2>
        <h3>Body → Parent → Child → Content</h3>
        <h4>الجسم ← الأب ← الابن ← المحتوى</h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Visual documentation of relationships in Arabic
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #e3f2fd; border-radius: 10px; direction: rtl;">
            <h3>🏠 الجسم</h3>
            <p>المنزل الكبير الذي يحمل كل شيء</p>
            <p><strong>يتحكم في:</strong> مكان الأب</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #c8e6c9; border-radius: 10px; direction: rtl;">
            <h3>📦 الأب</h3>
            <p>الصندوق الحاوي الرئيسي</p>
            <p><strong>يتحكم في:</strong> مكان الأطفال</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #ffcc80; border-radius: 10px; direction: rtl;">
            <h3>🎁 الابن</h3>
            <p> الصناديق داخل الأب</p>
            <p><strong>يتحكم في:</strong> محتواه الداخلي</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div style="text-align: center; padding: 15px; background: #f8bbd0; border-radius: 10px; direction: rtl;">
            <h3>📝 المحتوى</h3>
            <p>النص والعناصر داخل الابن</p>
            <p><strong>يتبع فقط</strong> ما يقوله الابن</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Audience selection in Arabic
    audience = st.radio("اختر طريقة التعلم:", ["شرح مبسط", "للأطفال 🧒", "مثال حي"])
    
    if audience == "شرح مبسط":
        
        st.header("🤔 المشكلة الأولى: لماذا لا أرى justify-content تعمل؟")
        
        st.markdown("""
        <div class="step-box" style="text-align: right; direction: rtl;">
            <h4>🔍 المشكلة:</h4>
            عندما تستخدم <code>inline-flex</code>، يصبح حاويك بنفس عرض صناديقك بالضبط.
            لذا عندما تحاول نقل الصناديق إلى النهاية، تكون بالفعل في النهاية!
        </div>
        """, unsafe_allow_html=True)
        
        # Visual example in Arabic
        st.subheader("👀 شاهد الفرق:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**حاوية صغيرة (inline-flex):**")
            st.markdown("""
            <div class="visual-demo">
                <div style="display: inline-flex; background: #c8e6c9; padding: 10px;">
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">صندوق ١</div>
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">صندوق ٢</div>
                </div>
                <p><small>الحاوية بنفس عرض الصناديق - لا مساحة للحركة!</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("**حاوية كبيرة (flex):**")
            st.markdown("""
            <div class="visual-demo">
                <div style="display: flex; background: #c8e6c9; padding: 10px; justify-content: flex-end;">
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">صندوق ١</div>
                    <div style="background: #ffcc80; padding: 10px; margin: 5px;">صندوق ٢</div>
                </div>
                <p><small>الحاوية واسعة - الصناديق يمكنها التحرك!</small></p>
            </div>
            """, unsafe_allow_html=True)
        
        st.header("🎯 المشكلة الثانية: كيفية توسيط الحاوية مع الخلفية")
        
        st.markdown("""
        <div class="step-box" style="text-align: right; direction: rtl;">
            <h4>🏠 الحل: استخدم النظام العائلي</h4>
            اجعل الجسم يتحكم في الأب، والأب يتحكم في الأطفال!
        </div>
        """, unsafe_allow_html=True)
        
        # Step by step solution in Arabic
        st.subheader("📋 الحل خطوة بخطوة:")
        
        steps = [
            ("الخطوة ١", "اجعل الجسم حاوية مرنة", "body { display: flex; justify-content: center; }"),
            ("الخطوة ٢", "الجسم يوسط حاوية الأب", "هذا يحدث تلقائياً الآن!"),
            ("الخطوة ٣", "الأب يتحكم في أطفاله", ".container { display: flex; justify-content: center; }")
        ]
        
        for step, description, code in steps:
            with st.expander(f"{step}: {description}"):
                st.code(code, language="css")
        
        # Final visual result in Arabic
        st.subheader("🎉 النتيجة النهائية:")
        st.markdown("""
        <div class="visual-demo body-demo">
            <div class="container-demo" style="justify-content: center;">
                <div class="box-demo">صندوق ١</div>
                <div class="box-demo">صندوق ٢</div>
                <div class="box-demo">صندوق ٣</div>
            </div>
        </div>
        <p style="text-align: right; direction: rtl;"><strong>شاهد كيف:</strong> الجسم (أزرق) يوسط الأب (أخضر)، الأب يوسط الأطفال (برتقالي)</p>
        """, unsafe_allow_html=True)

# Footer with key takeaways
st.markdown("---")
st.markdown("""
### 🗝️ Key Things to Remember:

1. **Every parent controls its direct children** - Body → Container → Boxes
2. **Use flex (not inline-flex) when you need space** for justify-content to work
3. **To center a container**, make its parent (body) a flex container with justify-content: center
4. **Start simple** and add complexity gradually

### 🎯 Practice Exercise:
Try creating a simple page with:
- Body that centers everything
- Container that holds 3 boxes  
- Boxes centered inside container
- Different colors for each level
""")
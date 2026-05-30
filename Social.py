import streamlit as st
import random

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="AI Social Media Content Assistant",
    page_icon="✨",
    layout="centered"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: #000000;
}

#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

.block-container {
    padding-top: 2rem;
    max-width: 950px;
}

.main-title {
    text-align: center;
    color: white;
    font-size: 52px;
    font-weight: 800;
    line-height: 1.2;
    margin-bottom: 10px;
}

.by-artistude {
    text-align: center;
    color: teal;
    font-size: 22px;
    font-weight: 900;
    letter-spacing: 2px;
    margin-bottom: 10px;
}

.sub-title {
    text-align: center;
    color: #D6E4FF;
    font-size: 18px;
    margin-bottom: 45px;
}

.section-title {
    color: beige !important;
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 20px;
}

.content-inputs-label {
    color: beige !important;
    font-size: 30px;
    font-weight: 700;
    margin-bottom: 20px;
}

div[data-testid="stWidgetLabel"] p {
    color: white !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

div[data-testid="stTextInput"] label,
div[data-testid="stTextInput"] label p,
div[data-testid="stTextInput"] div[data-testid="stWidgetLabel"] p {
    color: white !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

div[data-testid="stSelectbox"] label,
div[data-testid="stSelectbox"] label p,
div[data-testid="stSelectbox"] div[data-testid="stWidgetLabel"] p {
    color: white !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

.stTextInput input {
    background: white !important;
    color: black !important;
    border-radius: 15px !important;
    border: none !important;
    padding: 14px !important;
    font-size: 16px !important;
}

.stTextInput input::placeholder { color: gray !important; }

.stSelectbox div[data-baseweb="select"] {
    background: white !important;
    border-radius: 15px !important;
    border: none !important;
    min-height: 55px !important;
}

.stSelectbox span {
    color: black !important;
    font-weight: 600 !important;
    font-size: 16px !important;
}

div[role="listbox"] { background: white !important; }
div[role="option"] { color: black !important; font-size: 15px !important; }

.stButton {
    display: flex !important;
    justify-content: center !important;
}

.stButton button {
    width: 300px !important;
    min-width: 300px !important;
    white-space: nowrap !important;
    height: 60px;
    border: none;
    border-radius: 16px;
    background: linear-gradient(to right, #0000FF, #00C853);
    color: white;
    font-size: 19px;
    font-weight: 700;
    margin-top: 15px;
    transition: 0.3s ease;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.3);
}

.stButton button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #00C853, #0000FF);
    color: white;
}

.result-card {
    background: beige;
    padding: 25px;
    border-radius: 18px;
    margin-top: 18px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.15);
}

.result-card h3 { color: #001F54 !important; margin-bottom: 10px; }
.result-card p { color: black !important; font-size: 16px; }

/* ---- INFO SECTIONS BELOW BUTTON ---- */

.info-divider {
    border: none;
    border-top: 1px solid #222;
    margin: 50px 0 40px 0;
}

.info-main-title {
    color: white;
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 8px;
    margin-top: 50px;
}

.info-section-heading {
    color: teal;
    font-size: 28px;
    font-weight: 800;
    margin-top: 30px;
    margin-bottom: 10px;
}

.info-para {
    color: #bbbbbb;
    font-size: 15px;
    line-height: 1.85;
    margin-bottom: 14px;
}

.info-card {
    background: #0d0d0d;
    border: 1px solid #1a1a1a;
    border-left: 5px solid teal;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 18px;
}

.info-card h3 {
    color: teal !important;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 10px;
}

.info-card p {
    color: #bbbbbb !important;
    font-size: 15px;
    line-height: 1.8;
}

.numbered-card {
    background: #0d0d0d;
    border: 1px solid #1a1a1a;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 18px;
}

.numbered-card h3 {
    color: white !important;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 10px;
}

.numbered-card p {
    color: #bbbbbb !important;
    font-size: 15px;
    line-height: 1.8;
}

.numbered-card ul {
    color: #bbbbbb;
    font-size: 15px;
    line-height: 2;
    padding-left: 20px;
}

.who-card {
    background: #0d0d0d;
    border: 1px solid #222;
    border-radius: 14px;
    padding: 24px 28px;
    margin-bottom: 18px;
    text-align: center;
}

.who-card h3 {
    color: white !important;
    font-size: 18px;
    font-weight: 800;
    margin-bottom: 10px;
}

.who-card p {
    color: #bbbbbb !important;
    font-size: 15px;
    line-height: 1.8;
}

.who-icon {
    font-size: 36px;
    margin-bottom: 10px;
}

.footer {
    text-align: center;
    color: white;
    margin-top: 40px;
    opacity: 0.8;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ---------------- #

st.markdown("""
<div class="main-title">AI SOCIAL MEDIA CONTENT ASSISTANT</div>
<div class="by-artistude">BY ARTISTUDE</div>
<div class="sub-title">Generate captions, hashtags, CTAs and content ideas instantly.</div>
""", unsafe_allow_html=True)

# ---------------- INPUT SECTION ---------------- #

st.markdown("<div class='content-inputs-label'>Content Inputs</div>", unsafe_allow_html=True)

industry = st.text_input("Industry / Business Type", placeholder="Example: Photography")

platform = st.selectbox("Platform", ["Instagram", "Facebook", "LinkedIn", "YouTube", "Twitter/X"])

tone = st.selectbox("Tone", ["Professional", "Luxury", "Cinematic", "Casual", "Promotional"])

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    generate = st.button("Generate Content")

# ---------------- OUTPUT SECTION ---------------- #

if generate:
    if industry.strip() == "":
        st.warning("Please enter Industry / Business Type")
    else:
        captions = [
            f"Elevate your {industry} brand with stunning creativity.",
            f"Creating engaging {industry} content for modern audiences.",
            f"Transforming ideas into powerful {platform} experiences.",
            f"Bringing cinematic storytelling into the world of {industry}.",
            f"Helping brands grow smarter through creative content."
        ]
        hashtags = [
            f"#{industry.replace(' ','')}",
            "#ContentCreation",
            "#DigitalMarketing",
            "#SocialMedia",
            "#BrandGrowth"
        ]
        ctas = [
            "Message us today!",
            "Follow for more updates!",
            "Contact us to grow your brand!",
            "Start your creative journey with us!",
            "Let's build your online presence together!"
        ]
        ideas = [
            f"Behind-the-scenes {industry} reel concept.",
            f"{platform} storytelling campaign.",
            "Trending reel with cinematic editing.",
            "Customer testimonial video idea.",
            "Creative transformation content concept."
        ]

        caption = random.choice(captions)
        cta = random.choice(ctas)
        idea = random.choice(ideas)

        st.markdown("<div class='section-title'>Generated Content</div>", unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card"><h3>📌 Caption</h3><p>{caption}</p></div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card"><h3>#️⃣ Hashtags</h3><p>{" ".join(hashtags)}</p></div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card"><h3>📢 Call To Action</h3><p>{cta}</p></div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="result-card"><h3>💡 Content Idea</h3><p>{idea}</p></div>
        """, unsafe_allow_html=True)

# =============================================
# INFO SECTIONS BELOW THE TOOL
# =============================================

st.markdown("<hr class='info-divider'>", unsafe_allow_html=True)

# ---- SECTION 1: WHY USE ---- #
st.markdown("""
<div class="info-main-title">Why Use the AI Social Media Content Assistant?</div>
<p class="info-para">
    Whether you're a brand, creator, or agency — generating fresh, engaging social media content
    every single day is one of the biggest challenges in digital marketing. Our AI Social Media
    Content Assistant eliminates the blank page problem and delivers ready-to-use captions,
    hashtags, CTAs, and content ideas in seconds.
</p>

<div class="info-card">
    <h3>🚀 Unlimited Original Social Media Content On-Demand</h3>
    <p>
        Our AI Content Assistant delivers a constant stream of fresh, platform-specific captions,
        hashtags, and content ideas tailored to your industry and tone. Simply enter your business
        type, choose your platform and tone, and get polished social media content instantly.
    </p>
    <p>
        Whether you need ideas for your next viral Instagram reel, a professional LinkedIn post,
        or a promotional Facebook campaign — the assistant generates original content in seconds
        so you never run out of ideas that resonate with your audience.
    </p>
</div>

<div class="info-card">
    <h3>⚡ A Constant Stream of Fresh Content Ideas for Every Platform</h3>
    <p>
        Every social media platform has its own language, audience, and content style. What works
        on Instagram won't always land on LinkedIn. Our assistant understands the difference and
        generates captions and ideas perfectly matched to your selected platform — whether that's
        Instagram, Facebook, LinkedIn, YouTube, or Twitter/X.
    </p>
    <p>
        Stop spending hours crafting the perfect post from scratch. Let AI handle the heavy lifting
        while you focus on growing your brand, engaging your community, and building meaningful
        connections with your audience.
    </p>
</div>

<div class="info-card">
    <h3>🎯 Tone-Matched Content for Your Brand Voice</h3>
    <p>
        Every brand has a unique personality. Our tool lets you choose from Professional, Luxury,
        Cinematic, Casual, or Promotional tones — so every caption and CTA generated sounds
        authentically like your brand, not a generic AI template.
    </p>
    <p>
        Consistency in tone across all your social media channels builds trust and recognition.
        With our assistant, your brand voice stays sharp and consistent no matter how much content
        you produce.
    </p>
</div>
""", unsafe_allow_html=True)

# ---- SECTION 2: 5 WAYS ---- #
st.markdown("""
<div class="info-main-title">5 Ways to Generate Fresh Social Media Content Ideas</div>
<p class="info-para">
    Great social media content ideas can come from a wide variety of sources. Here are five
    proven strategies to keep your content calendar full — beyond using an AI assistant.
</p>

<div class="numbered-card">
    <h3>1. Follow Trending Topics on Social Media</h3>
    <p>
        Staying on top of what's trending in your niche is one of the fastest ways to generate
        relevant content ideas. Tools like Google Trends, Instagram Explore, and LinkedIn News
        highlight what's getting the most engagement right now in your industry. When you align
        your content with trending conversations, your posts are more likely to go viral and
        reach a wider audience.
    </p>
</div>

<div class="numbered-card">
    <h3>2. Listen to Your Audience</h3>
    <p>
        The best content ideas often come directly from the people you're trying to reach.
        Read comments on your posts, check your DMs, run Instagram polls or LinkedIn surveys,
        and pay attention to the questions your audience asks most. When your content directly
        answers what your followers want to know, engagement skyrockets naturally.
    </p>
</div>

<div class="numbered-card">
    <h3>3. Study Your Competitors' Best-Performing Posts</h3>
    <p>
        Competitor research is one of the most underrated content strategy tools. Identify
        the top accounts in your industry and study which of their posts get the most likes,
        comments, and shares. This gives you a clear picture of what content formats, topics,
        and tones your shared audience responds to — and helps you create better versions for
        your own brand.
    </p>
</div>

<div class="numbered-card">
    <h3>4. Repurpose Your Best Existing Content</h3>
    <p>
        You don't always need brand-new ideas. Revisit your top-performing posts and think about
        how you can refresh or repurpose them. Turn a popular caption into a carousel post,
        convert a blog article into a short reel script, or transform a customer testimonial into
        a quote graphic. Repurposing content saves time and gives your best ideas a second life
        across different platforms.
    </p>
</div>

<div class="numbered-card">
    <h3>5. Build a Monthly Content Calendar</h3>
    <p>
        Consistency is the foundation of social media growth. Plan your content a month in advance
        using a content calendar — mapping out post themes, platform-specific content, campaign
        dates, and seasonal trends. When you have a clear plan, you spend less time scrambling
        for ideas and more time creating high-quality content that actually grows your brand.
    </p>
</div>
""", unsafe_allow_html=True)

# ---- SECTION 3: WHO IS IT FOR ---- #
st.markdown("""
<div class="info-main-title">Who Is This Tool For?</div>
<p class="info-para">
    The AI Social Media Content Assistant is designed for anyone who creates, manages,
    or strategizes social media content for a brand or business.
</p>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="who-card">
        <div class="who-icon">📱</div>
        <h3>Content Creators</h3>
        <p>Generate fresh captions, hashtags, and content ideas for your personal brand or niche
        page — instantly, across any platform.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="who-card">
        <div class="who-icon">📊</div>
        <h3>Social Media Managers</h3>
        <p>Speed up your content workflow by generating platform-ready posts for multiple brands
        and clients in seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="who-card">
        <div class="who-icon">🏢</div>
        <h3>Business Owners</h3>
        <p>Promote your products and services with professional, tone-matched social media content
        — without needing a full marketing team.</p>
    </div>
    """, unsafe_allow_html=True)

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="who-card">
        <div class="who-icon">🎯</div>
        <h3>Digital Marketers</h3>
        <p>Create on-brand content for campaigns, product launches, and promotions across
        Instagram, LinkedIn, YouTube, and more.</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="who-card">
        <div class="who-icon">🎬</div>
        <h3>Video Creators</h3>
        <p>Get cinematic content ideas, reel concepts, and YouTube post descriptions tailored
        to your industry and storytelling style.</p>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="who-card">
        <div class="who-icon">🏆</div>
        <h3>Marketing Agencies</h3>
        <p>Scale your content production across multiple clients and industries with AI-powered
        captions, hashtags, and post ideas — on demand.</p>
    </div>
    """, unsafe_allow_html=True)

# ---- SECTION 4: FEATURES ---- #
st.markdown("""
<div class="info-main-title">What the AI Assistant Generates for You</div>
<p class="info-para">
    Every time you click Generate, the AI Social Media Content Assistant produces four
    powerful content outputs — each tailored to your industry, platform, and tone.
</p>

<div class="info-card">
    <h3>📌 AI-Generated Captions</h3>
    <p>
        Get scroll-stopping captions crafted specifically for your industry and chosen platform tone.
        Whether you need something professional for LinkedIn, cinematic for Instagram, or casual for
        Twitter/X — the assistant delivers captions that match your brand voice and engage your audience.
    </p>
</div>

<div class="info-card">
    <h3>#️⃣ Smart Hashtag Suggestions</h3>
    <p>
        Reach the right audience with relevant, industry-specific hashtags generated automatically.
        Each set includes your niche hashtag, plus high-performing general tags like
        #ContentCreation, #DigitalMarketing, and #BrandGrowth to maximize post visibility and reach.
    </p>
</div>

<div class="info-card">
    <h3>📢 High-Converting CTAs</h3>
    <p>
        Every great social media post ends with a strong Call To Action. Our assistant generates
        CTAs designed to drive real engagement — from "Message us today!" to "Start your creative
        journey with us!" — pushing your audience to take meaningful action after reading your post.
    </p>
</div>

<div class="info-card">
    <h3>💡 Creative Content Ideas</h3>
    <p>
        Never stare at a blank content calendar again. Get instant content concepts like
        behind-the-scenes reels, storytelling campaigns, customer testimonial videos, and
        cinematic transformation posts — all tailored to your specific industry and platform.
    </p>
</div>
""", unsafe_allow_html=True)

# ---- SECTION 5: BUILT BY ARTISTUDE ---- #
st.markdown("""
<div class="info-main-title">Built by Artistude — Powered by AI</div>
<p class="info-para">
    This AI Social Media Content Assistant is crafted as part of the <strong style="color:teal;">
    AI & Media Technology Internship</strong> at Artistude Innovations Pvt. Ltd. — combining
    cutting-edge artificial intelligence with real-world social media marketing expertise.
</p>
<p class="info-para">
    At Artistude, we believe that great content should be accessible to every brand — regardless
    of size, budget, or team capacity. Our mission is to empower creators, marketers, and
    businesses with AI-powered tools that save time, spark creativity, and deliver results
    across every social media platform.
</p>
<p class="info-para">
    Whether you're a solo creator just starting out or an established agency managing multiple
    brands — the AI Social Media Content Assistant is your always-on creative partner, ready
    to generate fresh, platform-perfect content at the click of a button.
</p>
""", unsafe_allow_html=True)

# ---------------- FOOTER ---------------- #
st.markdown("""
<div class="footer">
AI & Media Technology Internship Project | Artistude Innovations Pvt. Ltd.
</div>
""", unsafe_allow_html=True)
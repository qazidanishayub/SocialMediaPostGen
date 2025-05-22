import os
import google.generativeai as genai
from fasthtml import html, form, page, state, styles

# Apply basic styling
theme = styles.StyleSheet()
theme.add(
    """
    .container {
        max-width: 720px;
        margin: auto;
        padding: 2rem;
        font-family: Arial, sans-serif;
    }
    h1, h3 {
        color: #1e293b;
    }
    textarea {
        width: 100%;
        padding: 10px;
        font-size: 1rem;
    }
    button {
        background-color: #6366f1;
        color: white;
        border: none;
        padding: 0.5rem 1rem;
        font-size: 1rem;
        margin: 0.2rem;
        cursor: pointer;
        border-radius: 4px;
    }
    .tab-container button {
        display: inline-block;
    }
    .error {
        color: red;
        font-weight: bold;
        margin-top: 1rem;
    }
    .tab-container {
        margin-bottom: 1.5rem;
    }
    """
)

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise EnvironmentError("🚨 GEMINI_API_KEY environment variable not set. Please configure it in Vercel dashboard.")

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-001")

domains = [
    "AI/ML/GenAI/RAG (default)", "Data Science & Analytics", "Agentic AI / Autonomous Agents",
    "SaaS Business Applications", "Healthcare AI", "Fintech + AI", "eCommerce AI/ML",
    "LegalTech / RegTech", "Scientific Research + GenAI", "Content Creation & AI", "Custom Domain..."
]

@page(path="/", title="AI-Driven LinkedIn Post Generator", style=theme)
def main():
    with html("div", class_="container"):
        html("h1", "🤖 AI-Driven LinkedIn Post Generator")

        with html("div", class_="tab-container"):
            tab = state("tab", default="Quick Post")
            html("button", "Quick Post", onclick="tab='Quick Post'")
            html("button", "Guided Journey", onclick="tab='Guided Journey'")

        if tab.value == "Quick Post":
            quick_post()
        else:
            guided_journey()

def build_prompt(user_idea, domain):
    prompt = f"""
You are a LinkedIn content strategist and writing expert focused on cutting-edge technology domains. Your goal is to help a highly skilled expert create professional, engaging LinkedIn posts that:

• Showcase expertise in their field  
• Educate a technically-savvy audience  
• Generate leads and interest from peers or clients  
• Position the user as a thought leader

This post should focus on the domain: **{domain}**

Your task is to generate a LinkedIn post (250–350 words) that includes:
1. A compelling opening hook
2. A brief problem/opportunity statement
3. Simple breakdown or analogy (if needed)
4. A showcase of user expertise, tools, or impact
5. A CTA to drive engagement
6. Add relevant, trending hashtags at the end based on the theme (without explaining them)

If user guidance is given, integrate it naturally. Otherwise, choose a theme in the selected domain.

The tone should be:
- Confident and insightful
- Conversational yet professional
- Clean, short paragraphs or bullets for readability

Output a clean, copy-pasteable LinkedIn post.
"""
    if user_idea:
        prompt += f"\n\nUser Input:\n{user_idea.strip()}"
    return prompt

def quick_post():
    with form("quick_form"):
        user_idea = form.textarea("Focus or idea (optional)")
        selected_domain = form.select("Choose your content domain:", options=domains)
        if selected_domain == "Custom Domain...":
            selected_domain = form.text("Enter your custom domain")
        generate = form.submit("🚀 Generate Post")

    if generate:
        prompt = build_prompt(user_idea, selected_domain)
        try:
            response = model.generate_content(prompt)
            final_post = response.text.strip()
            html("h3", "✅ Your LinkedIn Post")
            html("textarea", final_post, readonly=True, rows=15)
        except Exception as e:
            html("div", f"❌ Error: {e}", class_="error")

def guided_journey():
    with form("guided_form"):
        role = form.select("Your Role", ["AI Engineer", "ML Researcher", "Tech Founder", "Product Manager", "Consultant", "Other"])
        industry = form.select("Industry", ["Technology", "Healthcare", "Finance", "Education", "Legal", "Other"])
        product = form.text("What product or service are you working on?")
        market = form.select("Target Market", ["B2B", "B2C", "Enterprise", "Startups", "Mixed"])
        region = form.select("Regional Focus", ["Global", "North America", "Europe", "APAC", "Other"])
        tone = form.select("Preferred Tone", ["Professional", "Conversational", "Technical", "Inspiring"])
        domain = form.select("Post Domain", domains)
        custom_topic = form.textarea("Any specific idea, success, or insight to include?")
        generate = form.submit("🚀 Generate My Post")

    if generate:
        if domain == "Custom Domain...":
            domain = form.text("Enter your custom domain")
        user_context = f"Role: {role}\nIndustry: {industry}\nProduct: {product}\nMarket: {market}\nRegion: {region}\nTone: {tone}\nCustom Input: {custom_topic}"
        prompt = build_prompt(user_context, domain)
        try:
            response = model.generate_content(prompt)
            final_post = response.text.strip()
            html("h3", "✅ Your LinkedIn Post")
            html("textarea", final_post, readonly=True, rows=15)
        except Exception as e:
            html("div", f"❌ Error: {e}", class_="error")

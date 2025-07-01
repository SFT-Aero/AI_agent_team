# UI to select category, signals preference, resource to scrap from
import streamlit as st

st.set_page_config(page_title="Foresight Signal Generator", layout="wide")
st.title("🔮 Foresight Signal Generator")

categories = ["All", "Societal", "Technological", "Economical", "Environmental", "Political", "Threat", "Space"]
selected_categories = st.multiselect("Select Article Categories", categories, default=["All"])
feedback = st.text_input("What kind of signals do you want?", placeholder="e.g., Something more surprising, novel, or optimistic")
num_signals = st.number_input("How many signals do you want?", min_value=1, max_value=10, value=5, step=1)

if st.button("🚀 Generate Signals"):
    st.info("Generating signals based on your preferences...")

    # Scrape and filter
    #raw_articles = scrape_articles(category_filters=selected_categories)

    # CrewAI task logic
    #top_signals = generate_signals(raw_articles, feedback)

    # Display results
    st.subheader("🔍 Top Signals of Future Change")
    #for i, signal in enumerate(top_signals, 1):
        #st.markdown(f"### {i}. {signal['title']}")
        #st.markdown(f"**Category**: {signal['category']}  ")
        #st.markdown(f"**Justification**: {signal['body']}")
        #col1, col2 = st.columns(2)
        #with col1:
            #st.button(f"👍 Useful", key=f"up_{i}")
        #with col2:
            #st.button(f"👎 Not Relevant", key=f"down_{i}")
        #st.markdown("---")
import email
import json
from select import select
import time
from unicodedata import name
import streamlit as st
import requests
import pandas as pd
import datetime as dt

# hide streamlit branding and hamburger menu
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# set today's date and time
curr_time_dec = time.localtime(time.time())
date = time.strftime("%Y-%m-%d", curr_time_dec)

# get learnapp's content data
f = open("content.json")
content_data = json.load(f)
f.close()

# functions for getting user specific course progress
url = "https://68o9pf66q0.execute-api.ap-south-1.amazonaws.com/"
payload = {}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
access_token = response.text

token = "Bearer " + access_token

def fetch_userid(email):
    email = email.replace("@", "%40")
    url = "https://hydra.prod.learnapp.com/kraken/users/search?q=" + email

    payload = {}
    headers = {
        "authorization": token,
        "x-api-key": "u36jbrsUjD8v5hx2zHdZNwqGA6Kz7gsm",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    try:
        data = json.loads(response.text)["users"][0]
        try:
            return data["userId"]
        except:
            return -1
    except:
        return -1


def course_progress(email_id, course_id):
    try:
        user_id = fetch_userid(email_id)
        url = f"https://census.prod.learnapp.com/kraken/users/{user_id}/courses/{course_id}"
        payload = {}
        headers = {
            "authorization": token,
            "x-api-key": "Ch2rqJp3rxH8ZVccQT8ywV7zMR3Ac8fQ",
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        progress = data["courseDetailData"]["percentage"]
    except:
        progress = 0

    return progress


# function for creating the course cards
def course_container(course_key):

    st.subheader(f"📘 {content_data[course_key]['title']}")
    canonical_title = content_data[course_key]["canonicalTitle"]
    course_id = content_data[course_key]["id"]
    progress = course_progress(name, course_id)
    if progress >= 85:
        progress_str = f"✅ {progress}"
    else:
        progress_str = f"📖 {progress}"
    course_url = (
        f"https://learnapp.com/courses/{canonical_title}/topics/trailer?locale=en-us"
    )

    col1, col2 = st.columns(2)
    with col1:
        st.image(
            content_data[course_key]["assetUrl"],
            width=300,
        )

    with col2:

        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.write("")
        st.markdown(
            f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
        )
        st.caption(f"{progress_str}% completed")

    st.write("")


# personalized path function
def create_path(a, b):

    # I just opened my demat account

    if (
        a == "I just opened my demat account"
        and b == "I want to get started with trading"
    ):

        course_key = "basics-of-personal-finance"
        course_container(course_key)

        course_key = "learn-how-capital-markets-work"
        course_container(course_key)

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "intro-to-technical-analysis"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

    elif (
        a == "I just opened my demat account"
        and b == "I want to dive deeper into technical analysis"
    ):

        course_key = "basics-of-personal-finance"
        course_container(course_key)

        course_key = "learn-how-capital-markets-work"
        course_container(course_key)

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "intro-to-technical-analysis"
        course_container(course_key)

        course_key = "support-resistance-"
        course_container(course_key)

        course_key = "single-candlesticks"
        course_container(course_key)

        course_key = "multiple-candlestick-pattern"
        course_container(course_key)

        course_key = "trading-breakouts-and-breakdowns"
        course_container(course_key)

        course_key = "trading-flags-and-pennants"
        course_container(course_key)

        course_key = "reversal-patterns"
        course_container(course_key)

        course_key = "learn-trend-indicators"
        course_container(course_key)

        course_key = "learn-how-trend-trading-works"
        course_container(course_key)

        course_key = "learn-momentum-indicators"
        course_container(course_key)

        course_key = "learn-volume-indicators-"
        course_container(course_key)

    # I just know the basics of stock market

    elif (
        a == "I just know the basics of stock market"
        and b == "I want to get started with trading"
    ):

        course_key = "basics-of-personal-finance"
        course_container(course_key)

        course_key = "learn-how-capital-markets-work"
        course_container(course_key)

        course_key = "intro-to-technical-analysis"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

    elif (
        a == "I just know the basics of stock market"
        and b == "I want to dive deeper into technical analysis"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "intro-to-technical-analysis"
        course_container(course_key)

        course_key = "support-resistance-"
        course_container(course_key)

        course_key = "single-candlesticks"
        course_container(course_key)

        course_key = "multiple-candlestick-pattern"
        course_container(course_key)

        course_key = "trading-breakouts-and-breakdowns"
        course_container(course_key)

        course_key = "trading-flags-and-pennants"
        course_container(course_key)

        course_key = "reversal-patterns"
        course_container(course_key)

        course_key = "learn-trend-indicators"
        course_container(course_key)

        course_key = "learn-how-trend-trading-works"
        course_container(course_key)

        course_key = "learn-momentum-indicators"
        course_container(course_key)

        course_key = "learn-volume-indicators-"
        course_container(course_key)

    elif (
        a == "I just know the basics of stock market"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

        course_key = "price-action-strategy"
        course_container(course_key)

        course_key = "intraday-gap-up-equity-strategy"
        course_container(course_key)

        course_key = "long-term-momentum-strategy"
        course_container(course_key)

        course_key = "bullet-momentum-strategy"
        course_container(course_key)

    # I trade based on my gut feeling

    elif (
        a == "I trade based on my gut feeling"
        and b == "I want to dive deeper into technical analysis"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "intro-to-technical-analysis"
        course_container(course_key)

        course_key = "support-resistance-"
        course_container(course_key)

        course_key = "single-candlesticks"
        course_container(course_key)

        course_key = "multiple-candlestick-pattern"
        course_container(course_key)

        course_key = "trading-breakouts-and-breakdowns"
        course_container(course_key)

        course_key = "trading-flags-and-pennants"
        course_container(course_key)

        course_key = "reversal-patterns"
        course_container(course_key)

        course_key = "learn-trend-indicators"
        course_container(course_key)

        course_key = "learn-how-trend-trading-works"
        course_container(course_key)

        course_key = "learn-momentum-indicators"
        course_container(course_key)

        course_key = "learn-volume-indicators-"
        course_container(course_key)

    elif (
        a == "I trade based on my gut feeling"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

        course_key = "price-action-strategy"
        course_container(course_key)

        course_key = "intraday-gap-up-equity-strategy"
        course_container(course_key)

        course_key = "long-term-momentum-strategy"
        course_container(course_key)

        course_key = "bullet-momentum-strategy"
        course_container(course_key)

    # I know the basics of technical analysis

    elif (
        a == "I know the basics of technical analysis"
        and b == "I want to dive deeper into technical analysis"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "intro-to-technical-analysis"
        course_container(course_key)

        course_key = "support-resistance-"
        course_container(course_key)

        course_key = "single-candlesticks"
        course_container(course_key)

        course_key = "multiple-candlestick-pattern"
        course_container(course_key)

        course_key = "trading-breakouts-and-breakdowns"
        course_container(course_key)

        course_key = "trading-flags-and-pennants"
        course_container(course_key)

        course_key = "reversal-patterns"
        course_container(course_key)

        course_key = "learn-trend-indicators"
        course_container(course_key)

        course_key = "learn-how-trend-trading-works"
        course_container(course_key)

        course_key = "learn-momentum-indicators"
        course_container(course_key)

        course_key = "learn-volume-indicators-"
        course_container(course_key)

    elif (
        a == "I know the basics of technical analysis"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

        course_key = "price-action-strategy"
        course_container(course_key)

        course_key = "intraday-gap-up-equity-strategy"
        course_container(course_key)

        course_key = "long-term-momentum-strategy"
        course_container(course_key)

        course_key = "bullet-momentum-strategy"
        course_container(course_key)

    elif (
        a == "I know the basics of technical analysis"
        and b == "I want to learn how FNO works"
    ):

        course_key = "intro-to-futures-and-options"
        course_container(course_key)

        course_key = "basics-of-options"
        course_container(course_key)

        course_key = "basics-of-options-ii"
        course_container(course_key)

        course_key = "option-spreads-and-option-chain"
        course_container(course_key)

        course_key = "straddles-and-strangles"
        course_container(course_key)

        course_key = "iron-condors-butterfly-and-calendar-spreads"
        course_container(course_key)

    # I trade systematic trading strategies manually

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to dive deeper into technical analysis"
    ):

        course_key = "support-resistance-"
        course_container(course_key)

        course_key = "single-candlesticks"
        course_container(course_key)

        course_key = "multiple-candlestick-pattern"
        course_container(course_key)

        course_key = "trading-breakouts-and-breakdowns"
        course_container(course_key)

        course_key = "trading-flags-and-pennants"
        course_container(course_key)

        course_key = "reversal-patterns"
        course_container(course_key)

        course_key = "learn-trend-indicators"
        course_container(course_key)

        course_key = "learn-how-trend-trading-works"
        course_container(course_key)

        course_key = "learn-momentum-indicators"
        course_container(course_key)

        course_key = "learn-volume-indicators-"
        course_container(course_key)

    elif (
        a == "I trade systematic trading strategies manually"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

        course_key = "price-action-strategy"
        course_container(course_key)

        course_key = "intraday-gap-up-equity-strategy"
        course_container(course_key)

        course_key = "long-term-momentum-strategy"
        course_container(course_key)

        course_key = "bullet-momentum-strategy"
        course_container(course_key)

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to learn how FNO works"
    ):

        course_key = "intro-to-futures-and-options"
        course_container(course_key)

        course_key = "basics-of-options"
        course_container(course_key)

        course_key = "basics-of-options-ii"
        course_container(course_key)

        course_key = "option-spreads-and-option-chain"
        course_container(course_key)

        course_key = "straddles-and-strangles"
        course_container(course_key)

        course_key = "iron-condors-butterfly-and-calendar-spreads"
        course_container(course_key)

    elif (
        a == "I trade systematic trading strategies manually"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        course_key = "banknifty-weekly-options-strategy"
        course_container(course_key)

        course_key = "intraday-banknifty-straddle-strategy"
        course_container(course_key)

        course_key = "intraday-expiry-trading-strategy"
        course_container(course_key)

        course_key = "nifty-hedged-short-strangle"
        course_container(course_key)

        course_key = "index-futures-intraday-strategy"
        course_container(course_key)

        course_key = "intraday-option-buying-strategy"
        course_container(course_key)

        course_key = "positional-banknifty-options-strategy"
        course_container(course_key)

        course_key = "option-buying-momentum-strategy"
        course_container(course_key)

        course_key = "learn-an-options-writing-strategy"
        course_container(course_key)

        course_key = "options-program-with-backtested-strategies"
        course_container(course_key)

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to build my own trading strategy"
    ):

        course_key = "build-your-trading-system"
        course_container(course_key)

        course_key = "basics-of-backtesting"
        course_container(course_key)

        course_key = "amibroker-strategy-development-and-algo-execution"
        course_container(course_key)

    elif (
        a == "I trade systematic trading strategies manually"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        course_key = "trading-podcasts"
        course_container(course_key)

        course_key = "trading-podcast-ii"
        course_container(course_key)

        course_key = "psychology-and-journals"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to learn how to backtest trading strategies"
    ):

        course_key = "basics-of-backtesting"
        course_container(course_key)

        course_key = "trading-and-excel"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "backtesting-stocks-with-indicators---i"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "backtesting-stocks-with-indicators---ii"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = "https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "amibroker-strategy-development-and-algo-execution"
        course_container(course_key)

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to learn how to automate trading strategies"
    ):

        course_key = "amibroker-strategy-development-and-algo-execution"
        course_container(course_key)

        course_key = "python-algo-execution-programme"
        course_container(course_key)

    # I know the basics of futures and options

    elif (
        a == "I know the basics of futures and options"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        course_key = "banknifty-weekly-options-strategy"
        course_container(course_key)

        course_key = "intraday-banknifty-straddle-strategy"
        course_container(course_key)

        course_key = "intraday-expiry-trading-strategy"
        course_container(course_key)

        course_key = "nifty-hedged-short-strangle"
        course_container(course_key)

        course_key = "index-futures-intraday-strategy"
        course_container(course_key)

        course_key = "intraday-option-buying-strategy"
        course_container(course_key)

        course_key = "positional-banknifty-options-strategy"
        course_container(course_key)

        course_key = "option-buying-momentum-strategy"
        course_container(course_key)

        course_key = "learn-an-options-writing-strategy"
        course_container(course_key)

        course_key = "options-program-with-backtested-strategies"
        course_container(course_key)

    elif (
        a == "I know the basics of futures and options"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        course_key = "trading-podcasts"
        course_container(course_key)

        course_key = "trading-podcast-ii"
        course_container(course_key)

        course_key = "psychology-and-journals"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

    # I have my own trading strategy

    elif (
        a == "I have my own trading strategy"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

        course_key = "price-action-strategy"
        course_container(course_key)

        course_key = "intraday-gap-up-equity-strategy"
        course_container(course_key)

        course_key = "long-term-momentum-strategy"
        course_container(course_key)

        course_key = "bullet-momentum-strategy"
        course_container(course_key)

    elif (
        a == "I have my own trading strategy"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        course_key = "banknifty-weekly-options-strategy"
        course_container(course_key)

        course_key = "intraday-banknifty-straddle-strategy"
        course_container(course_key)

        course_key = "intraday-expiry-trading-strategy"
        course_container(course_key)

        course_key = "nifty-hedged-short-strangle"
        course_container(course_key)

        course_key = "index-futures-intraday-strategy"
        course_container(course_key)

        course_key = "intraday-option-buying-strategy"
        course_container(course_key)

        course_key = "positional-banknifty-options-strategy"
        course_container(course_key)

        course_key = "option-buying-momentum-strategy"
        course_container(course_key)

        course_key = "learn-an-options-writing-strategy"
        course_container(course_key)

        course_key = "options-program-with-backtested-strategies"
        course_container(course_key)

    elif (
        a == "I have my own trading strategy"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        course_key = "trading-podcasts"
        course_container(course_key)

        course_key = "trading-podcast-ii"
        course_container(course_key)

        course_key = "psychology-and-journals"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

    elif (
        a == "I have my own trading strategy"
        and b == "I want to learn how to backtest trading strategies"
    ):

        course_key = "basics-of-backtesting"
        course_container(course_key)

        course_key = "trading-and-excel"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "backtesting-stocks-with-indicators---i"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "backtesting-stocks-with-indicators---ii"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = "https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "amibroker-strategy-development-and-algo-execution"
        course_container(course_key)

    elif (
        a == "I have my own trading strategy"
        and b == "I want to learn how to automate trading strategies"
    ):

        course_key = "amibroker-strategy-development-and-algo-execution"
        course_container(course_key)

        course_key = "python-algo-execution-programme"
        course_container(course_key)

    # I know how to backtest trading strategies

    elif (
        a == "I know how to backtest trading strategies"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

        course_key = "price-action-strategy"
        course_container(course_key)

        course_key = "intraday-gap-up-equity-strategy"
        course_container(course_key)

        course_key = "long-term-momentum-strategy"
        course_container(course_key)

        course_key = "bullet-momentum-strategy"
        course_container(course_key)

    elif (
        a == "I know how to backtest trading strategies"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        course_key = "banknifty-weekly-options-strategy"
        course_container(course_key)

        course_key = "intraday-banknifty-straddle-strategy"
        course_container(course_key)

        course_key = "intraday-expiry-trading-strategy"
        course_container(course_key)

        course_key = "nifty-hedged-short-strangle"
        course_container(course_key)

        course_key = "index-futures-intraday-strategy"
        course_container(course_key)

        course_key = "intraday-option-buying-strategy"
        course_container(course_key)

        course_key = "positional-banknifty-options-strategy"
        course_container(course_key)

        course_key = "option-buying-momentum-strategy"
        course_container(course_key)

        course_key = "learn-an-options-writing-strategy"
        course_container(course_key)

        course_key = "options-program-with-backtested-strategies"
        course_container(course_key)

    elif (
        a == "I know how to backtest trading strategies"
        and b == "I want to build my own trading strategy"
    ):

        course_key = "build-your-trading-system"
        course_container(course_key)

    elif (
        a == "I know how to backtest trading strategies"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        course_key = "trading-podcasts"
        course_container(course_key)

        course_key = "trading-podcast-ii"
        course_container(course_key)

        course_key = "psychology-and-journals"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

    elif (
        a == "I know how to backtest trading strategies"
        and b == "I want to learn how to automate trading strategies"
    ):

        course_key = "amibroker-strategy-development-and-algo-execution"
        course_container(course_key)

        course_key = "python-algo-execution-programme"
        course_container(course_key)

    # I know how to automate trading strategies

    elif (
        a == "I know how to automate trading strategies"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        course_key = "basics-of-trading"
        course_container(course_key)

        course_key = "learn-intraday-strategy"
        course_container(course_key)

        course_key = "price-action-strategy"
        course_container(course_key)

        course_key = "intraday-gap-up-equity-strategy"
        course_container(course_key)

        course_key = "long-term-momentum-strategy"
        course_container(course_key)

        course_key = "bullet-momentum-strategy"
        course_container(course_key)

    elif (
        a == "I know how to automate trading strategies"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        course_key = "banknifty-weekly-options-strategy"
        course_container(course_key)

        course_key = "intraday-banknifty-straddle-strategy"
        course_container(course_key)

        course_key = "intraday-expiry-trading-strategy"
        course_container(course_key)

        course_key = "nifty-hedged-short-strangle"
        course_container(course_key)

        course_key = "index-futures-intraday-strategy"
        course_container(course_key)

        course_key = "intraday-option-buying-strategy"
        course_container(course_key)

        course_key = "positional-banknifty-options-strategy"
        course_container(course_key)

        course_key = "option-buying-momentum-strategy"
        course_container(course_key)

        course_key = "learn-an-options-writing-strategy"
        course_container(course_key)

        course_key = "options-program-with-backtested-strategies"
        course_container(course_key)

    elif (
        a == "II know how to automate trading strategies"
        and b == "I want to build my own trading strategy"
    ):

        course_key = "build-your-trading-system"
        course_container(course_key)

    elif (
        a == "I know how to automate trading strategies"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        course_key = "trading-podcasts"
        course_container(course_key)

        course_key = "trading-podcast-ii"
        course_container(course_key)

        course_key = "psychology-and-journals"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

    elif (
        a == "I know how to automate trading strategies"
        and b == "I want to learn how to backtest trading strategies"
    ):

        course_key = "basics-of-backtesting"
        course_container(course_key)

        course_key = "trading-and-excel"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "backtesting-stocks-with-indicators---i"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = f"https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "backtesting-stocks-with-indicators---ii"
        st.subheader(f"📘 {content_data[course_key]['title']}")
        canonical_title = content_data[course_key]["canonicalTitle"]
        course_id = content_data[course_key]["id"]
        progress = course_progress(name, course_id)
        if progress == 100:
            progress = f"✅ {progress}"
        else:
            progress = f"📖 {progress}"
        course_url = "https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands?locale=en-us"

        col1, col2 = st.columns(2)
        with col1:
            st.image(
                content_data[course_key]["assetUrl"],
                width=300,
            )

        with col2:

            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.markdown(
                f"[![Play Now](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-15-nov-22-la-announcement-akriti-singh/5e7bcdd4-039a-4a0f-a255-7c48d3993eaa.png)]({course_url})"
            )
            st.caption(f"{progress}% completed")

        st.write("")

        course_key = "amibroker-strategy-development-and-algo-execution"
        course_container(course_key)


col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.image("logo.png", width=225)
    st.write("")
with col3:
    st.write("")


st.subheader("Want to make the most of your LearnApp Subscription? ")
st.write(
    "🎯 Use this tool to create your personalized learning path to help you reach your trading goals in the next 30 days"
)
st.write("-----")

name = (
    (
        st.text_input(
            "Enter your LearnApp Registered Email Address",
            help="We use your email address to track progress",
        )
    )
    .strip()
    .lower()
)
st.write("")

tab1, tab2 = st.tabs(["Create New Learning Path", "My saved Learning Paths"])
st.write("-----")

with tab1:
    st.write("")
    a = st.selectbox(
        "Where I Stand?",
        (
            "I just opened my demat account",
            "I just know the basics of stock market",
            "I trade based on my gut feeling",
            "I know the basics of technical analysis",
            "I trade systematic trading strategies manually",
            "I know the basics of futures and options",
            "I have my own trading strategy",
            "I know how to backtest trading strategies",
            "I know how to automate trading strategies",
        ),
    )

    if a == "I just opened my demat account":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want to get started with trading",
                "I want to dive deeper into technical analysis",
            ),
        )

    elif a == "I just know the basics of stock market":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want to get started with trading",
                "I want to dive deeper into technical analysis",
                "I want trading strategies that will help me become a profitable trader",
            ),
        )

    elif a == "I trade based on my gut feeling":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want to dive deeper into technical analysis",
                "I want trading strategies that will help me become a profitable trader",
            ),
        )

    elif a == "I know the basics of technical analysis":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want to dive deeper into technical analysis",
                "I want trading strategies that will help me become a profitable trader",
                "I want to learn how FNO works",
            ),
        )

    elif a == "I trade systematic trading strategies manually":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want to dive deeper into technical analysis",
                "I want trading strategies that will help me become a profitable trader",
                "I want to learn how FNO works",
                "I want FNO trading strategies that will help me become a profitable trader",
                "I want to build my own trading strategy",
                "I want to get better at managing my risks and psychology during trading",
                "I want to learn how to backtest trading strategies",
                "I want to learn how to automate trading strategies",
            ),
        )

    elif a == "I know the basics of futures and options":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want FNO trading strategies that will help me become a profitable trader",
                "I want to get better at managing my risks and psychology during trading",
            ),
        )

    elif a == "I have my own trading strategy":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want trading strategies that will help me become a profitable trader",
                "I want FNO trading strategies that will help me become a profitable trader",
                "I want to get better at managing my risks and psychology during trading",
                "I want to learn how to backtest trading strategies",
                "I want to learn how to automate trading strategies",
            ),
        )

    elif a == "I know how to backtest trading strategies":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want trading strategies that will help me become a profitable trader",
                "I want FNO trading strategies that will help me become a profitable trader",
                "I want to build my own trading strategy",
                "I want to get better at managing my risks and psychology during trading",
                "I want to learn how to automate trading strategies",
            ),
        )

    elif a == "I know how to automate trading strategies":
        st.write("")
        b = st.selectbox(
            "What I want to achieve?",
            (
                "I want trading strategies that will help me become a profitable trader",
                "I want FNO trading strategies that will help me become a profitable trader",
                "I want to build my own trading strategy",
                "I want to get better at managing my risks and psychology during trading",
                "I want to learn how to backtest trading strategies",
            ),
        )

    st.write("")
    c = "just checking"
    commit = st.checkbox(
        "I Commit to completing the courses in the next 30 days (optional)"
    )
    if commit:
        st.write("")

        if b == "I want to get started with trading":
            c = "Get started with trading"

        elif b == "I want to dive deeper into technical analysis":
            c = "Learn Technical Analysis"

        elif (
            b
            == "I want trading strategies that will help me become a profitable trader"
        ):
            c = "Equity Trading Strategies"

        elif b == "I want to learn how FNO works":
            c = "Learn FNO Basics"

        elif (
            b
            == "I want FNO trading strategies that will help me become a profitable trader"
        ):
            c = "FNO Trading Strategies"

        elif b == "I want to build my own trading strategy":
            c = "Build my strategy"

        elif (
            b
            == "I want to get better at managing my risks and psychology during trading"
        ):
            c = "Improve risk management and psychology"

        elif b == "I want to learn how to backtest trading strategies":
            c = "Learn Backtesting"

        elif b == "I want to learn how to automate trading strategies":
            c = "Learn Automation"

        # c = st.text_input(
        #     "Name your Learning Path (ex: Learn Technical Anlaysis, Learn FNO, Learn Algo)",
        #     help="Make sure you use different name for different Learning Paths",
        # )

    st.write("")

    if st.button(
        "Create my Learning Path",
        help="Learning Path is a collection of courses on LearnApp which you need to complete step by step to achieve your trading goals",
    ):

        if name == "":
            st.error("Please enter a valid email ID")
        elif c == "":
            st.error("Please enter the name of your learning path")

        else:
            with st.spinner("Creating Learning Path for you"):

                if commit:
                    # store data in database
                    url_email = (
                        "https://3749e8lxlf.execute-api.ap-south-1.amazonaws.com/"
                    )
                    payload_email = {
                        "query_date": date,
                        "tool_name": "tool-learnapp-course-recommendation",
                        "Name": name,
                        "where_i_stand": a,
                        "where_i_want_to_be": b,
                        "lp_name": c,
                    }
                    headers_email = {"Content-Type": "text/plain"}
                    response = requests.request(
                        "POST",
                        url_email,
                        headers=headers_email,
                        data=json.dumps(payload_email),
                    )
                st.write("-----")
                st.subheader("🚀 Your Personalized Learning Path")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write("Need help completing this learning path?")
                with col2:
                    st.subheader("➡➡➡➡➡➡➡")
                with col3:
                    st.markdown(
                        "[![Join our club](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-14-oct-22-la-announcement-ahmad-qureshi/e4a09bb4-2e6d-4ec4-8b94-34011ca24f2e.png)](https://join.slack.com/t/learnappsubscribers/shared_invite/zt-1j944zbnr-2rbea2tVYJJF_gNTOoq9Bg)"
                    )
                st.write("-----")
                create_path(a, b)

    with tab2:
        with st.spinner("Loading your Learning Path"):
            st.write("")
            # fetch user's learning paths
            try:
                url_path = (
                    "https://3749e8lxlf.execute-api.ap-south-1.amazonaws.com/paths"
                )
                payload_path = {"Name": name}
                headers_path = {"Content-Type": "text/plain"}
                response = requests.request(
                    "GET",
                    url_path,
                    headers=headers_path,
                    data=json.dumps(payload_path),
                )

                data = json.loads(response.text)
                learning_paths = [i["lp_name"] for i in data]

                selected_path = st.selectbox(
                    "Choose one of your committed learning paths",
                    learning_paths,
                    help="Learning Path is a collection of courses on LearnApp which you need to complete step by step to achieve your trading goals",
                )
                st.write("-----")

                a1 = [i["where_i_stand"] for i in data if i["lp_name"] == selected_path]
                b1 = [
                    i["where_i_want_to_be"]
                    for i in data
                    if i["lp_name"] == selected_path
                ]
                if selected_path != None:
                    st.subheader("🚀 Your Personalized Learning Path")
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.write("Need help completing this learning path?")
                    with col2:
                        st.subheader("➡➡➡➡➡➡➡")
                    with col3:
                        st.markdown(
                            "[![Join our club](https://s3.ap-south-1.amazonaws.com/messenger.prod.learnapp.com/emails/newsLetters-14-oct-22-la-announcement-ahmad-qureshi/e4a09bb4-2e6d-4ec4-8b94-34011ca24f2e.png)](https://join.slack.com/t/learnappsubscribers/shared_invite/zt-1j944zbnr-2rbea2tVYJJF_gNTOoq9Bg)"
                        )
                    st.write("-----")
                    create_path(a1[0], b1[0])
            except:
                st.error("You haven't created any Learning Paths yet!")


# Admin dashboard
if name == "product@learnapp.com":

    # check if token expired or not
    if fetch_userid(name) == -1:
        st.error("token expired")
    else:
        st.success("token is fine!")

    # function to get all users data
    def get_all_data():
        url = "https://6tdvr200th.execute-api.ap-south-1.amazonaws.com/"

        payload = {}

        headers = {"Content-Type": "text/plain"}

        response = requests.request(
            "GET",
            url,
            headers=headers,
            data=json.dumps(payload),
        )

        data = json.loads(response.text)

        return data

    # visalization
    def color_survived(val):

        if float(val) >= 0 and float(val) < 25:
            color = "#FF0000"

        elif float(val) >= 25 and float(val) < 50:
            color = "#ff9900"

        elif float(val) >= 50 and float(val) < 75:
            color = "#FFCC00"

        elif float(val) >= 75 and float(val) < 100:
            color = "#00FF00"

        return f"color: {color}"

    expt_day = (dt.datetime.today() - dt.datetime(2022, 11, 14)).days
    st.header(f"Course Recommendation Experiment Day {expt_day}")

    curr_date = dt.date.today().strftime("%Y-%m-%d")
    data = get_all_data()
    df = pd.DataFrame(data)

    df["total_courses"] = df["total_courses"].astype(str)
    df["completed_courses"] = df["completed_courses"].astype(str)

    df["completed/total"] = df["completed_courses"] + "/" + df["total_courses"]
    df.dropna(inplace=True)

    df["lp_progress_%"] = df["learning_path_progress"].apply(
        lambda x: str(round(x[list(x.keys())[-1]], 2))
    )

    metric_df = df[df["user_type"] == "Paid User"]
    metric_df = metric_df[
        ["Name", "lp_name", "completed/total", "lp_progress_%", "phone_number"]
    ]

    percentile_25 = metric_df[
        (metric_df["lp_progress_%"].astype(float) >= 0)
        & (metric_df["lp_progress_%"].astype(float) < 25)
    ].shape[0]

    percentile_50 = metric_df[
        (metric_df["lp_progress_%"].astype(float) >= 25)
        & (metric_df["lp_progress_%"].astype(float) < 50)
    ].shape[0]

    percentile_85 = metric_df[
        (metric_df["lp_progress_%"].astype(float) >= 50)
        & (metric_df["lp_progress_%"].astype(float) < 85)
    ].shape[0]

    percentile_100 = metric_df[
        (metric_df["lp_progress_%"].astype(float) >= 85)
        & (metric_df["lp_progress_%"].astype(float) <= 100)
    ].shape[0]

    st.write("-----")
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Learning Paths", value=metric_df.shape[0])
    col2.metric("Total Unique Users", value=metric_df["Name"].nunique())
    col3.metric("Success %", round((percentile_100 / metric_df.shape[0]) * 100, 2))
    col4.metric(
        "Success Users",
        value=metric_df[
            (metric_df["lp_progress_%"].astype(float) >= 85)
            & (metric_df["lp_progress_%"].astype(float) <= 100)
        ]["Name"].nunique(),
    )

    st.write("-----")

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("25th percentile", value=percentile_25)
    col2.metric("50th percentile", value=percentile_50)
    col3.metric("85th percentile", value=percentile_85)
    col4.metric("100th percentile", value=percentile_100)
    st.write("-----")

    st.dataframe(metric_df.style.applymap(color_survived, subset=["lp_progress_%"]))

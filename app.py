import email
import json
from select import select
import time
from unicodedata import name
import streamlit as st
import requests

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

# custom path function
def create_path(a, b):

    # I just opened my demat account

    if (
        a == "I just opened my demat account"
        and b == "I want to get started with trading"
    ):

        st.subheader("1. Basics of Personal Finance")
        st.markdown(
            "[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Personal+Finance.jpeg)](https://learnapp.com/courses/basics-of-personal-finance/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn How Capital Market Works")
        st.markdown(
            "[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Capital+Market+Works.jpeg)](https://learnapp.com/courses/learn-how-capital-markets-work/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intro to technical Analysis")
        st.markdown(
            "[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I just opened my demat account"
        and b == "I want to learn trading from scratch"
    ):

        st.subheader("1. Basics of Personal Finance")
        st.markdown(
            "[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Personal+Finance.jpeg)](https://learnapp.com/courses/basics-of-personal-finance/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn How Capital Market Works")
        st.markdown(
            "[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Capital+Market+Works.jpeg)](https://learnapp.com/courses/learn-how-capital-markets-work/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intro to technical Analysis")
        st.markdown(
            "[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    # I just know the basics of stock market

    elif (
        a == "I just know the basics of stock market"
        and b == "I want to get started with trading"
    ):

        st.subheader("1. Basics of Personal Finance")
        st.markdown(
            "[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Personal+Finance.jpeg)](https://learnapp.com/courses/basics-of-personal-finance/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Intro to technical Analysis")
        st.markdown(
            "[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I just know the basics of stock market"
        and b == "I want to dive deeper into technical analysis"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intro to technical Analysis")
        st.markdown(
            "[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Support and Resistance")
        st.markdown(
            "[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Single Candlesticks")
        st.markdown(
            "[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Multiple Candlestick Pattern")
        st.markdown(
            "[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Trading Breakouts and Breakdowns")
        st.markdown(
            "[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Trading Flags and Pennants")
        st.markdown(
            "[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Reversal Patterns")
        st.markdown(
            "[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn Trend Indicators")
        st.markdown(
            "[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Learn How Trend Trading Works")
        st.markdown(
            "[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("11. Learn Momentum Indicators")
        st.markdown(
            "[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("12. Learn Volume Indicators")
        st.markdown(
            "[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I just know the basics of stock market"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Price Action Strategy")
        st.markdown(
            "[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intraday Gapup Equity Strategy")
        st.markdown(
            "[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Long Term Momentum Strategy")
        st.markdown(
            "[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Bullet Momentum Strategy")
        st.markdown(
            "[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    # I trade based on my gut feeling

    elif (
        a == "I trade based on my gut feeling"
        and b == "I want to dive deeper into technical analysis"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intro to technical Analysis")
        st.markdown(
            "[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Support and Resistance")
        st.markdown(
            "[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Single Candlesticks")
        st.markdown(
            "[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Multiple Candlestick Pattern")
        st.markdown(
            "[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Trading Breakouts and Breakdowns")
        st.markdown(
            "[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Trading Flags and Pennants")
        st.markdown(
            "[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Reversal Patterns")
        st.markdown(
            "[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn Trend Indicators")
        st.markdown(
            "[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Learn How Trend Trading Works")
        st.markdown(
            "[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("11. Learn Momentum Indicators")
        st.markdown(
            "[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("12. Learn Volume Indicators")
        st.markdown(
            "[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade based on my gut feeling"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Price Action Strategy")
        st.markdown(
            "[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intraday Gapup Equity Strategy")
        st.markdown(
            "[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Long Term Momentum Strategy")
        st.markdown(
            "[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Bullet Momentum Strategy")
        st.markdown(
            "[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    # I know the basics of technical analysis

    elif (
        a == "I know the basics of technical analysis"
        and b == "I want to dive deeper into technical analysis"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intro to technical Analysis")
        st.markdown(
            "[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Support and Resistance")
        st.markdown(
            "[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Single Candlesticks")
        st.markdown(
            "[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Multiple Candlestick Pattern")
        st.markdown(
            "[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Trading Breakouts and Breakdowns")
        st.markdown(
            "[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Trading Flags and Pennants")
        st.markdown(
            "[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Reversal Patterns")
        st.markdown(
            "[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn Trend Indicators")
        st.markdown(
            "[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Learn How Trend Trading Works")
        st.markdown(
            "[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("11. Learn Momentum Indicators")
        st.markdown(
            "[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("12. Learn Volume Indicators")
        st.markdown(
            "[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know the basics of technical analysis"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Price Action Strategy")
        st.markdown(
            "[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intraday Gapup Equity Strategy")
        st.markdown(
            "[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Long Term Momentum Strategy")
        st.markdown(
            "[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Bullet Momentum Strategy")
        st.markdown(
            "[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know the basics of technical analysis"
        and b == "I want to learn how FNO works"
    ):

        st.subheader("1. Intro to Futures and Options")
        st.markdown(
            "[![Intro to Futures and Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Futures+and+Options.jpeg)](https://learnapp.com/courses/intro-to-futures-and-options/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Basics of Options")
        st.markdown(
            "[![Basics of Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options.jpeg)](https://learnapp.com/courses/basics-of-options/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Basics of Options II")
        st.markdown(
            "[![Basics of Options II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options+II.jpeg)](https://learnapp.com/courses/basics-of-options-ii/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Option Spreads and Option Chain")
        st.markdown(
            "[![Option Spreads and Option Chain](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Spreads+and+Option+Chain.jpeg)](https://learnapp.com/courses/option-spreads-and-option-chain/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Straddles and Strangles")
        st.markdown(
            "[![Straddles and Strangles](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Straddles+and+Strangles.jpeg)](https://learnapp.com/courses/straddles-and-strangles/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Iron Condors, Butterfly and Calendar Spreads")
        st.markdown(
            "[![Iron Condors, Butterfly and Calendar Spreads](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Iron+Condors%2C+Butterfly+and+Calendar+Spreads.jpeg)](https://learnapp.com/courses/iron-condors-butterfly-and-calendar-spreads/topics/trailer?locale=en-us)"
        )
        st.write("")

    # I trade systematic trading strategies manually

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to dive deeper into technical analysis"
    ):

        st.subheader("1. Support and Resistance")
        st.markdown(
            "[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Single Candlesticks")
        st.markdown(
            "[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Multiple Candlestick Pattern")
        st.markdown(
            "[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Trading Breakouts and Breakdowns")
        st.markdown(
            "[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Trading Flags and Pennants")
        st.markdown(
            "[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Reversal Patterns")
        st.markdown(
            "[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Learn Trend Indicators")
        st.markdown(
            "[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Learn How Trend Trading Works")
        st.markdown(
            "[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn Momentum Indicators")
        st.markdown(
            "[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Learn Volume Indicators")
        st.markdown(
            "[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Price Action Strategy")
        st.markdown(
            "[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intraday Gapup Equity Strategy")
        st.markdown(
            "[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Long Term Momentum Strategy")
        st.markdown(
            "[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Bullet Momentum Strategy")
        st.markdown(
            "[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to learn how FNO works"
    ):

        st.subheader("1. Intro to Futures and Options")
        st.markdown(
            "[![Intro to Futures and Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Futures+and+Options.jpeg)](https://learnapp.com/courses/intro-to-futures-and-options/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Basics of Options")
        st.markdown(
            "[![Basics of Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options.jpeg)](https://learnapp.com/courses/basics-of-options/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Basics of Options II")
        st.markdown(
            "[![Basics of Options II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options+II.jpeg)](https://learnapp.com/courses/basics-of-options-ii/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Option Spreads and Option Chain")
        st.markdown(
            "[![Option Spreads and Option Chain](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Spreads+and+Option+Chain.jpeg)](https://learnapp.com/courses/option-spreads-and-option-chain/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Straddles and Strangles")
        st.markdown(
            "[![Straddles and Strangles](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Straddles+and+Strangles.jpeg)](https://learnapp.com/courses/straddles-and-strangles/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Iron Condors, Butterfly and Calendar Spreads")
        st.markdown(
            "[![Iron Condors, Butterfly and Calendar Spreads](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Iron+Condors%2C+Butterfly+and+Calendar+Spreads.jpeg)](https://learnapp.com/courses/iron-condors-butterfly-and-calendar-spreads/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. BankNifty Weekly Options Strategy")
        st.markdown(
            "[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intraday Banknifty Straddle Strategy")
        st.markdown(
            "[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Intraday Expiry Trading Strategy")
        st.markdown(
            "[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Nifty Hedged Short Strangle")
        st.markdown(
            "[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Index Futures Intraday Strategy")
        st.markdown(
            "[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Intraday Option Buying Strategy")
        st.markdown(
            "[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Positional Banknifty Options Stratgey")
        st.markdown(
            "[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Option Buying Momentum Strategy")
        st.markdown(
            "[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn an Options Writing Strategy")
        st.markdown(
            "[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Options Program with Backtested Strategies")
        st.markdown(
            "[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to build my own trading strategy"
    ):

        st.subheader("1. Build Your Trading System")
        st.markdown(
            "[![Build Your Trading System](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Build+Your+Trading+System.jpeg)](https://learnapp.com/courses/build-your-trading-system/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Basics of Backtesting")
        st.markdown(
            "[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Amibroker Strategy Development and Algo Execution")
        st.markdown(
            "[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        st.subheader("1. Trading Podcasts")
        st.markdown(
            "[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading Podcast II")
        st.markdown(
            "[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Psychology and Journals")
        st.markdown(
            "[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to learn how to backtest trading strategies"
    ):

        st.subheader("1. Basics of Backtesting")
        st.markdown(
            "[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading and Excel")
        st.markdown(
            "[![Trading and Excel](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+and+Excel.jpg)](https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Backtesting Stocks with Indicators - I")
        st.markdown(
            "[![Backtesting Stocks with Indicators - I](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+I.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Backtesting Stocks with Indicators - II")
        st.markdown(
            "[![Backtesting Stocks with Indicators - II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+II.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Amibroker Strategy Development and Algo Execution")
        st.markdown(
            "[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I trade systematic trading strategies manually"
        and b == "I want to learn how to automate trading strategies"
    ):

        st.subheader("1. Amibroker Strategy Development and Algo Execution")
        st.markdown(
            "[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Python Algo Execution Programme")
        st.markdown(
            "[![Python Algo Execution Programme](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Python+Algo+Execution+Programme.jpg)](https://learnapp.com/advanced-courses/python-algo-execution-programme?locale=en-us)"
        )
        st.write("")

    # I know the basics of futures and options

    elif (
        a == "I know the basics of futures and options"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. BankNifty Weekly Options Strategy")
        st.markdown(
            "[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intraday Banknifty Straddle Strategy")
        st.markdown(
            "[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Intraday Expiry Trading Strategy")
        st.markdown(
            "[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Nifty Hedged Short Strangle")
        st.markdown(
            "[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Index Futures Intraday Strategy")
        st.markdown(
            "[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Intraday Option Buying Strategy")
        st.markdown(
            "[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Positional Banknifty Options Stratgey")
        st.markdown(
            "[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Option Buying Momentum Strategy")
        st.markdown(
            "[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn an Options Writing Strategy")
        st.markdown(
            "[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Options Program with Backtested Strategies")
        st.markdown(
            "[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know the basics of futures and options"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        st.subheader("1. Trading Podcasts")
        st.markdown(
            "[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading Podcast II")
        st.markdown(
            "[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Psychology and Journals")
        st.markdown(
            "[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us)"
        )
        st.write("")

    # I have my own trading strategy

    elif (
        a == "I have my own trading strategy"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Price Action Strategy")
        st.markdown(
            "[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intraday Gapup Equity Strategy")
        st.markdown(
            "[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Long Term Momentum Strategy")
        st.markdown(
            "[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Bullet Momentum Strategy")
        st.markdown(
            "[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I have my own trading strategy"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. BankNifty Weekly Options Strategy")
        st.markdown(
            "[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intraday Banknifty Straddle Strategy")
        st.markdown(
            "[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Intraday Expiry Trading Strategy")
        st.markdown(
            "[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Nifty Hedged Short Strangle")
        st.markdown(
            "[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Index Futures Intraday Strategy")
        st.markdown(
            "[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Intraday Option Buying Strategy")
        st.markdown(
            "[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Positional Banknifty Options Stratgey")
        st.markdown(
            "[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Option Buying Momentum Strategy")
        st.markdown(
            "[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn an Options Writing Strategy")
        st.markdown(
            "[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Options Program with Backtested Strategies")
        st.markdown(
            "[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I have my own trading strategy"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        st.subheader("1. Trading Podcasts")
        st.markdown(
            "[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading Podcast II")
        st.markdown(
            "[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Psychology and Journals")
        st.markdown(
            "[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I have my own trading strategy"
        and b == "I want to learn how to backtest trading strategies"
    ):

        st.subheader("1. Basics of Backtesting")
        st.markdown(
            "[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading and Excel")
        st.markdown(
            "[![Trading and Excel](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+and+Excel.jpg)](https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Backtesting Stocks with Indicators - I")
        st.markdown(
            "[![Backtesting Stocks with Indicators - I](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+I.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Backtesting Stocks with Indicators - II")
        st.markdown(
            "[![Backtesting Stocks with Indicators - II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+II.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Amibroker Strategy Development and Algo Execution")
        st.markdown(
            "[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I have my own trading strategy"
        and b == "I want to learn how to automate trading strategies"
    ):

        st.subheader("1. Amibroker Strategy Development and Algo Execution")
        st.markdown(
            "[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Python Algo Execution Programme")
        st.markdown(
            "[![Python Algo Execution Programme](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Python+Algo+Execution+Programme.jpg)](https://learnapp.com/advanced-courses/python-algo-execution-programme?locale=en-us)"
        )
        st.write("")

    # I know how to backtest trading strategies

    elif (
        a == "I know how to backtest trading strategies"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Price Action Strategy")
        st.markdown(
            "[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intraday Gapup Equity Strategy")
        st.markdown(
            "[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Long Term Momentum Strategy")
        st.markdown(
            "[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Bullet Momentum Strategy")
        st.markdown(
            "[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know how to backtest trading strategies"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. BankNifty Weekly Options Strategy")
        st.markdown(
            "[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intraday Banknifty Straddle Strategy")
        st.markdown(
            "[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Intraday Expiry Trading Strategy")
        st.markdown(
            "[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Nifty Hedged Short Strangle")
        st.markdown(
            "[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Index Futures Intraday Strategy")
        st.markdown(
            "[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Intraday Option Buying Strategy")
        st.markdown(
            "[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Positional Banknifty Options Stratgey")
        st.markdown(
            "[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Option Buying Momentum Strategy")
        st.markdown(
            "[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn an Options Writing Strategy")
        st.markdown(
            "[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Options Program with Backtested Strategies")
        st.markdown(
            "[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know how to backtest trading strategies"
        and b == "I want to build my own trading strategy"
    ):

        st.subheader("1. Build Your Trading System")
        st.markdown(
            "[![Build Your Trading System](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Build+Your+Trading+System.jpeg)](https://learnapp.com/courses/build-your-trading-system/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know how to backtest trading strategies"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        st.subheader("1. Trading Podcasts")
        st.markdown(
            "[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading Podcast II")
        st.markdown(
            "[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Psychology and Journals")
        st.markdown(
            "[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know how to backtest trading strategies"
        and b == "I want to learn how to automate trading strategies"
    ):

        st.subheader("1. Amibroker Strategy Development and Algo Execution")
        st.markdown(
            "[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Python Algo Execution Programme")
        st.markdown(
            "[![Python Algo Execution Programme](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Python+Algo+Execution+Programme.jpg)](https://learnapp.com/advanced-courses/python-algo-execution-programme?locale=en-us)"
        )
        st.write("")

    # I know how to automate trading strategies

    elif (
        a == "I know how to automate trading strategies"
        and b
        == "I want trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. Basics of Trading")
        st.markdown(
            "[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Learn Intraday Strategy")
        st.markdown(
            "[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Price Action Strategy")
        st.markdown(
            "[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Intraday Gapup Equity Strategy")
        st.markdown(
            "[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Long Term Momentum Strategy")
        st.markdown(
            "[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Bullet Momentum Strategy")
        st.markdown(
            "[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know how to automate trading strategies"
        and b
        == "I want FNO trading strategies that will help me become a profitable trader"
    ):

        st.subheader("1. BankNifty Weekly Options Strategy")
        st.markdown(
            "[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Intraday Banknifty Straddle Strategy")
        st.markdown(
            "[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Intraday Expiry Trading Strategy")
        st.markdown(
            "[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Nifty Hedged Short Strangle")
        st.markdown(
            "[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Index Futures Intraday Strategy")
        st.markdown(
            "[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("6. Intraday Option Buying Strategy")
        st.markdown(
            "[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("7. Positional Banknifty Options Stratgey")
        st.markdown(
            "[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("8. Option Buying Momentum Strategy")
        st.markdown(
            "[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("9. Learn an Options Writing Strategy")
        st.markdown(
            "[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("10. Options Program with Backtested Strategies")
        st.markdown(
            "[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies?locale=en-us)"
        )
        st.write("")

    elif (
        a == "II know how to automate trading strategies"
        and b == "I want to build my own trading strategy"
    ):

        st.subheader("1. Build Your Trading System")
        st.markdown(
            "[![Build Your Trading System](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Build+Your+Trading+System.jpeg)](https://learnapp.com/courses/build-your-trading-system/topics/trailer?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know how to automate trading strategies"
        and b
        == "I want to get better at managing my risks and psychology during trading"
    ):

        st.subheader("1. Trading Podcasts")
        st.markdown(
            "[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading Podcast II")
        st.markdown(
            "[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Psychology and Journals")
        st.markdown(
            "[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1?locale=en-us)"
        )
        st.write("")

    elif (
        a == "I know how to automate trading strategies"
        and b == "I want to learn how to backtest trading strategies"
    ):

        st.subheader("1. Basics of Backtesting")
        st.markdown(
            "[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer?locale=en-us)"
        )
        st.write("")

        st.subheader("2. Trading and Excel")
        st.markdown(
            "[![Trading and Excel](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+and+Excel.jpg)](https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel?locale=en-us)"
        )
        st.write("")

        st.subheader("3. Backtesting Stocks with Indicators - I")
        st.markdown(
            "[![Backtesting Stocks with Indicators - I](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+I.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi?locale=en-us)"
        )
        st.write("")

        st.subheader("4. Backtesting Stocks with Indicators - II")
        st.markdown(
            "[![Backtesting Stocks with Indicators - II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+II.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands?locale=en-us)"
        )
        st.write("")

        st.subheader("5. Amibroker Strategy Development and Algo Execution")
        st.markdown(
            "[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution?locale=en-us)"
        )
        st.write("")


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
name = st.text_input(
    "Enter your LearnApp Registered Email Address",
    help="We use your email address to track progress",
)
st.write("")

# feature = st.radio(
#     "What do you want to do?",
#     ("create new learning path", "my commited learning path"),
# )
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
                "I want to learn trading from scratch",
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
        c = st.text_input(
            "Name your Learning Path (ex: Learn Technical Anlaysis, Learn FNO, Learn Algo)",
            help="Make sure you use different name for different Learning Paths",
        )

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
                time.sleep(1.5)

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
        st.write("")
        # fetch user's learning paths
        try:
            url_path = "https://3749e8lxlf.execute-api.ap-south-1.amazonaws.com/paths"
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
                i["where_i_want_to_be"] for i in data if i["lp_name"] == selected_path
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

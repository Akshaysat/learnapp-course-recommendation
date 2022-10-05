import json
from select import select
import time
import streamlit as st
import requests

#set today's date and time
curr_time_dec = time.localtime(time.time())
date = time.strftime("%Y-%m-%d", curr_time_dec)

st.title("Find courses on LearnApp that will help you achieve your goals 🎯")

name = st.text_input("What's your name?")

a = st.selectbox("Where I Stand?",("I just opened my demat account and I don’t know how stock market works",
                                                "I just know the basics of stock market",
                                                "I trade based on my gut feeling",
                                                "I know the basics of technical analysis",
                                                "I trade systematic trading strategies manually",
                                                "I know the basics of futures and options",
                                                "I have my own trading strategy",
                                                "I know how to backtest trading strategies",
                                                "I know how to automate trading strategies"))

if a == "I just opened my demat account and I don’t know how stock market works":
    b = st.selectbox("Where I want to be?", ("I want to get started with trading", "I want to learn trading from scratch"))

elif a == "I just know the basics of stock market":
    b = st.selectbox("Where I want to be?",("I want to get started with trading",
                                            "I want to dive deeper into technical analysis",
                                            "I want trading strategies that will help me become a profitable trader"))

elif a == "I trade based on my gut feeling":
    b = st.selectbox("Where I want to be?", ("I want to dive deeper into technical analysis",
                                            "I want trading strategies that will help me become a profitable trader"))

elif a == "I know the basics of technical analysis":
    b = st.selectbox("Where I want to be?",("I want to dive deeper into technical analysis",
                                            "I want trading strategies that will help me become a profitable trader",
                                            "I want to learn how FNO works"))

elif a == "I trade systematic trading strategies manually":
    b = st.selectbox("Where I want to be?", ("I want to dive deeper into technical analysis",
                                            "I want trading strategies that will help me become a profitable trader",
                                            "I want to learn how FNO works",
                                            "I want FNO trading strategies that will help me become a profitable trader",
                                            "I want to build my own trading strategy",
                                            "I want to get better at managing my risks and psychology during trading",
                                            "I want to learn how to backtest trading strategies",
                                            "I want to learn how to automate trading strategies"))

elif a == "I know the basics of futures and options":
    b = st.selectbox("Where I want to be?", ("I want FNO trading strategies that will help me become a profitable trader",
                                            "I want to get better at managing my risks and psychology during trading"))

elif a == "I have my own trading strategy":
    b = st.selectbox("Where I want to be?", ("I want trading strategies that will help me become a profitable trader",
                                            "I want FNO trading strategies that will help me become a profitable trader",
                                            "I want to get better at managing my risks and psychology during trading",
                                            "I want to learn how to backtest trading strategies",
                                            "I want to learn how to automate trading strategies"))

elif a == "I know how to backtest trading strategies":
    b = st.selectbox("Where I want to be?",("I want trading strategies that will help me become a profitable trader",
                                            "I want FNO trading strategies that will help me become a profitable trader",
                                            "I want to build my own trading strategy",
                                            "I want to get better at managing my risks and psychology during trading",
                                            "I want to learn how to automate trading strategies"))

elif a == "I know how to automate trading strategies":
    b = st.selectbox("Where I want to be?", ("I want trading strategies that will help me become a profitable trader",
                                            "I want FNO trading strategies that will help me become a profitable trader",
                                            "I want to build my own trading strategy",
                                            "I want to get better at managing my risks and psychology during trading",
                                            "I want to learn how to backtest trading strategies"))


if st.button("Create my Customized Learning Path"):

    if name == "":
        st.error("Please enter a valid name")
    else:
        with st.spinner("Creating Learning Path for " + name):
            time.sleep(1.5)
            st.header("")
            st.header(name + "'s Learning Path")

            #store data in database
            url_email = "https://3749e8lxlf.execute-api.ap-south-1.amazonaws.com/"
            payload_email = {"query_date" : date, "tool_name" : "tool-learnapp-course-recommendation","Name":name ,"where_i_stand": a, "where_i_want_to_be":b}
            headers_email = {'Content-Type': 'text/plain'}
            response = requests.request("POST", url_email, headers=headers_email, data = json.dumps(payload_email))


            # I just opened my demat account and I don’t know how stock market works

            if a == "I just opened my demat account and I don’t know how stock market works" and b == "I want to get started with trading":

                st.header("1. Basics of Personal Finance")
                st.markdown("[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Personal+Finance.jpeg)](https://learnapp.com/courses/basics-of-personal-finance/topics/trailer)")
                st.write("")

                st.header("2. Learn How Capital Market Works")
                st.markdown("[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Capital+Market+Works.jpeg)](https://learnapp.com/courses/learn-how-capital-markets-work/topics/trailer)")
                st.write("")
                
                st.header("3. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("4. Intro to technical Analysis")
                st.markdown("[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer)")
                st.write("")

                st.header("5. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")


            elif a == "I just opened my demat account and I don’t know how stock market works" and b == "I want to learn trading from scratch":

                st.header("1. Basics of Personal Finance")
                st.markdown("[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Personal+Finance.jpeg)](https://learnapp.com/courses/basics-of-personal-finance/topics/trailer)")
                st.write("")

                st.header("2. Learn How Capital Market Works")
                st.markdown("[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Capital+Market+Works.jpeg)](https://learnapp.com/courses/learn-how-capital-markets-work/topics/trailer)")
                st.write("")
                
                st.header("3. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("4. Intro to technical Analysis")
                st.markdown("[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer)")
                st.write("")

                st.header("5. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")


            # I just know the basics of stock market

            elif a == "I just know the basics of stock market" and b == "I want to get started with trading":

                st.header("1. Basics of Personal Finance")
                st.markdown("[![Basics of Personal Finance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Personal+Finance.jpeg)](https://learnapp.com/courses/basics-of-personal-finance/topics/trailer)")
                st.write("")
                
                st.header("2. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("3. Intro to technical Analysis")
                st.markdown("[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer)")
                st.write("")

                st.header("4. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

            elif a == "I just know the basics of stock market" and b == "I want to dive deeper into technical analysis":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Intro to technical Analysis")
                st.markdown("[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer)")
                st.write("")

                st.header("3. Support and Resistance")
                st.markdown("[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer)")
                st.write("")

                st.header("4. Single Candlesticks")
                st.markdown("[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer)")
                st.write("")

                st.header("5. Multiple Candlestick Pattern")
                st.markdown("[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer)")
                st.write("")

                st.header("6. Trading Breakouts and Breakdowns")
                st.markdown("[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer)")
                st.write("")

                st.header("7. Trading Flags and Pennants")
                st.markdown("[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer)")
                st.write("")

                st.header("8. Reversal Patterns")
                st.markdown("[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer)")
                st.write("")

                st.header("9. Learn Trend Indicators")
                st.markdown("[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer)")
                st.write("")

                st.header("10. Learn How Trend Trading Works")
                st.markdown("[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer)")
                st.write("")

                st.header("11. Learn Momentum Indicators")
                st.markdown("[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer)")
                st.write("")

                st.header("12. Learn Volume Indicators")
                st.markdown("[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer)")
                st.write("")

            elif a == "I just know the basics of stock market" and b == "I want trading strategies that will help me become a profitable trader":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("3. Price Action Strategy")
                st.markdown("[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
                st.write("")

                st.header("4. Intraday Gapup Equity Strategy")
                st.markdown("[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer)")
                st.write("")

                st.header("5. Long Term Momentum Strategy")
                st.markdown("[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("6. Bullet Momentum Strategy")
                st.markdown("[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer)")
                st.write("")


            # I trade based on my gut feeling

            elif a == "I trade based on my gut feeling" and b == "I want to dive deeper into technical analysis":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Intro to technical Analysis")
                st.markdown("[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer)")
                st.write("")

                st.header("3. Support and Resistance")
                st.markdown("[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer)")
                st.write("")

                st.header("4. Single Candlesticks")
                st.markdown("[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer)")
                st.write("")

                st.header("5. Multiple Candlestick Pattern")
                st.markdown("[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer)")
                st.write("")

                st.header("6. Trading Breakouts and Breakdowns")
                st.markdown("[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer)")
                st.write("")

                st.header("7. Trading Flags and Pennants")
                st.markdown("[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer)")
                st.write("")

                st.header("8. Reversal Patterns")
                st.markdown("[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer)")
                st.write("")

                st.header("9. Learn Trend Indicators")
                st.markdown("[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer)")
                st.write("")

                st.header("10. Learn How Trend Trading Works")
                st.markdown("[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer)")
                st.write("")

                st.header("11. Learn Momentum Indicators")
                st.markdown("[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer)")
                st.write("")

                st.header("12. Learn Volume Indicators")
                st.markdown("[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer)")
                st.write("")
        
            elif a == "I trade based on my gut feeling" and b == "I want trading strategies that will help me become a profitable trader":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("3. Price Action Strategy")
                st.markdown("[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
                st.write("")

                st.header("4. Intraday Gapup Equity Strategy")
                st.markdown("[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer)")
                st.write("")

                st.header("5. Long Term Momentum Strategy")
                st.markdown("[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("6. Bullet Momentum Strategy")
                st.markdown("[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer)")
                st.write("")
    

            # I know the basics of technical analysis

            elif a == "I know the basics of technical analysis" and b == "I want to dive deeper into technical analysis":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Intro to technical Analysis")
                st.markdown("[![Intro to technical Analysis](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Technical+Analysis.jpeg)](https://learnapp.com/courses/intro-to-technical-analysis/topics/trailer)")
                st.write("")

                st.header("3. Support and Resistance")
                st.markdown("[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer)")
                st.write("")

                st.header("4. Single Candlesticks")
                st.markdown("[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer)")
                st.write("")

                st.header("5. Multiple Candlestick Pattern")
                st.markdown("[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer)")
                st.write("")

                st.header("6. Trading Breakouts and Breakdowns")
                st.markdown("[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer)")
                st.write("")

                st.header("7. Trading Flags and Pennants")
                st.markdown("[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer)")
                st.write("")

                st.header("8. Reversal Patterns")
                st.markdown("[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer)")
                st.write("")

                st.header("9. Learn Trend Indicators")
                st.markdown("[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer)")
                st.write("")

                st.header("10. Learn How Trend Trading Works")
                st.markdown("[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer)")
                st.write("")

                st.header("11. Learn Momentum Indicators")
                st.markdown("[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer)")
                st.write("")

                st.header("12. Learn Volume Indicators")
                st.markdown("[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer)")
                st.write("")

            elif a == "I know the basics of technical analysis" and b == "I want trading strategies that will help me become a profitable trader":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("3. Price Action Strategy")
                st.markdown("[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
                st.write("")

                st.header("4. Intraday Gapup Equity Strategy")
                st.markdown("[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer)")
                st.write("")

                st.header("5. Long Term Momentum Strategy")
                st.markdown("[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("6. Bullet Momentum Strategy")
                st.markdown("[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer)")
                st.write("")


            elif a == "I know the basics of technical analysis" and b == "I want to learn how FNO works":
                
                st.header("1. Intro to Futures and Options")
                st.markdown("[![Intro to Futures and Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Futures+and+Options.jpeg)](https://learnapp.com/courses/intro-to-futures-and-options/topics/trailer)")
                st.write("")

                st.header("2. Basics of Options")
                st.markdown("[![Basics of Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options.jpeg)](https://learnapp.com/courses/basics-of-options/topics/trailer)")
                st.write("")

                st.header("3. Basics of Options II")
                st.markdown("[![Basics of Options II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options+II.jpeg)](https://learnapp.com/courses/basics-of-options-ii/topics/trailer)")
                st.write("")

                st.header("4. Option Spreads and Option Chain")
                st.markdown("[![Option Spreads and Option Chain](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Spreads+and+Option+Chain.jpeg)](https://learnapp.com/courses/option-spreads-and-option-chain/topics/trailer)")
                st.write("")

                st.header("5. Straddles and Strangles")
                st.markdown("[![Straddles and Strangles](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Straddles+and+Strangles.jpeg)](https://learnapp.com/courses/straddles-and-strangles/topics/trailer)")
                st.write("")

                st.header("6. Iron Condors, Butterfly and Calendar Spreads")
                st.markdown("[![Iron Condors, Butterfly and Calendar Spreads](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Iron+Condors%2C+Butterfly+and+Calendar+Spreads.jpeg)](https://learnapp.com/courses/iron-condors-butterfly-and-calendar-spreads/topics/trailer)")
                st.write("")


            # I trade systematic trading strategies manually

            elif a == "I trade systematic trading strategies manually" and b == "I want to dive deeper into technical analysis":

                st.header("1. Support and Resistance")
                st.markdown("[![Support and Resistance](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Support+and+Resistance.jpeg)](https://learnapp.com/courses/support-resistance-/topics/trailer)")
                st.write("")

                st.header("2. Single Candlesticks")
                st.markdown("[![Single Candlesticks](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Single+Candlesticks.jpeg)](https://learnapp.com/courses/single-candlesticks/topics/trailer)")
                st.write("")

                st.header("3. Multiple Candlestick Pattern")
                st.markdown("[![Multiple Candlestick Pattern](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Multiple+Candlestick+Pattern.jpeg)](https://learnapp.com/courses/multiple-candlestick-pattern/topics/trailer)")
                st.write("")

                st.header("4. Trading Breakouts and Breakdowns")
                st.markdown("[![Trading Breakouts and Breakdowns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Breakouts+and+Breakdowns.jpeg)](https://learnapp.com/courses/trading-breakouts-and-breakdowns/topics/trailer)")
                st.write("")

                st.header("5. Trading Flags and Pennants")
                st.markdown("[![Trading Flags and Pennants](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Flags+and+Pennants.jpeg)](https://learnapp.com/courses/trading-flags-and-pennants/topics/trailer)")
                st.write("")

                st.header("6. Reversal Patterns")
                st.markdown("[![Reversal Patterns](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Reversal+Patterns.jpeg)](https://learnapp.com/courses/reversal-patterns/topics/trailer)")
                st.write("")

                st.header("7. Learn Trend Indicators")
                st.markdown("[![Learn Trend Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Trend+Indicators.jpeg)](https://learnapp.com/courses/learn-trend-indicators/topics/trailer)")
                st.write("")

                st.header("8. Learn How Trend Trading Works")
                st.markdown("[![Learn How Trend Trading Works](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+How+Trend+Trading+Works.jpeg)](https://learnapp.com/courses/learn-how-trend-trading-works/topics/trailer)")
                st.write("")

                st.header("9. Learn Momentum Indicators")
                st.markdown("[![Learn Momentum Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Momentum+Indicators.jpeg)](https://learnapp.com/courses/learn-momentum-indicators/topics/trailer)")
                st.write("")

                st.header("10. Learn Volume Indicators")
                st.markdown("[![Learn Volume Indicators](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Volume+Indicators.jpeg)](https://learnapp.com/courses/learn-volume-indicators-/topics/trailer)")
                st.write("")

            elif a == "I trade systematic trading strategies manually" and b == "I want trading strategies that will help me become a profitable trader":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("3. Price Action Strategy")
                st.markdown("[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
                st.write("")

                st.header("4. Intraday Gapup Equity Strategy")
                st.markdown("[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer)")
                st.write("")

                st.header("5. Long Term Momentum Strategy")
                st.markdown("[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("6. Bullet Momentum Strategy")
                st.markdown("[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer)")
                st.write("")

            elif a == "I trade systematic trading strategies manually" and b == "I want to learn how FNO works":
                
                st.header("1. Intro to Futures and Options")
                st.markdown("[![Intro to Futures and Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intro+to+Futures+and+Options.jpeg)](https://learnapp.com/courses/intro-to-futures-and-options/topics/trailer)")
                st.write("")

                st.header("2. Basics of Options")
                st.markdown("[![Basics of Options](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options.jpeg)](https://learnapp.com/courses/basics-of-options/topics/trailer)")
                st.write("")

                st.header("3. Basics of Options II")
                st.markdown("[![Basics of Options II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Options+II.jpeg)](https://learnapp.com/courses/basics-of-options-ii/topics/trailer)")
                st.write("")

                st.header("4. Option Spreads and Option Chain")
                st.markdown("[![Option Spreads and Option Chain](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Spreads+and+Option+Chain.jpeg)](https://learnapp.com/courses/option-spreads-and-option-chain/topics/trailer)")
                st.write("")

                st.header("5. Straddles and Strangles")
                st.markdown("[![Straddles and Strangles](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Straddles+and+Strangles.jpeg)](https://learnapp.com/courses/straddles-and-strangles/topics/trailer)")
                st.write("")

                st.header("6. Iron Condors, Butterfly and Calendar Spreads")
                st.markdown("[![Iron Condors, Butterfly and Calendar Spreads](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Iron+Condors%2C+Butterfly+and+Calendar+Spreads.jpeg)](https://learnapp.com/courses/iron-condors-butterfly-and-calendar-spreads/topics/trailer)")
                st.write("")

            elif a == "I trade systematic trading strategies manually" and b == "I want FNO trading strategies that will help me become a profitable trader":
                
                st.header("1. BankNifty Weekly Options Strategy")
                st.markdown("[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer)")
                st.write("")

                st.header("2. Intraday Banknifty Straddle Strategy")
                st.markdown("[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer)")
                st.write("")

                st.header("3. Intraday Expiry Trading Strategy")
                st.markdown("[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer)")
                st.write("")

                st.header("4. Nifty Hedged Short Strangle")
                st.markdown("[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer)")
                st.write("")

                st.header("5. Index Futures Intraday Strategy")
                st.markdown("[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("6. Intraday Option Buying Strategy")
                st.markdown("[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer)")
                st.write("")

                st.header("7. Positional Banknifty Options Stratgey")
                st.markdown("[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer)")
                st.write("")

                st.header("8. Option Buying Momentum Strategy")
                st.markdown("[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("9. Learn an Options Writing Strategy")
                st.markdown("[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer)")
                st.write("")

                st.header("10. Options Program with Backtested Strategies")
                st.markdown("[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies)")
                st.write("")

            elif a == "I trade systematic trading strategies manually" and b == "I want to build my own trading strategy":
                
                st.header("1. Build Your Trading System")
                st.markdown("[![Build Your Trading System](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Build+Your+Trading+System.jpeg)](https://learnapp.com/courses/build-your-trading-system/topics/trailer)")
                st.write("")

                st.header("2. Basics of Backtesting")
                st.markdown("[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer)")
                st.write("")

                st.header("3. Amibroker Strategy Development and Algo Execution")
                st.markdown("[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution)")
                st.write("")

            elif a == "I trade systematic trading strategies manually" and b == "I want to get better at managing my risks and psychology during trading":
                
                st.header("1. Trading Podcasts")
                st.markdown("[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer)")
                st.write("")

                st.header("2. Trading Podcast II")
                st.markdown("[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer)")
                st.write("")

                st.header("3. Psychology and Journals")
                st.markdown("[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1)")
                st.write("")

            elif a == "I trade systematic trading strategies manually" and b == "I want to learn how to backtest trading strategies":
                
                st.header("1. Basics of Backtesting")
                st.markdown("[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer)")
                st.write("")

                st.header("2. Trading and Excel")
                st.markdown("[![Trading and Excel](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+and+Excel.jpg)](https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel)")
                st.write("")

                st.header("3. Backtesting Stocks with Indicators - I")
                st.markdown("[![Backtesting Stocks with Indicators - I](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+I.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi)")
                st.write("")

                st.header("4. Backtesting Stocks with Indicators - II")
                st.markdown("[![Backtesting Stocks with Indicators - II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+II.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands)")
                st.write("")

                st.header("5. Amibroker Strategy Development and Algo Execution")
                st.markdown("[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution)")
                st.write("")

            elif a == "I trade systematic trading strategies manually" and b == "I want to learn how to automate trading strategies":
                
                st.header("1. Amibroker Strategy Development and Algo Execution")
                st.markdown("[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution)")
                st.write("")

                st.header("2. Python Algo Execution Programme")
                st.markdown("[![Python Algo Execution Programme](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Python+Algo+Execution+Programme.jpg)](https://learnapp.com/advanced-courses/python-algo-execution-programme)")
                st.write("")

            
            # I know the basics of futures and options
            
            elif a == "I know the basics of futures and options" and b == "I want FNO trading strategies that will help me become a profitable trader":
                
                st.header("1. BankNifty Weekly Options Strategy")
                st.markdown("[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer)")
                st.write("")

                st.header("2. Intraday Banknifty Straddle Strategy")
                st.markdown("[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer)")
                st.write("")

                st.header("3. Intraday Expiry Trading Strategy")
                st.markdown("[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer)")
                st.write("")

                st.header("4. Nifty Hedged Short Strangle")
                st.markdown("[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer)")
                st.write("")

                st.header("5. Index Futures Intraday Strategy")
                st.markdown("[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("6. Intraday Option Buying Strategy")
                st.markdown("[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer)")
                st.write("")

                st.header("7. Positional Banknifty Options Stratgey")
                st.markdown("[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer)")
                st.write("")

                st.header("8. Option Buying Momentum Strategy")
                st.markdown("[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("9. Learn an Options Writing Strategy")
                st.markdown("[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer)")
                st.write("")

                st.header("10. Options Program with Backtested Strategies")
                st.markdown("[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies)")
                st.write("")

            elif a == "I know the basics of futures and options" and b == "I want to get better at managing my risks and psychology during trading":
                
                st.header("1. Trading Podcasts")
                st.markdown("[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer)")
                st.write("")

                st.header("2. Trading Podcast II")
                st.markdown("[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer)")
                st.write("")

                st.header("3. Psychology and Journals")
                st.markdown("[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1)")
                st.write("")         

            
            # I have my own trading strategy
            
            elif a == "I have my own trading strategy" and b == "I want trading strategies that will help me become a profitable trader":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("3. Price Action Strategy")
                st.markdown("[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
                st.write("")

                st.header("4. Intraday Gapup Equity Strategy")
                st.markdown("[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer)")
                st.write("")

                st.header("5. Long Term Momentum Strategy")
                st.markdown("[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("6. Bullet Momentum Strategy")
                st.markdown("[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer)")
                st.write("")

            elif a == "I have my own trading strategy" and b == "I want FNO trading strategies that will help me become a profitable trader":
                
                st.header("1. BankNifty Weekly Options Strategy")
                st.markdown("[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer)")
                st.write("")

                st.header("2. Intraday Banknifty Straddle Strategy")
                st.markdown("[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer)")
                st.write("")

                st.header("3. Intraday Expiry Trading Strategy")
                st.markdown("[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer)")
                st.write("")

                st.header("4. Nifty Hedged Short Strangle")
                st.markdown("[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer)")
                st.write("")

                st.header("5. Index Futures Intraday Strategy")
                st.markdown("[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("6. Intraday Option Buying Strategy")
                st.markdown("[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer)")
                st.write("")

                st.header("7. Positional Banknifty Options Stratgey")
                st.markdown("[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer)")
                st.write("")

                st.header("8. Option Buying Momentum Strategy")
                st.markdown("[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("9. Learn an Options Writing Strategy")
                st.markdown("[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer)")
                st.write("")

                st.header("10. Options Program with Backtested Strategies")
                st.markdown("[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies)")
                st.write("")

            elif a == "I have my own trading strategy" and b == "I want to get better at managing my risks and psychology during trading":
                
                st.header("1. Trading Podcasts")
                st.markdown("[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer)")
                st.write("")

                st.header("2. Trading Podcast II")
                st.markdown("[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer)")
                st.write("")

                st.header("3. Psychology and Journals")
                st.markdown("[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1)")
                st.write("")

            elif a == "I have my own trading strategy" and b == "I want to learn how to backtest trading strategies":
                
                st.header("1. Basics of Backtesting")
                st.markdown("[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer)")
                st.write("")

                st.header("2. Trading and Excel")
                st.markdown("[![Trading and Excel](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+and+Excel.jpg)](https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel)")
                st.write("")

                st.header("3. Backtesting Stocks with Indicators - I")
                st.markdown("[![Backtesting Stocks with Indicators - I](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+I.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi)")
                st.write("")

                st.header("4. Backtesting Stocks with Indicators - II")
                st.markdown("[![Backtesting Stocks with Indicators - II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+II.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands)")
                st.write("")

                st.header("5. Amibroker Strategy Development and Algo Execution")
                st.markdown("[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution)")
                st.write("")

            elif a == "I have my own trading strategy" and b == "I want to learn how to automate trading strategies":
                
                st.header("1. Amibroker Strategy Development and Algo Execution")
                st.markdown("[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution)")
                st.write("")

                st.header("2. Python Algo Execution Programme")
                st.markdown("[![Python Algo Execution Programme](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Python+Algo+Execution+Programme.jpg)](https://learnapp.com/advanced-courses/python-algo-execution-programme)")
                st.write("")


            # I know how to backtest trading strategies

            elif a == "I know how to backtest trading strategies" and b == "I want trading strategies that will help me become a profitable trader":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("3. Price Action Strategy")
                st.markdown("[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
                st.write("")

                st.header("4. Intraday Gapup Equity Strategy")
                st.markdown("[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer)")
                st.write("")

                st.header("5. Long Term Momentum Strategy")
                st.markdown("[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("6. Bullet Momentum Strategy")
                st.markdown("[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer)")
                st.write("")

            elif a == "I know how to backtest trading strategies" and b == "I want FNO trading strategies that will help me become a profitable trader":
                
                st.header("1. BankNifty Weekly Options Strategy")
                st.markdown("[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer)")
                st.write("")

                st.header("2. Intraday Banknifty Straddle Strategy")
                st.markdown("[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer)")
                st.write("")

                st.header("3. Intraday Expiry Trading Strategy")
                st.markdown("[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer)")
                st.write("")

                st.header("4. Nifty Hedged Short Strangle")
                st.markdown("[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer)")
                st.write("")

                st.header("5. Index Futures Intraday Strategy")
                st.markdown("[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("6. Intraday Option Buying Strategy")
                st.markdown("[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer)")
                st.write("")

                st.header("7. Positional Banknifty Options Stratgey")
                st.markdown("[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer)")
                st.write("")

                st.header("8. Option Buying Momentum Strategy")
                st.markdown("[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("9. Learn an Options Writing Strategy")
                st.markdown("[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer)")
                st.write("")

                st.header("10. Options Program with Backtested Strategies")
                st.markdown("[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies)")
                st.write("")

            elif a == "I know how to backtest trading strategies" and b == "I want to build my own trading strategy":
                
                st.header("1. Build Your Trading System")
                st.markdown("[![Build Your Trading System](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Build+Your+Trading+System.jpeg)](https://learnapp.com/courses/build-your-trading-system/topics/trailer)")
                st.write("")

            elif a == "I know how to backtest trading strategies" and b == "I want to get better at managing my risks and psychology during trading":
                
                st.header("1. Trading Podcasts")
                st.markdown("[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer)")
                st.write("")

                st.header("2. Trading Podcast II")
                st.markdown("[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer)")
                st.write("")

                st.header("3. Psychology and Journals")
                st.markdown("[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1)")
                st.write("")

            elif a == "I know how to backtest trading strategies" and b == "I want to learn how to automate trading strategies":
                
                st.header("1. Amibroker Strategy Development and Algo Execution")
                st.markdown("[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution)")
                st.write("")

                st.header("2. Python Algo Execution Programme")
                st.markdown("[![Python Algo Execution Programme](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Python+Algo+Execution+Programme.jpg)](https://learnapp.com/advanced-courses/python-algo-execution-programme)")
                st.write("")


            # I know how to automate trading strategies

            elif a == "I know how to automate trading strategies" and b == "I want trading strategies that will help me become a profitable trader":
                
                st.header("1. Basics of Trading")
                st.markdown("[![Basics of Trading](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Trading.jpeg)](https://learnapp.com/courses/basics-of-trading/topics/trailer)")
                st.write("")

                st.header("2. Learn Intraday Strategy")
                st.markdown("[![Learn Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+Intraday+Strategy.jpeg)](https://learnapp.com/courses/learn-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("3. Price Action Strategy")
                st.markdown("[![Price Action Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Price+Action+Strategy.jpeg)](https://learnapp.com/courses/price-action-strategy/topics/trailer)")
                st.write("")

                st.header("4. Intraday Gapup Equity Strategy")
                st.markdown("[![Intraday Gapup Equity Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Gapup+Equity+Strategy.jpeg)](https://learnapp.com/courses/intraday-gap-up-equity-strategy/topics/trailer)")
                st.write("")

                st.header("5. Long Term Momentum Strategy")
                st.markdown("[![Long Term Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Long+Term+Momentum+Strategy.jpeg)](https://learnapp.com/courses/long-term-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("6. Bullet Momentum Strategy")
                st.markdown("[![Bullet Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Bullet+Momentum+Strategy.jpeg)](https://learnapp.com/courses/bullet-momentum-strategy/topics/trailer)")
                st.write("")

            elif a == "I know how to automate trading strategies" and b == "I want FNO trading strategies that will help me become a profitable trader":
                
                st.header("1. BankNifty Weekly Options Strategy")
                st.markdown("[![BankNifty Weekly Options Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/BankNifty+Weekly+Options+Strategy.jpeg)](https://learnapp.com/courses/banknifty-weekly-options-strategy/topics/trailer)")
                st.write("")

                st.header("2. Intraday Banknifty Straddle Strategy")
                st.markdown("[![Intraday Banknifty Straddle Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Banknifty+Straddle+Strategy.jpeg)](https://learnapp.com/courses/intraday-banknifty-straddle-strategy/topics/trailer)")
                st.write("")

                st.header("3. Intraday Expiry Trading Strategy")
                st.markdown("[![Intraday Expiry Trading Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Expiry+Trading+Strategy.jpeg)](https://learnapp.com/courses/intraday-expiry-trading-strategy/topics/trailer)")
                st.write("")

                st.header("4. Nifty Hedged Short Strangle")
                st.markdown("[![Nifty Hedged Short Strangle](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Nifty+Hedged+Short+Strangle.jpeg)](https://learnapp.com/courses/nifty-hedged-short-strangle/topics/trailer)")
                st.write("")

                st.header("5. Index Futures Intraday Strategy")
                st.markdown("[![Index Futures Intraday Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Index+Futures+Intraday+Strategy.jpeg)](https://learnapp.com/courses/index-futures-intraday-strategy/topics/trailer)")
                st.write("")

                st.header("6. Intraday Option Buying Strategy")
                st.markdown("[![Intraday Option Buying Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Intraday+Option+Buying+Strategy.jpeg)](https://learnapp.com/courses/intraday-option-buying-strategy/topics/trailer)")
                st.write("")

                st.header("7. Positional Banknifty Options Stratgey")
                st.markdown("[![Positional Banknifty Options Stratgey](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Positional+Banknifty+Options+Stratgey.jpeg)](https://learnapp.com/courses/positional-banknifty-options-strategy/topics/trailer)")
                st.write("")

                st.header("8. Option Buying Momentum Strategy")
                st.markdown("[![Option Buying Momentum Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Option+Buying+Momentum+Strategy.jpeg)](https://learnapp.com/courses/option-buying-momentum-strategy/topics/trailer)")
                st.write("")

                st.header("9. Learn an Options Writing Strategy")
                st.markdown("[![Learn an Options Writing Strategy](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Learn+an+Options+Writing+Strategy.jpeg)](https://learnapp.com/courses/learn-an-options-writing-strategy/topics/trailer)")
                st.write("")

                st.header("10. Options Program with Backtested Strategies")
                st.markdown("[![Options Program with Backtested Strategies](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Options+Program+with+Backtested+Strategies.jpeg)](https://learnapp.com/advanced-courses/options-program-with-backtested-strategies)")
                st.write("")

            elif a == "II know how to automate trading strategies" and b == "I want to build my own trading strategy":
                
                st.header("1. Build Your Trading System")
                st.markdown("[![Build Your Trading System](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Build+Your+Trading+System.jpeg)](https://learnapp.com/courses/build-your-trading-system/topics/trailer)")
                st.write("")

            elif a == "I know how to automate trading strategies" and b == "I want to get better at managing my risks and psychology during trading":
                
                st.header("1. Trading Podcasts")
                st.markdown("[![Trading Podcasts](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcasts.jpeg)](https://learnapp.com/courses/trading-podcasts/topics/trailer)")
                st.write("")

                st.header("2. Trading Podcast II")
                st.markdown("[![Trading Podcast II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+Podcast+II.jpeg)](https://learnapp.com/courses/trading-podcast-ii/topics/trailer)")
                st.write("")

                st.header("3. Psychology and Journals")
                st.markdown("[![Psychology and Journals](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Psychology+and+Journals.jpg)](https://learnapp.com/classes/psychology-and-journals/topics/the-brain-behind-trading--1)")
                st.write("")


            elif a == "I know how to automate trading strategies" and b == "I want to learn how to backtest trading strategies":
                
                st.header("1. Basics of Backtesting")
                st.markdown("[![Basics of Backtesting](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Basics+of+Backtesting.jpeg)](https://learnapp.com/courses/basics-of-backtesting/topics/trailer)")
                st.write("")

                st.header("2. Trading and Excel")
                st.markdown("[![Trading and Excel](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Trading+and+Excel.jpg)](https://learnapp.com/classes/trading-and-excel/topics/trading-and-excel)")
                st.write("")

                st.header("3. Backtesting Stocks with Indicators - I")
                st.markdown("[![Backtesting Stocks with Indicators - I](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+I.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---i/topics/backtesting-stocks-with-rsi)")
                st.write("")

                st.header("4. Backtesting Stocks with Indicators - II")
                st.markdown("[![Backtesting Stocks with Indicators - II](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Backtesting+Stocks+with+Indicators+-+II.jpg)](https://learnapp.com/classes/backtesting-stocks-with-indicators---ii/topics/backtesting-stocks-with-bollinger-bands)")
                st.write("")

                st.header("5. Amibroker Strategy Development and Algo Execution")
                st.markdown("[![Amibroker Strategy Development and Algo Execution](https://la-course-recommendation-engine.s3.ap-south-1.amazonaws.com/Amibroker+Strategy+Development+and+Algo+Execution.jpg)](https://learnapp.com/advanced-courses/amibroker-strategy-development-and-algo-execution)")
                st.write("")


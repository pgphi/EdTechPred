import streamlit as st
from PIL import Image
import datetime
import time

from preprocessing import y
from predictions import make_prediction
from gasApi import get_gas_info
from predictions import mc_simulation


def user_interface(DF, url):
    """
    :param DF: raw dataset
    :param url: api data of gas provider shown for gas information metrics
    """

    # Build Web-Application with Streamlit further see: https://docs.streamlit.io/library/api-reference/media/st.image

    st.title("EdTech Project: Gas Price Prediction")
    st.subheader("By Philipp Ganster")
    st.image("Images/Hero.jpg")
    st.header("Let's Predict Your Future Gas Price  🎓")
    st.write(
        "In order to help private households easing financial uncertainty due to the rise of gas prices in Germany,"
        " this application predicts your future gas price based on data from the Trading Hub Europe which is "
        "responsible for managing the gas market in Germany.")

    st.text("")
    st.markdown("***")

    st.subheader("Information of Uniper Energy"
                 " \nGermany's largest Gas Provider")

    st.text("")

    # Show Metrics of Gas Provider
    cur_day = get_gas_info(url)[1]  # YYYY-MM-DD
    cur_gasInStorage = get_gas_info(url)[2]  # In Percent %
    cur_withdraw = get_gas_info(url)[3]  # in Gwh/d
    cur_trend = get_gas_info(url)[4]  # Change in Percent %

    col1, col2, col3 = st.columns(3)
    col1.metric("Date", cur_day)
    col2.metric("Storage Capacity (Full)", f"{cur_gasInStorage} %")
    col3.metric("Gas Demand", f"{cur_withdraw} GWh/day", f"{cur_trend} %")
    st.info("Here You Can See Information from Germany's largest Gas Provider")
    with st.expander("Further Information"):
        st.write("Datasets of german gas providers further see: https://agsi.gie.eu/")
    st.text("")
    st.markdown("***")
    st.markdown("<h4 style='text-align: center;'>Gas Price Development Over Time</h4>", unsafe_allow_html=True)
    st.text("")
    image = Image.open('Images/Gas_Price_Dev.png')
    st.image(image)
    st.text("")
    st.text("")
    if st.checkbox('Show Raw Dataset'):
        st.subheader('Raw dataset')
        st.write(DF)
    with st.expander("Further Information"):
        st.write("""
                Gas price in EUR/kWh from GASPOOL and Trading Hub Europe (THE) - responsible for german gas market.
    
                Data from 1.10.2015 - 01.09.2021: \n
                https://www.tradinghub.eu/Portals/0/Archiv%20NCG/20211019_Monatsdurchschnittspreise_20211019.xlsx?ver=SfV9SAubpW1e1bGte96d4Q%3d%3d \n
    
                Data from 01.10.2021 - 01.08.2022: \n
                https://www.tradinghub.eu/en-gb/Publications/Prices/Reconciliation-price \n
    
                German Gas Storage Capacity (in TWh) from 1.10.2015 - 01.08.2022: \n
                https://agsi.gie.eu/historical/DE \n
    
                Model Performance: \n
                Polynomial Function MAE = 0.008515221391126407\n
                Polynomial Function R_squared = 0.6370797480659653 \n
            """)

        st.image(
            "https://tradinghub.eu/Portals/0/THE%20Imagebilder/Imagebilder_klein/_DSC6728_klein.jpg?ver=OAYj5BO8XcGh0KtljbE_ZQ%3d%3d")


    st.text("")
    st.markdown("***")
    st.write \
        ("The graph above shows the price development (f) dependent on the storage capacity and time (X) and its polynomial function,"
         " for making predictions.")
    st.text("")
    st.latex(r'''
                 \tiny f(x_1 , x_2) = 5.02 - (6.69 {e-09}) * x_1 + (1.25 {e-09}) * x_2 + (2.24 {e-18}) * x_1^2 - (7.83 {e-19}) * x_2^2 - (3.19 {e-19}) *x_1 * x_2
                 ''')
    st.text("")
    st.write("Still unclear? No worries, we're in this together. Imagine the following: Pick one field of expertise i.e. your hobby. In my case it's playing"
         " the piano - and yours? After a while we become really good in this certain area through deliberate practice. So by practice"
         " and time passing, we can make good estimates of our outcome i.e. we know where to hit the right note, shot the football"
         " in the right corner of the goal or paint the picture in a well manner etc. Looking again on the graph above this means,"
         " that with our dataset (time, practice, experience and learning) we can make precise predictions of our desired outcome.")

    st.text("")
    tab1, tab2, tab3, tab4 = st.tabs(["Piano", "Football", "Paint", "And You?"])

    with tab1:
        st.subheader("One Note at a time.")
        st.image("Images/Piano.jpg", width=300)

    with tab2:
        st.subheader("One Step at a time.")
        st.image("Images/Football.jpg", width=300)

    with tab3:
        st.subheader("One Brush at a time.")
        st.image("Images/Painting.jpg", width=300)

    with tab4:
        st.subheader("One '...' at a time.")
        st.image("Images/You.jpg", width=300)

    st.text("")
    st.text("")
    st.markdown("***")
    st.header("Make a Prediction:")

    number = st.number_input('Insert your past or current gas consumption in kWh i.e. a 2 person household uses ca. 10000kWh/year:')  # i.e. number = 10000

    date = st.date_input(
        "Type in the date you want to know your gas costs in the future i.e. 2022/31/12:",
        datetime.date(2022, 12, 31))  # i.e. date = "2022/08/01"

    error = 0.008515221391126407
    # print(error)
    costs = make_prediction(date, number, error)[0]
    cost_variance = make_prediction(date, number, error)[1]
    # print(gas_costs)

    if st.button('Make a Prediction'):

        my_bar = st.progress(0)

        for percent_complete in range(100):
            time.sleep(0.005)
            my_bar.progress(percent_complete + 1)

        st.write(f'Your estimated Gas costs will reach {costs} Euros by {date}.')
        st.write(f'Due to variance in forecast model your costs can vary by ca. +- {cost_variance} Euros.')
        st.write('Also be aware of tax cuts from the government or other external factors.')
    st.info("If the calculation takes to long, please update your browser (usually on top).")
    st.text("")
    st.text("")
    st.text("")
    st.markdown("***")
    st.subheader("Monte Carlo Simulation")
    st.write("For Future Gas Price Predictions")
    st.image("Images/Monte_Carlo_Simulation.jpg")
    st.write("Monte Carlo Simulation is a mathematical technique that generates random variables for modelling "
             "risk or uncertainty of a certain system. The random variables or inputs are modelled on the basis "
             "of probability distributions such as normal, log normal, etc.")
    st.write("I know - this sounds complicated. Let us pick our hobby again. How good or bad our progress will be"
             " over time, depends on various factors. In my case, if i injure my hand, my skills on the piano will"
             " decrease over a certain period of time. Monte Carlo Simulation takes those various random effects, which could occur"
             " in the future, into account. When it comes to gas price one factor maybe a de-escalation in conflict"
             " between Ukraine and Russia. This could lead to a decrease or normalization in gas prices.")

    with st.expander("Further Information"):
        st.write("https://www.investopedia.com/terms/m/montecarlosimulation.asp")
    st.text("")
    st.markdown("***")
    st.markdown("#### Try it Out For Yourself")
    st.text("")
    st.text("")
    iterations = st.slider("For how long into the future do you want to simulate?", 0, 500)
    outcomes = st.slider("How many possible outcomes do you want to simulate?", 0, 10)
    st.text("")
    st.text("")
    st.markdown("***")

    if iterations and outcomes != 0:
        st.subheader("Here is Your Monte Carlo Simulation")
        mc_simulation(y, iterations, outcomes)
        st.image("Images/mc_prediction.png")

    st.text("")
    st.text("")
    st.write("I talked a lot about my hobby: Playing the piano. So here is one piece i composed called 'New Day'.")
    st.text("")
    st.audio("New_Day.mp3")
    st.markdown("**Rhythm and harmony find their way into the inward places of the soul.**")
    st.write("Plato")
    st.text("")
    st.caption("LinkedIn: www.linkedin.com/in/pganster | More about this Project: https://github.com/pgphi/GasPred")
